# LED 점등 
import modi_plus
import time

bundle = modi_plus.MODIPlus()
print(bundle.modules)

led = bundle.leds[0]

led.red = 255
time.sleep(3)

led.red = 0
time.sleep(1)

led.green = 100
time.sleep(3)

led.green = 0
time.sleep(1)

led.blue = 100
time.sleep(3)

# 켜고 끄기
led.turn_on()
time.sleep(2)
led.turn_off()
time.sleep(1)

#rgb 표현
led.rgb=(30, 100, 100)
time.sleep(2)
led.turn_off()