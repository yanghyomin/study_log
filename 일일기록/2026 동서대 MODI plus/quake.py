import modi_plus
import time
bundle = modi_plus.MODIPlus()

led = bundle.leds[0]
imu = bundle.imus[0]
speaker = bundle.speakers[0]
display = bundle.displays[0]

time.sleep(3)


while 1:
    led.turn_off()
    speaker.reset()
    if imu.acceleration_z > -47 or imu.acceleration_z < -51:
        time.sleep(1.5)
        if imu.acceleration_z > -47 or imu.acceleration_z < -51:
            time.sleep(0.5)
            while 1:
                time.sleep(0.5)
                if imu.acceleration_z > -47 or imu.acceleration_z < -51:
                    display.text = "지진이야!!!!"
                    led.rgb = 255,0 ,0
                    speaker.tune = 1975, 20
                    time.sleep(0.5)
                    led.rgb = 255 ,255 , 0
                    speaker.tune = 1975, 20
                    time.sleep(0.5)
                else:
                    display.reset()
                    break