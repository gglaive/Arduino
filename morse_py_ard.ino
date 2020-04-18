byte receivedChar;
boolean newData = false;

int led = 9; 

void setup() {
 Serial.begin(9600);
 pinMode(led, OUTPUT);
}

void loop() {
  

    receivedChar = Serial.read();
    //Serial.println(Serial.read());
    
    
    digitalWrite(led, LOW);
    delay(100);
    
    if (receivedChar == '1') {
      digitalWrite(led, HIGH);
      delay(1000);
    }
    if (receivedChar == '0') {
      digitalWrite(led, HIGH);
      delay(100);
    }
    if (receivedChar == '2') {
      digitalWrite(led, LOW);
      delay(1000);
    }
    
}
