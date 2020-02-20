/*
  DigitalReadSerial

  Reads a digital input on pin 2, prints the result to the Serial Monitor

  This example code is in the public domain.

  http://www.arduino.cc/en/Tutorial/DigitalReadSerial
*/

// digital pin 2 has a pushbutton attached to it. Give it a name:
int pushButton = 2;
int compteur = 0;
int pause = 0;

// the setup routine runs once when you press reset:
void setup() {
  // initialize serial communication at 9600 bits per second:
  Serial.begin(9600);
  // make the pushbutton's pin an input:
  pinMode(pushButton, INPUT);
}

// the loop routine runs over and over again forever:
void loop() {
  // read the input pin:
  int buttonState = digitalRead(pushButton);
  // print out the state of the button:
  if (buttonState == HIGH) {
    pause = 0;
    compteur = compteur + 1;
    delay(1);
  }
  if (buttonState == LOW){
    if (compteur > 1 && compteur < 500) {
      Serial.println("0"); // Signal court
      delay(10);
    } else if (compteur >= 500) {
      Serial.println("1"); // Signal long
      delay(10);
    }
    compteur = 0;
    pause = pause + 1;
    delay(1);
    
    if (pause >= 000) {
      Serial.println("2");
      pause = 0;
    }
  }
}