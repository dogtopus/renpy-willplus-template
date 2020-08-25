# Simple Alignment Gem maturity indicator for LL
# Add the CurrentGemIndicator() call to either the say screen or its own screen that is on the same or higher layer as say.

init -1 python:
    # The actual indicator Displayable. Displayed as a small triangle on the top right corner.
    class GemIndicator(renpy.Displayable):
        def __init__(self, maturity, **properties):
            super(GemIndicator, self).__init__(**properties)
            self._maturity = maturity

        def render(self, width, height, st, at):
            r = renpy.Render(48, 48)
            canvas = r.canvas()
            fill_color = Color(hsv=(1.0 - (self._maturity / 100.0 * 0.333), 0.7, 1.0), alpha=0.8)
            #canvas.polygon(fill_color, ((0, 0), (48, 0), (48, 48)))
            canvas.circle(fill_color, (48, 0), 48)
            return r

        @property
        def maturity(self):
            return self._maturity

        @maturity.setter
        def maturity(self, val):
            self._maturity = max(0, min(100, val))

    # Just a white triangle
    class BlankGemIndicator(renpy.Displayable):
        def __init__(self, **properties):
            super(BlankGemIndicator, self).__init__(**properties)

        def render(self, width, height, st, at):
            r = renpy.Render(48, 48)
            canvas = r.canvas()
            #canvas.polygon('#ffffff', ((0, 0), (48, 0), (48, 48)))
            canvas.circle(Color(rgb=(1, 1, 1)), (48, 0), 48)
            return r

init:
    # Define a blank gem indicator so we can reuse it forever.
    define BlankGemIndicatorInstance = BlankGemIndicator()

transform gem_flash(old, new):
    old
    new with MultipleTransition((False, Dissolve(0.1), BlankGemIndicatorInstance, Dissolve(0.1), True))

init:
    default gem.inst_current = GemIndicator(0)
    default gem.inst_display = GemIndicator(0)
    python:
        # Main indicator animation logic. Flash every time the gem value is updated. Also limit the maximum value to 100 to prevent issues.
        def update_gem_indicator():
            # Cap to 100 since that's what the original did.
            val = min(will_flagbank['gem_maturity'], 100)
            will_flagbank['gem_maturity'] = val

            # Skip or rollback and there's a change in value. Update the indicator without animation.
            if config.skipping or renpy.game.after_rollback and val != gem.inst_current.maturity:
                gem.inst_current = GemIndicator(val)
                gem.inst_display = gem.inst_current
            # Normal interaction. Update the indicator with a new instance with flash effect.
            elif val != gem.inst_current.maturity:
                # Indicator sound effect
                renpy.sound.play('PARAM.OGG')
                inst_old = gem.inst_current
                gem.inst_current = GemIndicator(val)
                gem.inst_display = gem_flash(inst_old, gem.inst_current)
            # No change. Ensure display instance and current indicator instance are consistent.
            # (This should also ensure that the animation is cleared and only the non-flashing indicator is shown.)
            elif gem.inst_display is not gem.inst_current:
                gem.inst_display = gem.inst_current

        # Hook into the start interact event.
        config.start_interact_callbacks.append(update_gem_indicator)

        # Helper to get the current gem indicator.
        def CurrentGemIndicator():
            return gem.inst_display
