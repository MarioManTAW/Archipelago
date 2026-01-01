from dataclasses import dataclass

from Options import Range, PerGameCommonOptions, StartInventoryPool, Choice, Toggle


class GoalCharacters(Range):
    """How many characters you need to have unlocked in order to fight Bowser Jr. and Bowser."""
    display_name = "Goal Characters"
    range_start = 9
    range_end = 58
    default = 30


class StartingCaptain(Choice):
    """Choose which captain you want to start with."""
    display_name = "Starting Captain"
    option_mario = 0
    option_peach = 1
    option_yoshi = 2
    option_donkey_kong = 3
    alias_dk = 3
    option_wario = 4
    default = "random"


class ReducedCutscenes(Toggle):
    """Marks certain one-time cutscenes as already watched to speed up gameplay."""
    display_name = "Reduced Cutscenes"

@dataclass
class MarioSuperSluggersOptions(PerGameCommonOptions):
    goal_characters: GoalCharacters
    starting_captain: StartingCaptain
    reduced_cutscenes: ReducedCutscenes
    start_inventory_from_pool: StartInventoryPool
