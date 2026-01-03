import asyncio
import traceback
from typing import TYPE_CHECKING, Any, Optional

import dolphin_memory_engine

import Utils
from CommonClient import ClientCommandProcessor, CommonContext, get_base_parser, gui_enabled, logger, server_loop
from NetUtils import ClientStatus

from .locations import LOCATION_NAME_TO_ID

if TYPE_CHECKING:
    import kvui

CONNECTION_REFUSED_GAME_STATUS = (
    "Dolphin failed to connect. Please load a ROM for Mario Super Sluggers. Trying again in 5 seconds..."
)
CONNECTION_REFUSED_SAVE_STATUS = (
    "Dolphin failed to connect. Please load into the save file. Trying again in 5 seconds..."
)
CONNECTION_LOST_STATUS = (
    "Dolphin connection was lost. Please restart your emulator and make sure Mario Super Sluggers is running."
)
CONNECTION_CONNECTED_STATUS = "Dolphin connected successfully."
CONNECTION_INITIAL_STATUS = "Dolphin connection has not been initiated."

WORLD_VERSION = Utils.tuplize_version("0.0.0")

# The expected index for the following item that should be received.
EXPECTED_INDEX_ADDR = 0x80E55000

IN_GAME_FLAG = 0x80E55D59
GOAL_FLAG = 0x80E55C04
COIN_COUNT = 0x80E55C0A
CURR_STAGE = 0x80E55D89
CURR_MISSION = 0x80E55DBC
REQ_CHARS = [0x80205F57, 0x801E8E2B, 0x801ABC2B, 0x801AB6E7]
CURR_CAPTAIN = 0x80E55C2B
CHAR_BASE = 0x80E552E9
TEAM_BASE = 0x80E55C10
DAY_NIGHT = 0x80E55AE0
IS_NIGHT = 0x80E55DC1
AUTO_NIGHT = 0x802076CB
BOWSER_ACTIVE = 0x80E55D3A

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

MISSION_CHARS = {
    0x1C: [0x80E55301, 0x80E55302, 0x80E55303, 0x80E55311],
    0x2C: [0x80E552EF, 0x80E5532B, 0x80E5532C, 0x80E5532D, 0x80E5532E, 0x80E5532F],
    0x2D: [0x80E552EE, 0x80E552F9, 0x80E55315, 0x80E55316, 0x80E55317, 0x80E55318],
    0x33: [0x80E552EA, 0x80E552F1, 0x80E552FD, 0x80E55312, 0x80E55314],
    0x34: [0x80E552EA, 0x80E552F1, 0x80E552FD, 0x80E55312, 0x80E55314]
}

MOVED_FLAGS = [
    0x8006BABA, 0x801945B6, 0x80194626, 0x801964E2, 0x80196C62, 0x80196CAE, 0x801BE38E, 0x801C3F22, 0x801C4196,
    0x801C41B6, 0x801C41D6, 0x801C41F6, 0x801C4216, 0x801C4236, 0x801C4256, 0x801D9526, 0x801D954A, 0x801D956E,
    0x801D9592, 0x801D95B6, 0x801D95DA, 0x801D95FE, 0x801E304E, 0x801E34A2, 0x801E824E, 0x801E8272, 0x801E8DF6,
    0x801EBCFE, 0x801EBD1A, 0x801EEBB6, 0x801EEBD6, 0x801EEBFA, 0x801EEC1E, 0x801EEC42, 0x801EEECA, 0x801F4BC6,
    0x801F524E, 0x801F5A0A, 0x801F5D62, 0x801F69EE, 0x801F768E, 0x802024AA, 0x80202522, 0x8020253A, 0x802025B2,
    0x802025BE, 0x80202636, 0x80203382, 0x8020BCBA, 0x8020BCC6, 0x8020BF36, 0x8020C43A, 0x8020EEAE
]

ZERO_SHORTS = [
    0x806564AA, 0x80657A3C, 0x80657A3E, 0x80657A40, 0x80657A42, 0x80657A44, 0x80657A46, 0x80657A48, 0x80657A4A,
    0x80657A4C, 0x80657A4E, 0x80657A50, 0x80657A52, 0x80657A54, 0x80657A56, 0x80657A70, 0x80657A72, 0x80657A74,
    0x80657A76, 0x80657A78, 0x80657A7A, 0x80657A7C, 0x80657A7E, 0x80657A80, 0x80657A82, 0x80657A84, 0x80657A86,
    0x80657A88, 0x80657A8A, 0x80657A8C, 0x80657A8E, 0x80657A90, 0x80657A7C, 0x80657AB4, 0x80657AB6, 0x80657AB8,
    0x80657ABA, 0x80657AC0, 0x80657AC2, 0x80657AC4, 0x80657AC6, 0x80657AC8, 0x80657ACA, 0x80657AD8, 0x80657ADA,
    0x80657ADC, 0x80657ADE, 0x80657AE0, 0x80657AE2, 0x80657AE4, 0x80657AE6, 0x80657AE8, 0x80657AEA, 0x80657AEC,
    0x80657AEE, 0x80657AF0, 0x80657AF2, 0x80657AF4, 0x80657AF6, 0x80657AF8, 0x80657AFA, 0x80657AFC, 0x80657AFE,
    0x80657B0C, 0x80657B0E, 0x80657B10, 0x80657B12, 0x80657B14, 0x80657B16, 0x80657B18, 0x80657B1A, 0x80657B1C,
    0x80657B1E, 0x8078FAD8
]

NOPS = [0x801E0270, 0x801E3114, 0x801E4AF8, 0x801E4B74, 0x801E6684, 0x802390F8]

BRANCH = [0x801E8E18]

CUSTOM_BYTES = {
    0x80214815: 0x96
}

CUSTOM_WORDS = {
    0x8020F99C: 0x8803024C,
    0x8020EDC0: 0x388000AD,
    0x8020EDC4: 0x8803014F,
    0x8020EDC8: 0x2C000004,
    0x8020EDCC: 0x40820034,
    0x8020EDD0: 0x88030011,
    0x8020EDD4: 0x2C000002,
    0x8020EDD8: 0x40820028,
    0x8020EDDC: 0x38600001,
    0x8020EDE0: 0x987C01B5,
    0x8020EDE4: 0x881C01EF,
    0x8020EDE8: 0x2C000000,
    0x8020EDEC: 0x40820008,
    0x8020EDF0: 0x987C01EF,
    0x8020EDF4: 0x38000001,
    0x8020EDF8: 0x981503A0,
    0x8020EDFC: 0x38840001,
    0x8020EE00: 0x7F63DB78,
    0x8020EE04: 0x38A00001,
    0x8020EE08: 0x4BFB0489,
    0x8020EE0C: 0x60000000,
    0x80214898: 0x40820010,
    0x8021489C: 0x8803001B,
    0x802148A0: 0x2C000002,
    0x802148A4: 0x41820068
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

    def __init__(self, ctx: CommonContext):
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
        if dolphin_memory_engine.is_hooked() and self.ctx.dolphin_status == CONNECTION_CONNECTED_STATUS:
            dolphin_memory_engine.write_byte(CURR_MISSION, 0)
            logger.info("Changed mission.")
        else:
            logger.info("Dolphin not connected.")

class MarioSuperSluggersContext(CommonContext):
    """
    The context for the Mario Super Sluggers client.

    This class manages all interactions with the Dolphin emulator and the Archipelago server for Mario Super Sluggers.
    """

    command_processor = MarioSuperSluggersCommandProcessor
    game: str = "Mario Super Sluggers"
    items_handling: int = 0b111

    def __init__(self, server_address: Optional[str], password: Optional[str]) -> None:
        """
        Initialize the MarioSuperSluggers context.

        :param server_address: Address of the Archipelago server.
        :param password: Password for server authentication.
        """

        super().__init__(server_address, password)
        self.dolphin_sync_task: Optional[asyncio.Task[None]] = None
        self.dolphin_status: str = CONNECTION_INITIAL_STATUS

        self.starting_captain: int = 0
        self.goal_characters: int = 72
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
        self.starting_captain = 0
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
            self.goal_characters = args["slot_data"]["goal_characters"]
            self.starting_captain = args["slot_data"]["starting_captain"]
            self.reduced_cutscenes = args["slot_data"]["reduced_cutscenes"]
            self.world_version = Utils.tuplize_version(args["slot_data"]["world_version"])
            if self.world_version > WORLD_VERSION:
                logger.error("This multiworld was generated on a newer APWorld version. Please update your APWorld "
                             "installation.")
                self.disconnect()
                return
            elif self.world_version < WORLD_VERSION:
                logger.warning("This multiworld was generated on an older APWorld version. Please let the host know "
                               "to update their APWorld installation.")
            if dolphin_memory_engine.is_hooked() and self.dolphin_status == CONNECTION_CONNECTED_STATUS:
                if check_ingame():
                    init_game(self)

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
    else:
        dolphin_memory_engine.write_byte(addr, value)
        if value == 0x02 and read_short(TEAM_BASE + 0x10) == 0xFFFF:
            team_slot = TEAM_BASE
            while read_short(team_slot) != 0xFFFF:
                team_slot += 2
            write_short(team_slot, addr - CHAR_BASE)

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

        if checked:
            ctx.locations_checked.add(id)

    if not ctx.finished_game and dolphin_memory_engine.read_byte(GOAL_FLAG) == 1:
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
    if mission in MISSION_CHARS:
        valid = False
        for char in MISSION_CHARS[mission]:
            valid = dolphin_memory_engine.read_byte(char) == 2
            if valid: break
        if not valid:
            dolphin_memory_engine.write_byte(CURR_MISSION, 0)


def check_ingame() -> bool:
    """
    Check if the player is currently in-game.

    :return: `True` if the player is in-game, otherwise `False`.
    """
    # Currently have not found a relevant flag to check, so checking Mario Stadium coin flags for time being...
    return dolphin_memory_engine.read_byte(IN_GAME_FLAG) != 0


def init_game(ctx):
    ctx.locations_checked = set()
    for addr in REQ_CHARS:
        dolphin_memory_engine.write_byte(addr, ctx.goal_characters)
    for addr in MOVED_FLAGS:
        dolphin_memory_engine.write_byte(addr, dolphin_memory_engine.read_byte(addr) | 0xF8)
    for addr in ZERO_SHORTS:
        write_short(addr, 0)
    for addr in NOPS:
        dolphin_memory_engine.write_word(addr, 0x60000000)
    for addr in BRANCH:
        write_short(addr, 0x4800)
    for addr in CUSTOM_BYTES:
        dolphin_memory_engine.write_byte(addr, CUSTOM_BYTES[addr])
    for addr in CUSTOM_WORDS:
        dolphin_memory_engine.write_word(addr, CUSTOM_WORDS[addr])
    if ctx.reduced_cutscenes:
        for i in CUTSCENES:
            addr = i >> 8
            value = i % 0x100
            dolphin_memory_engine.write_byte(addr, dolphin_memory_engine.read_byte(addr) | value)
    dolphin_memory_engine.write_byte(CURR_CAPTAIN, ctx.starting_captain)
    write_short(TEAM_BASE, ctx.starting_captain)
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
                    if dolphin_memory_engine.read_bytes(0x80000000, 6) != b"RMBE01":
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
