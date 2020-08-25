# Transitions and full screen effects

## Instruction `screen_effect` (`0x4d`)

### Format

```c++
enum ScreenEffectType : uint8_t {
    none = 0,
    shake,
    vwave,
    hwave,
    negative_flash,
};

struct ScreenEffect {
    ScreenEffectType type;
    uint8_t duration; // per 200ms
    uint8_t magnitude; // only available to certain effects (at least shake)
};
```

### Equivalent implementation

#### Indefinite screen shake (`type == ScreenEffectType::shake && duration == 0xff`)

```renpy
show layer master:
    function WillShakeDriverIndefinite(magnitude)
```

#### Regular screen shake (`type == ScreenEffectType::shake && duration != 0xff`)

```renpy
with WillScreenShake(duration, magnitude)
```

### Note

Generally indefinite effects will be implemented using layer-wide ATL. This is to ensure `clear_screen_effect` can be easily implemented (by clearing the layer-wide ATL). Regular effects, on the other hand, will normally be implemented as a transition effect (invoked with `with` statements) in order to stick to the Ren'Py idiom as much as possible.

## Instruction `clear_screen_effect` (`0x62`)

### Equivalent implementation

```renpy
show layer master
```

## Instruction `tint` (`0xb9`)

### Format

```c++
struct Tint {
    uint8_t table_index; // 1-4 seems to be common across games.
};
```

### Equivalent implementation

#### Using ATL `matrixcolor` (`7.4.0-g9b819d5` and later)
```renpy
show eileen happy as fg_iindex:
    # ...
    matrixcolor WillTintTable(table_index)
    # ...
```

#### Legacy `im`-based implementation

```renpy
show WillImTint('eileen happy', table_index) as fg_iindex
```

## Instruction `transition` (`0x4a`)

```c++
enum TransitionType : uint8_t {
    none = 0,
    wipe_down_all_strip,
    wipe_up_all_strip,
    wipe_right_all_strip,
    wipe_left_all_strip,
    zoom_out,
    boxes,
    vwipe_interlace,
    dithered_dissolve,
    diagonal,
    shutter_open,
    wipe_down_strip,
    wipe_up_strip,
    wipe_right_strip,
    wipe_left_strip,
    vwipe_checkerboard,
    hwipe_interlace,
    wipe_down,
    wipe_up,
    wipe_right,
    wipe_left,
    pixellate,
    dissolve_to_zoom_out,
    mask_wipe,
    mask_wipe_r,
    fade_in,
    fade_out,
    mask_dissolve_white_out,
    dissolve_to_push_up,
    dissolve_to_push_down,
    dissolve_to_push_left,
    dissolve_to_push_right,
    rotate_90_ccw,
    rotate_90_cw,
    new_dissolve_to_zoom_out_while_image_dissolve_r_to_new,
    old_dissolve_to_zoom_in_while_image_dissolve_to_new,
    vwave,
    hwave,
    xrotate_new_ccw_with_vwave,
    xrotate_new_cw_with_vwave,
    xrotate_new_ccw,
    xrotate_new_cw,
    mask_dissolve,
    stretch,
    mask_dissolve_r,
    mask_dissolve_r_white_out,
};

struct ScreenEffect {
    TransitionType type;
    uint16_t duration; // ms
};
```

### Equivalent implementation

All transitions are implemented as Ren'Py transitions. Below is a table of the supported transitions along with their corresponding implementation in Ren'Py. All durations follow Ren'Py convention i.e. using seconds as the unit instead of milliseconds like WillPlus ADV engine.

| WillPlus Transition | Ren'Py Equivalent | Note |
| ------------------- | ----------------- | ---- |
| `wipe_(down\|up\|left\|right)_all_strip` | `WillWipeAllStrip` | Available modes: wipe(down\|up\|left\|right) |
| `zoom_out` | `WillZoomOut` | |
| `boxes` | `WillBoxes` | |
| `(v\|h)wipe_interlace` | `WillWipeInterlace` | Available modes: vertical, horizontal |
| `dithered_dissolve` | `WillDitheredDissolve` | |
| `diagonal` | `WillDiagonalStrip` | |
| `shutter_open` | `WillShutterOpen` | |
