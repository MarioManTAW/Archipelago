from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import Location
from . import items

if TYPE_CHECKING:
    from . import MarioSuperSluggersWorld

LOCATION_NAME_TO_ID = {
    "Mario Stadium: Recruit Luigi":                       0x80E55AEA02,
    "DK Jungle: Recruit Donkey Kong":                     0x80E55AEB02,
    "DK Jungle: Recruit Diddy Kong":                      0x80E55AEC02,
    "Peach Ice Garden: Recruit Peach":                    0x80E55AED02,
    "Peach Ice Garden: Recruit Daisy":                    0x80E55AEE02,
    "Yoshi Park: Recruit Yoshi":                          0x80E55AEF02,
    "Mario Stadium: Recruit Baby Mario":                  0x80E55AF002,
    "Mario Stadium: Recruit Baby Luigi":                  0x80E55AF102,
    "Bowser Castle: Recruit Bowser":                      0x80E55AF202,
    "Wario City: Recruit Wario":                          0x80E55AF302,
    "Wario City: Recruit Waluigi":                        0x80E55AF402,
    "Wario City: Recruit Koopa":                          0x80E55AF502,
    "Peach Ice Garden: Recruit Red Toad":                 0x80E55AF602,
    "Wario City: Recruit Boo":                            0x80E55AF702,
    "Peach Ice Garden: Recruit Toadette":                 0x80E55AF802,
    "Yoshi Park: Recruit Shy Guy":                        0x80E55AF902,
    "Yoshi Park: Recruit Birdo":                          0x80E55AFA02,
    "Mario Stadium: Recruit Monty Mole":                  0x80E55AFB02,
    "Bowser Castle: Recruit Bowser Jr.":                  0x80E55AFC02,
    "Wario City: Recruit Paratroopa":                     0x80E55AFD02,
    "Mario Stadium: Recruit Blue Pianta":                 0x80E55AFE02,
    "Mario Stadium: Recruit Red Pianta":                  0x80E55AFF02,
    "Mario Stadium: Recruit Yellow Pianta":               0x80E55B0002,
    "Mario Stadium: Recruit Blue Noki":                   0x80E55B0102,
    "Mario Stadium: Recruit Red Noki":                    0x80E55B0202,
    "Mario Stadium: Recruit Green Noki":                  0x80E55B0302,
    "Bowser Castle: Recruit Hammer Bro":                  0x80E55B0402,
    "Peach Ice Garden: Recruit Toadsworth":               0x80E55B0502,
    "Peach Ice Garden: Recruit Blue Toad":                0x80E55B0602,
    "Peach Ice Garden: Recruit Yellow Toad":              0x80E55B0702,
    "Peach Ice Garden: Recruit Green Toad":               0x80E55B0802,
    "Peach Ice Garden: Recruit Purple Toad":              0x80E55B0902,
    "Bowser Castle: Recruit Magikoopa":                   0x80E55B0A02,
    "Bowser Castle: Recruit Red Magikoopa":               0x80E55B0B02,
    "Bowser Castle: Recruit Green Magikoopa":             0x80E55B0C02,
    "Bowser Castle: Recruit Yellow Magikoopa":            0x80E55B0D02,
    "Wario City: Recruit King Boo":                       0x80E55B0E02,
    "Peach Ice Garden: Recruit Petey Piranha":            0x80E55B0F02,
    "DK Jungle: Recruit Dixie Kong":                      0x80E55B1002,
    "Wario City: Recruit Goomba":                         0x80E55B1102,
    "Wario City: Recruit Paragoomba":                     0x80E55B1202,
    "Wario City: Recruit Red Koopa":                      0x80E55B1302,
    "Wario City: Recruit Green Paratroopa":               0x80E55B1402,
    "Yoshi Park: Recruit Blue Shy Guy":                   0x80E55B1502,
    "Yoshi Park: Recruit Yellow Shy Guy":                 0x80E55B1602,
    "Yoshi Park: Recruit Green Shy Guy":                  0x80E55B1702,
    "Yoshi Park: Recruit Gray Shy Guy":                   0x80E55B1802,
    "Bowser Castle: Recruit Dry Bones":                   0x80E55B1902,
    "Bowser Castle: Recruit Green Dry Bones":             0x80E55B1A02,
    "Bowser Castle: Recruit Dark Bones":                  0x80E55B1B02,
    "Bowser Castle: Recruit Blue Dry Bones":              0x80E55B1C02,
    "Bowser Castle: Recruit Fire Bro":                    0x80E55B1D02,
    "Bowser Castle: Recruit Boomerang Bro":               0x80E55B1E02,
    "Yoshi Park: Recruit Wiggler":                        0x80E55B1F02,
    "Mario Stadium: Recruit Blooper":                     0x80E55B2002,
    "DK Jungle: Recruit Funky Kong":                      0x80E55B2102,
    "DK Jungle: Recruit Tiny Kong":                       0x80E55B2202,
    "DK Jungle: Recruit Kritter":                         0x80E55B2302,
    "DK Jungle: Recruit Blue Kritter":                    0x80E55B2402,
    "DK Jungle: Recruit Red Kritter":                     0x80E55B2502,
    "DK Jungle: Recruit Brown Kritter":                   0x80E55B2602,
    "DK Jungle: Recruit King K. Rool":                    0x80E55B2702,
    "Peach Ice Garden: Recruit Baby Peach":               0x80E55B2802,
    "Peach Ice Garden: Recruit Baby Daisy":               0x80E55B2902,
    "DK Jungle: Recruit Baby DK":                         0x80E55B2A02,
    "Yoshi Park: Recruit Red Yoshi":                      0x80E55B2B02,
    "Yoshi Park: Recruit Blue Yoshi":                     0x80E55B2C02,
    "Yoshi Park: Recruit Yellow Yoshi":                   0x80E55B2D02,
    "Yoshi Park: Recruit Light Blue Yoshi":               0x80E55B2E02,
    "Yoshi Park: Recruit Pink Yoshi":                     0x80E55B2F02,
    "Bowser Castle: Unlock star for Mario":               0x80E5538002,
    "Bowser Castle: Unlock star for Luigi":               0x80E5538102,
    "Bowser Castle: Unlock star for Donkey Kong":         0x80E5538202,
    "Bowser Castle: Unlock star for Diddy Kong":          0x80E5538302,
    "Bowser Castle: Unlock star for Peach":               0x80E5538402,
    "Bowser Castle: Unlock star for Daisy":               0x80E5538502,
    "Bowser Castle: Unlock star for Yoshi":               0x80E5538602,
    "Bowser Castle: Unlock star for Baby Mario":          0x80E5538702,
    "Bowser Castle: Unlock star for Baby Luigi":          0x80E5538802,
    "Bowser Castle: Unlock star for Bowser":              0x80E5538902,
    "Bowser Castle: Unlock star for Wario":               0x80E5538A02,
    "Bowser Castle: Unlock star for Waluigi":             0x80E5538B02,
    "Bowser Castle: Unlock star for Koopa":               0x80E5538C02,
    "Bowser Castle: Unlock star for Toad":                0x80E5538D02,
    "Bowser Castle: Unlock star for Boo":                 0x80E5538E02,
    "Bowser Castle: Unlock star for Toadette":            0x80E5538F02,
    "Bowser Castle: Unlock star for Shy Guy":             0x80E5539002,
    "Bowser Castle: Unlock star for Birdo":               0x80E5539102,
    "Bowser Castle: Unlock star for Monty Mole":          0x80E5539202,
    "Bowser Castle: Unlock star for Bowser Jr.":          0x80E5539302,
    "Bowser Castle: Unlock star for Paratroopa":          0x80E5539402,
    "Bowser Castle: Unlock star for Pianta":              0x80E5539502,
    "Bowser Castle: Unlock star for Noki":                0x80E5539602,
    "Bowser Castle: Unlock star for Hammer Bro":          0x80E5539702,
    "Bowser Castle: Unlock star for Toadsworth":          0x80E5539802,
    "Bowser Castle: Unlock star for Magikoopa":           0x80E5539902,
    "Bowser Castle: Unlock star for King Boo":            0x80E5539A02,
    "Bowser Castle: Unlock star for Petey Piranha":       0x80E5539B02,
    "Bowser Castle: Unlock star for Dixie Kong":          0x80E5539C02,
    "Bowser Castle: Unlock star for Goomba":              0x80E5539D02,
    "Bowser Castle: Unlock star for Paragoomba":          0x80E5539E02,
    "Bowser Castle: Unlock star for Dry Bones":           0x80E5539F02,
    "Bowser Castle: Unlock star for Wiggler":             0x80E553A002,
    "Bowser Castle: Unlock star for Blooper":             0x80E553A102,
    "Bowser Castle: Unlock star for Funky Kong":          0x80E553A202,
    "Bowser Castle: Unlock star for Tiny Kong":           0x80E553A302,
    "Bowser Castle: Unlock star for Kritter":             0x80E553A402,
    "Bowser Castle: Unlock star for King K. Rool":        0x80E553A502,
    "Bowser Castle: Unlock star for Baby Peach":          0x80E553A602,
    "Bowser Castle: Unlock star for Baby Daisy":          0x80E553A702,
    "Bowser Castle: Unlock star for Baby DK":             0x80E553A802,
    "Mario Stadium: Chest":                               0x80E55BAD01,
    "Peach Ice Garden: Chest":                            0x80E55BB101,
    "DK Jungle: Chest":                                   0x80E55BB801,
    "Yoshi Park: Chest":                                  0x80E55BBC01,
    "Wario City: Chest":                                  0x80E55BC701,
    "Mario Stadium: Red Noki's gift":                     0x80E55C9501,
    "Mario Stadium: Bottom barrel":                       0x80E55D5901,
    "Mario Stadium: Middle barrel after Yellow Pianta":   0x80E55D5902,
    "Mario Stadium: Top barrel":                          0x80E55D5904,
    "Mario Stadium: Bottom bush":                         0x80E55D5908,
    "Mario Stadium: Top bush":                            0x80E55D5910,
    "Mario Stadium: Central tree after Red Pianta":       0x80E55D5920,
    "Mario Stadium: Top tree":                            0x80E55D5940,
    "Peach Ice Garden: Right mushroom after Yellow Toad": 0x80E55D5A01,
    "Peach Ice Garden: Top bush":                         0x80E55D5B01,
    "Peach Ice Garden: Left bush after Green Toad":       0x80E55D5B02,
    "Peach Ice Garden: Bottom bush":                      0x80E55D5B04,
    "Peach Ice Garden: Right bush after Purple Toad":     0x80E55D5B08,
    "Peach Ice Garden: Top topiary after Toad Statue":    0x80E55D5B10,
    "Peach Ice Garden: Left topiary after Baby Peach":    0x80E55D5B20,
    "Peach Ice Garden: Right topiary":                    0x80E55D5B40,
    "Peach Ice Garden: Top mushroom":                     0x80E55D5B80,
    "Wario City: Central tree":                           0x80E55D5C01,
    "Wario City: Right tree after Paragoomba":            0x80E55D5C02,
    "Wario City: Trash can near entrance":                0x80E55D5D10,
    "Wario City: Trash can near dynamo":                  0x80E55D5D20,
    "Wario City: Top tree":                               0x80E55D5D80,
    "DK Jungle: Top flowers near entrance":               0x80E55D5E01,
    "DK Jungle: Barrel after Blue Kritter":               0x80E55D5E02,
    "DK Jungle: Tree near shop":                          0x80E55D5F01,
    "DK Jungle: Tree near Dixie Kong":                    0x80E55D5F02,
    "DK Jungle: Tree below entrance after Baby DK":       0x80E55D5F04,
    "DK Jungle: Bottom flowers near entrance":            0x80E55D5F08,
    "DK Jungle: Flowers near bridge":                     0x80E55D5F10,
    "DK Jungle: Flowers below central tree":              0x80E55D5F20,
    "DK Jungle: Flowers near Funky Kong":                 0x80E55D5F40,
    "DK Jungle: Flowers below entrance":                  0x80E55D5F80,
    "Yoshi Park: Left stump after Shy Guys":              0x80E55D6101,
    "Yoshi Park: Right stump after Shy Guys":             0x80E55D6102,
    "Yoshi Park: Tree near shop after Pink Yoshi":        0x80E55D6104,
    "Yoshi Park: Tree near Birdo after Yellow Yoshi":     0x80E55D6108,
    "Yoshi Park: Tree near Bowser Jr.":                   0x80E55D6110,
    "Bowser Jr. Playroom: Unlock night mode":             0x80E552E001,
    "Yoshi Park: Toy Field Pass":                         0x80E553F401,
    "Mario Stadium: Sea Hut Key":                         0x80E553F701,
    "Peach Ice Garden: Baby Daisy's Rattle":              0x80E553F801,
    "Peach Ice Garden: Toad Statue":                      0x80E553F901,
    "Peach Ice Garden: Daisy Statue":                     0x80E553FA01,
    "DK Jungle: Stone tablet piece behind exit sign":     0x80E553FB01,
    "DK Jungle: Stone tablet piece near Funky Kong":      0x80E553FC01,
    "DK Jungle: Stone tablet piece in central flower":    0x80E553FD01,
    "Blue Pianta's shop: Buy Luigi's Flashlight":         0x80E553F201,
    "Toadsworth's shop: Buy Cruiser Pass":                0x80E553F301,
    "Blue Pianta's shop: Buy Nice Bat":                   0x80E554BF01,
    "Blue Pianta's shop: Buy Power Bat":                  0x80E554C001,
    "Blue Pianta's shop: Buy Dr. K":                      0x80E554C101,
    "Blue Pianta's shop: Buy Lucky Glove":                0x80E554C201,
    "Blue Pianta's shop: Buy Dash Spikes":                0x80E554C301,
    "Blue Pianta's shop: Buy Buddy Badge":                0x80E554C401,
    "Blue Pianta's shop: Buy Error Booster":              0x80E554C501,
    "Blue Pianta's shop: Buy Charge Bat":                 0x80E554C601,
    "Toadsworth's shop: Buy Nice Bat":                    0x80E554CF01,
    "Toadsworth's shop: Buy Power Bat":                   0x80E554D001,
    "Toadsworth's shop: Buy Dr. K":                       0x80E554D101,
    "Toadsworth's shop: Buy Lucky Glove":                 0x80E554D201,
    "Toadsworth's shop: Buy Dash Spikes":                 0x80E554D301,
    "Toadsworth's shop: Buy Buddy Badge":                 0x80E554D401,
    "Toadsworth's shop: Buy Error Booster":               0x80E554D501,
    "Toadsworth's shop: Buy Charge Bat":                  0x80E554D601,
    "Goomba's shop: Buy Nice Bat":                        0x80E554DF01,
    "Goomba's shop: Buy Power Bat":                       0x80E554E001,
    "Goomba's shop: Buy Dr. K":                           0x80E554E101,
    "Goomba's shop: Buy Lucky Glove":                     0x80E554E201,
    "Goomba's shop: Buy Dash Spikes":                     0x80E554E301,
    "Goomba's shop: Buy Buddy Badge":                     0x80E554E401,
    "Goomba's shop: Buy Error Booster":                   0x80E554E501,
    "Goomba's shop: Buy Charge Bat":                      0x80E554E601,
    "Funky Kong's shop: Buy Nice Bat":                    0x80E554EF01,
    "Funky Kong's shop: Buy Power Bat":                   0x80E554F001,
    "Funky Kong's shop: Buy Dr. K":                       0x80E554F101,
    "Funky Kong's shop: Buy Lucky Glove":                 0x80E554F201,
    "Funky Kong's shop: Buy Dash Spikes":                 0x80E554F301,
    "Funky Kong's shop: Buy Buddy Badge":                 0x80E554F401,
    "Funky Kong's shop: Buy Error Booster":               0x80E554F501,
    "Funky Kong's shop: Buy Charge Bat":                  0x80E554F601,
    "Red Yoshi's shop: Buy Nice Bat":                     0x80E554FF01,
    "Red Yoshi's shop: Buy Power Bat":                    0x80E5550001,
    "Red Yoshi's shop: Buy Dr. K":                        0x80E5550101,
    "Red Yoshi's shop: Buy Lucky Glove":                  0x80E5550201,
    "Red Yoshi's shop: Buy Dash Spikes":                  0x80E5550301,
    "Red Yoshi's shop: Buy Buddy Badge":                  0x80E5550401,
    "Red Yoshi's shop: Buy Error Booster":                0x80E5550501,
    "Red Yoshi's shop: Buy Charge Bat":                   0x80E5550601,
    "Secret shop: Buy Nice Bat":                          0x80E5550F01,
    "Secret shop: Buy Power Bat":                         0x80E5551001,
    "Secret shop: Buy Dr. K":                             0x80E5551101,
    "Secret shop: Buy Lucky Glove":                       0x80E5551201,
    "Secret shop: Buy Dash Spikes":                       0x80E5551301,
    "Secret shop: Buy Buddy Badge":                       0x80E5551401,
    "Secret shop: Buy Error Booster":                     0x80E5551501,
    "Secret shop: Buy Charge Bat":                        0x80E5551601,
    "Secret shop: Buy Star Candy":                        0x80E5551701,
    "Secret shop: Buy x2 Star Candy":                     0x80E5551801,
    "Secret shop: Buy Superstar":                         0x80E5551901,
}


class MarioSuperSluggersLocation(Location):
    game = "Mario Super Sluggers"


def get_location_names_with_ids(location_names: list[str]) -> dict[str, int | None]:
    return {location_name: LOCATION_NAME_TO_ID[location_name] for location_name in location_names}


def create_locations(world: MarioSuperSluggersWorld) -> None:
    overworld = world.get_region("Baseball Kingdom")
    mario = world.get_region("Mario Stadium")
    mario_bridge = world.get_region("Mario Stadium past bridge")
    mario_shop = world.get_region("Blue Pianta's shop")
    peach = world.get_region("Peach Ice Garden")
    peach_bushes = world.get_region("Peach Ice Garden bushes")
    peach_topiaries = world.get_region("Peach Ice Garden topiaries")
    peach_flood = world.get_region("Peach Ice Garden after flood")
    peach_manhole = world.get_region("Peach Ice Garden past manhole")
    peach_shop = world.get_region("Toadsworth's shop")
    dk = world.get_region("DK Jungle")
    dk_vines = world.get_region("DK Jungle past vines")
    dk_tablet = world.get_region("DK Jungle after stone tablet")
    dk_pipe = world.get_region("DK Jungle past pipe")
    dk_shop = world.get_region("Funky Kong's shop")
    wario = world.get_region("Wario City")
    wario_vines = world.get_region("Wario City past vines")
    wario_containers = world.get_region("Wario City past containers")
    wario_shop = world.get_region("Goomba's shop")
    yoshi = world.get_region("Yoshi Park")
    yoshi_pipe = world.get_region("Yoshi Park past pipe")
    yoshi_manhole = world.get_region("Yoshi Park past manholes")
    yoshi_shop = world.get_region("Red Yoshi's shop")
    daisy = world.get_region("Daisy Cruiser")
    daisy_shop = world.get_region("Secret shop")
    luigi_flashlight = world.get_region("Luigi's Flashlight")
    luigi = world.get_region("Luigi's Mansion")
    toy_field = world.get_region("Toy Field")
    bowser_jr = world.get_region("Bowser Jr. Playroom")
    bowser = world.get_region("Bowser Castle")

    overworld.add_event(
        "Baseball Kingdom: Play all minigames", "Play Badge", location_type=MarioSuperSluggersLocation,
        item_type=items.MarioSuperSluggersItem
    )

    overworld.add_event(
        "Baseball Kingdom: Recruit all characters", "Friend Badge", location_type=MarioSuperSluggersLocation,
        item_type=items.MarioSuperSluggersItem
    )

    mario.add_locations(get_location_names_with_ids([
        "Mario Stadium: Recruit Luigi",
        "Mario Stadium: Recruit Blue Pianta",
        "Mario Stadium: Recruit Red Pianta",
        "Mario Stadium: Recruit Yellow Pianta",
        "Mario Stadium: Recruit Blue Noki",
        "Mario Stadium: Recruit Green Noki",
        "Mario Stadium: Recruit Monty Mole",
        "Mario Stadium: Bottom barrel",
        "Mario Stadium: Middle barrel after Yellow Pianta",
        "Mario Stadium: Top barrel",
        "Mario Stadium: Bottom bush",
        "Mario Stadium: Top bush",
        "Mario Stadium: Central tree after Red Pianta",
        "Mario Stadium: Top tree",
    ]), MarioSuperSluggersLocation)
    
    mario_bridge.add_locations(get_location_names_with_ids([
        "Mario Stadium: Recruit Baby Mario",
        "Mario Stadium: Recruit Baby Luigi",
        "Mario Stadium: Recruit Red Noki",
        "Mario Stadium: Recruit Blooper",
        "Mario Stadium: Chest",
        "Mario Stadium: Red Noki's gift",
        "Mario Stadium: Sea Hut Key",
    ]), MarioSuperSluggersLocation)

    mario_bridge.add_event(
        "Mario Stadium: Play Bob-omb Derby", "Play Bob-omb Derby", location_type=MarioSuperSluggersLocation,
        item_type=items.MarioSuperSluggersItem
    )

    peach.add_locations(get_location_names_with_ids([
        "Peach Ice Garden: Recruit Red Toad",
        "Peach Ice Garden: Recruit Toadette",
        "Peach Ice Garden: Daisy Statue",
    ]), MarioSuperSluggersLocation)
    
    peach_bushes.add_locations(get_location_names_with_ids([
        "Peach Ice Garden: Recruit Green Toad",
        "Peach Ice Garden: Recruit Purple Toad",
        "Peach Ice Garden: Top bush",
        "Peach Ice Garden: Left bush after Green Toad",
        "Peach Ice Garden: Bottom bush",
        "Peach Ice Garden: Right bush after Purple Toad",
    ]), MarioSuperSluggersLocation)

    peach_topiaries.add_locations(get_location_names_with_ids([
        "Peach Ice Garden: Recruit Baby Peach",
        "Peach Ice Garden: Top topiary after Toad Statue",
        "Peach Ice Garden: Left topiary after Baby Peach",
        "Peach Ice Garden: Right topiary",
        "Peach Ice Garden: Toad Statue",
    ]), MarioSuperSluggersLocation)

    peach_flood.add_locations(get_location_names_with_ids([
        "Peach Ice Garden: Recruit Peach",
        "Peach Ice Garden: Recruit Daisy",
        "Peach Ice Garden: Recruit Toadsworth",
        "Peach Ice Garden: Recruit Blue Toad",
        "Peach Ice Garden: Recruit Petey Piranha",
    ]), MarioSuperSluggersLocation)
    
    peach_flood.add_event(
        "Peach Ice Garden: Play Wall Ball", "Play Wall Ball", location_type=MarioSuperSluggersLocation,
        item_type=items.MarioSuperSluggersItem
    )

    peach_manhole.add_locations(get_location_names_with_ids([
        "Peach Ice Garden: Recruit Yellow Toad",
        "Peach Ice Garden: Recruit Baby Daisy",
        "Peach Ice Garden: Chest",
        "Peach Ice Garden: Right mushroom after Yellow Toad",
        "Peach Ice Garden: Top mushroom",
        "Peach Ice Garden: Baby Daisy's Rattle",
    ]), MarioSuperSluggersLocation)

    peach_shop.add_locations(get_location_names_with_ids([
        "Toadsworth's shop: Buy Cruiser Pass",
    ]), MarioSuperSluggersLocation)

    dk.add_locations(get_location_names_with_ids([
        "DK Jungle: Recruit Donkey Kong",
        "DK Jungle: Recruit Dixie Kong",
        "DK Jungle: Top flowers near entrance",
        "DK Jungle: Tree near shop",
        "DK Jungle: Tree near Dixie Kong",
        "DK Jungle: Bottom flowers near entrance",
        "DK Jungle: Flowers near bridge",
        "DK Jungle: Flowers below central tree",
        "DK Jungle: Stone tablet piece behind exit sign",
    ]), MarioSuperSluggersLocation)
    
    dk_vines.add_locations(get_location_names_with_ids([
        "DK Jungle: Recruit Funky Kong",
        "DK Jungle: Recruit Baby DK",
        "DK Jungle: Barrel after Blue Kritter",
        "DK Jungle: Tree below entrance after Baby DK",
        "DK Jungle: Flowers near Funky Kong",
        "DK Jungle: Flowers below entrance",
        "DK Jungle: Stone tablet piece near Funky Kong",
        "DK Jungle: Stone tablet piece in central flower",
    ]), MarioSuperSluggersLocation)

    dk_tablet.add_locations(get_location_names_with_ids([
        "DK Jungle: Recruit Diddy Kong",
        "DK Jungle: Recruit Tiny Kong",
    ]), MarioSuperSluggersLocation)
    
    dk_tablet.add_event(
        "DK Jungle: Play Barrel Basher", "Play Barrel Basher", location_type=MarioSuperSluggersLocation,
        item_type=items.MarioSuperSluggersItem
    )

    dk_pipe.add_locations(get_location_names_with_ids([
        "DK Jungle: Recruit Kritter",
        "DK Jungle: Recruit Blue Kritter",
        "DK Jungle: Recruit Red Kritter",
        "DK Jungle: Recruit Brown Kritter",
        "DK Jungle: Recruit King K. Rool",
        "DK Jungle: Chest",
    ]), MarioSuperSluggersLocation)
    
    wario.add_locations(get_location_names_with_ids([
        "Wario City: Recruit Paratroopa",
        "Wario City: Recruit Goomba",
        "Wario City: Recruit Paragoomba",
        "Wario City: Recruit Green Paratroopa",
        "Wario City: Central tree",
        "Wario City: Right tree after Paragoomba",
        "Wario City: Trash can near entrance",
        "Wario City: Trash can near dynamo",
        "Wario City: Top tree",
    ]), MarioSuperSluggersLocation)
    
    wario_vines.add_locations(get_location_names_with_ids([
        "Wario City: Recruit Wario",
        "Wario City: Recruit Koopa",
        "Wario City: Recruit King Boo",
        "Wario City: Recruit Red Koopa",
    ]), MarioSuperSluggersLocation)
    
    wario_vines.add_event(
        "Wario City: Play Gem Catch", "Play Gem Catch", location_type=MarioSuperSluggersLocation,
        item_type=items.MarioSuperSluggersItem
    )

    wario_containers.add_locations(get_location_names_with_ids([
        "Wario City: Recruit Waluigi",
        "Wario City: Recruit Boo",
        "Wario City: Chest",
    ]), MarioSuperSluggersLocation)
    
    yoshi.add_locations(get_location_names_with_ids([
        "Yoshi Park: Recruit Shy Guy",
        "Yoshi Park: Recruit Blue Shy Guy",
    ]), MarioSuperSluggersLocation)
    
    yoshi_pipe.add_locations(get_location_names_with_ids([
        "Yoshi Park: Recruit Yoshi",
        "Yoshi Park: Recruit Red Yoshi",
        "Yoshi Park: Recruit Light Blue Yoshi",
    ]), MarioSuperSluggersLocation)
    
    yoshi_manhole.add_locations(get_location_names_with_ids([
        "Yoshi Park: Recruit Birdo",
        "Yoshi Park: Recruit Yellow Shy Guy",
        "Yoshi Park: Recruit Green Shy Guy",
        "Yoshi Park: Recruit Gray Shy Guy",
        "Yoshi Park: Recruit Wiggler",
        "Yoshi Park: Recruit Blue Yoshi",
        "Yoshi Park: Recruit Yellow Yoshi",
        "Yoshi Park: Recruit Pink Yoshi",
        "Yoshi Park: Chest",
        "Yoshi Park: Left stump after Shy Guys",
        "Yoshi Park: Right stump after Shy Guys",
        "Yoshi Park: Tree near shop after Pink Yoshi",
        "Yoshi Park: Tree near Birdo after Yellow Yoshi",
        "Yoshi Park: Tree near Bowser Jr.",
        "Yoshi Park: Toy Field Pass",
    ]), MarioSuperSluggersLocation)
    
    yoshi_manhole.add_event(
        "Yoshi Park: Play Piranha Panic", "Play Piranha Panic", location_type=MarioSuperSluggersLocation,
        item_type=items.MarioSuperSluggersItem
    )

    daisy.add_event(
        "Daisy Cruiser: Play Blooper Baserun", "Play Blooper Baserun", location_type=MarioSuperSluggersLocation,
        item_type=items.MarioSuperSluggersItem
    )

    luigi_flashlight.add_locations(get_location_names_with_ids([
        "Blue Pianta's shop: Buy Luigi's Flashlight",
    ]), MarioSuperSluggersLocation)

    luigi.add_event(
        "Luigi's Mansion: Play Ghost K", "Play Ghost K", location_type=MarioSuperSluggersLocation,
        item_type=items.MarioSuperSluggersItem
    )

    toy_field.add_event(
        "Toy Field: Play Toy Field", "Play Toy Field", location_type=MarioSuperSluggersLocation,
        item_type=items.MarioSuperSluggersItem
    )

    bowser_jr.add_locations(get_location_names_with_ids([
        "Bowser Jr. Playroom: Unlock night mode",
    ]), MarioSuperSluggersLocation)
    
    bowser_jr.add_event(
        "Bowser Jr. Playroom: Play Graffiti Runner", "Play Graffiti Runner", location_type=MarioSuperSluggersLocation,
        item_type=items.MarioSuperSluggersItem
    )

    if world.options.goal_condition != world.options.goal_condition.option_defeat_bowser_monsters:
        bowser.add_locations(get_location_names_with_ids([
            "Bowser Castle: Recruit Bowser",
            "Bowser Castle: Recruit Bowser Jr.",
            "Bowser Castle: Recruit Hammer Bro",
            "Bowser Castle: Recruit Magikoopa",
            "Bowser Castle: Recruit Red Magikoopa",
            "Bowser Castle: Recruit Green Magikoopa",
            "Bowser Castle: Recruit Yellow Magikoopa",
            "Bowser Castle: Recruit Dry Bones",
            "Bowser Castle: Recruit Green Dry Bones",
            "Bowser Castle: Recruit Dark Bones",
            "Bowser Castle: Recruit Blue Dry Bones",
            "Bowser Castle: Recruit Fire Bro",
            "Bowser Castle: Recruit Boomerang Bro",
        ]), MarioSuperSluggersLocation)

    bowser.add_event(
        "Bowser Castle: Defeat Bowser Monsters", "Defeat Bowser Monsters", location_type=MarioSuperSluggersLocation,
        item_type=items.MarioSuperSluggersItem
    )

    bowser.add_event(
        "Bowser Castle: Play Bowser Pinball", "Play Bowser Pinball", location_type=MarioSuperSluggersLocation,
        item_type=items.MarioSuperSluggersItem
    )

    if world.options.randomize_shops == world.options.randomize_shops.option_full:
        mario_shop.add_locations(get_location_names_with_ids([
            "Blue Pianta's shop: Buy Nice Bat",
            "Blue Pianta's shop: Buy Power Bat",
            "Blue Pianta's shop: Buy Dr. K",
            "Blue Pianta's shop: Buy Lucky Glove",
            "Blue Pianta's shop: Buy Dash Spikes",
            "Blue Pianta's shop: Buy Buddy Badge",
            "Blue Pianta's shop: Buy Error Booster",
            "Blue Pianta's shop: Buy Charge Bat",
        ]), MarioSuperSluggersLocation)

        peach_shop.add_locations(get_location_names_with_ids([
            "Toadsworth's shop: Buy Nice Bat",
            "Toadsworth's shop: Buy Power Bat",
            "Toadsworth's shop: Buy Dr. K",
            "Toadsworth's shop: Buy Lucky Glove",
            "Toadsworth's shop: Buy Dash Spikes",
            "Toadsworth's shop: Buy Buddy Badge",
            "Toadsworth's shop: Buy Error Booster",
            "Toadsworth's shop: Buy Charge Bat",
        ]), MarioSuperSluggersLocation)

        dk_shop.add_locations(get_location_names_with_ids([
            "Funky Kong's shop: Buy Nice Bat",
            "Funky Kong's shop: Buy Power Bat",
            "Funky Kong's shop: Buy Dr. K",
            "Funky Kong's shop: Buy Lucky Glove",
            "Funky Kong's shop: Buy Dash Spikes",
            "Funky Kong's shop: Buy Buddy Badge",
            "Funky Kong's shop: Buy Error Booster",
            "Funky Kong's shop: Buy Charge Bat",
        ]), MarioSuperSluggersLocation)

        wario_shop.add_locations(get_location_names_with_ids([
            "Goomba's shop: Buy Nice Bat",
            "Goomba's shop: Buy Power Bat",
            "Goomba's shop: Buy Dr. K",
            "Goomba's shop: Buy Lucky Glove",
            "Goomba's shop: Buy Dash Spikes",
            "Goomba's shop: Buy Buddy Badge",
            "Goomba's shop: Buy Error Booster",
            "Goomba's shop: Buy Charge Bat",
        ]), MarioSuperSluggersLocation)

        yoshi_shop.add_locations(get_location_names_with_ids([
            "Red Yoshi's shop: Buy Nice Bat",
            "Red Yoshi's shop: Buy Power Bat",
            "Red Yoshi's shop: Buy Dr. K",
            "Red Yoshi's shop: Buy Lucky Glove",
            "Red Yoshi's shop: Buy Dash Spikes",
            "Red Yoshi's shop: Buy Buddy Badge",
            "Red Yoshi's shop: Buy Error Booster",
            "Red Yoshi's shop: Buy Charge Bat",
        ]), MarioSuperSluggersLocation)

        daisy_shop.add_locations(get_location_names_with_ids([
            "Secret shop: Buy Nice Bat",
            "Secret shop: Buy Power Bat",
            "Secret shop: Buy Dr. K",
            "Secret shop: Buy Lucky Glove",
            "Secret shop: Buy Dash Spikes",
            "Secret shop: Buy Buddy Badge",
            "Secret shop: Buy Error Booster",
            "Secret shop: Buy Charge Bat",
            "Secret shop: Buy Star Candy",
            "Secret shop: Buy x2 Star Candy",
            "Secret shop: Buy Superstar",
        ]), MarioSuperSluggersLocation)

    if world.options.randomize_stars or world.options.goal_condition == world.options.goal_condition.option_star_badge:
        overworld.add_event(
            "Baseball Kingdom: Star all characters", "Star Badge", location_type=MarioSuperSluggersLocation,
            item_type=items.MarioSuperSluggersItem
        )

        bowser.add_locations(get_location_names_with_ids([
            "Bowser Castle: Unlock star for Mario",
            "Bowser Castle: Unlock star for Luigi",
            "Bowser Castle: Unlock star for Donkey Kong",
            "Bowser Castle: Unlock star for Diddy Kong",
            "Bowser Castle: Unlock star for Peach",
            "Bowser Castle: Unlock star for Daisy",
            "Bowser Castle: Unlock star for Yoshi",
            "Bowser Castle: Unlock star for Baby Mario",
            "Bowser Castle: Unlock star for Baby Luigi",
            "Bowser Castle: Unlock star for Bowser",
            "Bowser Castle: Unlock star for Wario",
            "Bowser Castle: Unlock star for Waluigi",
            "Bowser Castle: Unlock star for Koopa",
            "Bowser Castle: Unlock star for Toad",
            "Bowser Castle: Unlock star for Boo",
            "Bowser Castle: Unlock star for Toadette",
            "Bowser Castle: Unlock star for Shy Guy",
            "Bowser Castle: Unlock star for Birdo",
            "Bowser Castle: Unlock star for Monty Mole",
            "Bowser Castle: Unlock star for Bowser Jr.",
            "Bowser Castle: Unlock star for Paratroopa",
            "Bowser Castle: Unlock star for Pianta",
            "Bowser Castle: Unlock star for Noki",
            "Bowser Castle: Unlock star for Hammer Bro",
            "Bowser Castle: Unlock star for Toadsworth",
            "Bowser Castle: Unlock star for Magikoopa",
            "Bowser Castle: Unlock star for King Boo",
            "Bowser Castle: Unlock star for Petey Piranha",
            "Bowser Castle: Unlock star for Dixie Kong",
            "Bowser Castle: Unlock star for Goomba",
            "Bowser Castle: Unlock star for Paragoomba",
            "Bowser Castle: Unlock star for Dry Bones",
            "Bowser Castle: Unlock star for Wiggler",
            "Bowser Castle: Unlock star for Blooper",
            "Bowser Castle: Unlock star for Funky Kong",
            "Bowser Castle: Unlock star for Tiny Kong",
            "Bowser Castle: Unlock star for Kritter",
            "Bowser Castle: Unlock star for King K. Rool",
            "Bowser Castle: Unlock star for Baby Peach",
            "Bowser Castle: Unlock star for Baby Daisy",
            "Bowser Castle: Unlock star for Baby DK",
        ]), MarioSuperSluggersLocation)
