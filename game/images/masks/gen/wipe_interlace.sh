#!/bin/bash

#VERTICAL=1
W=800
H=600

for VERTICAL in $(seq 0 1); do
    if [[ -z "${VERTICAL}" || VERTICAL -eq 0 ]]; then
        _zebra_type='vertical2'
        _gradient_dim=('-size' "${H}x${W}" 'gradient:black-white' '-rotate' '90')
        _flip='-flop'
        _prefix='h'
    else
        _zebra_type='horizontal2'
        _gradient_dim=('-size' "${W}x${H}" 'gradient:black-white' '-rotate' '180')
        _flip='-flip'
        _prefix='v'
    fi

    magick \
        '(' \
            '(' "${_gradient_dim[@]}" "${_flip}" ')' \
            '(' -size "${W}x${H}" "pattern:${_zebra_type}" ')' \
            -compose CopyOpacity -composite \
        ')' \
        '(' \
            '(' "${_gradient_dim[@]}" ')' \
            '(' -size "${W}x${H}" "pattern:${_zebra_type}" "${_flip}" ')' \
            -compose CopyOpacity -composite \
        ')' \
        -compose Overlay -composite \
        -define webp:lossless=true \
        "${_prefix}wipe_interlace.webp"
done
