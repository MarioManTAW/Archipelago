import asyncio
from logging import Logger, getLogger, setLoggerClass
import sys
from types import TracebackType
from typing import TYPE_CHECKING, Mapping, Optional

from CommonClient import ClientCommandProcessor, CommonContext, get_base_parser, server_loop

if TYPE_CHECKING:
    import kvui


def sm64ify(input: str, recent: str = "☺") -> tuple[str, str]:
    output: str = ""
    for x in input:
        if x in "!#%&*+,-.?":
            output += recent
        elif x.upper() in "JQVXZ":
            output += recent.upper() if x == x.upper() else recent.lower()
        elif x.upper() in "ABCDEFGHIKLMNOPRSTUWY0123456789":
            output += x
            recent = x
        elif x.strip() == "":
            output += x
        else:
            output += " "
    return (output, recent)


class TeetClientCommandProcessor(ClientCommandProcessor):
    def output(self, text: str):
        super().output(sm64ify(text))


class TeetClientContext(CommonContext):
    tags = CommonContext.tags | {"TextOnly"}
    game = ""  # empty matches any game since 0.3.2
    items_handling = 0b111  # receive all items for /received
    want_slot_data = False  # Can't use game specific slot_data

    def __init__(self, server_address: str | None = None, password: str | None = None) -> None:
        super().__init__(server_address, password)

    async def server_auth(self, password_requested: bool = False):
        if password_requested and not self.password:
            await super(TeetClientContext, self).server_auth(password_requested)
        await self.get_username()
        await self.send_connect(game="")

    def on_package(self, cmd: str, args: dict):
        if cmd == "Connected":
            self.game = self.slot_info[self.slot].game

    async def disconnect(self, allow_autoreconnect: bool = False):
        self.game = ""
        await super().disconnect(allow_autoreconnect)

    def on_print(self, args: dict):
        args["text"] = sm64ify(args["text"])[0]
        super().on_print(args)

    def on_print_json(self, args: dict):
        print(args)
        recent = "☺"
        for d in args["data"]:
            if "type" in d:
                if d["type"] == "player_id":
                    d["color"] = "magenta" if self.slot_concerns_self(int(d["text"])) else "yellow"
                    d["text"] = self.player_names[int(d["text"])]
                    d["type"] = "color"
                elif d["type"] == "item_id":
                    flags = d["flags"]
                    if flags == 0:
                        d["color"] = 'cyan'
                    elif flags & 0b001:  # advancement
                        d["color"] = 'plum'
                    elif flags & 0b010:  # useful
                        d["color"] = 'slateblue'
                    elif flags & 0b100:  # trap
                        d["color"] = 'salmon'
                    else:
                        d["color"] = 'cyan'
                    d["text"] = self.item_names.lookup_in_slot(int(d["text"]), d["player"])
                    d["type"] = "color"
                elif d["type"] == "location_id":
                    d["color"] = "green"
                    d["text"] = self.location_names.lookup_in_slot(int(d["text"]), d["player"])
                    d["type"] = "color"
            d["text"], recent = sm64ify(d["text"], recent)
        return super().on_print_json(args)
    
    def make_gui(self) -> type["kvui.GameManager"]:
        ui = super().make_gui()
        ui.base_title = "Archipelago Teet Client"
        return ui


def main(*args: str):
    async def _main(connect: Optional[str], password: Optional[str]):
        ctx = TeetClientContext(connect, password)
        ctx.server_task = asyncio.create_task(server_loop(ctx), name="server loop")

        if not sys.stdout or "--nogui" not in sys.argv:
            ctx.run_gui()
        ctx.run_cli()

        await ctx.exit_event.wait()
        await ctx.shutdown()

    import colorama

    parser = get_base_parser()
    parsed_args = parser.parse_args(args)

    colorama.init()
    asyncio.run(_main(parsed_args.connect, parsed_args.password))
    colorama.deinit()
