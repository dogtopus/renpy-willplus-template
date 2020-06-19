# WillPlus sound system helper

# Changes how renpy finds music, sound and voice files. Note that for some reason WillPlus SE (sound) symbols have file suffixes appended so sound effects need to be referenced with the full filename including the suffix. Also audio channel is not affected so references to UI sounds, etc. still need to be done using paths.
define will_bgm_suffix = '.OGG'
define will_se_suffix = ''
define will_voice_suffix = '.OGG'
define will_bgm_prefix = 'Bgm/'
define will_se_prefix = 'Se/'
define will_voice_prefix = 'Voice/'

init python hide:
    renpy.audio.audio.get_channel('music').file_prefix = will_bgm_prefix
    renpy.audio.audio.get_channel('sound').file_prefix = will_se_prefix
    renpy.audio.audio.get_channel('voice').file_prefix = will_voice_prefix
    renpy.audio.audio.get_channel('music').file_suffix = will_bgm_suffix
    renpy.audio.audio.get_channel('sound').file_suffix = will_se_suffix
    renpy.audio.audio.get_channel('voice').file_suffix = will_voice_suffix

    # Define all extra sound channels used by the game
    for i in will_extra_se_channels:
        renpy.music.register_channel('sound{}'.format(i+1), 'sfx', loop=False, file_prefix=will_se_prefix, file_suffix=will_se_suffix)

label stop_all_sounds(fadeout_=0.0):
    stop sound fadeout fadeout_
    # Stop all extra sound channels defined above
    python hide:
        for i in will_extra_se_channels:
            renpy.sound.stop('sound{}'.format(i+1), fadeout=fadeout_)
    return
