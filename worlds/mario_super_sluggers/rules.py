from __future__ import annotations

from typing import TYPE_CHECKING

from rule_builder.rules import And, Has, HasAll, HasAny, HasGroupUnique, Rule
from .items import MINIGAMES

if TYPE_CHECKING:
    from . import MarioSuperSluggersWorld


def set_all_rules(world: MarioSuperSluggersWorld) -> None:
    set_location_rules(world)
    set_completion_condition(world)


def set_location_rules(world: MarioSuperSluggersWorld) -> None:
    def set_rule(location: str, rule: Rule):
        world.set_rule(world.get_location(location), rule)
    set_rule("Peach Ice Garden: Recruit Daisy", Has("Toad Statue"))
    set_rule("Wario City: Recruit Wario", Has("Donkey Kong"))
    set_rule("Wario City: Recruit Waluigi", Has("Yoshi"))
    set_rule("Wario City: Recruit Koopa", Has("Peach"))
    set_rule("Mario Stadium: Recruit Monty Mole", Has("Peach"))
    set_rule("Mario Stadium: Recruit Blue Pianta", Has("Sea Hut Key"))
    set_rule("Mario Stadium: Recruit Red Pianta", Has("Yoshi"))
    set_rule("Mario Stadium: Recruit Yellow Pianta", Has("Donkey Kong"))
    set_rule("Mario Stadium: Recruit Green Noki", Has("Blue Noki"))
    set_rule("Peach Ice Garden: Recruit Yellow Toad", Has("Peach"))
    set_rule("Wario City: Recruit King Boo", HasAll("Boo", "Mini Boo"))
    set_rule("Peach Ice Garden: Recruit Petey Piranha", Has("Peach"))
    set_rule("Wario City: Recruit Paragoomba", Has("Yoshi"))
    set_rule("Wario City: Recruit Green Paratroopa", Has("Brush"))
    set_rule("Yoshi Park: Recruit Green Shy Guy", Has("Peach"))
    set_rule("Yoshi Park: Recruit Gray Shy Guy", Has("Peach"))
    set_rule("Mario Stadium: Recruit Blooper", Has("Peach"))
    set_rule("Peach Ice Garden: Recruit Baby Daisy", Has("Baby Daisy's Rattle"))
    set_rule("DK Jungle: Recruit Baby DK", Has("Yoshi"))
    set_rule("Yoshi Park: Recruit Red Yoshi", Has("Brush"))
    set_rule("Mario Stadium: Chest", HasAll("Mario", "Wario"))
    set_rule("Peach Ice Garden: Chest", HasAll("Wario", "Baby Daisy's Rattle"))
    set_rule("DK Jungle: Chest", Has("Wario"))
    set_rule("Yoshi Park: Chest", Has("Wario"))
    set_rule("Wario City: Chest", Has("Yoshi"))
    set_rule("Mario Stadium: Bottom barrel", Has("Donkey Kong"))
    set_rule("Mario Stadium: Middle barrel after Yellow Pianta", Has("Donkey Kong"))
    set_rule("Mario Stadium: Top barrel", Has("Donkey Kong"))
    set_rule("Mario Stadium: Bottom bush", Has("Mario"))
    set_rule("Mario Stadium: Top bush", Has("Mario"))
    set_rule("Mario Stadium: Central tree after Red Pianta", Has("Yoshi"))
    set_rule("Mario Stadium: Top tree", Has("Yoshi"))
    set_rule("Peach Ice Garden: Right mushroom after Yellow Toad", Has("Peach"))
    set_rule("Peach Ice Garden: Top mushroom", Has("Peach"))
    set_rule("Wario City: Central tree", Has("Yoshi"))
    set_rule("Wario City: Right tree after Paragoomba", Has("Yoshi"))
    set_rule("Wario City: Top tree", Has("Yoshi"))
    set_rule("DK Jungle: Top flowers near entrance", Has("Mario"))
    set_rule("DK Jungle: Tree near shop", Has("Yoshi"))
    set_rule("DK Jungle: Tree near Dixie Kong", Has("Yoshi"))
    set_rule("DK Jungle: Tree below entrance after Baby DK", Has("Yoshi"))
    set_rule("DK Jungle: Bottom flowers near entrance", Has("Mario"))
    set_rule("DK Jungle: Flowers near bridge", Has("Mario"))
    set_rule("DK Jungle: Flowers below central tree", Has("Mario"))
    set_rule("DK Jungle: Flowers near Funky Kong", Has("Mario"))
    set_rule("DK Jungle: Flowers below entrance", Has("Mario"))
    set_rule("Yoshi Park: Left stump after Shy Guys", Has("Peach"))
    set_rule("Yoshi Park: Right stump after Shy Guys", Has("Peach"))
    set_rule("Peach Ice Garden: Baby Daisy's Rattle", Has("Wario"))
    set_rule("Blue Pianta's shop: Buy Luigi's Flashlight", Has("Luigi"))
    set_rule("Toadsworth's shop: Buy Cruiser Pass", Has("Daisy"))
    set_rule("Mario Stadium: Play Bob-omb Derby", Has("Day-night cycle"))
    set_rule("Peach Ice Garden: Play Wall Ball", Has("Day-night cycle"))
    if world.options.randomize_stars or world.options.goal_condition == world.options.goal_condition.option_star_badge:
        set_rule("Bowser Castle: Unlock star for Mario", Has("Mario"))
        set_rule("Bowser Castle: Unlock star for Luigi", Has("Luigi"))
        set_rule("Bowser Castle: Unlock star for Donkey Kong", Has("Donkey Kong"))
        set_rule("Bowser Castle: Unlock star for Diddy Kong", Has("Diddy Kong"))
        set_rule("Bowser Castle: Unlock star for Peach", Has("Peach"))
        set_rule("Bowser Castle: Unlock star for Daisy", Has("Daisy"))
        set_rule("Bowser Castle: Unlock star for Yoshi",
                HasAny("Yoshi", "Red Yoshi", "Blue Yoshi", "Yellow Yoshi", "Light Blue Yoshi", "Pink Yoshi"))
        set_rule("Bowser Castle: Unlock star for Baby Mario", Has("Baby Mario"))
        set_rule("Bowser Castle: Unlock star for Baby Luigi", Has("Baby Luigi"))
        set_rule("Bowser Castle: Unlock star for Wario", Has("Wario"))
        set_rule("Bowser Castle: Unlock star for Waluigi", Has("Waluigi"))
        set_rule("Bowser Castle: Unlock star for Koopa", HasAny("Koopa", "Red Koopa"))
        set_rule("Bowser Castle: Unlock star for Toad",
                HasAny("Red Toad", "Blue Toad", "Yellow Toad", "Green Toad", "Purple Toad"))
        set_rule("Bowser Castle: Unlock star for Boo", Has("Boo"))
        set_rule("Bowser Castle: Unlock star for Toadette", Has("Toadette"))
        set_rule("Bowser Castle: Unlock star for Shy Guy",
                HasAny("Shy Guy", "Blue Shy Guy", "Yellow Shy Guy", "Green Shy Guy", "Gray Shy Guy"))
        set_rule("Bowser Castle: Unlock star for Birdo", Has("Birdo"))
        set_rule("Bowser Castle: Unlock star for Monty Mole", Has("Monty Mole"))
        set_rule("Bowser Castle: Unlock star for Paratroopa", HasAny("Paratroopa", "Green Paratroopa"))
        set_rule("Bowser Castle: Unlock star for Pianta", HasAny("Blue Pianta", "Red Pianta", "Yellow Pianta"))
        set_rule("Bowser Castle: Unlock star for Noki", HasAny("Blue Noki", "Red Noki", "Green Noki"))
        set_rule("Bowser Castle: Unlock star for Toadsworth", Has("Toadsworth"))
        set_rule("Bowser Castle: Unlock star for King Boo", Has("King Boo"))
        set_rule("Bowser Castle: Unlock star for Petey Piranha", Has("Petey Piranha"))
        set_rule("Bowser Castle: Unlock star for Dixie Kong", Has("Dixie Kong"))
        set_rule("Bowser Castle: Unlock star for Goomba", Has("Goomba"))
        set_rule("Bowser Castle: Unlock star for Paragoomba", Has("Paragoomba"))
        set_rule("Bowser Castle: Unlock star for Wiggler", Has("Wiggler"))
        set_rule("Bowser Castle: Unlock star for Blooper", Has("Blooper"))
        set_rule("Bowser Castle: Unlock star for Funky Kong", Has("Funky Kong"))
        set_rule("Bowser Castle: Unlock star for Tiny Kong", Has("Tiny Kong"))
        set_rule("Bowser Castle: Unlock star for Kritter",
                HasAny("Kritter", "Blue Kritter", "Red Kritter", "Brown Kritter"))
        set_rule("Bowser Castle: Unlock star for King K. Rool", Has("King K. Rool"))
        set_rule("Bowser Castle: Unlock star for Baby Peach", Has("Baby Peach"))
        set_rule("Bowser Castle: Unlock star for Baby Daisy", Has("Baby Daisy"))
        set_rule("Bowser Castle: Unlock star for Baby DK", Has("Baby DK"))
        set_rule("Baseball Kingdom: Star all characters",
                 And(HasGroupUnique("Stars", 41), Has("Defeat Bowser Monsters")))
    set_rule("Baseball Kingdom: Play all minigames", HasAll(*MINIGAMES))
    set_rule("Baseball Kingdom: Recruit all characters",
             HasAll("Mario", "Donkey Kong", "Peach", "Yoshi", "Wario", "Blue Noki", "Green Noki", "Boo", "Mini Boo",
                     "Defeat Bowser Monsters", "Sea Hut Key", "Baby Daisy's Rattle", "Toad Statue", "Daisy Statue",
                     "Stone tablet piece A", "Stone tablet piece B", "Stone tablet piece C", "Brush"))


def set_completion_condition(world: MarioSuperSluggersWorld) -> None:
    goal_events = ["Defeat Bowser Monsters", "Play Badge", "Friend Badge", "Star Badge"]
    world.set_completion_rule(Has(goal_events[world.options.goal_condition]))
