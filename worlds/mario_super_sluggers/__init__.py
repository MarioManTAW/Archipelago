from typing import Any
from BaseClasses import Tutorial
from worlds.AutoWorld import World, WebWorld
from worlds.LauncherComponents import Component, Type, components, launch_subprocess
from . import items, locations, options, regions, rules

def run_client() -> None:
    """
    Launch the Mario Super Sluggers client.
    """
    print("Running Mario Super Sluggers Client")
    from .client import main

    launch_subprocess(main, name="MarioSuperSluggersClient")


components.append(
    Component(
        "Mario Super Sluggers Client",
        func=run_client,
        component_type=Type.CLIENT,
    )
)


class MarioSuperSluggersWebWorld(WebWorld):
    theme = "partyTime"

    setup_en = Tutorial(
        tutorial_name="Start Guide",
        description="A guide to playing Mario Super Sluggers in Archipelago.",
        language="English",
        file_name="setup_en.md",
        link="setup/en",
        authors=["MarioManTAW"]
    )

    tutorials = [setup_en]


class MarioSuperSluggersWorld(World):
    """
    Mario Super Sluggers is a baseball game with a Mario twist. In the challenge mode, you'll embark on an adventure
    through the Baseball Kingdom, recruit familiar characters for your team, then face Bowser and his Bowser Monsters
    in a game. PLAY BALL!
    """
    game = "Mario Super Sluggers"
    options_dataclass = options.MarioSuperSluggersOptions
    options: options.MarioSuperSluggersOptions
    web = MarioSuperSluggersWebWorld()
    location_name_to_id = locations.LOCATION_NAME_TO_ID
    item_name_to_id = items.ITEM_NAME_TO_ID
    item_name_groups = items.ITEM_NAME_GROUPS
    origin_region_name = "Baseball Kingdom"

    def create_regions(self) -> None:
        regions.create_and_connect_regions(self)
        locations.create_locations(self)

    def set_rules(self) -> None:
        rules.set_all_rules(self)
    
    def get_filler_item_name(self) -> str:
        return items.get_filler_item_name()

    def create_item(self, name) -> items.MarioSuperSluggersItem:
        return items.create_item(self, name)

    def create_items(self) -> None:
        items.create_items(self)

    def fill_slot_data(self) -> dict[str, Any]:
        starting_captains = [0, 4, 6, 2, 10]
        starting_captain = starting_captains[self.options.starting_captain]
        slot_data = self.options.as_dict("goal_condition", "goal_characters", "randomize_stars", "randomize_shops",
                                         "reduced_cutscenes")
        slot_data["starting_captain"] = starting_captain
        if self.options.randomize_music:
            music = [
                0x06, 0x07, 0x08, 0x09, 0x0A, 0x0B, 0x0C, 0x0D, 0x0E, 0x0F, 0x12, 0x13, 0x14, 0x15, 0x16, 0x17, 0x18,
                0x19, 0x4B
            ]
            music_keys = [k for k in music]
            self.random.shuffle(music)
            slot_data["music"] = dict(zip(music_keys, music))
        slot_data["world_version"] = self.world_version.as_simple_string()
        return slot_data
