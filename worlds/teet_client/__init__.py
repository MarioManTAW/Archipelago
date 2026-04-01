from worlds.AutoWorld import World
from worlds.LauncherComponents import Component, Type, components, launch


def run_client(*args: str) -> None:
    from .client import main
    launch(main, name="TeetClient", args=args)


components.append(
    Component(
        "Teet Client",
        func=run_client,
        component_type=Type.CLIENT,
    )
)

class TeetClientWorld(World):
    """This Teet Client allows a small glimpse into a typical SM64 player s eeperience"""
    game = "Teet Client"
    item_name_to_id = {}
    location_name_to_id = {}
    
    @classmethod
    def stage_assert_generate(cls, multiworld):
        raise Exception("Teet Client cannot be used for generating worldss the client can instead connect to any slot from any world")
