#버튼의 토글
import modi_plus
import time

bundle = modi_plus.MODIPlus()
button = bundle.buttons[0]
led = bundle.leds[0]

# 현재 LED 상태 단계 (0: 꺼짐, 1: 빨간색, 2: 노란색)
state = 0

print("=버튼 입력 대기중")


while True:
    # 버튼이 눌렸는지 확인
    if button.pressed:
        # 상태 변경: 0 -> 1 -> 2 -> 0 순환
        state = (state + 1) % 3

        if state == 1:
            led.rgb = (100, 0, 0)      # 1번째 눌림: 빨간색
            print(">> [1단계] 빨간색 (ON)")
        elif state == 2:
            led.rgb = (100, 100, 0)    # 2번째 눌림: 노란색
            print(">> [2단계] 노란색 (ON)")
        else:
            led.rgb = (0, 0, 0)        # 3번째 눌림: 꺼짐
            print(">> [0단계] LED 꺼짐 (OFF)")

        # 손을 뗄 때까지 대기 (중복 입력 방지)
        #while button.pressed:
        #    time.sleep(0.05)

    time.sleep(0.02)  # CPU 과점유 방지