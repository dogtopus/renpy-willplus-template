# Save music ID for replay
label RIO_RESTBGM:
    # Don't save local variables
    python hide:
        if 1 <= will_flagbank[willplus.replay_index_ref] <= willplus.replay_index_max:
            if isinstance(willplus.replay_bgm_store, int):
                tmp_base_addr = willplus.replay_bgm_store
            else:
                tmp_base_addr = persistent.will_flagbank.name2addr(willplus.replay_bgm_store)
            tmp_flag_addr = tmp_base_addr + (will_flagbank[willplus.replay_index_ref] - 1)
            persistent.will_flagbank[tmp_flag_addr] = willplus.music_ids.get(renpy.music.get_playing(), 0)
    return
