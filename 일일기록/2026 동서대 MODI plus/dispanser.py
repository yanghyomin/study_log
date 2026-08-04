import modi_plus
import time
import random
bundle = modi_plus.MODIPlus()



led = bundle.leds[0]
button = bundle.buttons[0]
display = bundle.displays[0]
tof=bundle.tofs[0]
motor = bundle.motors[0]

state = 0
while True:

    if button.pressed:

        state = (state + 1) % 4

        if state == 1:
            led.rgb = (0, 255, 0)
            display.text = "set 25ml"
            time.sleep(0.5)
        elif state == 2:
            led.rgb = (0, 0, 255) 
            display.text = "set 35ml"
            time.sleep(0.5)
        elif state == 3:
            led.rgb = (255, 0, 0)
            display.text = "set 50ml"
            time.sleep(0.5)

        else :
            ran_val = random.randint(1, 3)

            if state == 1:
                ran_val = (0, 255, 0)
                display.text = "set random 25ml"
                time.sleep(0.5)
            elif state == 2:
                ran_val = (0, 0, 255) 
                display.text = "set random 35ml"
                time.sleep(0.5)
            elif state == 3:
                ran_val = (255, 0, 0)
                display.text = "set random 50ml"
                time.sleep(0.5)



    if tof.distance<=10:
        display.text = "음료가 나옵니다"
        motor.speed = 30
        time.sleep(2)
        display.reset()
        motor.speed = 0


    time.sleep(0.02)