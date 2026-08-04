import modi_plus
bundle = modi_plus. MODIPlus()
speaker = bundle. speakers [0]
tof=bundle.tofs[0]

print(tof.distance)

distance=tof.distance
print("distance:", distance)

while True:
    print(tof.distance, end="\r")
    if tof.distance<=20:
        speaker.tune = 2000, 50
    else :
        speaker.volume = 0

     