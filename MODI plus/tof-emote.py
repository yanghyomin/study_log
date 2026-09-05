import modi_plus
import time


if __name__ == "__main__":
    bundle = modi_plus.MODIPlus()


tof = bundle.tofs[0]
display = bundle.displays[0]


print("손을 느끼다")
while 1:
    distance = tof.distance

    if distance > 100: distance = 100
    print(f"현재 인식 거리 : {distance} mm")

    display.reset()
    if distance <= 30:
        display.text = "  ( >_< )    !!!!    가깝다"

    elif distance <= 70:
        display.text = "  ( ^_^ )    * ㅇㅇ *     굿"

    else :
        display.text = "  ( T_T )    * ? ? *      어딧노"

    time.sleep(0.2)



