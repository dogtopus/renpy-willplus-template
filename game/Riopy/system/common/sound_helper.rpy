# WillPlus sound system helper

init python hide:
    renpy.audio.audio.get_channel('music').file_prefix = willplus.bgm_prefix
    renpy.audio.audio.get_channel('sound').file_prefix = willplus.se_prefix
    renpy.audio.audio.get_channel('voice').file_prefix = willplus.voice_prefix
    renpy.audio.audio.get_channel('music').file_suffix = willplus.bgm_suffix
    renpy.audio.audio.get_channel('sound').file_suffix = willplus.se_suffix
    renpy.audio.audio.get_channel('voice').file_suffix = willplus.voice_suffix

    # Define all extra sound channels used by the game
    for i in willplus.extra_se_channels:
        renpy.music.register_channel('sound{}'.format(i+1), 'sfx', loop=False, file_prefix=willplus.se_prefix, file_suffix=willplus.se_suffix)

label stop_all_sounds(fadeout_=0.0):
    stop sound fadeout fadeout_
    # Stop all extra sound channels defined above
    python hide:
        for i in willplus.extra_se_channels:
            renpy.sound.stop('sound{}'.format(i+1), fadeout=fadeout_)
    return
