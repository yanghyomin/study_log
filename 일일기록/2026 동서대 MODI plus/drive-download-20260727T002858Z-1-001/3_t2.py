import modi_plus
import time
bundle=modi_plus. MODIPlus()

tof=bundle.tofs[0]
speaker=bundle.speakers[0]

distance=tof.distance
speaker.volume=distance
time.sleep(2)
speaker.frequency=distance
time.sleep(2)
speaker.tune=1975, distance
time.sleep(2)
speaker.reset()

while True:
    distance=tof.distance
    speaker.tune=1975, distance
    time.sleep(0.1)
    if distance==100:
        speaker.reset()
        break


    