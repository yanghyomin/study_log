import modi_plus
import time
bundle = modi_plus.MODIPlus()


tof = bundle.tofs[0]
speaker = bundle.speakers[0]
motor = bundle.motors[0] 


open_distance = 15
open_angle = 90
close_angle = 0

is_open = 0

print("스마트 휴지통 시작")

try:
    while 1:
        distance = tof.distance

        if distance > 0 and distance <= open_distance:
            if not is_open:
                print(f"사람 감지 거리 : {distance}mm -> 두껑 열림")

                speaker.tune = 1047, 20
                time.sleep(0.15)
                speaker.tune = 1318,20
                time.sleep(0.15)
                speaker.reset()

                motor.angle = open_angle, 20
                is_open = 1

        else:
            if is_open:
                print(f"사람 멀어짐 거리 : {distance}mm -> 뚜껑 닫힘")

                motor.angle = close_angle,20
                is_open = 0

        time.sleep(0.1)

except KeyboardInterrupt:
    print("\n스마트 휴지통 시스템을 종료합니다.")

    motor.angle = close_angle, 50
    speaker.reset()





