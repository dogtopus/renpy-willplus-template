init python:
    renpy.register_shader('willplus.wave', variables='''
        uniform sampler2D tex0;
        attribute vec2 a_tex_coord;
        varying vec2 v_tex_coord;
        uniform float u_willplus_wave_xamplitude;
        uniform float u_willplus_wave_yamplitude;
        uniform float u_willplus_wave_xphase;
        uniform float u_willplus_wave_yphase;
        uniform float u_willplus_wave_xwavelength;
        uniform float u_willplus_wave_ywavelength;
    ''', vertex_500='''
        v_tex_coord = a_tex_coord;
    ''', fragment_500='''
        const float PI = 3.1415926535897932384626;
        float xshift, yshift;
        if (u_willplus_wave_xamplitude > 0.0) {
            xshift = sin(v_tex_coord.y * (PI / u_willplus_wave_xwavelength) + u_willplus_wave_xphase * PI / 180.0) * u_willplus_wave_xamplitude;
        } else {
            xshift = 0.0;
        }
        if (u_willplus_wave_yamplitude > 0.0) {
            yshift = sin(v_tex_coord.x * (PI / u_willplus_wave_ywavelength) + u_willplus_wave_yphase * PI / 180.0) * u_willplus_wave_yamplitude;
        } else {
            yshift = 0.0;
        }
        vec2 uv = vec2(v_tex_coord.x + xshift, v_tex_coord.y + yshift);
        vec4 color0 = texture2D(tex0, uv);
        gl_FragColor = color0;
    ''')

