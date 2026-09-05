import modi_plus
import time

bundle = modi_plus.MODIPlus()


button = bundle.buttons[0]
joystick = bundle.joysticks[0]
display = bundle.displays[0]
led = bundle.leds[0]
motor = bundle.motors[0]
speaker = bundle. speakers [0]

비밀번호  = [1,2,3,4]
입력 = []

print("위 : 1, 왼쪽 : 2, 아래 : 3, 오른쪽 : 4")
while 1:
    motor.angle = 270, 20
    display.text = f"입력한 비밀번호 : {입력}"

    if button.double_clicked:
        비밀번호 = []
        while 1:
            display.text = "비밀번호 설정 중.."
            if button.clicked:
                display.text = "비밀번호 설정 완료"
                led.rgb = (0,255,0)
                time.sleep(2)
                led.turn_off()
                break

            if joystick.x == 100:
                비밀번호.append(4)
                display.text = f"비밀번호 : {비밀번호}"
                speaker.tune = 800, 10
                time.sleep(0.3)
                speaker.tune = 800, 0
            if joystick.x == -100:
                비밀번호.append(2)
                display.text = f"비밀번호 : {비밀번호}"
                speaker.tune = 800, 10
                time.sleep(0.3)
                speaker.tune = 800, 0
            if joystick.y == 100:
                비밀번호.append(1)
                display.text = f"비밀번호 : {비밀번호}"
                speaker.tune = 800, 10
                time.sleep(0.3)
                speaker.tune = 800, 0
            if joystick.y == -100:
                비밀번호.append(3)
                display.text = f"비밀번호 : {비밀번호}"
                speaker.tune = 800, 10
                time.sleep(0.3)
                speaker.tune = 800, 0
            time.sleep(0.1)
        
    if button.clicked:
        if 입력 == 비밀번호:
            display.text = "정답입니다"
            led.rgb = (0,255,0)
            motor.angle = 360, 20
            speaker.tune = 600, 10
            time.sleep(0.5)
            speaker.tune = 800, 10
            time.sleep(0.5)
            speaker.tune = 1000, 10
            time.sleep(0.5)
            입력  = []
            display.reset()
            led.turn_off()
            speaker.tune = 1000, 0
        else :
            display.text = "틀렸습니다"
            led.rgb = (255,0,0)
            speaker.tune = 500, 10
            time.sleep(2)
            입력 = []
            display.reset()
            led.turn_off()
            speaker.tune = 500, 0

    

    if joystick.x == 100:
        입력.append(4)
        speaker.tune = 800, 10
        time.sleep(0.3)
        speaker.tune = 800, 0
    if joystick.x == -100:
        입력.append(2)
        speaker.tune = 800, 10
        time.sleep(0.3)
        speaker.tune = 800, 0
    if joystick.y == 100:
        입력.append(1)
        speaker.tune = 800, 10
        time.sleep(0.3)
        speaker.tune = 800, 0
    if joystick.y == -100:
        입력.append(3)
        speaker.tune = 800, 10
        time.sleep(0.3)
        speaker.tune = 800, 0

    time.sleep(0.1)



