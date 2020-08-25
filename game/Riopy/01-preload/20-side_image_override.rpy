python early:
    def parse_will_side(lex):
        action = lex.word()
        if action == 'show':
            image = lex.rest()
        elif action == 'hide':
            image = None
        else:
            renpy.error('will_side: Unknown action {}.'.format(action))
        return image

    def execute_will_side(o):
        image = o
        globals()['side_image_override'] = image

    def lint_will_side(o):
        image = o
        if image is not None and renpy.get_registered_image(image) is None:
            renpy.error('{} is not an image.'.format(repr(str(image))))

    def predict_will_side(o):
        image = o
        if image is None:
            return tuple()
        else:
            return (renpy.get_registered_image(image), )

    renpy.register_statement('will_side',
        parse=parse_will_side,
        execute=execute_will_side,
        lint=lint_will_side,
        predict=predict_will_side,
    )
