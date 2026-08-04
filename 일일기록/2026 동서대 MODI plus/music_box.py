import modi_plus
import time
bundle = modi_plus.MODIPlus()

speaker = bundle.speakers[0]
button = bundle.buttons[0]
dial = bundle.dials[0]


while 1:
    speaker.reset()
    if button.clicked:
        for i in range(2):
            speaker.tune = 1047, dial.turn
            time.sleep(0.3)
            speaker.tune = 1175, dial.turn
            time.sleep(0.3)
            speaker.tune = 1319, dial.turn
            time.sleep(0.3)
        for i in range(3):
            speaker.tune = 1568, dial.turn
            time.sleep(0.3)
            speaker.reset()






