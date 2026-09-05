import modi_plus
import time
bundle = modi_plus.MODIPlus()

speaker = bundle.speakers[0]
tof=bundle.tofs[0]
dial = bundle.dials[0]


while 1:
    speaker.reset()
    if tof.distance <= 10:
  
        speaker.volume = 100 # 기본 볼륨 설정

        # --- Part 1: 특유의 땃! 땃! 땃! -- 땃! ---
        speaker.tune = 659.25, dial.turn  # E5 (미)
        time.sleep(0.12)
        speaker.volume = 0                # 끊기
        time.sleep(0.05)

        speaker.volume = 100
        speaker.tune = 659.25, dial.turn  # E5 (미)
        time.sleep(0.12)
        speaker.volume = 0                # 끊기
        time.sleep(0.12)

        speaker.volume = 100
        speaker.tune = 659.25, dial.turn  # E5 (미)
        time.sleep(0.12)
        speaker.volume = 0                # 끊기
        time.sleep(0.12)

        speaker.volume = 100
        speaker.tune = 523.25, dial.turn  # C5 (도)
        time.sleep(0.12)
        speaker.volume = 0                # 끊기
        time.sleep(0.05)

        speaker.volume = 100
        speaker.tune = 659.25, dial.turn  # E5 (미)
        time.sleep(0.12)
        speaker.volume = 0                # 끊기
        time.sleep(0.12)

        # --- Part 2: 솔! (저음) 솔! ---
        speaker.volume = 100
        speaker.tune = 783.99, dial.turn  # G5 (솔)
        time.sleep(0.25)
        speaker.volume = 0                # 끊기
        time.sleep(0.25)

        speaker.volume = 100
        speaker.tune = 392.00, dial.turn  # G4 (낮은 솔)
        time.sleep(0.25)
        speaker.volume = 0                # 소리 끔 (마무리)