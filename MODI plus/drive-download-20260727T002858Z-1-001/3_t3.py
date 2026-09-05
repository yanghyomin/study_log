import modi_plus
import time
bundle=modi_plus. MODIPlus()

time.sleep(2)
dial=bundle.dials[0]
motor=bundle.motors[0]
turn=dial.turn
motor.angle=turn, turn

while True:
    speed=dial.turn
    motor.speed=speed
    time.sleep(0.1)
    if speed>90:
        motor.speed=0
        break

