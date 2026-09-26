from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import Region
from rule_builder.rules import Has, HasAll, HasAny

if TYPE_CHECKING:
    from . import ForestsEndWorld


def create_and_connect_regions(world: ForestsEndWorld) -> None:
    create_all_regions(world)
    connect_regions(world)


def create_all_regions(world: ForestsEndWorld) -> None:
    world.multiworld.regions += [
        Region("Tutorial", world.player, world.multiworld),
        Region("Street (Left)", world.player, world.multiworld),
        Region("Street (Right)", world.player, world.multiworld),
        Region("Giant Tree", world.player, world.multiworld),
        Region("Giant Tree (Upper)", world.player, world.multiworld),
        Region("Chasm (Upper)", world.player, world.multiworld),
        Region("Chasm (Lower)", world.player, world.multiworld),
        Region("Skyscraper", world.player, world.multiworld),
        Region("Abandoned Train", world.player, world.multiworld),
        Region("Subway (Upper)", world.player, world.multiworld),
        Region("Subway (Lower)", world.player, world.multiworld),
        Region("Subway (Right)", world.player, world.multiworld),
	]


def connect_regions(world: ForestsEndWorld) -> None:
    tutorial = world.get_region("Tutorial")
    street_left = world.get_region("Street (Left)")
    street_right = world.get_region("Street (Right)")
    giant_tree = world.get_region("Giant Tree")
    giant_tree_upper = world.get_region("Giant Tree (Upper)")
    chasm_upper = world.get_region("Chasm (Upper)")
    chasm_lower = world.get_region("Chasm (Lower)")
    skyscraper = world.get_region("Skyscraper")
    abandoned_train = world.get_region("Abandoned Train")
    subway_upper = world.get_region("Subway (Upper)")
    subway_lower = world.get_region("Subway (Lower)")
    subway_right = world.get_region("Subway (Right)")

    tutorial.connect(street_left, None, HasAny("Progressive Melee Attack", "Drill", "Saw Blade"))
    street_left.connect(street_right, None, HasAny("Progressive Hover", "Wall Jump"))
    street_left.connect(abandoned_train, None, Has("Drill"))
    street_right.connect(giant_tree)
    street_right.connect(subway_upper, None, Has("Drill"))
    giant_tree.connect(giant_tree_upper, None, HasAll("Wall Jump", "Progressive Hover"))
    giant_tree.connect(chasm_upper)
    giant_tree_upper.connect(skyscraper)
    chasm_upper.connect(chasm_lower, None, Has("Saw Blade"))
    chasm_lower.connect(subway_right)
    abandoned_train.connect(subway_upper, None, Has("Saw Blade"))
    subway_upper.connect(subway_lower, None, HasAll("Wall Jump", "Saw Blade"))
