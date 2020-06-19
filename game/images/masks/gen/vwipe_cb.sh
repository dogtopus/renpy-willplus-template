#!/bin/bash

magick -size 80x60 'gradient:black-grey' -flip tile2.png
magick -size 80x60 'gradient:grey-white' tile.png

montage tile.png tile2.png -tile 2x -geometry +0+0 tile12.png
montage tile2.png tile.png -tile 2x -geometry +0+0 tile21.png
montage tile12.png -duplicate 4 -tile 5x -geometry +0+0 row.png
montage tile21.png -duplicate 4 -tile 5x -geometry +0+0 row_alt.png
montage row.png row_alt.png -tile 1x2 -geometry +0+0 row2.png

montage row2.png -duplicate 4 -tile 1x -geometry +0+0 vwipe_cb.png

