import modi_plus
import time
bundle = modi_plus. MODIPlus()


# 센서 초기 데이터 동기화를 위해 1초 대기
time.sleep(1)

# 환경 센서 가져오기
env = bundle.envs[0]
display = bundle.displays[0]

# 센서 값 한 번만 출력
print(f"습도: {env.humidity}")
print(f"온도: {env.temperature}")
print(f"조도: {env.illuminance}")
print(f"소리: {env.volume}")

while 1:
    display.text = f"습도 : {env.humidity}  온도: {env.temperature}  조도: {env.illuminance}  소리: {env.volume}"