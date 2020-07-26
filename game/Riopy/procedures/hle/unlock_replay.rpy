# Unlock replays in event gallery by index.
# For some reason this is called RESTBGM while it has nothing to do with BGM. Possible copypasta fail?

label RIO_RESTBGM:
    # Don't save local variables
    python hide:
        if 1 <= will_flagbank[willplus.replay_index_ref] <= willplus.replay_index_max:
            tmp_base_addr = persistent.will_flagbank.name2addr(willplus.replay_flag_array_base)
            tmp_flag_addr = tmp_base_addr + (will_flagbank[willplus.replay_index_ref] - 1)
            persistent.will_flagbank[tmp_flag_addr] = True
    return
