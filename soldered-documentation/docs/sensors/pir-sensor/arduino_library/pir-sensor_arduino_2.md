---
slug: /pir-sensor/arduino/detecting-movement-standard
title: Detecting movement (Standard)
id: pir-sensor-arduino-2
hide_title: False
---

This page contains a movement detecting example for the standard version of the board

---

## Setting up the pins

First, we must define what pins we are using and for what:

```cpp

#define SOUT_PIN 2
#define DOUT_PIN 4

//Variables that hold time since last measurement for specific pins
unsigned long dout_delay=0;
unsigned long sout_delay=0;

```

In the `setup()` function, we are setting the pin mode for the specific pins, as well as initializing the Serial communication. There is also a 20s delay that is needed to warm up the sensor for more accurate readings:

```cpp

void setup() {
  //Set the pins as input
  pinMode(DOUT_PIN, INPUT);
  pinMode(SOUT_PIN, INPUT);

  //Initialize serial communication
  Serial.begin(115200);

  Serial.println("Warming up sensor...");
  //Wait 20s so the sensor can warm up
  delay(20000);

  Serial.println("Warmup done!");
}

```
---

## Detecting movement

In the `loop()` function, we are seeing if there was a HIGH signal from the pins, if there was AND if the last measurement was more than 4s ago, we print out the detection to the serial monitor.

```cpp

void loop() {
  //If the pin is set to high at it has been less than 4s since last measurement, print detection
  if(digitalRead(DOUT_PIN) && millis()-dout_delay>=4000)
  {
    Serial.println("DOUT Motion detected!");
    dout_delay=millis();
  }
  //If the pin is set to high at it has been less than 4s since last measurement, print detection
  if(digitalRead(SOUT_PIN) && millis()-sout_delay>=4000)
  {
    Serial.println("SOUT Motion detected!");
    sout_delay=millis();
  }

}

```

<CenteredImage src="/img/pir-sensor/output.png" alt="Motion detection on serial monitor" caption="Motion detection on serial monitor" width="100%" />

<InfoBox>

You can see by the timestamps that the DOUT pin passes the 4s delay treshold, when the onboard potentiometer is put to the highest delay (counter-clockwise), it gives a HIGH reading for 2s more, this can be useful when creating a motion detector that is not to sensitive to small movements

</InfoBox>

---

## Full example

The full example is listed below:

```cpp

#define SOUT_PIN 2
#define DOUT_PIN 4

//Variables that hold time since last measurement for specific pins
unsigned long dout_delay=0;
unsigned long sout_delay=0;

void setup() {
  //Set the pins as input
  pinMode(DOUT_PIN, INPUT);
  pinMode(SOUT_PIN, INPUT);

  //Initialize serial communication
  Serial.begin(115200);

  Serial.println("Warming up sensor...");
  //Wait 20s so the sensor can warm up
  delay(20000);

  Serial.println("Warmup done!");
}

void loop() {
  //If the pin is set to high at it has been less than 4s since last measurement, print detection
  if(digitalRead(DOUT_PIN) && millis()-dout_delay>=4000)
  {
    Serial.println("DOUT Motion detected!");
    dout_delay=millis();
  }
  //If the pin is set to high at it has been less than 4s since last measurement, print detection
  if(digitalRead(SOUT_PIN) && millis()-sout_delay>=4000)
  {
    Serial.println("SOUT Motion detected!");
    sout_delay=millis();
  }

}

```