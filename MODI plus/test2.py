import modi_plus
import time

bundle = modi_plus.MODIPlus()
print(bundle.modules)

display = bundle.displays[0]
led = bundle.leds[0]
speaker = bundle. speakers [0]

led.rgb = (255,0,0)
display.text = "STOP"
speaker.tune = 523, 50
time.sleep(3)

led.rgb = (0,255,0)
display.text = "WALK"
for i in range(5):
    speaker.tune = 1500,70
    time.sleep(0.15)
    speaker.volume = 0
    time.sleep(0.15)
time.sleep(0.5)


led.rgb = (255,100,0)
display.text = "WAIT"
time.sleep(3)

display.reset()
speaker.reset()
led.turn_off()