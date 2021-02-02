#include <Servo.h>

Servo servoX;
Servo servoY;

void setup() {
  Serial.begin(9600);
  servoX.attach(9);
  servoY.attach(10);
  pinMode(13,OUTPUT);
}

void loop() {
  recvWithEndMarker();
  showNewData();
}

void moveServos(){
  servoX.write(90);
  servoY.write(90);
  delay(1000);
}
