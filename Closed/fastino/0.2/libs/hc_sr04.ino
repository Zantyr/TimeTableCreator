//distance sensor lib
//header
#define TRIGPIN 3
#define LISTPIN 4
int Distance;

//fndef
int hc_sr04_0()
{
    long echoTime;
    int dist;
    digitalWrite(TRIGPIN, LOW);
    delayMicroseconds(2);
    digitalWrite(TRIGPIN, HIGH);
    delayMicroseconds(10);
    digitalWrite(TRIGPIN, LOW);
    echoTime = pulseIn(LISTPIN, HIGH);
    dist = echoTime / 58;
    return dist;
}

//setup
void setup()
{
    pinMode(TRIGPIN,OUTPUT);
    pinMode(LISTPIN,INPUT);
}

//main
void loop()
{
    Distance = hc_sr04_0();
    Serial.print("Odleglosc: ");
    Serial.print(Distance);
    Serial.print("\n");
    delay(10); //optional
}