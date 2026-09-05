
import modi_plus
import time

bundle = modi_plus.MODIPlus()

led = bundle.leds[0]
button = bundle.buttons[0]
dial = bundle.dials[0]



turn = dial.turn
state = 0

while True:
    turn = dial.turn

    if button.pressed:

        state = (state + 1) % 3

        if state == 1:
            led.rgb = (turn, 0, 0)

        elif state == 2:
            led.rgb = (0, turn, 0) 

        else:
            led.rgb = (0, 0, turn)
    time.sleep(0.02)
