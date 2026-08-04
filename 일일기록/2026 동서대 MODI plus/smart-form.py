import modi_plus
import time
bundle = modi_plus.MODIPlus()


led = bundle.leds[0]
env = bundle.envs[0]
speaker = bundle. speakers [0]
motor = bundle.motors[0]
button = bundle.buttons[0]
display = bundle.displays[0]


while 1:
    display.text = env.humidity
    humidity = env.humidity
    if humidity <= 50:
        motor.angle = 270,20
        led.rgb = (255,0,0)
        speaker.tune = 1047,20

        if button.clicked:
            while humidity <= 50:
                display.text = env.humidity
                motor.angle = 180,20
                led.rgb = (255,0,0)
                speaker.tune = 800,20
                time.sleep(1)
                speaker.tune = 700,20
                time.sleep(1)
                speaker.tune = 1047,20
                time.sleep(1)
                speaker.reset()
                time.sleep(0.02)

    else:
        motor.angle = 270, 20
        led.rgb = 0, 255, 0
        speaker.reset()

    time.sleep(0.02)
