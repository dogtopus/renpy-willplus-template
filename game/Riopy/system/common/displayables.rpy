# Common displayable identifiers
init:
    # Pure color backgrounds
    image bg BLACK = "#000"
    image bg WHITE = "#ffffff"
    image bg RED = "#ff0000"

    # Weather
    image sprite rain = 'Chip/RAIN.webp'
    image tileset snow = 'Chip/SNOW.webp'

    image sprite snow small 3 = Crop((0, 0, 14, 14), "tileset snow")
    image sprite snow small 2 = Crop((14, 0, 14, 14), "tileset snow")
    image sprite snow small 1 = Crop((28, 0, 14, 14), "tileset snow")
    image sprite snow small 0 = Crop((42, 0, 14, 14), "tileset snow")

    image sprite snow medium 3 = Crop((0, 14, 28, 28), "tileset snow")
    image sprite snow medium 2 = Crop((28, 14, 28, 28), "tileset snow")
    image sprite snow medium 1 = Crop((56, 14, 28, 28), "tileset snow")
    image sprite snow medium 0 = Crop((84, 14, 28, 28), "tileset snow")

    image sprite snow large 2 = Crop((0, 42, 56, 56), "tileset snow")
    image sprite snow large 1 = Crop((56, 42, 56, 56), "tileset snow")
    image sprite snow large 0 = Crop((112, 42, 56, 56), "tileset snow")

    # Convention: weather <name> [sprite_limiter_table_index]
    # Omit sprite_limiter_table_index if it's 0
    image weather rain = SnowBlossom('sprite rain', count=20, xspeed=0, yspeed=(3000, 3500))
    # TODO very high CPU usage. Find a way to optimize.
    # TODO add other modes as well
    image weather snow = Fixed(
        SnowBlossom('sprite snow small 0', count=50),
        SnowBlossom('sprite snow small 1', count=50),
        SnowBlossom('sprite snow small 2', count=50),
        SnowBlossom('sprite snow small 3', count=50),
    )
