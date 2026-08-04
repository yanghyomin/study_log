import modi_plus
import time
bundle = modi_plus.MODIPlus()

env = bundle.envs[0]
display = bundle.displays[0]
speaker = bundle. speakers [0]
led = bundle.leds[0]

# env.volume
# display.text
# display.reset()

display.text = "준비"


while True:
    time.sleep(0.5)
    val = 0
    volume = 0
    while env.volume >= 10:
        display.text = "측정 중"
        time.sleep(0.1)
        val += 0.1

    if val >= 6:
        display.text = f"ㄹㅈㄷ  점수 : {str(val)}s"
        led.rgb=(255, 0,0)
        while volume <= 830:
            speaker.tune = volume, 50
            volume += 1
        time.sleep(3)
        led.turn_off()
        time.sleep(3)
        display.text = "준비"
        speaker.volume = 0
    
    elif val >= 1:
        display.text = f"점수 : {str(val)}s"
        time.sleep(3)
        display.text = "준비"
    