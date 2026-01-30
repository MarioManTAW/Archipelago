
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
    "Mario":                  MarioSuperSluggersItemData(0x80E552E902, ItemClassification.progression),
    "Luigi":                  MarioSuperSluggersItemData(0x80E552EA02, ItemClassification.progression_skip_balancing),
    "Donkey Kong":            MarioSuperSluggersItemData(0x80E552EB02, ItemClassification.progression),
    "Diddy Kong":             MarioSuperSluggersItemData(0x80E552EC02, ItemClassification.progression_skip_balancing),
    "Peach":                  MarioSuperSluggersItemData(0x80E552ED02, ItemClassification.progression),
    "Daisy":                  MarioSuperSluggersItemData(0x80E552EE02, ItemClassification.progression_skip_balancing),
    "Yoshi":                  MarioSuperSluggersItemData(0x80E552EF02, ItemClassification.progression),
    "Baby Mario":             MarioSuperSluggersItemData(0x80E552F002, ItemClassification.progression_skip_balancing),
    "Baby Luigi":             MarioSuperSluggersItemData(0x80E552F102, ItemClassification.progression_skip_balancing),
    "Bowser":                 MarioSuperSluggersItemData(0x80E552F202, ItemClassification.progression_skip_balancing),
    "Wario":                  MarioSuperSluggersItemData(0x80E552F302, ItemClassification.progression),
    "Waluigi":                MarioSuperSluggersItemData(0x80E552F402, ItemClassification.progression_skip_balancing),
    "Koopa":                  MarioSuperSluggersItemData(0x80E552F502, ItemClassification.progression_skip_balancing),
    "Red Toad":               MarioSuperSluggersItemData(0x80E552F602, ItemClassification.progression_skip_balancing),
    "Boo":                    MarioSuperSluggersItemData(0x80E552F702, ItemClassification.progression_skip_balancing),
    "Toadette":               MarioSuperSluggersItemData(0x80E552F802, ItemClassification.progression_skip_balancing),
    "Shy Guy":                MarioSuperSluggersItemData(0x80E552F902, ItemClassification.progression_skip_balancing),
    "Birdo":                  MarioSuperSluggersItemData(0x80E552FA02, ItemClassification.progression_skip_balancing),
    "Monty Mole":             MarioSuperSluggersItemData(0x80E552FB02, ItemClassification.progression_skip_balancing),
    "Bowser Jr.":             MarioSuperSluggersItemData(0x80E552FC02, ItemClassification.progression_skip_balancing),
    "Paratroopa":             MarioSuperSluggersItemData(0x80E552FD02, ItemClassification.progression_skip_balancing),
    "Blue Pianta":            MarioSuperSluggersItemData(0x80E552FE02, ItemClassification.progression_skip_balancing),
    "Red Pianta":             MarioSuperSluggersItemData(0x80E552FF02, ItemClassification.progression_skip_balancing),
    "Yellow Pianta":          MarioSuperSluggersItemData(0x80E5530002, ItemClassification.progression_skip_balancing),
    "Blue Noki":              MarioSuperSluggersItemData(0x80E5530102, ItemClassification.progression),
    "Red Noki":               MarioSuperSluggersItemData(0x80E5530202, ItemClassification.progression_skip_balancing),
    "Green Noki":             MarioSuperSluggersItemData(0x80E5530302, ItemClassification.progression),
    "Hammer Bro":             MarioSuperSluggersItemData(0x80E5530402, ItemClassification.progression_skip_balancing),
    "Toadsworth":             MarioSuperSluggersItemData(0x80E5530502, ItemClassification.progression_skip_balancing),
    "Blue Toad":              MarioSuperSluggersItemData(0x80E5530602, ItemClassification.progression_skip_balancing),
    "Yellow Toad":            MarioSuperSluggersItemData(0x80E5530702, ItemClassification.progression_skip_balancing),
    "Green Toad":             MarioSuperSluggersItemData(0x80E5530802, ItemClassification.progression_skip_balancing),
    "Purple Toad":            MarioSuperSluggersItemData(0x80E5530902, ItemClassification.progression_skip_balancing),
    "Magikoopa":              MarioSuperSluggersItemData(0x80E5530A02, ItemClassification.progression_skip_balancing),
    "Red Magikoopa":          MarioSuperSluggersItemData(0x80E5530B02, ItemClassification.progression_skip_balancing),
    "Green Magikoopa":        MarioSuperSluggersItemData(0x80E5530C02, ItemClassification.progression_skip_balancing),
    "Yellow Magikoopa":       MarioSuperSluggersItemData(0x80E5530D02, ItemClassification.progression_skip_balancing),
    "King Boo":               MarioSuperSluggersItemData(0x80E5530E02, ItemClassification.progression_skip_balancing),
    "Petey Piranha":          MarioSuperSluggersItemData(0x80E5530F02, ItemClassification.progression_skip_balancing),
    "Dixie Kong":             MarioSuperSluggersItemData(0x80E5531002, ItemClassification.progression_skip_balancing),
    "Goomba":                 MarioSuperSluggersItemData(0x80E5531102, ItemClassification.progression_skip_balancing),
    "Paragoomba":             MarioSuperSluggersItemData(0x80E5531202, ItemClassification.progression_skip_balancing),
    "Red Koopa":              MarioSuperSluggersItemData(0x80E5531302, ItemClassification.progression_skip_balancing),
    "Green Paratroopa":       MarioSuperSluggersItemData(0x80E5531402, ItemClassification.progression_skip_balancing),
    "Blue Shy Guy":           MarioSuperSluggersItemData(0x80E5531502, ItemClassification.progression_skip_balancing),
    "Yellow Shy Guy":         MarioSuperSluggersItemData(0x80E5531602, ItemClassification.progression_skip_balancing),
    "Green Shy Guy":          MarioSuperSluggersItemData(0x80E5531702, ItemClassification.progression_skip_balancing),
    "Gray Shy Guy":           MarioSuperSluggersItemData(0x80E5531802, ItemClassification.progression_skip_balancing),
    "Dry Bones":              MarioSuperSluggersItemData(0x80E5531902, ItemClassification.progression_skip_balancing),
    "Green Dry Bones":        MarioSuperSluggersItemData(0x80E5531A02, ItemClassification.progression_skip_balancing),
    "Dark Bones":             MarioSuperSluggersItemData(0x80E5531B02, ItemClassification.progression_skip_balancing),
    "Blue Dry Bones":         MarioSuperSluggersItemData(0x80E5531C02, ItemClassification.progression_skip_balancing),
    "Fire Bro":               MarioSuperSluggersItemData(0x80E5531D02, ItemClassification.progression_skip_balancing),
    "Boomerang Bro":          MarioSuperSluggersItemData(0x80E5531E02, ItemClassification.progression_skip_balancing),
    "Wiggler":                MarioSuperSluggersItemData(0x80E5531F02, ItemClassification.progression_skip_balancing),
    "Blooper":                MarioSuperSluggersItemData(0x80E5532002, ItemClassification.progression_skip_balancing),
    "Funky Kong":             MarioSuperSluggersItemData(0x80E5532102, ItemClassification.progression_skip_balancing),
    "Tiny Kong":              MarioSuperSluggersItemData(0x80E5532202, ItemClassification.progression_skip_balancing),
    "Kritter":                MarioSuperSluggersItemData(0x80E5532302, ItemClassification.progression_skip_balancing),
    "Blue Kritter":           MarioSuperSluggersItemData(0x80E5532402, ItemClassification.progression_skip_balancing),
    "Red Kritter":            MarioSuperSluggersItemData(0x80E5532502, ItemClassification.progression_skip_balancing),
    "Brown Kritter":          MarioSuperSluggersItemData(0x80E5532602, ItemClassification.progression_skip_balancing),
    "King K. Rool":           MarioSuperSluggersItemData(0x80E5532702, ItemClassification.progression_skip_balancing),
    "Baby Peach":             MarioSuperSluggersItemData(0x80E5532802, ItemClassification.progression_skip_balancing),
    "Baby Daisy":             MarioSuperSluggersItemData(0x80E5532902, ItemClassification.progression_skip_balancing),
    "Baby DK":                MarioSuperSluggersItemData(0x80E5532A02, ItemClassification.progression_skip_balancing),
    "Red Yoshi":              MarioSuperSluggersItemData(0x80E5532B02, ItemClassification.progression_skip_balancing),
    "Blue Yoshi":             MarioSuperSluggersItemData(0x80E5532C02, ItemClassification.progression_skip_balancing),
    "Yellow Yoshi":           MarioSuperSluggersItemData(0x80E5532D02, ItemClassification.progression_skip_balancing),
    "Light Blue Yoshi":       MarioSuperSluggersItemData(0x80E5532E02, ItemClassification.progression_skip_balancing),
    "Pink Yoshi":             MarioSuperSluggersItemData(0x80E5532F02, ItemClassification.progression_skip_balancing),
    "Star for Mario":         MarioSuperSluggersItemData(0x80E55B8002, ItemClassification.progression_skip_balancing),
    "Star for Luigi":         MarioSuperSluggersItemData(0x80E55B8102, ItemClassification.progression_skip_balancing),
    "Star for Donkey Kong":   MarioSuperSluggersItemData(0x80E55B8202, ItemClassification.progression_skip_balancing),
    "Star for Diddy Kong":    MarioSuperSluggersItemData(0x80E55B8302, ItemClassification.progression_skip_balancing),
    "Star for Peach":         MarioSuperSluggersItemData(0x80E55B8402, ItemClassification.progression_skip_balancing),
    "Star for Daisy":         MarioSuperSluggersItemData(0x80E55B8502, ItemClassification.progression_skip_balancing),
    "Star for Yoshi":         MarioSuperSluggersItemData(0x80E55B8602, ItemClassification.progression_skip_balancing),
    "Star for Baby Mario":    MarioSuperSluggersItemData(0x80E55B8702, ItemClassification.progression_skip_balancing),
    "Star for Baby Luigi":    MarioSuperSluggersItemData(0x80E55B8802, ItemClassification.progression_skip_balancing),
    "Star for Bowser":        MarioSuperSluggersItemData(0x80E55B8902, ItemClassification.progression_skip_balancing),
    "Star for Wario":         MarioSuperSluggersItemData(0x80E55B8A02, ItemClassification.progression_skip_balancing),
    "Star for Waluigi":       MarioSuperSluggersItemData(0x80E55B8B02, ItemClassification.progression_skip_balancing),
    "Star for Koopa":         MarioSuperSluggersItemData(0x80E55B8C02, ItemClassification.progression_skip_balancing),
    "Star for Toad":          MarioSuperSluggersItemData(0x80E55B8D02, ItemClassification.progression_skip_balancing),
    "Star for Boo":           MarioSuperSluggersItemData(0x80E55B8E02, ItemClassification.progression_skip_balancing),
    "Star for Toadette":      MarioSuperSluggersItemData(0x80E55B8F02, ItemClassification.progression_skip_balancing),
    "Star for Shy Guy":       MarioSuperSluggersItemData(0x80E55B9002, ItemClassification.progression_skip_balancing),
    "Star for Birdo":         MarioSuperSluggersItemData(0x80E55B9102, ItemClassification.progression_skip_balancing),
    "Star for Monty Mole":    MarioSuperSluggersItemData(0x80E55B9202, ItemClassification.progression_skip_balancing),
    "Star for Bowser Jr.":    MarioSuperSluggersItemData(0x80E55B9302, ItemClassification.progression_skip_balancing),
    "Star for Paratroopa":    MarioSuperSluggersItemData(0x80E55B9402, ItemClassification.progression_skip_balancing),
    "Star for Pianta":        MarioSuperSluggersItemData(0x80E55B9502, ItemClassification.progression_skip_balancing),
    "Star for Noki":          MarioSuperSluggersItemData(0x80E55B9602, ItemClassification.progression_skip_balancing),
    "Star for Hammer Bro":    MarioSuperSluggersItemData(0x80E55B9702, ItemClassification.progression_skip_balancing),
    "Star for Toadsworth":    MarioSuperSluggersItemData(0x80E55B9802, ItemClassification.progression_skip_balancing),
    "Star for Magikoopa":     MarioSuperSluggersItemData(0x80E55B9902, ItemClassification.progression_skip_balancing),
    "Star for King Boo":      MarioSuperSluggersItemData(0x80E55B9A02, ItemClassification.progression_skip_balancing),
    "Star for Petey Piranha": MarioSuperSluggersItemData(0x80E55B9B02, ItemClassification.progression_skip_balancing),
    "Star for Dixie Kong":    MarioSuperSluggersItemData(0x80E55B9C02, ItemClassification.progression_skip_balancing),
    "Star for Goomba":        MarioSuperSluggersItemData(0x80E55B9D02, ItemClassification.progression_skip_balancing),
    "Star for Paragoomba":    MarioSuperSluggersItemData(0x80E55B9E02, ItemClassification.progression_skip_balancing),
    "Star for Dry Bones":     MarioSuperSluggersItemData(0x80E55B9F02, ItemClassification.progression_skip_balancing),
    "Star for Wiggler":       MarioSuperSluggersItemData(0x80E55BA002, ItemClassification.progression_skip_balancing),
    "Star for Blooper":       MarioSuperSluggersItemData(0x80E55BA102, ItemClassification.progression_skip_balancing),
    "Star for Funky Kong":    MarioSuperSluggersItemData(0x80E55BA202, ItemClassification.progression_skip_balancing),
    "Star for Tiny Kong":     MarioSuperSluggersItemData(0x80E55BA302, ItemClassification.progression_skip_balancing),
    "Star for Kritter":       MarioSuperSluggersItemData(0x80E55BA402, ItemClassification.progression_skip_balancing),
    "Star for King K. Rool":  MarioSuperSluggersItemData(0x80E55BA502, ItemClassification.progression_skip_balancing),
    "Star for Baby Peach":    MarioSuperSluggersItemData(0x80E55BA602, ItemClassification.progression_skip_balancing),
    "Star for Baby Daisy":    MarioSuperSluggersItemData(0x80E55BA702, ItemClassification.progression_skip_balancing),
    "Star for Baby DK":       MarioSuperSluggersItemData(0x80E55BA802, ItemClassification.progression_skip_balancing),
    "Day-night cycle":        MarioSuperSluggersItemData(0x80E55AE001, ItemClassification.progression),
    "Fireball":               MarioSuperSluggersItemData(0x80E55AE301, ItemClassification.filler),
    "POW-Ball":               MarioSuperSluggersItemData(0x80E55AE501, ItemClassification.filler),
    "Mini Boo":               MarioSuperSluggersItemData(0x80E55AE701, ItemClassification.progression_skip_balancing),
    "Luigi's Flashlight":     MarioSuperSluggersItemData(0x80E55BF201, ItemClassification.progression),
    "Cruiser Pass":           MarioSuperSluggersItemData(0x80E55BF301, ItemClassification.progression),
    "Toy Field Pass":         MarioSuperSluggersItemData(0x80E55BF401, ItemClassification.progression),
    "Special Shop Pass":      MarioSuperSluggersItemData(0x80E55BF501, ItemClassification.progression),
    "Sea Hut Key":            MarioSuperSluggersItemData(0x80E55BF701, ItemClassification.progression),
    "Baby Daisy's Rattle":    MarioSuperSluggersItemData(0x80E55BF801, ItemClassification.progression_skip_balancing),
    "Toad Statue":            MarioSuperSluggersItemData(0x80E55BF901, ItemClassification.progression_skip_balancing),
    "Daisy Statue":           MarioSuperSluggersItemData(0x80E55BFA01, ItemClassification.progression),
    "Stone tablet piece A":   MarioSuperSluggersItemData(0x80E55BFB01, ItemClassification.progression),
    "Stone tablet piece B":   MarioSuperSluggersItemData(0x80E55BFC01, ItemClassification.progression),
    "Stone tablet piece C":   MarioSuperSluggersItemData(0x80E55BFD01, ItemClassification.progression),
    "Brush":                  MarioSuperSluggersItemData(0x80E55BFE01, ItemClassification.progression),
    "5 coins":                MarioSuperSluggersItemData(0x80E55C0A05, ItemClassification.filler),
    "10 coins":               MarioSuperSluggersItemData(0x80E55C0A0A, ItemClassification.filler),
    "20 coins":               MarioSuperSluggersItemData(0x80E55C0A14, ItemClassification.filler),
    "30 coins":               MarioSuperSluggersItemData(0x80E55C0A1E, ItemClassification.filler),
    "40 coins":               MarioSuperSluggersItemData(0x80E55C0A28, ItemClassification.filler),
    "50 coins":               MarioSuperSluggersItemData(0x80E55C0A32, ItemClassification.filler),
    "70 coins":               MarioSuperSluggersItemData(0x80E55C0A46, ItemClassification.filler),
    "80 coins":               MarioSuperSluggersItemData(0x80E55C0A50, ItemClassification.filler),
    "100 coins":              MarioSuperSluggersItemData(0x80E55C0A64, ItemClassification.filler),
    "Nice Bat":               MarioSuperSluggersItemData(0x80E55DAC01, ItemClassification.filler),
    "Power Bat":              MarioSuperSluggersItemData(0x80E55DAD01, ItemClassification.filler),
    "Dr. K":                  MarioSuperSluggersItemData(0x80E55DAE01, ItemClassification.filler),
    "Lucky Glove":            MarioSuperSluggersItemData(0x80E55DAF01, ItemClassification.filler),
    "Dash Spikes":            MarioSuperSluggersItemData(0x80E55DB001, ItemClassification.filler),
    "Buddy Badge":            MarioSuperSluggersItemData(0x80E55DB101, ItemClassification.filler),
    "Error Booster":          MarioSuperSluggersItemData(0x80E55DB201, ItemClassification.filler),
    "Charge Bat":             MarioSuperSluggersItemData(0x80E55DB301, ItemClassification.filler),
    "Star Candy":             MarioSuperSluggersItemData(0x80E55DB401, ItemClassification.filler),
    "x2 Star Candy":          MarioSuperSluggersItemData(0x80E55DB501, ItemClassification.filler),
    "Superstar":              MarioSuperSluggersItemData(0x80E55DB601, ItemClassification.filler),
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
        "Bowser",
        "Wario",
        "Waluigi",
        "Koopa",
        "Red Toad",
        "Boo",
        "Toadette",
        "Shy Guy",
        "Birdo",
        "Monty Mole",
        "Bowser Jr.",
        "Paratroopa",
        "Blue Pianta",
        "Red Pianta",
        "Yellow Pianta",
        "Blue Noki",
        "Red Noki",
        "Green Noki",
        "Hammer Bro",
        "Toadsworth",
        "Blue Toad",
        "Yellow Toad",
        "Green Toad",
        "Purple Toad",
        "Magikoopa",
        "Red Magikoopa",
        "Green Magikoopa",
        "Yellow Magikoopa",
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
        "Dry Bones",
        "Green Dry Bones",
        "Dark Bones",
        "Blue Dry Bones",
        "Fire Bro",
        "Boomerang Bro",
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
    "Stars": {
        "Star for Mario",
        "Star for Luigi",
        "Star for Donkey Kong",
        "Star for Diddy Kong",
        "Star for Peach",
        "Star for Daisy",
        "Star for Yoshi",
        "Star for Baby Mario",
        "Star for Baby Luigi",
        "Star for Bowser",
        "Star for Wario",
        "Star for Waluigi",
        "Star for Koopa",
        "Star for Toad",
        "Star for Boo",
        "Star for Toadette",
        "Star for Shy Guy",
        "Star for Birdo",
        "Star for Monty Mole",
        "Star for Bowser Jr.",
        "Star for Paratroopa",
        "Star for Pianta",
        "Star for Noki",
        "Star for Hammer Bro",
        "Star for Toadsworth",
        "Star for Magikoopa",
        "Star for King Boo",
        "Star for Petey Piranha",
        "Star for Dixie Kong",
        "Star for Goomba",
        "Star for Paragoomba",
        "Star for Dry Bones",
        "Star for Wiggler",
        "Star for Blooper",
        "Star for Funky Kong",
        "Star for Tiny Kong",
        "Star for Kritter",
        "Star for King K. Rool",
        "Star for Baby Peach",
        "Star for Baby Daisy",
        "Star for Baby DK",
    },
    "Stone tablet": {
        "Stone tablet piece A",
        "Stone tablet piece B",
        "Stone tablet piece C",
    }
}

MINIGAMES = [
    "Play Bob-omb Derby", "Play Wall Ball", "Play Barrel Basher", "Play Gem Catch", "Play Piranha Panic",
    "Play Blooper Baserun", "Play Ghost K", "Play Toy Field", "Play Graffiti Runner", "Play Bowser Pinball"
]

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
    items_to_create += ["10 coins"] * 8
    items_to_create += ["20 coins"] * 5
    items_to_create += ["30 coins"] * 5
    items_to_create += ["40 coins"]
    items_to_create += ["50 coins"] * 3
    items_to_create += ["100 coins"]
    game_items = [
        "Nice Bat", "Power Bat", "Dr. K", "Lucky Glove", "Dash Spikes", "Buddy Badge", "Error Booster", "Charge Bat"
    ]
    special_game_items = [
        "Star Candy", "x2 Star Candy", "Superstar"
    ]
    if world.options.randomize_shops == world.options.randomize_shops.option_full:
        items_to_create += game_items * 5
    else:
        for item in game_items:
            items_to_create.remove(item)
        for item in special_game_items:
            items_to_create.remove(item)
        if world.options.randomize_shops == world.options.randomize_shops.option_none:
            items_to_create.remove("Luigi's Flashlight")
            items_to_create.remove("Cruiser Pass")
            world.get_location("Blue Pianta's shop: Buy Luigi's Flashlight")\
                .place_locked_item(create_item(world, "Luigi's Flashlight"))
            world.get_location("Toadsworth's shop: Buy Cruiser Pass")\
                .place_locked_item(create_item(world, "Cruiser Pass"))
    bowser_monsters = [
        "Bowser", "Bowser Jr.", "Hammer Bro", "Magikoopa", "Red Magikoopa", "Green Magikoopa", "Yellow Magikoopa",
        "Dry Bones", "Green Dry Bones", "Dark Bones", "Blue Dry Bones", "Fire Bro", "Boomerang Bro",
    ]
    if world.options.goal_condition == world.options.goal_condition.option_defeat_bowser_monsters:
        for item in bowser_monsters:
            items_to_create.remove(item)
    if not world.options.randomize_stars:
        for item in ITEM_NAME_GROUPS["Stars"]:
            items_to_create.remove(item)
        if world.options.goal_condition == world.options.goal_condition.option_star_badge:
            for item in ITEM_NAME_GROUPS["Stars"]:
                world.get_location("Bowser Castle: Unlock s" + item[1:])\
                    .place_locked_item(create_item(world, item))
    number_of_unfilled_locations = len(world.multiworld.get_unfilled_locations(world.player))
    items_to_create += [get_filler_item_name() for _ in range(number_of_unfilled_locations - len(items_to_create))]
    world.multiworld.itempool += [create_item(world, item) for item in items_to_create]
