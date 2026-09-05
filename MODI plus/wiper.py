import modi_plus
import time

bundle = modi_plus.MODIPlus()

button = bundle.buttons[0]

motor0 = bundle.motors[0]
motor1 = bundle.motors[1]
dial = bundle.dials[0]




time.sleep(1)

motor0.angle = 90,0
motor1.angle = 90,0


def start_wiper():
    motor0.angle = 0, 20
    motor1.angle = 0, 20
    time.sleep(rain_time)
    motor0.angle = 90,20
    motor1.angle = 90, 20
    time.sleep(rain_time)


def stop_wiper():
    motor0.angle = 90,20
    motor1.angle = 90, 20



while 1:


    rain_time = 2.0 - (dial.turn / 100.0) * 1.8

    if button.toggled:
        start_wiper()

    else :
        stop_wiper()

    time.sleep(0.1)

        