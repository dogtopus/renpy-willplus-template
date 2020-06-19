# Common displayable identifiers
init:
    # Pure color backgrounds
    image bg BLACK = "#000"
    image bg WHITE = "#ffffff"
    image bg RED = "#ff0000"

    # Weather
    image sprite rain = 'Chip/RAIN.webp'
    # TODO cut the tileset and tag them individually.
    #image sprite snow = 'Chip/SNOW.webp'

    # Convention: weather <name> [sprite_limiter_table_index]
    # Omit sprite_limiter_table_index if it's 0
    image weather rain = SnowBlossom('sprite rain', count=20, xspeed=0, yspeed=(3000, 3500))
