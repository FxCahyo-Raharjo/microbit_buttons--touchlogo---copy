input.onButtonPressed(Button.A, function () {
    basic.showString("A")
    music.play(music.builtinPlayableSoundEffect(soundExpression.happy), music.PlaybackMode.UntilDone)
    basic.pause(3000)
    basic.clearScreen()
})
input.onButtonPressed(Button.B, function () {
    basic.showString("B")
    music.play(music.builtinPlayableSoundEffect(soundExpression.yawn), music.PlaybackMode.UntilDone)
    basic.pause(3000)
    basic.clearScreen()
})
input.onLogoEvent(TouchButtonEvent.Pressed, function () {
    basic.showIcon(IconNames.Heart)
    basic.pause(3000)
    basic.showString("I'm Micro:bit")
    basic.clearScreen()
})
basic.clearScreen()
basic.forever(function () {
    if (input.buttonIsPressed(Button.AB)) {
        music.play(music.builtinPlayableSoundEffect(soundExpression.hello), music.PlaybackMode.UntilDone)
        basic.showString("Halo!")
    }
})
