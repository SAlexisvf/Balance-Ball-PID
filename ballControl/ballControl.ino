#include <PID_v1.h>
#include <Servo.h>

int coordY = 0;
int coordX = 0;

int tolerance = 2;


// PID params
unsigned int noTouchCount = 0; //viariable for noTouch
double Setpoint, Output; //for X
double Setpoint1, Output1; //for Y
Servo servo1; //X axis
Servo servo2; //Y axis

/////TIME SAMPLE
int Ts = 50; 
unsigned long Stable=0;
//PID const
float Kp = 2;                                                     
float Ki = 0.1;                                                      
float Kd = 0.3;

float Kp1 = 2;                                                       
float Ki1 = 0.1;                                                      
float Kd1 = 0.13;

double xx, yy;

//INIT PID
PID myPID(&xx, &Output, &Setpoint, Kp, Ki, Kd, DIRECT);
PID myPID1(&yy, &Output1, &Setpoint1,Kp1,Ki1,Kd1, DIRECT);


void setup() {
  //INIT PINS
  pinMode(13, OUTPUT);
  digitalWrite(13,LOW); //LED INIT

  Serial.begin(115200);
  coordX, coordY = 0;
  //INIT SETPOINT
  Setpoint, Setpoint1=0;
  //// Make plate flat
  servo1.attach(9); 
  servo2.attach(10);
  Output=90;
  Output1=90;
  servo1.write(Output);
  servo2.write(Output1);
  
  //Zapnutie PID
  // Servos move from 50° to 130°; balance = 90°
  myPID.SetMode(AUTOMATIC);
  myPID.SetOutputLimits(45, 150);
  myPID1.SetMode(AUTOMATIC);
  myPID1.SetOutputLimits(45, 135);
  // TIME SAMPLE
  myPID1.SetSampleTime(Ts); 
  myPID.SetSampleTime(Ts);  
  /////
  delay(100);
}

void loop() {
  // pidControl();
  receiveCoord();
  showNewData();
  if(abs(coordX) > tolerance){
    Output = map(coordX, -270, 270, 180, 45);
    servo1.write(Output);
  }else{
    servo1.write(90);
  }
  if(abs(coordY) > tolerance){
    Output = map(coordY, -240, 210, 130, 45);
    servo2.write(Output);
  }else{
    servo1.write(90);
  }
}
