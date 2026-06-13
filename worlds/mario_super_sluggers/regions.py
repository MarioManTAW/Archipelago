from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import Region
from rule_builder.rules import And, Has, HasAll, HasAny, HasGroupUnique
from .items import MINIGAMES_OR_OOL

if TYPE_CHECKING:
    from . import MarioSuperSluggersWorld


def create_and_connect_regions(world: MarioSuperSluggersWorld) -> None:
    create_all_regions(world)
    connect_regions(world)


def create_all_regions(world: MarioSuperSluggersWorld) -> None:
    world.multiworld.regions += [
        Region("Baseball Kingdom", world.player, world.multiworld),
        Region("Mario Stadium", world.player, world.multiworld),
        Region("Mario Stadium past bridge", world.player, world.multiworld),
        Region("Blue Pianta's shop", world.player, world.multiworld),
        Region("Peach Ice Garden", world.player, world.multiworld),
        Region("Peach Ice Garden bushes", world.player, world.multiworld),
        Region("Peach Ice Garden topiaries", world.player, world.multiworld),
        Region("Peach Ice Garden after flood", world.player, world.multiworld),
        Region("Peach Ice Garden past manhole", world.player, world.multiworld),
        Region("Toadsworth's shop", world.player, world.multiworld),
        Region("DK Jungle", world.player, world.multiworld),
        Region("DK Jungle past vines", world.player, world.multiworld),
        Region("DK Jungle after stone tablet", world.player, world.multiworld),
        Region("DK Jungle past pipe", world.player, world.multiworld),
        Region("Funky Kong's shop", world.player, world.multiworld),
        Region("Wario City", world.player, world.multiworld),
        Region("Wario City after dynamo", world.player, world.multiworld),
        Region("Wario City past containers", world.player, world.multiworld),
        Region("Goomba's shop", world.player, world.multiworld),
        Region("Yoshi Park", world.player, world.multiworld),
        Region("Yoshi Park past pipe", world.player, world.multiworld),
        Region("Yoshi Park past manholes", world.player, world.multiworld),
        Region("Red Yoshi's shop", world.player, world.multiworld),
        Region("Daisy Cruiser", world.player, world.multiworld),
        Region("Secret shop", world.player, world.multiworld),
        Region("Luigi's Flashlight", world.player, world.multiworld),
        Region("Luigi's Mansion", world.player, world.multiworld),
        Region("Toy Field", world.player, world.multiworld),
        Region("Bowser Jr. Playroom", world.player, world.multiworld),
        Region("Bowser Castle", world.player, world.multiworld),
	]


def connect_regions(world: MarioSuperSluggersWorld) -> None:
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
    wario_dynamo = world.get_region("Wario City after dynamo")
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

    overworld.connect(mario)
    mario.connect(mario_bridge, None, HasAll("Blue Noki", "Green Noki"))
    mario.connect(mario_shop, None, And(Has("Sea Hut Key"), HasAny(*MINIGAMES_OR_OOL)))
    mario_shop.connect(luigi_flashlight)
    overworld.connect(peach)
    peach.connect(peach_flood, None, Has("Daisy Statue"))
    peach.connect(peach_bushes, None, Has("Mario"))
    peach.connect(peach_topiaries, None, Has("Peach"))
    peach_flood.connect(peach_manhole, None, Has("Yoshi"))
    peach_flood.connect(peach_shop, None, HasAny(*MINIGAMES_OR_OOL))
    overworld.connect(dk)
    dk.connect(dk_vines, None, Has("Donkey Kong"))
    dk_vines.connect(dk_tablet, None, HasGroupUnique("Stone tablet", 3))
    dk_vines.connect(dk_shop, None, HasAny(*MINIGAMES_OR_OOL))
    dk_tablet.connect(dk_pipe, None, Has("Mario"))
    overworld.connect(wario)
    wario.connect(wario_dynamo, None, Has("Wario"))
    wario.connect(wario_shop, None, HasAny(*MINIGAMES_OR_OOL))
    wario_dynamo.connect(wario_containers, None, Has("Donkey Kong"))
    overworld.connect(yoshi)
    yoshi.connect(yoshi_pipe, None, Has("Mario"))
    yoshi_pipe.connect(yoshi_manhole, None, Has("Yoshi"))
    yoshi_pipe.connect(yoshi_shop, None, And(Has("Brush"), HasAny(*MINIGAMES_OR_OOL)))
    overworld.connect(daisy, None, Has("Cruiser Pass"))
    daisy.connect(daisy_shop, None, And(Has("Day-night cycle"), Has("Special Shop Pass"), HasAny(*MINIGAMES_OR_OOL)))
    daisy_shop.connect(luigi_flashlight)
    overworld.connect(luigi, None, And(Has("Luigi's Flashlight"), Has("Day-night cycle")))
    overworld.connect(toy_field, None, Has("Toy Field Pass"))
    overworld.connect(bowser_jr, None, HasGroupUnique("Characters", world.options.goal_characters.value))
    bowser_jr.connect(bowser, None, Has("Day-night cycle"))
