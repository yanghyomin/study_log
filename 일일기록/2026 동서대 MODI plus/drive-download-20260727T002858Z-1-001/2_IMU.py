import modi_plus
import time

bundle = modi_plus.MODIPlus()
imu = bundle.imus[0]

try:
    while True:
        # 1. 가속도 (Acceleration) - 직선 움직임 및 중력
        acc_x = imu.acceleration_x
        acc_y = imu.acceleration_y
        acc_z = imu.acceleration_z

        # 2. 각속도 (Angular Velocity) - 회전하는 속도
        gyro_x = imu.angular_vel_x
        gyro_y = imu.angular_vel_y
        gyro_z = imu.angular_vel_z

        # 3. 회전 각도 (Angle) 
        ang_x = imu.angle_x    # X축 기준 기울기
        ang_y = imu.angle_y    # Y축 기준 기울기
        ang_z = imu.angle_z    # Z축 기준 기울기

        # 4. 진동 / 충격 (Vibration / Impact) - 3축 가속도 합성값
        impact = (acc_x**2 + acc_y**2 + acc_z**2) ** 0.5

        print("[기울기 각도] X:", round(ang_x, 1), "| Y:", round(ang_y, 1), "| Z:", round(ang_z, 1))
        print("[회전 각속도] X:", round(gyro_x, 1), "| Y:", round(gyro_y, 1), "| Z:", round(gyro_z, 1))
        print("[직선 가속도] X:", round(acc_x, 1), "| Y:", round(acc_y, 1), "| Z:", round(acc_z, 1))
        print("[진동 및 충격] 수치:", round(impact, 1))
        
        time.sleep(0.3)  # 화면 갱신 

except KeyboardInterrupt:
    print("\n종료")