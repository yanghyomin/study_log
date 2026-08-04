import modi_plus
import time
bundle=modi_plus. MODIPlus()

time.sleep(2)
dial=bundle.dials[0]
motor0=bundle.motors[0]
motor1=bundle.motors[1]
turn=dial.turn
motor0.angle=turn, turn

while True:
    speed=dial.turn
    motor0.speed=speed
    motor1.speed=speed
    time.sleep(0.1)
    if speed>90:
        motor0.speed=0
        motor1.speed=0

