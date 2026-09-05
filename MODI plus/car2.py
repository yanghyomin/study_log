import modi_plus
import time

bundle = modi_plus.MODIPlus()
print(bundle.modules)

button = bundle.buttons[0]
led = bundle.leds[0]

motor0 = bundle.motors[0]
motor1 = bundle.motors[1] 
motor2 = bundle.motors[2] 
motor3 = bundle.motors[3]
motor4 = bundle.motors[4] 
motor5 = bundle.motors[5]

time.sleep(3)


motor0.speed = 50
motor1.speed = 50
motor2.speed = 50
motor3.speed =50
motor4.speed =50 
motor5.speed =50

time.sleep(10)


