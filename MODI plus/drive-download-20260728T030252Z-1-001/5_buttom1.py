# 버튼 동작
import modi_plus
import time

bundle = modi_plus.MODIPlus()

button = bundle.buttons[0]
led = bundle.leds[0]

print("버튼 입력 대기중")

while True:
    # 1. 클릭 : 빨간색
    if button.clicked:
        print("클릭! -> 빨간색")
        led.rgb = 255, 0, 0
        time.sleep(0.3)  # 바운싱 효과로 인한 딜레이

    # 2. 더블 클릭 (두 번 딸깍): 초록색
    elif button.double_clicked:
        print("더블 클릭! -> 초록색")
        led.rgb = 0, 255, 0
        time.sleep(0.4)  

    # 3. 누르고 있는 상태 (꾹~): 파란색
    elif button.pressed:
        print("누르는 중... -> 파란색")
        led.rgb = 0, 0, 255
        time.sleep(0.1)  

    # 4. 아무것도 안 누르면 LED 끄기
    else:
        led.rgb = 0, 0, 0
        time.sleep(0.05)  # CPU 과부하 방지용 미세 딜레이