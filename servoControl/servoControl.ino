#include <Servo.h>

Servo servoX;
Servo servoY;
int coordY = 0;
int coordX = 0;

void setup() {
  Serial.begin(9600);
  servoX.attach(9);
  servoY.attach(10);
  pinMode(13,OUTPUT);
  digitalWrite(13, LOW);
}

void loop() {
  receiveCoord();
  showNewData();
}

void moveServos(){
  servoX.write(90);
  servoY.write(90);
  delay(1000);
}
