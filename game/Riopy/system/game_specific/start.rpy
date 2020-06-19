# Game start logic. Put all the starting points here if the game has multiple starting points.

label start:
    stop music fadeout 0.5
    scene bg BLACK
    with dissolve
    # Check for unlocks here
    if config.developer:
        menu:
            'Select a route to begin...'
            'Start':
            #    jump RIO_first_scenario  # start the game
                jump RIO_MAINMENU
            # Add more entries here if needed.
            #'Start (Skip prologue)' if blah:
            #    jump RIO_after_prologue  # skip prologue

            'Execute script labeled `user_test`' if config.developer:
                jump user_test
    else:
        #jump RIO_first_scenario
        jump RIO_MAINMENU
