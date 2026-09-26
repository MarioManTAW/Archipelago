from typing import Any, Dict

from BaseClasses import Tutorial
from worlds.AutoWorld import WebWorld, World
from . import items, locations, regions, rules, options


class ForestsEndWebWorld(WebWorld):
    theme = "jungle"

    setup_en = Tutorial(
        tutorial_name="Start Guide",
        description="A guide to playing The Forest's End in Archipelago.",
        language="English",
        file_name="setup_en.md",
        link="setup/en",
        authors=["MarioManTAW"]
    )

    tutorials = [setup_en]


class ForestsEndWorld(World):
    """Developed within 30 days for Metroidvania Month 31 x Magical Girl Game Jam 13, The Forest's End is a modern take
    on the Metroidvania genre set in a futuristic and mysterious forest! Construct the ultimate magical girl robot in a
    far-off forest!"""
    game = "The Forest's End"
    options_dataclass = options.ForestsEndOptions
    options: options.ForestsEndOptions
    web = ForestsEndWebWorld()
    location_name_to_id = locations.LOCATION_NAME_TO_ID
    item_name_to_id = items.ITEM_NAME_TO_ID
    origin_region_name = "Tutorial"
    ut_can_gen_without_yaml: bool = True

    def create_regions(self) -> None:
        regions.create_and_connect_regions(self)
        locations.create_locations(self)

    def set_rules(self) -> None:
        rules.set_all_rules(self)
    
    def get_filler_item_name(self) -> str:
        return items.get_filler_item_name()

    def create_item(self, name) -> items.ForestsEndItem:
        return items.create_item(self, name)

    def create_items(self) -> None:
        items.create_items(self)

    def fill_slot_data(self) -> Dict[str, Any]:
        return dict(self.options.as_dict("death_link"), version=self.world_version.as_simple_string())
