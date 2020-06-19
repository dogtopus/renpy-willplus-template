# Unlock replays in event gallery by index.
# For some reason this is called RESTBGM while it has nothing to do with BGM. Possible copypasta fail?

# Configure
# TODO fill this in 
define replay_index_ref = 'current_event_id'
define replay_index_max = 0
define replay_flag_array_base = 'unlock_event_0'

label RIO_RESTBGM:
    # Don't save local variables
    python hide:
        if 1 <= will_flagbank[replay_index_base] <= replay_index_max:
            tmp_base_addr = persistent.will_flagbank.name2addr(replay_flag_array_base)
            tmp_flag_addr = tmp_base_addr + (will_flagbank[replay_index_ref] - 1)
            persistent.will_flagbank[tmp_flag_addr] = True
    return
