music.stop_all_sounds()
def on_forever():
    if not (input.pin_is_pressed(TouchPin.P0)):
        music.play(music.tone_playable(262, music.beat(BeatFraction.WHOLE)),
            music.PlaybackMode.UNTIL_DONE)
basic.forever(on_forever)
