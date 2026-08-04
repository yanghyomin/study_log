import modi_plus
import time

bundle = modi_plus.MODIPlus()
print(bundle.modules)

speaker = bundle. speakers [0]

speaker.tune = 3951, 50  #(주파수, 볼륨)
time.sleep(2)
speaker. frequency = 1975
time.sleep(2)
speaker.volume = 100
time.sleep(2)
speaker.reset()