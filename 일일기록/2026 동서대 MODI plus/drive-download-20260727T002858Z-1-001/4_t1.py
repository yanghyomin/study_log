#잠자는 표정 봇

import modi_plus
import time
bundle=modi_plus. MODIPlus()

display=bundle.displays[0]
env=bundle.envs[0]
motor = bundle.motors[0]

while True:
    if env.volume>20:
        display.text="        !!!!   0    0                     0"
        motor.speed = 100
        time.sleep(2)
        display.text="        zzzz  --   --                  -----"
        motor.speed = 0
    else:
        display.text="        zzzz  --   --                  -----"

