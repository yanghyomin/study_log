import modi_plus
import time
bundle = modi_plus.MODIPlus()

button = bundle.buttons[0]
imu = bundle.imus[0]
motor = bundle.motors[0]
display = bundle.displays[0]
env = bundle.envs[0]
dial = bundle.dials[0]



while 1:
    if button.toggled:
        turn = dial.turn
        ang_x = imu.angle_x
        display.text = f"각도 : {ang_x}켜짐 상태  현재 온도 : {env.temperature}"
        if ang_x < -50:
            if env.temperature > 32:
                if turn <= 20:
                    display.text = f"각도 : {ang_x}켜짐 상태  현재 온도 : {env.temperature}" + "1단계"
                    motor.speed = 20
                elif turn <= 50:
                    display.text = f"각도 : {ang_x}켜짐 상태  현재 온도 : {env.temperature}" + "2단계"
                    motor.speed = 50
                elif turn <= 100:
                    display.text = f"각도 : {ang_x}켜짐 상태  현재 온도 : {env.temperature}" + "3단계"
                    motor.speed = 100
        else :
            motor.speed = 0
            

    else:
        motor.speed = 0
        display.text = "꺼짐 상태"

    time.sleep(0.2)