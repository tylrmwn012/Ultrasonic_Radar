#include <Servo.h>
Servo myservo;
int pos = 0;
long duration;
int distance;

const int trigPin = 10;
const int echoPin = 11;

void setup() {
  myservo.attach(9);
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);
  Serial.begin(9600);
}

int object() {
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);

  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);

  duration = pulseIn(echoPin, HIGH);

  distance = duration * 0.034 / 2;

  return distance;
}

void loop() {
  for (pos = 0; pos <= 180; pos ++) {
    myservo.write(pos);
    distance = object();
    Serial.print(distance);
    Serial.print(",");
    Serial.println(pos);
    delay(15); 
  }
  for (pos = 180; pos >= 0; pos --) { 
    myservo.write(pos);
    distance = object();
    Serial.print(distance);
    Serial.print(",");
    Serial.println(pos);
    delay(15);                     
  }

}
