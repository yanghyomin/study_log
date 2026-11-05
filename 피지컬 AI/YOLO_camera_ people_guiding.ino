#include "Keyboard.h"
#include <Servo.h> // 서보모터 라이브러리 가져오기

Servo myservo;

int led = 13;

void setup() {
  Serial.begin(9600);
  pinMode(led,OUTPUT);
  myservo.attach(9);
}

void loop() {
  if (Serial.available() > 0) { // 시리얼이 python파일에서 통신한 값을 받고 센서 제어
    char val = Serial.read();
    if (val == 'a'){
      digitalWrite(led, 1);
    }
    if (val == 'b'){
      digitalWrite(led, 0);
    }
    if (val == 'c'){
      myservo.write(45);
    }
    if (val == 'd'){
      myservo.write(90);
    }
    if (val == 'e'){
      myservo.write(125);
    }

  }
}
