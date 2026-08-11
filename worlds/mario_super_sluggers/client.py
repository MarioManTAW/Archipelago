import asyncio
import traceback
import random
from typing import TYPE_CHECKING, Any, Optional

import dolphin_memory_engine

import Utils
tracker_loaded = False
try:
    from worlds.tracker.TrackerClient import TrackerGameContext as SuperContext
    tracker_loaded = True
except ModuleNotFoundError:
    from CommonClient import CommonContext as SuperContext
from CommonClient import ClientCommandProcessor, get_base_parser, gui_enabled, logger, server_loop
from NetUtils import ClientStatus

from .locations import LOCATION_NAME_TO_ID

if TYPE_CHECKING:
    import kvui

CONNECTION_REFUSED_GAME_STATUS = (
    "Dolphin failed to connect. Please load a patched ROM for Mario Super Sluggers. Trying again in 5 seconds..."
)
CONNECTION_REFUSED_SAVE_STATUS = (
    "Dolphin failed to connect. Please load into the save file. Trying again in 5 seconds..."
)
CONNECTION_LOST_STATUS = (
    "Dolphin connection was lost. Please restart your emulator and make sure Mario Super Sluggers is running."
)
CONNECTION_CONNECTED_STATUS = "Dolphin connected successfully."
CONNECTION_INITIAL_STATUS = "Dolphin connection has not been initiated."

WORLD_VERSION = Utils.tuplize_version("1.0.0")
WORLD_BACKCOMPAT_MIN_VERSION = Utils.tuplize_version("1.0.0")

# The expected index for the following item that should be received.
EXPECTED_INDEX_ADDR = 0x80E55000

IN_GAME_FLAG = 0x80E55D59
GOAL_FLAG = [0x80E55C04, 0x80E55B3B, 0x80E55B3A, 0x80E55B36]
COIN_COUNT = 0x80E55C0A
ITEM_COUNTS = [0x80E55DAC, 0x80E55DAD, 0x80E55DAE, 0x80E55DAF, 0x80E55DB0, 0x80E55DB1, 0x80E55DB2]
CURR_STAGE = 0x80E55D89
CURR_MISSION = 0x80E55DBC
TEAM_BASE = 0x80E55C10
DAY_NIGHT = 0x80E55AE0
IS_NIGHT = 0x80E55DC1
AUTO_NIGHT = 0x802076CB
BOWSER_ACTIVE = 0x80E55D3A
BABY_DAISY_CHECK = 0x80E55B29
RATTLE_ACTIVE = 0x80E55D4C

FLAG_BYTE_MIN = 0x80E55D59
FLAG_BYTE_MAX = 0x80E55D61

STAGE_NAMES = {
    0: "Baseball Kingdom",
    1: "Mario Stadium",
    2: "Peach Ice Garden",
    5: "DK Jungle",
    9: "Wario City",
    10: "Yoshi Park"
}

SAFE_MISSIONS = [0x00, 0x01, 0x02, 0x0F, 0x12, 0x13, 0x14, 0x15, 0x24, 0x29, 0x2F, 0x31]

MISSION_OPPONENT = 0x80E55C0E
CHARACTERS = [
    0x80E552E9, 0x80E552EA, 0x80E552EB, 0x80E552EC, 0x80E552ED, 0x80E552EE, 0x80E552EF, 0x80E552F0, 0x80E552F1,
    0x80E552F3, 0x80E552F4, 0x80E552F5, 0x80E552F6, 0x80E552F7, 0x80E552F8, 0x80E552F9, 0x80E552FA, 0x80E552FB,
    0x80E552FD, 0x80E552FE, 0x80E552FF, 0x80E55300, 0x80E55301, 0x80E55302, 0x80E55303, 0x80E55305, 0x80E55306,
    0x80E55307, 0x80E55308, 0x80E55309, 0x80E5530E, 0x80E5530F, 0x80E55310, 0x80E55311, 0x80E55312, 0x80E55313,
    0x80E55314, 0x80E55315, 0x80E55316, 0x80E55317, 0x80E55318, 0x80E5531F, 0x80E55320, 0x80E55321, 0x80E55322,
    0x80E55323, 0x80E55324, 0x80E55325, 0x80E55326, 0x80E55327, 0x80E55328, 0x80E55329, 0x80E5532A, 0x80E5532B,
    0x80E5532C, 0x80E5532D, 0x80E5532E, 0x80E5532F
]
CAPTAINS = [
    0x80E552E9, 0x80E552EA, 0x80E552EB, 0x80E552EC, 0x80E552ED, 0x80E552EE, 0x80E552EF, 0x80E552F3, 0x80E552F4,
    0x80E552FA
]

CHEMISTRY_MISSIONS = [0x2A, 0x2B, 0x3A, 0x3B, 0x3C, 0x3D, 0x3E, 0x3F, 0x40, 0x41]
CHEMISTRY_PAIRS = [
    [0x80E552E9,0x80E552EA],
    [0x80E552E9,0x80E552ED],
    [0x80E552E9,0x80E552EF],
    [0x80E552E9,0x80E552FE],
    [0x80E552E9,0x80E552FF],
    [0x80E552E9,0x80E55300],
    [0x80E552E9,0x80E55301],
    [0x80E552E9,0x80E55302],
    [0x80E552E9,0x80E55303],
    [0x80E552E9,0x80E5532B],
    [0x80E552E9,0x80E5532C],
    [0x80E552E9,0x80E5532D],
    [0x80E552E9,0x80E5532E],
    [0x80E552E9,0x80E5532F],
    [0x80E552EA,0x80E552EE],
    [0x80E552EB,0x80E552EC],
    [0x80E552EB,0x80E55310],
    [0x80E552EB,0x80E55321],
    [0x80E552EB,0x80E55322],
    [0x80E552EC,0x80E55310],
    [0x80E552EC,0x80E55321],
    [0x80E552EC,0x80E55322],
    [0x80E552ED,0x80E552EE],
    [0x80E552ED,0x80E552F6],
    [0x80E552ED,0x80E552F8],
    [0x80E552ED,0x80E55305],
    [0x80E552ED,0x80E55306],
    [0x80E552ED,0x80E55307],
    [0x80E552ED,0x80E55308],
    [0x80E552ED,0x80E55309],
    [0x80E552EE,0x80E552FA],
    [0x80E552EF,0x80E552F0],
    [0x80E552EF,0x80E552F1],
    [0x80E552EF,0x80E552FA],
    [0x80E552EF,0x80E55328],
    [0x80E552EF,0x80E55329],
    [0x80E552EF,0x80E5532A],
    [0x80E552F0,0x80E552F1],
    [0x80E552F0,0x80E55328],
    [0x80E552F0,0x80E55329],
    [0x80E552F0,0x80E5532A],
    [0x80E552F0,0x80E5532B],
    [0x80E552F0,0x80E5532C],
    [0x80E552F0,0x80E5532D],
    [0x80E552F0,0x80E5532E],
    [0x80E552F0,0x80E5532F],
    [0x80E552F1,0x80E55328],
    [0x80E552F1,0x80E55329],
    [0x80E552F1,0x80E5532A],
    [0x80E552F1,0x80E5532B],
    [0x80E552F1,0x80E5532C],
    [0x80E552F1,0x80E5532D],
    [0x80E552F1,0x80E5532E],
    [0x80E552F1,0x80E5532F],
    [0x80E552F3,0x80E552F4],
    [0x80E552F5,0x80E552FD],
    [0x80E552F5,0x80E55311],
    [0x80E552F5,0x80E55314],
    [0x80E552F6,0x80E552F8],
    [0x80E552F6,0x80E552FE],
    [0x80E552F6,0x80E552FF],
    [0x80E552F6,0x80E55300],
    [0x80E552F6,0x80E55305],
    [0x80E552F6,0x80E55328],
    [0x80E552F7,0x80E552F9],
    [0x80E552F7,0x80E5530E],
    [0x80E552F7,0x80E55315],
    [0x80E552F7,0x80E55316],
    [0x80E552F7,0x80E55317],
    [0x80E552F7,0x80E55318],
    [0x80E552F7,0x80E55320],
    [0x80E552F8,0x80E552FA],
    [0x80E552F8,0x80E55301],
    [0x80E552F8,0x80E55302],
    [0x80E552F8,0x80E55303],
    [0x80E552F8,0x80E55305],
    [0x80E552F8,0x80E55306],
    [0x80E552F8,0x80E55307],
    [0x80E552F8,0x80E55308],
    [0x80E552F8,0x80E55309],
    [0x80E552F9,0x80E552FA],
    [0x80E552F9,0x80E552FB],
    [0x80E552FA,0x80E5530F],
    [0x80E552FA,0x80E55315],
    [0x80E552FA,0x80E55316],
    [0x80E552FA,0x80E55317],
    [0x80E552FA,0x80E55318],
    [0x80E552FA,0x80E5532B],
    [0x80E552FA,0x80E5532C],
    [0x80E552FA,0x80E5532D],
    [0x80E552FA,0x80E5532E],
    [0x80E552FA,0x80E5532F],
    [0x80E552FB,0x80E55311],
    [0x80E552FB,0x80E55312],
    [0x80E552FB,0x80E55315],
    [0x80E552FB,0x80E55316],
    [0x80E552FB,0x80E55317],
    [0x80E552FB,0x80E55318],
    [0x80E552FD,0x80E55312],
    [0x80E552FD,0x80E55313],
    [0x80E552FE,0x80E55301],
    [0x80E552FE,0x80E55302],
    [0x80E552FE,0x80E55303],
    [0x80E552FE,0x80E55305],
    [0x80E552FE,0x80E55306],
    [0x80E552FE,0x80E55307],
    [0x80E552FE,0x80E55308],
    [0x80E552FE,0x80E55309],
    [0x80E552FF,0x80E55301],
    [0x80E552FF,0x80E55302],
    [0x80E552FF,0x80E55303],
    [0x80E552FF,0x80E55305],
    [0x80E552FF,0x80E55306],
    [0x80E552FF,0x80E55307],
    [0x80E552FF,0x80E55308],
    [0x80E552FF,0x80E55309],
    [0x80E55300,0x80E55301],
    [0x80E55300,0x80E55302],
    [0x80E55300,0x80E55303],
    [0x80E55300,0x80E55305],
    [0x80E55300,0x80E55306],
    [0x80E55300,0x80E55307],
    [0x80E55300,0x80E55308],
    [0x80E55300,0x80E55309],
    [0x80E55305,0x80E55306],
    [0x80E55305,0x80E55307],
    [0x80E55305,0x80E55308],
    [0x80E55305,0x80E55309],
    [0x80E55305,0x80E55328],
    [0x80E55306,0x80E55328],
    [0x80E55307,0x80E55328],
    [0x80E55308,0x80E55328],
    [0x80E55309,0x80E55328],
    [0x80E5530E,0x80E5530F],
    [0x80E5530E,0x80E5531F],
    [0x80E5530E,0x80E55327],
    [0x80E5530F,0x80E5531F],
    [0x80E5530F,0x80E55320],
    [0x80E55310,0x80E55321],
    [0x80E55310,0x80E55322],
    [0x80E55310,0x80E5532A],
    [0x80E55311,0x80E55312],
    [0x80E55311,0x80E55313],
    [0x80E55312,0x80E55314],
    [0x80E55313,0x80E55314],
    [0x80E5531F,0x80E55320],
    [0x80E55321,0x80E55322],
    [0x80E55321,0x80E5532A],
    [0x80E55322,0x80E5532A],
    [0x80E55323,0x80E55327],
    [0x80E55324,0x80E55327],
    [0x80E55325,0x80E55327],
    [0x80E55326,0x80E55327],
    [0x80E55328,0x80E55329],
    [0x80E55328,0x80E5532A],
    [0x80E55328,0x80E5532B],
    [0x80E55328,0x80E5532C],
    [0x80E55328,0x80E5532D],
    [0x80E55328,0x80E5532E],
    [0x80E55328,0x80E5532F],
    [0x80E55329,0x80E5532A],
    [0x80E55329,0x80E5532B],
    [0x80E55329,0x80E5532C],
    [0x80E55329,0x80E5532D],
    [0x80E55329,0x80E5532E],
    [0x80E55329,0x80E5532F],
    [0x80E5532A,0x80E5532B],
    [0x80E5532A,0x80E5532C],
    [0x80E5532A,0x80E5532D],
    [0x80E5532A,0x80E5532E],
    [0x80E5532A,0x80E5532F]
]

MISSION_COUNTS = {
    0x07: 9,
    0x08: 12,
    0x0E: 9,
    0x10: 10,
    0x16: 9,
    0x17: 9,
    0x18: 9,
    0x19: 11,
    0x1A: 11,
    0x1B: 3,
    0x1C: 3,
    0x1D: 4,
    0x1E: 3,
    0x1F: 2,
    0x20: 9,
    0x21: 9,
    0x2A: 3,
    0x2B: 3,
    0x2C: 3,
    0x2D: 3,
    0x2E: 3,
    0x30: 4,
    0x32: 3,
    0x33: 3,
    0x34: 3,
    0x35: 3,
    0x36: 3,
    0x37: 3,
    0x38: 3,
    0x39: 3,
    0x3A: 3,
    0x3B: 3,
    0x3C: 3,
    0x3D: 3,
    0x3E: 3,
    0x3F: 3,
    0x40: 3,
    0x41: 3,
}

MISSION_CAPTAINS = [0x0E, 0x10, 0x16, 0x17, 0x18, 0x19, 0x1A, 0x20, 0x21]

MISSION_CHARS = {
    0x1B: [0x80E552EA, 0x80E552F1, 0x80E552FD, 0x80E55312, 0x80E55314],
    0x1C: [0x80E55301, 0x80E55302, 0x80E55303, 0x80E55311],
    0x2C: [0x80E552EF, 0x80E5532B, 0x80E5532C, 0x80E5532D, 0x80E5532E, 0x80E5532F],
    0x2D: [0x80E552EE, 0x80E552F9, 0x80E55315, 0x80E55316, 0x80E55317, 0x80E55318],
    0x32: [0x80E552EA, 0x80E552F1, 0x80E552FD, 0x80E55312, 0x80E55314],
    0x33: [0x80E552EA, 0x80E552F1, 0x80E552FD, 0x80E55312, 0x80E55314],
    0x34: [0x80E552EA, 0x80E552F1, 0x80E552FD, 0x80E55312, 0x80E55314],
    0x35: [0x80E552EA, 0x80E552F1, 0x80E552FD, 0x80E55312, 0x80E55314],
}

ZERO_SHORTS = [0x8078FAD8]

CUSTOM_BYTES = {
    0x80E55AE9: 0x02,
    0x80E55DBA: 0x01
}

SHOP_WORDS = {
    0x8078FBC0: 0x00000000,
}

CUTSCENES = [
    0x80E55C0901, 0x80E55C9201, 0x80E55C9701, 0x80E55C9D01, 0x80E55C9E01, 0x80E55CA001, 0x80E55CA101, 0x80E55CA301,
    0x80E55CA401, 0x80E55CAB01, 0x80E55CAC01, 0x80E55CAD01, 0x80E55CAE01, 0x80E55CB201, 0x80E55CB501, 0x80E55CBB01,
    0x80E55CBC01, 0x80E55CBE01, 0x80E55D3D02, 0x80E55D3E01, 0x80E55D4901, 0x80E55D4A01, 0x80E55D4C07, 0x80E55D4DF6,
    0x80E55D4F01, 0x80E55D51C1, 0x80E55D52C0, 0x80E55D5378
]

class MarioSuperSluggersCommandProcessor(ClientCommandProcessor):
    """
    Command Processor for Mario Super Sluggers client commands.

    This class handles commands specific to Mario Super Sluggers.
    """

    def __init__(self, ctx: SuperContext):
        """
        Initialize the command processor with the provided context.

        :param ctx: Context for the client.
        """
        super().__init__(ctx)

    def _cmd_dolphin(self) -> None:
        """
        Display the current Dolphin emulator connection status.
        """
        if isinstance(self.ctx, MarioSuperSluggersContext):
            logger.info(f"Dolphin Status: {self.ctx.dolphin_status}")

    def _cmd_reset_mission(self) -> None:
        """
        Reset the current mission to an alternative if no unlocked character can complete the mission.
        """
        if isinstance(self.ctx, MarioSuperSluggersContext) and \
            dolphin_memory_engine.is_hooked() and self.ctx.dolphin_status == CONNECTION_CONNECTED_STATUS:
            dolphin_memory_engine.write_byte(CURR_MISSION, random.choice(SAFE_MISSIONS))
            logger.info("Changed mission.")
        else:
            logger.info("Dolphin not connected.")

class MarioSuperSluggersContext(SuperContext):
    """
    The context for the Mario Super Sluggers client.

    This class manages all interactions with the Dolphin emulator and the Archipelago server for Mario Super Sluggers.
    """

    command_processor = MarioSuperSluggersCommandProcessor
    game = "Mario Super Sluggers"
    items_handling = 0b111
    tags = {"AP"}

    def __init__(self, server_address: Optional[str], password: Optional[str]) -> None:
        """
        Initialize the MarioSuperSluggers context.

        :param server_address: Address of the Archipelago server.
        :param password: Password for server authentication.
        """

        super().__init__(server_address, password)
        self.dolphin_sync_task: Optional[asyncio.Task[None]] = None
        self.dolphin_status: str = CONNECTION_INITIAL_STATUS

        self.goal_condition: int = 0
        self.goal_characters: int = 72
        self.randomize_shops: int = 0
        self.reduced_cutscenes: bool = False
        self.current_stage_name: str = "Baseball Kingdom"
        self.world_version: Utils.Version = WORLD_VERSION

        # Length of the item get array in memory.
        self.len_give_item_array: int = 0x10

    async def disconnect(self, allow_autoreconnect: bool = False) -> None:
        """
        Disconnect the client from the server and reset game state variables.

        :param allow_autoreconnect: Allow the client to auto-reconnect to the server. Defaults to `False`.
        """
        self.auth = None
        self.goal_characters = 72
        self.world_version = WORLD_VERSION
        await super().disconnect(allow_autoreconnect)

    async def server_auth(self, password_requested: bool = False) -> None:
        """
        Authenticate with the Archipelago server.

        :param password_requested: Whether the server requires a password. Defaults to `False`.
        """
        if password_requested and not self.password:
            await super().server_auth(password_requested)
        await self.get_username()
        await self.send_connect()

    def on_package(self, cmd: str, args: dict[str, Any]) -> None:
        """
        Handle incoming packages from the server.

        :param cmd: The command received from the server.
        :param args: The command arguments.
        """
        if cmd == "Connected":
            if "goal_condition" in args["slot_data"]: self.goal_condition = args["slot_data"]["goal_condition"]
            self.goal_characters = args["slot_data"]["goal_characters"]
            if "randomize_shops" in args["slot_data"]: self.randomize_shops = args["slot_data"]["randomize_shops"]
            self.reduced_cutscenes = args["slot_data"]["reduced_cutscenes"]
            self.world_version = Utils.tuplize_version(args["slot_data"]["world_version"])
            if self.world_version > WORLD_VERSION:
                logger.error("This multiworld was generated on a newer APWorld version ({self.world_version} vs "
                             "{WORLD_VERSION}). Please update your APWorld installation before connecting.")
                self.disconnect()
                return
            elif self.world_version < WORLD_BACKCOMPAT_MIN_VERSION:
                logger.error("This multiworld was generated on an older APWorld version ({self.world_version} vs "
                             "{WORLD_VERSION}). Please downgrade to a compatible version before connecting.")
                self.disconnect()
                return
            elif self.world_version < WORLD_VERSION:
                logger.warning("This multiworld was generated on an older APWorld version ({self.world_version} vs "
                               "{WORLD_VERSION}). Please let the host know to update their APWorld installation.")
            if dolphin_memory_engine.is_hooked() and self.dolphin_status == CONNECTION_CONNECTED_STATUS:
                if check_ingame():
                    init_game(self)
        super().on_package(cmd, args)

    def make_gui(self) -> type["kvui.GameManager"]:
        """
        Initialize the GUI for Mario Super Sluggers client.

        :return: The client's GUI.
        """
        ui = super().make_gui()
        ui.base_title = "Archipelago Mario Super Sluggers Client"
        return ui


def read_short(console_address: int) -> int:
    """
    Read a 2-byte short from Dolphin memory.

    :param console_address: Address to read from.
    :return: The value read from memory.
    """
    return int.from_bytes(dolphin_memory_engine.read_bytes(console_address, 2), byteorder="big")


def write_short(console_address: int, value: int) -> None:
    """
    Write a 2-byte short to Dolphin memory.

    :param console_address: Address to write to.
    :param value: Value to write.
    """
    dolphin_memory_engine.write_bytes(console_address, value.to_bytes(2, byteorder="big"))


def read_string(console_address: int, strlen: int) -> str:
    """
    Read a string from Dolphin memory.

    :param console_address: Address to start reading from.
    :param strlen: Length of the string to read.
    :return: The string.
    """
    return dolphin_memory_engine.read_bytes(console_address, strlen).split(b"\0", 1)[0].decode()


def _give_item(item_id: int) -> bool:
    """
    Give an item to the player in-game.

    :param ctx: Mario Super Sluggers client context.
    :param item_id: ID of the item to give.
    :return: Whether the item was successfully given.
    """
    if not check_ingame():
        return False

    addr = item_id >> 8
    value = item_id % 0x100

    if addr == COIN_COUNT:
        write_short(addr, min(read_short(addr) + value, 999))
    elif addr in ITEM_COUNTS:
        dolphin_memory_engine.write_byte(addr, min(dolphin_memory_engine.read_byte(addr) + value, 99))
    else:
        dolphin_memory_engine.write_byte(addr, value)

    if addr == DAY_NIGHT:
        dolphin_memory_engine.write_byte(AUTO_NIGHT, value)

    return True


async def give_items(ctx: MarioSuperSluggersContext) -> None:
    """
    Give the player all outstanding items they have yet to receive.

    :param ctx: Mario Super Sluggers client context.
    """
    if check_ingame():
        # Read the expected index of the player, which is the index of the next item they're expecting to receive.
        # The expected index starts at 0 for a fresh save file.

        expected_idx = read_short(EXPECTED_INDEX_ADDR)

        # Check if there are new items.
        received_items = ctx.items_received
        if len(received_items) <= expected_idx:
            # There are no new items.
            return

        # Loop through items to give.
        # Give the player all items at an index greater than or equal to the expected index.
        for idx, item in enumerate(received_items[expected_idx:], start=expected_idx):
            # Attempt to give the item and increment the expected index.
            while not _give_item(item.item):
                await asyncio.sleep(0.01)

            # Increment the expected index.
            write_short(EXPECTED_INDEX_ADDR, idx + 1)


async def check_locations(ctx: MarioSuperSluggersContext) -> None:
    """
    Iterate through all locations and check whether the player has checked each location.

    Update the server with all newly checked locations since the last update. If the player has completed the goal,
    notify the server.

    :param ctx: Mario Super Sluggers client context.
    """
    if not check_ingame():
        return
    # Loop through all locations to see if each has been checked.
    for id in LOCATION_NAME_TO_ID.values():
        checked = False
        addr = id >> 8
        value = id % 0x100
        if addr >= FLAG_BYTE_MIN and addr <= FLAG_BYTE_MAX:
            checked = dolphin_memory_engine.read_byte(addr) & value == 0
        else:
            checked = dolphin_memory_engine.read_byte(addr) == value
            if addr == BABY_DAISY_CHECK and checked:
                dolphin_memory_engine.write_byte(RATTLE_ACTIVE, dolphin_memory_engine.read_byte(RATTLE_ACTIVE) | 0x20)

        if checked:
            ctx.locations_checked.add(id)

    if not ctx.finished_game and dolphin_memory_engine.read_byte(GOAL_FLAG[ctx.goal_condition]) == 1:
        await ctx.send_msgs([{"cmd": "StatusUpdate", "status": ClientStatus.CLIENT_GOAL}])
        ctx.finished_game = True

    # Send the list of newly-checked locations to the server.
    locations_checked = ctx.locations_checked.difference(ctx.checked_locations)
    if locations_checked:
        await ctx.send_msgs([{"cmd": "LocationChecks", "locations": locations_checked}])


async def check_current_stage_changed(ctx: MarioSuperSluggersContext) -> None:
    """
    Check if the player has moved to a new stage.
    If so, update all trackers with the new stage name.
    If the game is set to night, additionally allow Bowser to be fought.

    :param ctx: Mario Super Sluggers client context.
    """
    new_stage = dolphin_memory_engine.read_byte(CURR_STAGE)
    new_stage_name = STAGE_NAMES[new_stage] if new_stage in STAGE_NAMES else "Baseball Kingdom"

    current_stage_name = ctx.current_stage_name
    if new_stage_name != current_stage_name:
        ctx.current_stage_name = new_stage_name
        # Send a Bounced message containing the new stage name to all trackers connected to the current slot.
        data_to_send = {"MarioSuperSluggers_stage_name": new_stage_name}
        message = {
            "cmd": "Bounce",
            "slots": [ctx.slot],
            "data": data_to_send,
        }
        await ctx.send_msgs([message])

    dolphin_memory_engine.write_byte(BOWSER_ACTIVE, dolphin_memory_engine.read_byte(IS_NIGHT) * 2)


async def check_mission_condition() -> None:
    """
    Check if the player is in a mission that requires specific characters.
    If so, check if the characters are available and change the mission to something neutral if not.

    :param ctx: Mario Super Sluggers client context.
    """
    mission = dolphin_memory_engine.read_byte(CURR_MISSION)
    opponent = read_short(MISSION_OPPONENT)
    if mission in MISSION_CHARS:
        valid = False
        for char in MISSION_CHARS[mission]:
            valid = char - CHARACTERS[0] != opponent and dolphin_memory_engine.read_byte(char) == 2
            if valid: break
        if not valid:
            dolphin_memory_engine.write_byte(CURR_MISSION, random.choice(SAFE_MISSIONS))
            return
    if mission in MISSION_COUNTS:
        unlocked = {
            addr: dolphin_memory_engine.read_byte(addr) if addr - CHARACTERS[0] != opponent else 0 for addr in CHARACTERS
        }
        valid = len([1 for x in unlocked if unlocked[x] == 0x02]) >= MISSION_COUNTS[mission] and\
            (not mission in MISSION_CAPTAINS or len([1 for x in CAPTAINS if unlocked[x] == 0x02]) >= 2)
        if not valid:
            dolphin_memory_engine.write_byte(CURR_MISSION, random.choice(SAFE_MISSIONS))
            return
    if mission in CHEMISTRY_MISSIONS:
        valid = False
        for pair in CHEMISTRY_PAIRS:
            valid = pair[0] - CHARACTERS[0] != opponent and pair[1] - CHARACTERS[0] != opponent and\
                dolphin_memory_engine.read_byte(pair[0]) == 2 and dolphin_memory_engine.read_byte(pair[1]) == 2
            if valid: break
        if not valid:
            dolphin_memory_engine.write_byte(CURR_MISSION, random.choice(SAFE_MISSIONS))


def check_ingame() -> bool:
    """
    Check if the player is currently in-game.

    :return: `True` if the player is in-game, otherwise `False`.
    """
    # Currently have not found a relevant flag to check, so checking Mario Stadium coin flags for time being...
    return dolphin_memory_engine.read_byte(IN_GAME_FLAG) != 0


def init_game(ctx: MarioSuperSluggersContext):
    ctx.locations_checked = set()
    for addr in ZERO_SHORTS:
        write_short(addr, 0)
    for addr in CUSTOM_BYTES:
        dolphin_memory_engine.write_byte(addr, CUSTOM_BYTES[addr])
    if ctx.randomize_shops == 2:
        for addr in SHOP_WORDS:
            dolphin_memory_engine.write_word(addr, SHOP_WORDS[addr])
    if ctx.reduced_cutscenes:
        for i in CUTSCENES:
            addr = i >> 8
            value = i % 0x100
            dolphin_memory_engine.write_byte(addr, dolphin_memory_engine.read_byte(addr) | value)
    dolphin_memory_engine.write_byte(AUTO_NIGHT, 0)


async def dolphin_sync_task(ctx: MarioSuperSluggersContext) -> None:
    """
    The task loop for managing the connection to Dolphin.

    While connected, read the emulator's memory to look for any relevant changes made by the player in the game.

    :param ctx: Mario Super Sluggers client context.
    """
    logger.info("Starting Dolphin connector. Use /dolphin for status information.")
    sleep_time = 0.0
    while not ctx.exit_event.is_set():
        if sleep_time > 0.0:
            try:
                # ctx.watcher_event gets set when receiving ReceivedItems or LocationInfo, or when shutting down.
                await asyncio.wait_for(ctx.watcher_event.wait(), sleep_time)
            except asyncio.TimeoutError:
                pass
            sleep_time = 0.0
        ctx.watcher_event.clear()

        try:
            if dolphin_memory_engine.is_hooked() and ctx.dolphin_status == CONNECTION_CONNECTED_STATUS:
                if not check_ingame():
                    sleep_time = 0.1
                    continue
                if ctx.slot is not None:
                    await give_items(ctx)
                    await check_locations(ctx)
                    await check_current_stage_changed(ctx)
                    await check_mission_condition()
                sleep_time = 0.1
            else:
                if ctx.dolphin_status == CONNECTION_CONNECTED_STATUS:
                    logger.info("Connection to Dolphin lost, reconnecting...")
                    ctx.dolphin_status = CONNECTION_LOST_STATUS
                logger.info("Attempting to connect to Dolphin...")
                dolphin_memory_engine.hook()
                if dolphin_memory_engine.is_hooked():
                    if dolphin_memory_engine.read_bytes(0x80000000, 6) != b"RMBE01" or\
                        dolphin_memory_engine.read_bytes(0x80000010, 2) != b"AP":
                        logger.info(CONNECTION_REFUSED_GAME_STATUS)
                        ctx.dolphin_status = CONNECTION_REFUSED_GAME_STATUS
                        dolphin_memory_engine.un_hook()
                        sleep_time = 5
                    elif not check_ingame():
                        logger.info("Connected to Dolphin, waiting for challenge mode...")
                        sleep_time = 5
                    else:
                        init_game(ctx)
                        logger.info(CONNECTION_CONNECTED_STATUS)
                        ctx.dolphin_status = CONNECTION_CONNECTED_STATUS
                        ctx.locations_checked = set()
                else:
                    logger.info("Connection to Dolphin failed, attempting again in 5 seconds...")
                    ctx.dolphin_status = CONNECTION_LOST_STATUS
                    await ctx.disconnect()
                    sleep_time = 5
                    continue
        except Exception:
            dolphin_memory_engine.un_hook()
            logger.info("Connection to Dolphin failed, attempting again in 5 seconds...")
            logger.error(traceback.format_exc())
            ctx.dolphin_status = CONNECTION_LOST_STATUS
            await ctx.disconnect()
            sleep_time = 5
            continue


def main(connect: Optional[str] = None, password: Optional[str] = None) -> None:
    """
    Run the main async loop for the Mario Super Sluggers client.

    :param connect: Address of the Archipelago server.
    :param password: Password for server authentication.
    """
    Utils.init_logging("Mario Super Sluggers Client")

    async def _main(connect: Optional[str], password: Optional[str]) -> None:
        ctx = MarioSuperSluggersContext(connect, password)
        ctx.server_task = asyncio.create_task(server_loop(ctx), name="ServerLoop")
        if gui_enabled:
            ctx.run_gui()
        ctx.run_cli()
        await asyncio.sleep(1)

        ctx.dolphin_sync_task = asyncio.create_task(dolphin_sync_task(ctx), name="DolphinSync")

        await ctx.exit_event.wait()
        # Wake the sync task, if it is currently sleeping, so it can start shutting down when it sees that the
        # exit_event is set.
        ctx.watcher_event.set()
        ctx.server_address = None

        await ctx.shutdown()

        if ctx.dolphin_sync_task:
            await ctx.dolphin_sync_task

    import colorama

    colorama.init()
    asyncio.run(_main(connect, password))
    colorama.deinit()


if __name__ == "__main__":
    parser = get_base_parser()
    args = parser.parse_args()
    main(args.connect, args.password)
