#3 환경과 디스플레이, 습도값 출력
import modi_plus
import time
bundle=modi_plus. MODIPlus()

env=bundle.envs[0]
display=bundle.displays[0]

humidity=env.humidity
temperature=env.temperature
illuminance=env.illuminance
display.write_variable_xy(0,0,humidity)
time.sleep(2)
display.write_variable_xy(0,0,temperature)
time.sleep(2)
display.write_variable_xy(0,0,illuminance)
time.sleep(2)
display.reset()

humidity=env.humidity
if humidity>50:
    display.text="습도가 높아요"
else:
    display.text="습도가 낮아요"
time.sleep(2)
display.reset()

## 미션
