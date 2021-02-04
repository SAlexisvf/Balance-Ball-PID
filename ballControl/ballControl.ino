#include <PID_v1.h>
#include <Servo.h>

double coordY = 0;
double coordX = 0;

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
float Kp = 0.6;                                                     
float Ki = 0.03;                                                      
float Kd = 0.13;

float Kp1 = 0.6;                                                       
float Ki1 = 0.08;                                                      
float Kd1 = 0.13;

//INIT PID
PID myPID(&coordX, &Output, &Setpoint, Kp, Ki, Kd, DIRECT);
PID myPID1(&coordY, &Output1, &Setpoint1,Kp1,Ki1,Kd1, DIRECT);


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
  myPID.SetOutputLimits(45, 135);
  myPID1.SetMode(AUTOMATIC);
  myPID1.SetOutputLimits(45, 135);
  // TIME SAMPLE
  myPID1.SetSampleTime(Ts); 
  myPID.SetSampleTime(Ts);  
  /////
  delay(100);
}

void loop() {
  pidControl();
}
