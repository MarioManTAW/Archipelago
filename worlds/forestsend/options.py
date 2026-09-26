from dataclasses import dataclass

from Options import Choice, DeathLink, PerGameCommonOptions, StartInventoryPool


class EarlyAbilities(Choice):
    """
    Determines where the game's early abilities can be placed.
    
    Vanilla: Transforming in the starting room will give you a Progressive Hover and a Progressive Melee Attack.
    Local Early: At least one of Melee, Drill, or Saw Blade (to leave the starting room) and one of Wall Jump, Hover,
                 or Drill (to make progress in the following room) will be present in the starting room.
    Early: The abilities listed in Local Early will be available from the start but may be in another world.
    Anywhere: Abilities may be placed in any valid location.
    """
    option_vanilla = 0
    option_local_early = 1
    option_early = 2
    option_anywhere = 3


@dataclass
class ForestsEndOptions(PerGameCommonOptions):
    early_abilities: EarlyAbilities
    death_link: DeathLink
    start_inventory_from_pool: StartInventoryPool
