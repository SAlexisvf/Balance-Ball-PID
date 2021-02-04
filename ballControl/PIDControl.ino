
void pidControl()
{
  while(Stable<125) //REGULATION LOOP
  {
    receiveCoord();
    if(abs(coordX)<Setpoint+tolerance && abs(coordY)<Setpoint1+tolerance)//if ball is close to setpoint
    {
        Stable=Stable+1; //increment STABLE
        digitalWrite(13,HIGH);
          
    } else {
        digitalWrite(9,LOW);
    }
    myPID.Compute();  //action control X compute
    myPID1.Compute(); //   action control  Y compute   
    servo1.write(Output);//control
    servo2.write(Output1);//control
  }////END OF REGULATION LOOP///
  
 ///CONTROLER STABILITY////
 while(Stable>=125)//if is stable
 { //still measure actual postiion
    receiveCoord();
    if(abs(coordX)>Setpoint+tolerance && abs(coordY)>Setpoint1+tolerance) //if ball isnt close to setpoint
    {
      digitalWrite(13,LOW);
      Stable=0; //change STABLE state
    }
  }//end of STABLE LOOP
}//loop end
