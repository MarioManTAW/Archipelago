
from __future__ import annotations

from typing import TYPE_CHECKING, NamedTuple

from BaseClasses import Item, ItemClassification

if TYPE_CHECKING:
    from . import MarioSuperSluggersWorld


class MarioSuperSluggersItem(Item):
    game = "Mario Super Sluggers"


class MarioSuperSluggersItemData(NamedTuple):
    code: int
    type: ItemClassification


ITEM_DATA = {
    "Mario":                MarioSuperSluggersItemData(0x80E552E902, ItemClassification.progression),
    "Luigi":                MarioSuperSluggersItemData(0x80E552EA02, ItemClassification.progression_skip_balancing),
    "Donkey Kong":          MarioSuperSluggersItemData(0x80E552EB02, ItemClassification.progression),
    "Diddy Kong":           MarioSuperSluggersItemData(0x80E552EC02, ItemClassification.progression_skip_balancing),
    "Peach":                MarioSuperSluggersItemData(0x80E552ED02, ItemClassification.progression),
    "Daisy":                MarioSuperSluggersItemData(0x80E552EE02, ItemClassification.progression_skip_balancing),
    "Yoshi":                MarioSuperSluggersItemData(0x80E552EF02, ItemClassification.progression),
    "Baby Mario":           MarioSuperSluggersItemData(0x80E552F002, ItemClassification.progression_skip_balancing),
    "Baby Luigi":           MarioSuperSluggersItemData(0x80E552F102, ItemClassification.progression_skip_balancing),
    "Wario":                MarioSuperSluggersItemData(0x80E552F302, ItemClassification.progression),
    "Waluigi":              MarioSuperSluggersItemData(0x80E552F402, ItemClassification.progression_skip_balancing),
    "Koopa":                MarioSuperSluggersItemData(0x80E552F502, ItemClassification.progression_skip_balancing),
    "Red Toad":             MarioSuperSluggersItemData(0x80E552F602, ItemClassification.progression_skip_balancing),
    "Boo":                  MarioSuperSluggersItemData(0x80E552F702, ItemClassification.progression_skip_balancing),
    "Toadette":             MarioSuperSluggersItemData(0x80E552F802, ItemClassification.progression_skip_balancing),
    "Shy Guy":              MarioSuperSluggersItemData(0x80E552F902, ItemClassification.progression_skip_balancing),
    "Birdo":                MarioSuperSluggersItemData(0x80E552FA02, ItemClassification.progression_skip_balancing),
    "Monty Mole":           MarioSuperSluggersItemData(0x80E552FB02, ItemClassification.progression_skip_balancing),
    "Paratroopa":           MarioSuperSluggersItemData(0x80E552FD02, ItemClassification.progression_skip_balancing),
    "Blue Pianta":          MarioSuperSluggersItemData(0x80E552FE02, ItemClassification.progression_skip_balancing),
    "Red Pianta":           MarioSuperSluggersItemData(0x80E552FF02, ItemClassification.progression_skip_balancing),
    "Yellow Pianta":        MarioSuperSluggersItemData(0x80E5530002, ItemClassification.progression_skip_balancing),
    "Blue Noki":            MarioSuperSluggersItemData(0x80E5530102, ItemClassification.progression),
    "Red Noki":             MarioSuperSluggersItemData(0x80E5530202, ItemClassification.progression_skip_balancing),
    "Green Noki":           MarioSuperSluggersItemData(0x80E5530302, ItemClassification.progression),
    "Toadsworth":           MarioSuperSluggersItemData(0x80E5530502, ItemClassification.progression_skip_balancing),
    "Blue Toad":            MarioSuperSluggersItemData(0x80E5530602, ItemClassification.progression_skip_balancing),
    "Yellow Toad":          MarioSuperSluggersItemData(0x80E5530702, ItemClassification.progression_skip_balancing),
    "Green Toad":           MarioSuperSluggersItemData(0x80E5530802, ItemClassification.progression_skip_balancing),
    "Purple Toad":          MarioSuperSluggersItemData(0x80E5530902, ItemClassification.progression_skip_balancing),
    "King Boo":             MarioSuperSluggersItemData(0x80E5530E02, ItemClassification.progression_skip_balancing),
    "Petey Piranha":        MarioSuperSluggersItemData(0x80E5530F02, ItemClassification.progression_skip_balancing),
    "Dixie Kong":           MarioSuperSluggersItemData(0x80E5531002, ItemClassification.progression_skip_balancing),
    "Goomba":               MarioSuperSluggersItemData(0x80E5531102, ItemClassification.progression_skip_balancing),
    "Paragoomba":           MarioSuperSluggersItemData(0x80E5531202, ItemClassification.progression_skip_balancing),
    "Red Koopa":            MarioSuperSluggersItemData(0x80E5531302, ItemClassification.progression_skip_balancing),
    "Green Paratroopa":     MarioSuperSluggersItemData(0x80E5531402, ItemClassification.progression_skip_balancing),
    "Blue Shy Guy":         MarioSuperSluggersItemData(0x80E5531502, ItemClassification.progression_skip_balancing),
    "Yellow Shy Guy":       MarioSuperSluggersItemData(0x80E5531602, ItemClassification.progression_skip_balancing),
    "Green Shy Guy":        MarioSuperSluggersItemData(0x80E5531702, ItemClassification.progression_skip_balancing),
    "Gray Shy Guy":         MarioSuperSluggersItemData(0x80E5531802, ItemClassification.progression_skip_balancing),
    "Wiggler":              MarioSuperSluggersItemData(0x80E5531F02, ItemClassification.progression_skip_balancing),
    "Blooper":              MarioSuperSluggersItemData(0x80E5532002, ItemClassification.progression_skip_balancing),
    "Funky Kong":           MarioSuperSluggersItemData(0x80E5532102, ItemClassification.progression_skip_balancing),
    "Tiny Kong":            MarioSuperSluggersItemData(0x80E5532202, ItemClassification.progression_skip_balancing),
    "Kritter":              MarioSuperSluggersItemData(0x80E5532302, ItemClassification.progression_skip_balancing),
    "Blue Kritter":         MarioSuperSluggersItemData(0x80E5532402, ItemClassification.progression_skip_balancing),
    "Red Kritter":          MarioSuperSluggersItemData(0x80E5532502, ItemClassification.progression_skip_balancing),
    "Brown Kritter":        MarioSuperSluggersItemData(0x80E5532602, ItemClassification.progression_skip_balancing),
    "King K. Rool":         MarioSuperSluggersItemData(0x80E5532702, ItemClassification.progression_skip_balancing),
    "Baby Peach":           MarioSuperSluggersItemData(0x80E5532802, ItemClassification.progression_skip_balancing),
    "Baby Daisy":           MarioSuperSluggersItemData(0x80E5532902, ItemClassification.progression_skip_balancing),
    "Baby DK":              MarioSuperSluggersItemData(0x80E5532A02, ItemClassification.progression_skip_balancing),
    "Red Yoshi":            MarioSuperSluggersItemData(0x80E5532B02, ItemClassification.progression_skip_balancing),
    "Blue Yoshi":           MarioSuperSluggersItemData(0x80E5532C02, ItemClassification.progression_skip_balancing),
    "Yellow Yoshi":         MarioSuperSluggersItemData(0x80E5532D02, ItemClassification.progression_skip_balancing),
    "Light Blue Yoshi":     MarioSuperSluggersItemData(0x80E5532E02, ItemClassification.progression_skip_balancing),
    "Pink Yoshi":           MarioSuperSluggersItemData(0x80E5532F02, ItemClassification.progression_skip_balancing),
    "Day-night cycle":      MarioSuperSluggersItemData(0x80E55AE001, ItemClassification.progression_skip_balancing),
    "Fireball":             MarioSuperSluggersItemData(0x80E55AE301, ItemClassification.filler),
    "POW-Ball":             MarioSuperSluggersItemData(0x80E55AE501, ItemClassification.filler),
    "Mini Boo":             MarioSuperSluggersItemData(0x80E55AE701, ItemClassification.progression_skip_balancing),
    "Toy Field Pass":       MarioSuperSluggersItemData(0x80E55BF401, ItemClassification.filler),
    "Special Shop Pass":    MarioSuperSluggersItemData(0x80E55BF501, ItemClassification.filler),
    "Sea Hut Key":          MarioSuperSluggersItemData(0x80E55BF701, ItemClassification.progression_skip_balancing),
    "Baby Daisy's Rattle":  MarioSuperSluggersItemData(0x80E55BF801, ItemClassification.progression_skip_balancing),
    "Toad Statue":          MarioSuperSluggersItemData(0x80E55BF901, ItemClassification.progression_skip_balancing),
    "Daisy Statue":         MarioSuperSluggersItemData(0x80E55BFA01, ItemClassification.progression),
    "Stone tablet piece A": MarioSuperSluggersItemData(0x80E55BFB01, ItemClassification.progression),
    "Stone tablet piece B": MarioSuperSluggersItemData(0x80E55BFC01, ItemClassification.progression),
    "Stone tablet piece C": MarioSuperSluggersItemData(0x80E55BFD01, ItemClassification.progression),
    "Brush":                MarioSuperSluggersItemData(0x80E55BFE01, ItemClassification.progression_skip_balancing),
    "5 coins":              MarioSuperSluggersItemData(0x80E55C0A05, ItemClassification.filler),
    "10 coins":             MarioSuperSluggersItemData(0x80E55C0A0A, ItemClassification.filler),
    "20 coins":             MarioSuperSluggersItemData(0x80E55C0A14, ItemClassification.filler),
    "30 coins":             MarioSuperSluggersItemData(0x80E55C0A1E, ItemClassification.filler),
    "40 coins":             MarioSuperSluggersItemData(0x80E55C0A28, ItemClassification.filler),
    "50 coins":             MarioSuperSluggersItemData(0x80E55C0A32, ItemClassification.filler),
    "70 coins":             MarioSuperSluggersItemData(0x80E55C0A46, ItemClassification.filler),
    "80 coins":             MarioSuperSluggersItemData(0x80E55C0A50, ItemClassification.filler),
    "100 coins":            MarioSuperSluggersItemData(0x80E55C0A64, ItemClassification.filler),
}

ITEM_NAME_TO_ID = {name: data.code for name, data in ITEM_DATA.items()}

ITEM_NAME_GROUPS = {
    "Characters": {
        "Mario",
        "Luigi",
        "Donkey Kong",
        "Diddy Kong",
        "Peach",
        "Daisy",
        "Yoshi",
        "Baby Mario",
        "Baby Luigi",
        "Wario",
        "Waluigi",
        "Koopa",
        "Red Toad",
        "Boo",
        "Toadette",
        "Shy Guy",
        "Birdo",
        "Monty Mole",
        "Paratroopa",
        "Blue Pianta",
        "Red Pianta",
        "Yellow Pianta",
        "Blue Noki",
        "Red Noki",
        "Green Noki",
        "Toadsworth",
        "Blue Toad",
        "Yellow Toad",
        "Green Toad",
        "Purple Toad",
        "King Boo",
        "Petey Piranha",
        "Dixie Kong",
        "Goomba",
        "Paragoomba",
        "Red Koopa",
        "Green Paratroopa",
        "Blue Shy Guy",
        "Yellow Shy Guy",
        "Green Shy Guy",
        "Gray Shy Guy",
        "Wiggler",
        "Blooper",
        "Funky Kong",
        "Tiny Kong",
        "Kritter",
        "Blue Kritter",
        "Red Kritter",
        "Brown Kritter",
        "King K. Rool",
        "Baby Peach",
        "Baby Daisy",
        "Baby DK",
        "Red Yoshi",
        "Blue Yoshi",
        "Yellow Yoshi",
        "Light Blue Yoshi",
        "Pink Yoshi",
	},
    "Stone tablet": {
        "Stone tablet piece A",
        "Stone tablet piece B",
        "Stone tablet piece C",
    }
}

def get_filler_item_name() -> str:
    return "5 coins"


def create_item(world: MarioSuperSluggersWorld, name: str) -> MarioSuperSluggersItem:
    return MarioSuperSluggersItem(name, ITEM_DATA[name].type, ITEM_DATA[name].code, world.player)


def create_items(world: MarioSuperSluggersWorld) -> None:
    items_to_create = list(ITEM_DATA.keys())
    starting_captains = ["Mario", "Peach", "Yoshi", "Donkey Kong", "Wario"]
    starting_captain = starting_captains[world.options.starting_captain]
    items_to_create.remove(starting_captain)
    world.push_precollected(create_item(world, starting_captain))
    items_to_create += ["5 coins"] * 5
    items_to_create += ["10 coins"] * 7
    items_to_create += ["20 coins"] * 5
    items_to_create += ["30 coins"] * 5
    items_to_create += ["40 coins"]
    items_to_create += ["50 coins"] * 3
    items_to_create += ["100 coins"]
    number_of_unfilled_locations = len(world.multiworld.get_unfilled_locations(world.player))
    items_to_create += [get_filler_item_name() for _ in range(number_of_unfilled_locations - len(items_to_create))]
    world.multiworld.itempool += [create_item(world, item) for item in items_to_create]
