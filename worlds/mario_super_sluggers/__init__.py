import json
import os
from typing import Any
from BaseClasses import Tutorial
from Utils import tuplize_version
from worlds.AutoWorld import World, WebWorld
from worlds.LauncherComponents import Component, Type, components, launch_subprocess
from . import items, locations, options, regions, rules
from .patch import MarioSuperSluggersPatch

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
    ut_can_gen_without_yaml: bool = True
    glitches_item_name = "Out-of-logic"

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

    def generate_early(self) -> None:
        re_gen_passthrough = getattr(self.multiworld, "re_gen_passthrough", {})
        if re_gen_passthrough and self.game in re_gen_passthrough:
            slot_data = re_gen_passthrough[self.game]
            self.options.starting_captain.value = [0, 4, 6, 2, 10].index(slot_data["starting_captain"])
            self.options.goal_condition.value = slot_data["goal_condition"]
            self.options.goal_characters.value = slot_data["goal_characters"]
            self.options.randomize_stars.value = slot_data["randomize_stars"]
            self.options.randomize_shops.value = slot_data["randomize_shops"]

    def generate_output(self, output_directory: str) -> None:
        patch = MarioSuperSluggersPatch(player=self.player, player_name=self.player_name)
        patchable_locations = [
            0x80E553F201,
            0x80E553F301,
            0x80E554BF01,
            0x80E554C001,
            0x80E554C101,
            0x80E554C201,
            0x80E554C301,
            0x80E554C401,
            0x80E554C501,
            0x80E554C601,
            0x80E554CF01,
            0x80E554D001,
            0x80E554D101,
            0x80E554D201,
            0x80E554D301,
            0x80E554D401,
            0x80E554D501,
            0x80E554D601,
            0x80E554DF01,
            0x80E554E001,
            0x80E554E101,
            0x80E554E201,
            0x80E554E301,
            0x80E554E401,
            0x80E554E501,
            0x80E554E601,
            0x80E554EF01,
            0x80E554F001,
            0x80E554F101,
            0x80E554F201,
            0x80E554F301,
            0x80E554F401,
            0x80E554F501,
            0x80E554F601,
            0x80E554FF01,
            0x80E5550001,
            0x80E5550101,
            0x80E5550201,
            0x80E5550301,
            0x80E5550401,
            0x80E5550501,
            0x80E5550601,
            0x80E5550F01,
            0x80E5551001,
            0x80E5551101,
            0x80E5551201,
            0x80E5551301,
            0x80E5551401,
            0x80E5551501,
            0x80E5551601,
            0x80E5551701,
            0x80E5551801,
            0x80E5551901,
        ]
        patch.data = json.dumps({
            "goal_characters": self.options.goal_characters.value,
            "locations": [
                {
                    "id": location.address,
                    "player": self.multiworld.player_name[location.item.player],
                    "item": location.item.name,
                    "flags": location.item.flags
                }
                for location in self.multiworld.get_locations(self.player)
                if location.address in patchable_locations and location.item
            ]
        })
        out_file_name = self.multiworld.get_out_file_name_base(self.player)
        patch.write(os.path.join(output_directory, f"{out_file_name}{patch.patch_file_ending}"))

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

    @staticmethod
    def interpret_slot_data(slot_data: dict[str, Any]) -> dict[str, Any]:
        if tuplize_version(slot_data["world_version"]) < tuplize_version("0.3.0"):
            raise Exception("This multiworld was generated on an older APWorld, Universal Tracker will not work. "
                            "Please refer to version 0.2.0 of the PopTracker pack for accurate tracking.")
        return slot_data
