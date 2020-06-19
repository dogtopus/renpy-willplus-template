#!/bin/bash

W=800
H=600

[[ $((W%2)) -eq 0 ]] || _die 'Width must be divisible by 2.'
[[ $((H%2)) -eq 0 ]] || _die 'Height must be divisible by 2.'

HW=$((W/2))
HH=$((H/2))

#magick -size ${HW}x${HH} 'gradient:black-white' v.png
#magick -size ${HH}x${HW} 'gradient:black-white' -rotate 90 h.png

montage \
    '(' -size ${HW}x${HH} 'gradient:black-white' ')' \
    '(' -size ${HH}x${HW} 'gradient:black-white' -rotate 90 ')' \
    '(' -size ${HH}x${HW} 'gradient:black-white' -rotate 90 -flop ')' \
    '(' -size ${HW}x${HH} 'gradient:black-white' -flip ')' \
    -tile 2x2 -geometry +0+0 shutter_open.png
