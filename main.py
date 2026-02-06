def on_button_pressed_a():
    basic.show_string("A")
    music.play(music.builtin_playable_sound_effect(soundExpression.happy),
        music.PlaybackMode.UNTIL_DONE)
    basic.pause(3000)
    basic.clear_screen()
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    basic.show_string("B")
    music.play(music.builtin_playable_sound_effect(soundExpression.yawn),
        music.PlaybackMode.UNTIL_DONE)
    basic.pause(3000)
    basic.clear_screen()
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_logo_pressed():
    basic.show_icon(IconNames.HEART)
    basic.pause(3000)
    basic.show_string("I'm Micro:bit")
    basic.clear_screen()
input.on_logo_event(TouchButtonEvent.PRESSED, on_logo_pressed)

basic.clear_screen()

def on_forever():
    if input.button_is_pressed(Button.AB):
        music.play(music.builtin_playable_sound_effect(soundExpression.hello),
            music.PlaybackMode.UNTIL_DONE)
        basic.show_string("Halo!")
basic.forever(on_forever)
