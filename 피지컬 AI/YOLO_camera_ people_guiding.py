import cv2 # cv2 패키지 가져오기
from ultralytics import YOLO # ultralytics의 YOLO 모델 가져오기
model = YOLO("yolo26n.pt") # YOLO의 학습된 데이터 가져오기
cap = cv2.VideoCapture(0)
import serial # 아두이노의 serial과 통신

ser = serial.Serial(
    port="/dev/cu.usbmodem11301", # 아두이노가 연결된 주소
    baudrate=9600,
    timeout=1,
)

while 1:
    ret, frame = cap.read()
    count = 0
    mid = 0
    if not ret:
        print("카메라를 찾을수 없음")
        break

    frame = cv2.flip(frame,1)

    cv2.putText(frame, "REC", (150,100), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 1, (0, 0,255),2)
    cv2.circle(frame,(100, 100), 30, (0,0,255),thickness=-1)
    cv2.rectangle(frame,(100,150), (1800,1000),(0,0,255),3)
    cv2.putText(frame, "부산소마고",(1500,980), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX,2,(255,0,0),10)

    results = model(frame)

    for box in results[0].boxes:
        conf = float(box.conf[0])
        if conf> 0.4:
            x1,y1,x2,y2 = map(int , box.xyxy[0])
            cls_id = int(box.cls[0])
            name = results[0].names[cls_id]
            cv2.rectangle(frame, (x1,y1), (x2,y2),(0,0,255), 3)
            label = f"{name} {conf:.2f}"
            cv2.putText(
                frame,
                label,
                (x1, y1 - 10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.6,
                (0, 255, 0),
                2,
            )
            
            if cls_id == 0:
                mid = (x1 + x2) / 2
                count += 1
    if count > 0:
        if mid < 600:
            ser.write(b"c")
        
        if mid > 600 and mid <= 1000:
            ser.write(b"d")
        
        if mid > 1200:
            ser.write(b"e")
        
        ser.write(b"a")
    else:
        ser.write(b"b")
    cv2.putText(frame, f"사람 수 : {count}",(1500,840), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX,2,(255,0,255),10)



    cv2.imshow("Webcam", frame)

    if cv2.waitKey(33) == ord("q"):
        break
ser.close()
cap.release()
cv2.destroyAllWindows()