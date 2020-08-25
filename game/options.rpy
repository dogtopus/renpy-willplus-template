## This file contains options that can be changed to customize your game.
##
## Lines beginning with two '#' marks are comments, and you shouldn't uncomment
## them. Lines beginning with a single '#' mark are commented-out code, and you
## may want to uncomment them when appropriate.


## Basics ######################################################################

## A human-readable name of the game. This is used to set the default window
## title, and shows up in the interface and error reports.
##
## The _() surrounding the string marks it as eligible for translation.

# TODO Name
define config.name = _("WillPlus ADV Template")


## Determines if the title given above is shown on the main menu screen. Set
## this to False to hide the title.

define gui.show_name = True


## The version of the game.

define config.version = "1.0"


## Text that is placed on the game's about screen. Place the text between the
## triple-quotes, and leave a blank line between paragraphs.

# TODO About
define gui.about = _p("""This copy is for personal use only.
Redistribution prohibited.

Original game is © WillPlus/Brand.

Assets/scripts conversion and Ren'Py WillPlus emulation environment is powered
by willplus-tools and renpy-willplus-template.
""")


## A short name for the game used for executables and directories in the built
## distribution. This must be ASCII-only, and must not contain spaces, colons,
## or semicolons.

# TODO Build name
define build.name = "willplus-adv"


## Sounds and music ############################################################

## These three variables control which mixers are shown to the player by
## default. Setting one of these to False will hide the appropriate mixer.

define config.has_sound = True
define config.has_music = True
define config.has_voice = True


## To allow the user to play a test sound on the sound or voice channel,
## uncomment a line below and use it to set a sample sound to play.

# define config.sample_sound = "sample-sound.ogg"
# define config.sample_voice = "sample-voice.ogg"


## Uncomment the following line to set an audio file that will be played while
## the player is at the main menu. This file will continue playing into the
## game, until it is stopped or another file is played.
##
## Note that for this template, unless symbol-only mode is disabled, this option
## should be set to the symbol name for the main menu music instead of the path.

# define config.main_menu_music = "BGM01"


## Transitions #################################################################
##
## These variables set transitions that are used when certain events occur.
## Each variable should be set to a transition, or None to indicate that no
## transition should be used.

## Entering or exiting the game menu.

define config.enter_transition = Dissolve(0.2)
define config.exit_transition = Dissolve(0.2)


## Between screens of the game menu.

define config.intra_transition = Dissolve(0.2)


## A transition that is used after a game has been loaded.

define config.after_load_transition = None


## Used when entering the main menu after the game has ended.

define config.end_game_transition = None


## A variable to set the transition used when the game starts does not exist.
## Instead, use a with statement after showing the initial scene.


## Window management ###########################################################
##
## This controls when the dialogue window is displayed. If "show", it is always
## displayed. If "hide", it is only displayed when dialogue is present. If
## "auto", the window is hidden before scene statements and shown again once
## dialogue is displayed.
##
## After the game has started, this can be changed with the "window show",
## "window hide", and "window auto" statements.

define config.window = "auto"


## Transitions used to show and hide the dialogue window

define config.window_show_transition = Dissolve(.05)
define config.window_hide_transition = Dissolve(.05)


## Preference defaults #########################################################

## Controls the default text speed. The default, 0, is infinite, while any other
## number is the number of characters per second to type out.

default preferences.text_cps = 0


## The default auto-forward delay. Larger numbers lead to longer waits, with 0
## to 30 being the valid range.

default preferences.afm_time = 15


## Save directory ##############################################################
##
## Controls the platform-specific place Ren'Py will place the save files for
## this game. The save files will be placed in:
##
## Windows: %APPDATA\RenPy\<config.save_directory>
##
## Macintosh: $HOME/Library/RenPy/<config.save_directory>
##
## Linux: $HOME/.renpy/<config.save_directory>
##
## This generally should not be changed, and if it is, should always be a
## literal string, not an expression.

# TODO Save directory (buildname-timestamp)
define config.save_directory = "willplus-adv-0"


## Icon ########################################################################
##
## The icon displayed on the taskbar or dock.

define config.window_icon = "gui/window_icon.png"


## Misc ########################################################################
##
## Other custom options.

## Weather layer
init -1 python hide:
    config.layers.insert(config.layers.index('master') + 1, 'weather')

## Init profiling (only available on 7.4+ or nightly)
# define config.profile_init = 0.001

## Build configuration #########################################################
##
## This section controls how Ren'Py turns your project into distribution files.

init python:

    ## The following functions take file patterns. File patterns are case-
    ## insensitive, and matched against the path relative to the base directory,
    ## with and without a leading /. If multiple patterns match, the first is
    ## used.
    ##
    ## In a pattern:
    ##
    ## / is the directory separator.
    ##
    ## * matches all characters, except the directory separator.
    ##
    ## ** matches all characters, including the directory separator.
    ##
    ## For example, "*.txt" matches txt files in the base directory, "game/
    ## **.ogg" matches ogg files in the game directory or any of its
    ## subdirectories, and "**.psd" matches psd files anywhere in the project.

    ## Classify files as None to exclude them from the built distributions.

    build.classify('**~', None)
    build.classify('**.bak', None)
    build.classify('**/.**', None)
    build.classify('**/#**', None)
    build.classify('**/thumbs.db', None)
    build.classify('game/cache/**', None)
    build.classify('game/images/**/gen/**', None) # Generator scripts
    build.classify('game/**/README.md', None)

    ## To archive files, classify them as 'archive'.

    # build.classify('game/**.png', 'archive')
    # build.classify('game/**.jpg', 'archive')

    ## Binary-only distribution
    build.archive("scripts", "all")
    build.archive("images", "all")
    build.archive("sounds", "all")
    build.archive("voices", "all")

    build.classify('game/audio/**.ogg', 'sounds')
    build.classify('game/Bgm/**.OGG', 'sounds')
    build.classify('game/Bgm/**.opus', 'sounds')
    build.classify('game/Chip/**.png', 'images')
    build.classify('game/Chip_*/**.png', 'images')
    build.classify('game/gui/**.png', 'images')
    build.classify('game/images/**.png', 'images')
    build.classify('game/Chip/**.webp', 'images')
    build.classify('game/Chip_*/**.webp', 'images')
    build.classify('game/gui/**.webp', 'images')
    build.classify('game/images/**.webp', 'images')
    build.classify('game/**.rpy', None)
    build.classify('game/**.rpym', None)
    build.classify('game/**.rpyc', 'scripts')
    build.classify('game/**.rpymc', 'scripts')
    build.classify('game/Se/**.OGG', 'sounds')
    build.classify('game/Se/**.opus', 'sounds')
    build.classify('game/Voice/**.OGG', 'voices')
    build.classify('game/Voice/**.opus', 'voices')

    ## Files matching documentation patterns are duplicated in a mac app build,
    ## so they appear in both the app and the zip file.

    build.documentation('*.html')
    build.documentation('*.txt')


## A Google Play license key is required to download expansion files and perform
## in-app purchases. It can be found on the "Services & APIs" page of the Google
## Play developer console.

# define build.google_play_key = "..."


## The username and project name associated with an itch.io project, separated
## by a slash.

# define build.itch_project = "renpytom/test-project"


## WillPlus ADV-specific settings ##############################################
##
## Optional features specific to WillPlus ADV emulation.

init offset = -2

## LL-specific: Enable alignment gem indicator support.

define willplus.enable_gem = False

## Set battle system type (None, pw, sen, ...) (TODO)

# define willplus.battle = None

## Define extra sound channels

define willplus.extra_se_channels = []

## Changes how renpy finds music, sound and voice files. Note that for some
## reason WillPlus SE (sound) symbols have file suffixes appended so sound
## effects need to be referenced with the full filename including the suffix.
## Also audio channel is not affected so references to UI sounds, etc. still
## need to be done using paths.

define willplus.bgm_suffix = '.OGG'
define willplus.se_suffix = ''
define willplus.voice_suffix = '.OGG'
define willplus.bgm_prefix = 'Bgm/'
define willplus.se_prefix = 'Se/'
define willplus.voice_prefix = 'Voice/'

## Tint table for character images. May vary engine-to-engine.
## {index: (r, g, b), ...}

define willplus.tint_table = {
    ## Note that these values are just approximations/plausible alternatives.
    ## They are not RGB-perfect in anyway.

    ## Warm environments
    1: (1.1, 1.0, 1.0),
    2: (1.15, 1.0, 1.0),

    ## Cold/low light environments
    3: (0.9, 0.9, 0.9),
    4: (0.75, 0.75, 0.8),

    ## LL-specific: collapsing world (significantly redder hue than the 2 warm
    ## tints)
    5: (1.33, 1.0, 1.0),
}

## Music IDs (used by at least replay)

## {symbol: id, ...}
define willplus.music_ids = {}

## Replay HLE

## Flag that stores the current replay id

define willplus.replay_index_ref = 'current_event_id'

## # of replays

define willplus.replay_index_max = 0

## Replay BGM store base address

define willplus.replay_bgm_store = 'replay_bgm_store'

init offset = -999

## Disable revision check for gfx-next loading condition. Useful when running on
## local builds without the revision value properly set. Note that it's the
## user's responsibility to ensure the correct revision is used or otherwise the
## game will crash.

define willplus.gfx_next_ignore_revision = False

init offset = 0
