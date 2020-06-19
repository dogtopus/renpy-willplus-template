#!/bin/bash

W=800
H=600

TILE_SIZE=40

_die() {
    echo "${@}"
    exit 1
}

[[ $((W%TILE_SIZE)) -eq 0 ]] || _die 'Width must be divisible by tile size.'
[[ $((H%TILE_SIZE)) -eq 0 ]] || _die 'Height must be divisible by tile size.'

NW=$((W/TILE_SIZE))
NH=$((H/TILE_SIZE))

magick '(' -size ${NW}x${NH} 'gradient:black-white' -rotate 180 ')' -filter point -resize ${W}x${H} modv.png 
magick '(' -size ${NH}x${NW} 'gradient:black-white' -rotate 90 ')' -filter point -resize ${W}x${H} modh.png

composite modv.png modh.png -blend 50% modifier.png

magick '(' -size ${TILE_SIZE}x${TILE_SIZE} 'gradient:black-white' -rotate 180 ')' '(' -size ${TILE_SIZE}x${TILE_SIZE} 'gradient:black-white' -rotate 90 ')' -compose Darken -composite tile.png

montage tile.png -duplicate $((NW*NH-1)) -tile ${NW}x${NH} -geometry +0+0 boxes_nomod.png

composite boxes_nomod.png modifier.png -blend 50% boxes.png
