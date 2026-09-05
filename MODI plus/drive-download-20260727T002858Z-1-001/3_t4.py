## IMU + led
# 변하는 값에 따라 LED변함
import modi_plus
import time
bundle=modi_plus. MODIPlus()
time.sleep(2)

imu=bundle.imus[0]
led=bundle.leds[0]

accel_x, accel_y, accel_z=imu.acceleration

abs_x=abs(accel_x)
abs_y=abs(accel_y)
abs_z=abs(accel_z)

print(f"X축(Red): {abs_x:.1f} | Y축(Green): {abs_y:.1f} | Z축(Blue): {abs_z:.1f}\n")

led.red=abs_x
time.sleep(2)
led.green=abs_y
time.sleep(2)
led.blue=abs_z
time.sleep(2)
led.turn_off()

while True:
    accel_x, accel_y, accel_z=imu.acceleration
    ang_x, ang_y, ang_z=imu.angle
    perfect_pitch=abs(0.5*accel_x)
    perfect_roll=abs(0.5*accel_y)
    perfect_yaw=abs(0.5*accel_z)

    #print(f"[가속도] X: {accel_x:6.1f} | Y: {accel_y:6.1f} | Z: {accel_z:6.1f}  ==>  [LED RGB] R: {perfect_pitch:5.1f}, G: {perfect_roll:5.1f}, B: {perfect_yaw:5.1f}")
    
    led.rgb=(perfect_pitch, perfect_roll, perfect_yaw)
    time.sleep(0.1)
    if abs(accel_x)>50:
        led.turn_off()
        break