long timee =0;
int x;
void setup() {
  
  
  Serial.begin(115200);

}

void loop() {
  while(!Serial);
  while (!Serial.available());
  x = Serial.readString().toInt();
  timee = millis();
  while(millis()-timee<10000){
    delay(4);
    Serial.println(analogRead(A0));
  }
  Serial.println("end");

}
