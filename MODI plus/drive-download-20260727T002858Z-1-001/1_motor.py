import modi_plus
import time

bundle = modi_plus.MODIPlus()
print(bundle.modules)

motor = bundle.motors[0]   #bundle.motors[1]
motor.angle = 0, 0
time.sleep(2)

motor.speed = 50
time.sleep(2)

motor.speed = 0  #모터 멈추기