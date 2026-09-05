import modi_plus
import time

bundle = modi_plus.MODIPlus()
print(bundle.modules)

display = bundle.displays[0]

display.text = "hi"
time.sleep(3)
display.reset()
time.sleep(1)