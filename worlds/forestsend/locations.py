from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import ItemClassification, Location

from . import items

if TYPE_CHECKING:
    from . import ForestsEndWorld

LOCATION_NAME_TO_ID = {
    "Tutorial - Lore Entry":               86,
    "Tutorial - Transformation (Hover)":    1,
    "Tutorial - Transformation (Melee)":    2,
    "Tutorial - Upper Lore Entry":         87,
    "Street - Health Upgrade":             64,
    "Street - Hover Upgrade":              63,
    "Street - Lore Entry":                 65,
    "Giant Tree - Hover Upgrade":          18,
    "Giant Tree - Health Upgrade":         19,
    "Giant Tree - Lore Entry":             20,
    "Giant Tree - Melee Attack Upgrade":   17,
    "Chasm - Wall Jump":                   16,
    "Chasm - Lore Entry":                  11,
    "Skyscraper - Hover Upgrade":          45,
    "Skyscraper - Lore Entry":             46,
    "Skyscraper - Drill":                  48,
    "Abandoned Train - Lore Entry":         6,
    "Abandoned Train - Saw Blade":          9,
    "Subway - Lore Entry":                 73,
    "Subway - Health Upgrade":             72,
}


class ForestsEndLocation(Location):
    game = "The Forest's End"


def get_location_names_with_ids(location_names: list[str]) -> dict[str, int | None]:
    return {location_name: LOCATION_NAME_TO_ID[location_name] for location_name in location_names}


def create_locations(world: ForestsEndWorld) -> None:
    tutorial = world.get_region("Tutorial")
    street_left = world.get_region("Street (Left)")
    street_right = world.get_region("Street (Right)")
    giant_tree = world.get_region("Giant Tree")
    giant_tree_upper = world.get_region("Giant Tree (Upper)")
    chasm_upper = world.get_region("Chasm (Upper)")
    chasm_lower = world.get_region("Chasm (Lower)")
    skyscraper = world.get_region("Skyscraper")
    abandoned_train = world.get_region("Abandoned Train")
    subway_lower = world.get_region("Subway (Lower)")
    subway_right = world.get_region("Subway (Right)")

    tutorial.add_locations(get_location_names_with_ids([
        "Tutorial - Lore Entry",
        "Tutorial - Transformation (Hover)",
        "Tutorial - Transformation (Melee)",
        "Tutorial - Upper Lore Entry",
    ]), ForestsEndLocation)

    street_left.add_locations(get_location_names_with_ids([
        "Street - Health Upgrade",
    ]), ForestsEndLocation)

    street_right.add_locations(get_location_names_with_ids([
        "Street - Hover Upgrade",
        "Street - Lore Entry",
    ]), ForestsEndLocation)

    giant_tree.add_locations(get_location_names_with_ids([
        "Giant Tree - Melee Attack Upgrade",
    ]), ForestsEndLocation)

    giant_tree_upper.add_locations(get_location_names_with_ids([
        "Giant Tree - Hover Upgrade",
        "Giant Tree - Health Upgrade",
        "Giant Tree - Lore Entry",
    ]), ForestsEndLocation)

    chasm_upper.add_locations(get_location_names_with_ids([
        "Chasm - Wall Jump",
    ]), ForestsEndLocation)

    chasm_lower.add_locations(get_location_names_with_ids([
        "Chasm - Lore Entry",
    ]), ForestsEndLocation)

    skyscraper.add_locations(get_location_names_with_ids([
        "Skyscraper - Hover Upgrade",
        "Skyscraper - Lore Entry",
        "Skyscraper - Drill",
    ]), ForestsEndLocation)

    abandoned_train.add_locations(get_location_names_with_ids([
        "Abandoned Train - Lore Entry",
        "Abandoned Train - Saw Blade",
    ]), ForestsEndLocation)

    subway_lower.add_locations(get_location_names_with_ids([
        "Subway - Lore Entry",
    ]), ForestsEndLocation)

    subway_right.add_locations(get_location_names_with_ids([
        "Subway - Health Upgrade",
    ]), ForestsEndLocation)

