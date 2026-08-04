import modi_plus
import time

bundle = modi_plus.MODIPlus()
print(bundle.modules)

display = bundle.displays[0]
led = bundle.leds[0]
# tof=bundle.tofs[0]

motor0 = bundle.motors[0]
motor1 = bundle.motors[1]
motor2 = bundle.motors[2]
motor3 = bundle.motors[3]


def hi():
    motor0.speed = 40
    time.sleep(0.5)
    motor0.speed = -40
    time.sleep(0.5)
    motor0.speed = 40
    time.sleep(0.5)
    motor0.speed = -40
    time.sleep(0.5)
    motor0.speed = 0


def forward():
    motor2.speed = 50
    motor3.speed = 50
    motor0.speed = -50
    motor1.speed = -50
    time.sleep(1)
    motor2.speed = 0
    motor3.speed = 0
    motor0.speed = 0
    motor1.speed = 0
    

display.text = "        !!!!   0    0                     0"\

while 1:
    a = input("hi,forward : ")
    if a == "hi":
        hi()
    if a == "w":
        forward()