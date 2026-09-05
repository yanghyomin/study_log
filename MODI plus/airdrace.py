import modi_plus
import time
bundle = modi_plus.MODIPlus()


led = bundle.leds[0]
dial = bundle.dials[0]
motor = bundle.motors[0]
speaker  = bundle.speakers[0]
display = bundle.displays[0]



while 1:
    trun = dial.turn
    count = 0
    if trun >= 5:
        for i in range(10):
            count += 1
            display.text = f"반복횟수 : {count}"
            led.rgb=(0,0,255)
            motor.angle = 90,50
            time.sleep(0.15)
            motor.angle = 180,50
            led.rgb = (0,0,0)
            time.sleep(0.15)
        speaker.tune = 800,20
        time.sleep(1)
        speaker.tune = 700,20
        time.sleep(1)
        speaker.tune = 1047,20
        time.sleep(1)
        speaker.reset()
        time.sleep(0.02)
        display.text = "다이얼을 꺼달라"

        while trun >= 5:
            trun = dial.turn
            time.sleep(0.1)

        display.text = "준비"


    else :
        motor.angle = 0,10
        led.rgb = (0,0,0)
        count = 0
        display.reset()

    time.sleep(0.02)



