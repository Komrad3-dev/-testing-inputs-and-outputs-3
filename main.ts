music.stopAllSounds()
basic.forever(function () {
    if (!(input.pinIsPressed(TouchPin.P0))) {
        music.play(music.tonePlayable(262, music.beat(BeatFraction.Whole)), music.PlaybackMode.UntilDone)
    }
})
