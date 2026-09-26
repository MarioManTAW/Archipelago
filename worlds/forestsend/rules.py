from __future__ import annotations

from typing import TYPE_CHECKING

from rule_builder.rules import CanReachLocation, Has, HasAll, Rule

if TYPE_CHECKING:
    from . import ForestsEndWorld


def set_all_rules(world: ForestsEndWorld) -> None:
    set_location_rules(world)
    set_completion_condition(world)


def set_location_rules(world: ForestsEndWorld) -> None:
    def set_rule(location: str, rule: Rule):
        world.set_rule(world.get_location(location), rule)
    set_rule("Tutorial - Upper Lore Entry", Has("Wall Jump"))
    set_rule("Street - Health Upgrade", Has("Drill"))
    set_rule("Street - Hover Upgrade", HasAll("Wall Jump", "Drill"))
    set_rule("Street - Lore Entry", Has("Saw Blade"))
    set_rule("Giant Tree - Melee Attack Upgrade", HasAll("Drill", "Wall Jump", "Saw Blade", "Progressive Hover"))
    set_rule("Chasm - Lore Entry", Has("Drill"))
    set_rule("Subway - Health Upgrade", HasAll("Wall Jump", "Progressive Hover"))


def set_completion_condition(world: ForestsEndWorld) -> None:
    world.set_completion_rule(CanReachLocation("Giant Tree - Melee Attack Upgrade"))
