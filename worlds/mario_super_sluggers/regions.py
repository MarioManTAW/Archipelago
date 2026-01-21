from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import Region
from .items import MINIGAMES

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
        Region("Wario City past vines", world.player, world.multiworld),
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

    overworld.connect(mario)
    mario.connect(mario_bridge, None, lambda state: state.has_all(("Blue Noki", "Green Noki"), world.player))
    mario.connect(mario_shop, None, lambda state:
                  state.has("Sea Hut Key", world.player) and state.has_any(MINIGAMES, world.player))
    mario_shop.connect(luigi_flashlight)
    overworld.connect(peach)
    peach.connect(peach_flood, None, lambda state: state.has("Daisy Statue", world.player))
    peach.connect(peach_bushes, None, lambda state: state.has("Mario", world.player))
    peach.connect(peach_topiaries, None, lambda state: state.has("Peach", world.player))
    peach_flood.connect(peach_manhole, None, lambda state: state.has("Yoshi", world.player))
    peach_flood.connect(peach_shop, None, lambda state: state.has_any(MINIGAMES, world.player))
    overworld.connect(dk)
    dk.connect(dk_vines, None, lambda state: state.has("Donkey Kong", world.player))
    dk_vines.connect(dk_tablet, None, lambda state: state.count_group_unique("Stone tablet", world.player) == 3)
    dk_vines.connect(dk_shop, None, lambda state: state.has_any(MINIGAMES, world.player))
    dk_tablet.connect(dk_pipe, None, lambda state: state.has("Mario", world.player))
    overworld.connect(wario)
    wario.connect(wario_vines, None, lambda state: state.has("Donkey Kong", world.player))
    wario.connect(wario_shop, None, lambda state: state.has_any(MINIGAMES, world.player))
    wario_vines.connect(wario_containers, None, lambda state: state.has("Wario", world.player))
    overworld.connect(yoshi)
    yoshi.connect(yoshi_pipe, None, lambda state: state.has("Mario", world.player))
    yoshi_pipe.connect(yoshi_manhole, None, lambda state: state.has("Yoshi", world.player))
    yoshi_pipe.connect(yoshi_shop, None, lambda state:
                       state.has("Brush", world.player) and state.has_any(MINIGAMES, world.player))
    overworld.connect(daisy, None, lambda state: state.has("Cruiser Pass", world.player))
    daisy.connect(daisy_shop, None, lambda state: state.has("Day-night cycle", world.player) and \
                  state.has("Special Shop Pass", world.player) and state.has_any(MINIGAMES, world.player))
    daisy_shop.connect(luigi_flashlight)
    overworld.connect(luigi, None, lambda state:
                      state.has("Luigi's Flashlight", world.player) and state.has("Day-night cycle", world.player))
    overworld.connect(toy_field, None, lambda state: state.has("Toy Field Pass", world.player))
    overworld.connect(bowser_jr, None, lambda state:
                      state.count_group_unique("Characters", world.player) >= world.options.goal_characters)
    bowser_jr.connect(bowser, None, lambda state: state.has("Day-night cycle", world.player))
