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
    if world.options.randomize_stars or world.options.goal_condition == world.options.goal_condition.option_star_badge:
        set_rule(world.get_location("Bowser Castle: Unlock star for Mario"),
                lambda state: state.has("Mario", world.player))
        set_rule(world.get_location("Bowser Castle: Unlock star for Luigi"),
                lambda state: state.has("Luigi", world.player))
        set_rule(world.get_location("Bowser Castle: Unlock star for Donkey Kong"),
                lambda state: state.has("Donkey Kong", world.player))
        set_rule(world.get_location("Bowser Castle: Unlock star for Diddy Kong"),
                lambda state: state.has("Diddy Kong", world.player))
        set_rule(world.get_location("Bowser Castle: Unlock star for Peach"),
                lambda state: state.has("Peach", world.player))
        set_rule(world.get_location("Bowser Castle: Unlock star for Daisy"),
                lambda state: state.has("Daisy", world.player))
        set_rule(world.get_location("Bowser Castle: Unlock star for Yoshi"),
                lambda state: state.has_any([
                    "Yoshi", "Red Yoshi", "Blue Yoshi", "Yellow Yoshi", "Light Blue Yoshi", "Pink Yoshi"
                ], world.player))
        set_rule(world.get_location("Bowser Castle: Unlock star for Baby Mario"),
                lambda state: state.has("Baby Mario", world.player))
        set_rule(world.get_location("Bowser Castle: Unlock star for Baby Luigi"),
                lambda state: state.has("Baby Luigi", world.player))
        set_rule(world.get_location("Bowser Castle: Unlock star for Wario"),
                lambda state: state.has("Wario", world.player))
        set_rule(world.get_location("Bowser Castle: Unlock star for Waluigi"),
                lambda state: state.has("Waluigi", world.player))
        set_rule(world.get_location("Bowser Castle: Unlock star for Koopa"),
                lambda state: state.has_any(["Koopa", "Red Koopa"], world.player))
        set_rule(world.get_location("Bowser Castle: Unlock star for Toad"),
                lambda state: state.has_any([
                    "Red Toad", "Blue Toad", "Yellow Toad", "Green Toad", "Purple Toad"
                ], world.player))
        set_rule(world.get_location("Bowser Castle: Unlock star for Boo"),
                lambda state: state.has("Boo", world.player))
        set_rule(world.get_location("Bowser Castle: Unlock star for Toadette"),
                lambda state: state.has("Toadette", world.player))
        set_rule(world.get_location("Bowser Castle: Unlock star for Shy Guy"),
                lambda state: state.has_any([
                    "Shy Guy", "Blue Shy Guy", "Yellow Shy Guy", "Green Shy Guy", "Gray Shy Guy"
                ], world.player))
        set_rule(world.get_location("Bowser Castle: Unlock star for Birdo"),
                lambda state: state.has("Birdo", world.player))
        set_rule(world.get_location("Bowser Castle: Unlock star for Monty Mole"),
                lambda state: state.has("Monty Mole", world.player))
        set_rule(world.get_location("Bowser Castle: Unlock star for Paratroopa"),
                lambda state: state.has_any(["Paratroopa", "Green Paratroopa"], world.player))
        set_rule(world.get_location("Bowser Castle: Unlock star for Pianta"),
                lambda state: state.has_any(["Blue Pianta", "Red Pianta", "Yellow Pianta"], world.player))
        set_rule(world.get_location("Bowser Castle: Unlock star for Noki"),
                lambda state: state.has_any(["Blue Noki", "Red Noki", "Green Noki"], world.player))
        set_rule(world.get_location("Bowser Castle: Unlock star for Toadsworth"),
                lambda state: state.has("Toadsworth", world.player))
        set_rule(world.get_location("Bowser Castle: Unlock star for King Boo"),
                lambda state: state.has("King Boo", world.player))
        set_rule(world.get_location("Bowser Castle: Unlock star for Petey Piranha"),
                lambda state: state.has("Petey Piranha", world.player))
        set_rule(world.get_location("Bowser Castle: Unlock star for Dixie Kong"),
                lambda state: state.has("Dixie Kong", world.player))
        set_rule(world.get_location("Bowser Castle: Unlock star for Goomba"),
                lambda state: state.has("Goomba", world.player))
        set_rule(world.get_location("Bowser Castle: Unlock star for Paragoomba"),
                lambda state: state.has("Paragoomba", world.player))
        set_rule(world.get_location("Bowser Castle: Unlock star for Wiggler"),
                lambda state: state.has("Wiggler", world.player))
        set_rule(world.get_location("Bowser Castle: Unlock star for Blooper"),
                lambda state: state.has("Blooper", world.player))
        set_rule(world.get_location("Bowser Castle: Unlock star for Funky Kong"),
                lambda state: state.has("Funky Kong", world.player))
        set_rule(world.get_location("Bowser Castle: Unlock star for Tiny Kong"),
                lambda state: state.has("Tiny Kong", world.player))
        set_rule(world.get_location("Bowser Castle: Unlock star for Kritter"),
                lambda state: state.has_any(["Kritter", "Blue Kritter", "Red Kritter", "Brown Kritter"], world.player))
        set_rule(world.get_location("Bowser Castle: Unlock star for King K. Rool"),
                lambda state: state.has("King K. Rool", world.player))
        set_rule(world.get_location("Bowser Castle: Unlock star for Baby Peach"),
                lambda state: state.has("Baby Peach", world.player))
        set_rule(world.get_location("Bowser Castle: Unlock star for Baby Daisy"),
                lambda state: state.has("Baby Daisy", world.player))
        set_rule(world.get_location("Bowser Castle: Unlock star for Baby DK"),
                lambda state: state.has("Baby DK", world.player))
        set_rule(world.get_location("Baseball Kingdom: Star all characters"),
                lambda state: state.count_group_unique("Stars", world.player) >= 41 and\
                    state.has("Defeat Bowser Monsters", world.player))
    set_rule(world.get_location("Baseball Kingdom: Play all minigames"),
             lambda state: state.has_all(MINIGAMES, world.player))
    set_rule(world.get_location("Baseball Kingdom: Recruit all characters"),
             lambda state: state.has_all(["Mario", "Donkey Kong", "Peach", "Yoshi", "Wario",
                                          "Blue Noki", "Green Noki", "Boo", "Mini Boo", "Defeat Bowser Monsters",
                                          "Sea Hut Key", "Baby Daisy's Rattle", "Toad Statue", "Daisy Statue",
                                          "Stone tablet piece A", "Stone tablet piece B", "Stone tablet piece C",
                                          "Brush"], world.player))


def set_completion_condition(world: MarioSuperSluggersWorld) -> None:
    goal_events = ["Defeat Bowser Monsters", "Play Badge", "Friend Badge", "Star Badge"]
    world.multiworld.completion_condition[world.player] = lambda state:\
        state.has(goal_events[world.options.goal_condition], world.player)
