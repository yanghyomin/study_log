import modi_plus
bundle = modi_plus. MODIPlus()

tof=bundle.tofs[0]
print(tof.distance)
print(tof.distance)
print(tof.distance)
distance=tof.distance
print("distance:", distance)

while True:
    print(tof.distance, end="\r")
    if tof.distance==100:
        break
    