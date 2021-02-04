const byte numChars = 32;
String receivedCoordinates = "hello";

void receiveCoord() {
    if (Serial.available() >0) {
      receivedCoordinates = Serial.readStringUntil('>');
      int position_comma = receivedCoordinates.indexOf(',');
      coordX = receivedCoordinates.substring(0, position_comma).toInt();
      coordY = receivedCoordinates.substring(position_comma + 1, receivedCoordinates.length()-2).toInt();
    }
}

void showNewData() {
    if(coordY == 999){
      digitalWrite(13, HIGH);
      coordY++;
      delay(1000);
      digitalWrite(13, LOW);
    }else{
      digitalWrite(13, LOW);
    }
}
