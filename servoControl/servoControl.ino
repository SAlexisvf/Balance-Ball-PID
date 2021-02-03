#include <Servo.h>

// Servos move from 45° to 135°; balance = 90°

Servo servoX;
Servo servoY;
int coordY = 0;
int coordX = 0;

int inclination=90;

int tolerance = 10;

void setup() {
  Serial.begin(115200);
  servoX.attach(9);
  servoY.attach(10);
  pinMode(13,OUTPUT);
  digitalWrite(13, LOW);
  servoX.write(90);
  servoY.write(90);
}

void loop() {
  receiveCoord();
  moveServos();
}

void moveServos(){
  if(coordY<0){
      servoY.write(45);
  }else if(coordY>0){
    servoY.write(135);
  }
//  if(abs(coordY)>tolerance){
//    if(coordY>0){
//      servoY.write(45);
//    }else{
//      servoY.write(135);
//    }
//  }else{
//    servoY.write(90);
//  }

  if(abs(coordX)>tolerance){
    if(coordX>0){
      servoX.write(45);
    }else{
      servoX.write(135);
    }
  }else{
    servoX.write(90);
  }
}
