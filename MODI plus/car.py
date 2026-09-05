import modi_plus
import time

bundle = modi_plus.MODIPlus()
print(bundle.modules)

display = bundle.displays[0]
led = bundle.leds[0]

motor0 = bundle.motors[0]
motor1 = bundle.motors[1] 
motor2 = bundle.motors[2] 
motor3 = bundle.motors[3]

dial = bundle.dials[0]
time.sleep(1)


def forward():
    led.rgb = (255,0,0)
    display.text = "forward"
    motor0.speed = -speed
    motor1.speed = speed
    motor2.speed = -speed
    motor3.speed = speed
    time.sleep(0.5)
    motor0.speed = 0
    motor1.speed = 0
    motor2.speed = 0
    motor3.speed = 0
    display.reset()
    led.turn_off()

def left():
    led.rgb = (255,255,0)
    display.text = "left"
    motor0.speed = 40
    motor1.speed = 40
    motor2.speed = 40
    motor3.speed = 40
    time.sleep(1)
    motor0.speed = 0
    motor1.speed = 0
    motor2.speed = 0
    motor3.speed = 0
    display.reset()
    led.turn_off()

def right():
    led.rgb = (0,255,255)
    display.text = "right"
    motor0.speed = -40
    motor1.speed = -40
    motor2.speed = -40
    motor3.speed = -40
    time.sleep(1)
    motor0.speed = 0
    motor1.speed = 0
    motor2.speed = 0
    motor3.speed = 0
    display.reset()
    led.turn_off()

def back():
    led.rgb = (0,0,255)
    display.text = "back"
    motor0.speed = speed
    motor1.speed = -speed
    motor2.speed = speed
    motor3.speed = -speed
    time.sleep(0.5)
    motor0.speed = 0
    motor1.speed = 0
    motor2.speed = 0
    motor3.speed = 0
    display.reset()
    led.turn_off()

def 입력():
    c = []
    while 1:
        b = input("명령(입력,입력실행,입력확인,입력초기화,종료) : ")
        if b == "입력":
            c = input("입력 : ").split(" ") # w a s d

        elif b == "입력실행":

            if c == []:
                print("입력이 비었습니다.")

            for i in c:
                speed = dial.turn
                
                if i == "w":
                    forward()
                
                elif i == "s":
                    back()
                
                elif i == "a":
                    left()
                
                elif i == "d":
                    right()
                
                elif i == "속력":
                    print(speed)
                
                elif i == "종료":
                    print("bye")
                    break
                
                else :
                    print("오류")
                    continue

        elif b == "입력확인":
            # if c == []:
            #     print("입력이 비었습니다.")
            # else:
            print(c)

        elif b == "입력초기화":
            c = []

        elif b == "종료":
            break



while 1:
    a = input("명령(w,a,s,d,속력,입력하기,종료) : ")
    speed = dial.turn

    if a == "w":
        forward()

    elif a == "s":
        back()

    elif a == "a":
        left()

    elif a == "d":
        right()

    elif a == "속력":
        print(speed)

    elif a == "입력하기":
        입력()

    elif a == "종료":
        print("bye")
        break

    else :
        print("오류")
        continue

