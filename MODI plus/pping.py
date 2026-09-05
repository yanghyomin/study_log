import modi_plus
import time

bundle = modi_plus.MODIPlus()


display = bundle.displays[0]
led = bundle.leds[0]
env=bundle.envs[0]




time.sleep(2)

while True:
    if env.volume > 5:
        display.text = "3"
        time.sleep(1)
        display.text = "2"
        time.sleep(1)
        display.text = "1"
        time.sleep(1)


        display.text = "눈 조심해!"
        time.sleep(0.5)


        led.rgb=(255,0, 0)
        time.sleep(2)
        led.turn_off()
        display.reset()
