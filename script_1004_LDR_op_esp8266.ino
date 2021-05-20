void setup() {
  Serial.begin(9600);
}
void loop() {
  delay(500);
  float ldrWaarde = analogRead(A0);
  Serial.println(ldrWaarde);
}
