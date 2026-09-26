
from __future__ import annotations

from typing import TYPE_CHECKING, NamedTuple

from BaseClasses import Item, ItemClassification

if TYPE_CHECKING:
    from . import ForestsEndWorld


class ForestsEndItem(Item):
    game = "The Forest's End"


class ForestsEndItemData(NamedTuple):
    code: int
    type: ItemClassification


ITEM_DATA = {
    "Lore Entry":               ForestsEndItemData(1, ItemClassification.filler),
    "Progressive Hover":        ForestsEndItemData(2, ItemClassification.progression),
    "Progressive Melee Attack": ForestsEndItemData(3, ItemClassification.progression),
    "Wall Jump":                ForestsEndItemData(4, ItemClassification.progression),
    "Health Upgrade":           ForestsEndItemData(5, ItemClassification.useful),
    "Drill":                    ForestsEndItemData(6, ItemClassification.progression),
    "Saw Blade":                ForestsEndItemData(7, ItemClassification.progression),
}

ITEM_NAME_TO_ID = {name: data.code for name, data in ITEM_DATA.items()}

def get_filler_item_name() -> str:
    return "Lore Entry"


def create_item(world: ForestsEndWorld, name: str) -> ForestsEndItem:
    return ForestsEndItem(name, ITEM_DATA[name].type, ITEM_DATA[name].code, world.player)


def create_items(world: ForestsEndWorld) -> None:
    items_to_create = list(ITEM_DATA.keys())
    items_to_create += ["Lore Entry"] * 7
    items_to_create += ["Progressive Hover"] * 3
    items_to_create += ["Progressive Melee Attack"]
    items_to_create += ["Health Upgrade"] * 2
    if world.options.early_abilities == world.options.early_abilities.option_vanilla:
        items_to_create.remove("Progressive Hover")
        items_to_create.remove("Progressive Melee Attack")
        world.get_location("Tutorial - Transformation (Hover)")\
            .place_locked_item(create_item(world, "Progressive Hover"))
        world.get_location("Tutorial - Transformation (Melee)")\
            .place_locked_item(create_item(world, "Progressive Melee Attack"))
    else:
        if world.multiworld.players == 1:
            world.options.early_abilities.value = world.options.early_abilities.option_local_early
        if world.options.early_abilities != world.options.early_abilities.option_anywhere:
            early_items = [world.random.choice(["Progressive Hover", "Wall Jump", "Drill"])]
            if "Drill" not in early_items:
                early_items.append(world.random.choice(["Progressive Melee Attack", "Saw Blade"]))
            for item in early_items:
                if world.options.early_abilities == world.options.early_abilities.option_local_early:
                    world.multiworld.local_early_items[world.player][item] = 1
                else:
                    world.multiworld.early_items[world.player][item] = 1
    number_of_unfilled_locations = len(world.multiworld.get_unfilled_locations(world.player))
    items_to_create += [get_filler_item_name() for _ in range(number_of_unfilled_locations - len(items_to_create))]
    world.multiworld.itempool += [create_item(world, item) for item in items_to_create]
