import modi_plus
import time
bundle = modi_plus.MODIPlus()


display = bundle.displays[0]
tof=bundle.tofs[0]
button = bundle.buttons[0]
led = bundle.leds[0]
env = bundle.envs[0]
motor = bundle.motors[0]

student_num = 0

while 1:
    motor.angle = 270, 20
    display.text = f"출석 된 학생수 : {student_num}"
    if tof.distance <= 20:
        display.text = "체온을 측정합니다. 온도계에 손을 올려주세요"
        time.sleep(3)
        while env.illuminance >= 10:
            display.text = "손 올리라고."
            time.sleep(3)
        display.text = "3"
        time.sleep(1)
        display.text = "2"
        time.sleep(1)
        display.text = "1"
        led.rgb=(255, 0, 0)
        time.sleep(1)
        led.rgb=(0, 255, 0)
        display.text = f"체온 : {env.temperature}"
        time.sleep(1)
        led.turn_off()
        if env.temperature <= 37:
            display.text = "정상체온입니다."
            time.sleep(1)
            display.text = "출석체크 확인"
            student_num += 1
            led.rgb=(0, 255, 0)
            motor.angle = 360, 20
            time.sleep(2)
            led.turn_off()
            display.reset()
        else :
            display.text = "병원 가세요"
            led.rgb=(255, 0, 0)
            time.sleep(2)
            led.turn_off()
            display.reset()


    if button.clicked:
        student_num = 0
        display.text = "학생 초기화"
        time.sleep(0.5)
        display.reset()


    if student_num >= 3:
        display.text = f"출석 된 학생수가 3명이 되었습니다 학생 수 : {student_num}"
        motor.angle = 270, 20
        break



    

    time.sleep(0.1)