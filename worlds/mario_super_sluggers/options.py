from dataclasses import dataclass

from Options import Range, PerGameCommonOptions, StartInventoryPool, Choice, Toggle


class GoalCondition(Choice):
    """Choose what you need to do to win.
    Defeat Bowser Monsters: Unlock a full team and the day-night cycle, then defeat the Bowser Monsters in a game.
    Play Badge: Unlock and win all minigames (including Toy Field).
    Friend Badge: Recruit all characters.
    Star Badge: Have star status on every character, then defeat the Bowser Monsters in a game."""
    display_name = "Goal Condition"
    option_defeat_bowser_monsters = 0
    option_play_badge = 1
    option_friend_badge = 2
    option_star_badge = 3
    default = 0


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


class RandomizeShops(Choice):
    """Choose whether shop items are randomized. Logical access to at least one minigame is expected in order to shop.
    Full: All shop items are randomized.
    Key Items Only: Luigi's Flashlight and the Cruiser Pass are randomized, all other shop items are unchanged.
    None: All shop items are in their vanilla locations."""
    display_name = "Randomize Shops"
    option_full = 2
    option_key_items_only = 1
    option_none = 0
    default = 0


class RandomizeStars(Toggle):
    """Adds a check for achieving star status with each character and randomizes the stars into the pool."""
    display_name = "Randomize Stars"


class RandomizeMusic(Toggle):
    """Shuffles music between different stadiums, overworld locations, and menus."""
    display_name = "Randomize Music"


class ReducedCutscenes(Toggle):
    """Marks certain one-time cutscenes as already watched to speed up gameplay."""
    display_name = "Reduced Cutscenes"


@dataclass
class MarioSuperSluggersOptions(PerGameCommonOptions):
    goal_condition: GoalCondition
    goal_characters: GoalCharacters
    starting_captain: StartingCaptain
    randomize_shops: RandomizeShops
    randomize_stars: RandomizeStars
    randomize_music: RandomizeMusic
    reduced_cutscenes: ReducedCutscenes
    start_inventory_from_pool: StartInventoryPool
