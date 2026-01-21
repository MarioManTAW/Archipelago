from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import CollectionState
from worlds.generic.Rules import set_rule
from .items import MINIGAMES

if TYPE_CHECKING:
    from . import MarioSuperSluggersWorld


def set_all_rules(world: MarioSuperSluggersWorld) -> None:
    set_location_rules(world)
    set_completion_condition(world)


def set_location_rules(world: MarioSuperSluggersWorld) -> None:
    def has_mario(state: CollectionState) -> bool:
        return state.has("Mario", world.player)
    def has_dk(state: CollectionState) -> bool:
        return state.has("Donkey Kong", world.player)
    def has_peach(state: CollectionState) -> bool:
        return state.has("Peach", world.player)
    def has_yoshi(state: CollectionState) -> bool:
        return state.has("Yoshi", world.player)
    def has_wario(state: CollectionState) -> bool:
        return state.has("Wario", world.player)
    
    set_rule(world.get_location("Peach Ice Garden: Recruit Daisy"),
             lambda state: state.has("Toad Statue", world.player))
    set_rule(world.get_location("Wario City: Recruit Waluigi"), has_yoshi)
    set_rule(world.get_location("Wario City: Recruit Koopa"), has_peach)
    set_rule(world.get_location("Mario Stadium: Recruit Monty Mole"), has_peach)
    set_rule(world.get_location("Mario Stadium: Recruit Blue Pianta"),
             lambda state: state.has("Sea Hut Key", world.player))
    set_rule(world.get_location("Mario Stadium: Recruit Red Pianta"), has_yoshi)
    set_rule(world.get_location("Mario Stadium: Recruit Yellow Pianta"), has_dk)
    set_rule(world.get_location("Mario Stadium: Recruit Green Noki"),
             lambda state: state.has("Blue Noki", world.player))
    set_rule(world.get_location("Peach Ice Garden: Recruit Yellow Toad"), has_peach)
    set_rule(world.get_location("Wario City: Recruit King Boo"),
             lambda state: state.has_all(("Boo", "Mini Boo"), world.player))
    set_rule(world.get_location("Peach Ice Garden: Recruit Petey Piranha"), has_peach)
    set_rule(world.get_location("Wario City: Recruit Paragoomba"), has_yoshi)
    set_rule(world.get_location("Wario City: Recruit Green Paratroopa"),
             lambda state: state.has("Brush", world.player))
    set_rule(world.get_location("Yoshi Park: Recruit Green Shy Guy"), has_peach)
    set_rule(world.get_location("Yoshi Park: Recruit Gray Shy Guy"), has_peach)
    set_rule(world.get_location("Mario Stadium: Recruit Blooper"), has_peach)
    set_rule(world.get_location("Peach Ice Garden: Recruit Baby Daisy"),
             lambda state: state.has("Baby Daisy's Rattle", world.player))
    set_rule(world.get_location("DK Jungle: Recruit Baby DK"), has_yoshi)
    set_rule(world.get_location("Yoshi Park: Recruit Red Yoshi"),
             lambda state: state.has("Brush", world.player))
    set_rule(world.get_location("Mario Stadium: Chest"),
             lambda state: state.has_all(("Mario", "Wario"), world.player))
    set_rule(world.get_location("Peach Ice Garden: Chest"),
             lambda state: state.has_all(("Wario", "Baby Daisy's Rattle"), world.player))
    set_rule(world.get_location("DK Jungle: Chest"), has_wario)
    set_rule(world.get_location("Yoshi Park: Chest"), has_wario)
    set_rule(world.get_location("Wario City: Chest"), has_yoshi)
    set_rule(world.get_location("Mario Stadium: Bottom barrel"), has_dk)
    set_rule(world.get_location("Mario Stadium: Middle barrel after Yellow Pianta"), has_dk)
    set_rule(world.get_location("Mario Stadium: Top barrel"), has_dk)
    set_rule(world.get_location("Mario Stadium: Bottom bush"), has_mario)
    set_rule(world.get_location("Mario Stadium: Top bush"), has_mario)
    set_rule(world.get_location("Mario Stadium: Central tree after Red Pianta"), has_yoshi)
    set_rule(world.get_location("Mario Stadium: Top tree"), has_yoshi)
    set_rule(world.get_location("Peach Ice Garden: Right mushroom after Yellow Toad"), has_peach)
    set_rule(world.get_location("Peach Ice Garden: Top mushroom"), has_peach)
    set_rule(world.get_location("Wario City: Central tree"), has_yoshi)
    set_rule(world.get_location("Wario City: Right tree after Paragoomba"), has_yoshi)
    set_rule(world.get_location("Wario City: Trash can near entrance"), has_wario)
    set_rule(world.get_location("Wario City: Trash can near dynamo"), has_wario)
    set_rule(world.get_location("Wario City: Top tree"), has_yoshi)
    set_rule(world.get_location("DK Jungle: Top flowers near entrance"), has_mario)
    set_rule(world.get_location("DK Jungle: Tree near shop"), has_yoshi)
    set_rule(world.get_location("DK Jungle: Tree near Dixie Kong"), has_yoshi)
    set_rule(world.get_location("DK Jungle: Tree below entrance after Baby DK"), has_yoshi)
    set_rule(world.get_location("DK Jungle: Bottom flowers near entrance"), has_mario)
    set_rule(world.get_location("DK Jungle: Flowers near bridge"), has_mario)
    set_rule(world.get_location("DK Jungle: Flowers below central tree"), has_mario)
    set_rule(world.get_location("DK Jungle: Flowers near Funky Kong"), has_mario)
    set_rule(world.get_location("DK Jungle: Flowers below entrance"), has_mario)
    set_rule(world.get_location("Yoshi Park: Left stump after Shy Guys"), has_peach)
    set_rule(world.get_location("Yoshi Park: Right stump after Shy Guys"), has_peach)
    set_rule(world.get_location("Peach Ice Garden: Baby Daisy's Rattle"), has_wario)
    set_rule(world.get_location("Blue Pianta's shop: Buy Luigi's Flashlight"),
             lambda state: state.has("Luigi", world.player))
    set_rule(world.get_location("Toadsworth's shop: Buy Cruiser Pass"),
             lambda state: state.has("Daisy", world.player))
    set_rule(world.get_location("Mario Stadium: Play Bob-omb Derby"),
             lambda state: state.has("Day-night cycle", world.player))
    set_rule(world.get_location("Peach Ice Garden: Play Wall Ball"),
             lambda state: state.has("Day-night cycle", world.player))
    set_rule(world.get_location("Baseball Kingdom: Play all minigames"),
             lambda state: state.has_all(MINIGAMES, world.player))


def set_completion_condition(world: MarioSuperSluggersWorld) -> None:
    goal_events = ["Defeat Bowser Monsters", "Play Badge"]
    world.multiworld.completion_condition[world.player] = lambda state:\
        state.has(goal_events[world.options.goal_condition], world.player)
