def on_sound_loud():
    pass
input.on_sound(DetectedSound.LOUD, on_sound_loud)

def on_every_interval():
    pass
loops.every_interval(500, on_every_interval)

def on_forever():
    pass
basic.forever(on_forever)
