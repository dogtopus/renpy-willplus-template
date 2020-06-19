# Graphics-related helpers/thunks/etc.

# Thunks
init python:
    # Used by op2rpy to simulate the shake screen effect.
    def WillScreenShake(duration, magnitude, **properties):
        return Shake((0, 0, 0, 0), duration*0.2, dist=magnitude*5)

    # Thunk for ImageDissolve() that "simulates" mask_blend{,_r} in a more compact form
    def WillImageDissolve(image, duration, reverse=False):
        if isinstance(image, str) or isinstance(image, unicode):
            image = renpy.get_registered_image(image)
        return ImageDissolve(image, duration, 256, reverse=(not reverse))

    # Short ramp variant of WillImageDissolve(). Used for implementing mask{,_r}
    def WillImageDissolveSR(image, duration, reverse=False):
        if isinstance(image, str) or isinstance(image, unicode):
            image = renpy.get_registered_image(image)
        return ImageDissolve(image, duration, 1, reverse=(not reverse))

    # Crude emulation of fade_out (fades to complete white instead of creating the "wash-out" effect)
    #def WillFadeOut(duration):
    #    half_duration = duration / 2.0
    #    return Fade(half_duration, 0.0, half_duration, color='#fff')

    # Implements dissolve_to_push_{up, down, left, right}
    def WillDissolveToPush(duration, push_mode='pushright'):
        return ComposeTransition(Dissolve(duration), after=PushMove(duration, push_mode))

    # Diagonal strips
    def WillDiagonalStrip(duration):
        return ImageDissolve('masks/diagonal.webp', duration, 1)

    # Diagonal box fills
    def WillBoxes(duration):
        return ImageDissolve('masks/boxes.webp', duration, 1)

    # Wipe effect with strips
    def WillWipeStrip(duration, mode='wiperight'):
        if mode in ('wiperight', 'wipeleft'):
            return ImageDissolve('masks/hwipe.webp', duration, ramplen=1, reverse=False if mode == 'wiperight' else True)
        elif mode in ('wipedown', 'wipeup'):
            return ImageDissolve('masks/vwipe.webp', duration, ramplen=1, reverse=False if mode == 'wipedown' else True)
        else:
            raise ValueError('Unknown mode {}'.format(mode))

    # Wipe effect with full-screen strips
    def WillWipeAllStrip(duration, mode='wiperight'):
        if mode in ('wiperight', 'wipeleft'):
            return ImageDissolve('masks/hwipe_s.webp', duration, ramplen=1, reverse=False if mode == 'wiperight' else True)
        elif mode in ('wipedown', 'wipeup'):
            return ImageDissolve('masks/vwipe_s.webp', duration, ramplen=1, reverse=False if mode == 'wipedown' else True)
        else:
            raise ValueError('Unknown mode {}'.format(mode))

    def WillShutterOpen(duration):
        return ImageDissolve('masks/shutter_open.webp', duration, 1)

    def WillWipeCheckboard(duration):
        return ImageDissolve('masks/vwipe_cb.webp', duration, 1)

# ATL transitions (see https://lemmasoft.renai.us/forums/viewtopic.php?f=32&t=14678)
# Dissolving to a new image that is zooming out
transform WillDissolveToZoomOut(duration, new_widget, old_widget):
    # Set delay for transitioning
    delay duration
    contains:
        old_widget
    contains:
        new_widget
        # Zoom out while dissolving in
        zoom 3.0 alpha 0.0 align (0.5, 0.5)
        linear duration zoom 1.0 alpha 1.0

# Zooming out only
transform WillZoomOut(duration, new_widget, old_widget):
    # Set delay for transitioning
    delay duration
    new_widget
    # Zoom out while dissolving in
    zoom 3.0 align (0.5, 0.5)
    linear duration zoom 1.0

# Better fade_out emulation
transform WillFadeOut(duration, new_widget, old_widget):
    delay duration
    contains:
        old_widget
    contains:
        new_widget
        alpha 0.0
        linear (duration) alpha 1.0
    # Top white layer
    contains:
        "#fff"
        alpha 0.0
        ease (duration / 2) alpha 0.8
        ease (duration / 2) alpha 0.0

transform WillXRotateProto(duration, sign, new_widget, old_widget):
    delay duration
    contains:
        old_widget
        align (0.5, 0.5)
        linear duration rotate (sign * 360.0) alpha 0.0
    contains:
        new_widget
        align (0.5, 0.5) alpha 0.0
        linear duration rotate (sign * -360.0) alpha 1.0

#transform WillFadeOutNoLeadIn(duration, new_widget, old_widget):
#    delay duration
#    contains:
#        old_widget
#    contains:
#        new_widget
#        alpha 0.5
#        time (duration / 2)
#        linear (duration / 2) alpha 1.0
#    # Top white layer
#    contains:
#        "#fff"
#        alpha 0.8
#        time (duration / 2)
#        ease (duration / 2) alpha 0.0

init python:
    def WillXRotate(duration, new_dir_cw=False):
        return WillXRotateProto(duration, -1 if new_dir_cw else 1)
