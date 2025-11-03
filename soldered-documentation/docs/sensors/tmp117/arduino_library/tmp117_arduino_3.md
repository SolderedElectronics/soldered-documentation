---
slug: /tmp117/arduino/simple-reading
title: TMP117 Temperature Sensor – Simple Reading
sidebar_label: Simple Reading
id: tmp117-arduino-3
hide_title: true
---

# Simple Reading

This page shows a minimal example that **reads temperature every 100 ms** and prints it to the Serial Monitor.

## Read temperature data

Open the Serial Monitor at **115200 baud** to observe the temperature values.

```cpp
#include "Soldered-TMP117.h"

// Default I2C address on this breakout is 0x49 (changeable via jumpers)
// Soldered_TMP117 tmp(0x48); // use this if you changed the address
Soldered_TMP117 tmp;

void setup() {
  Wire.begin();
  Serial.begin(115200);
  tmp.init(NULL);
}

void loop() {
  Serial.print("Temperature : ");
  Serial.print(tmp.getTemperature());
  Serial.println(" °C");
  delay(100);
}
```

## Function reference

<FunctionDocumentation
  functionName="tmp.init(void (*newDataCallback) = nullptr)"
  description="Initializes communication with the TMP117 sensor over I²C and prepares it for temperature measurement. Must be called once in setup()."
  returnDescription="bool, true if initialization succeeded, false if the sensor was not detected"
/>

<FunctionDocumentation
  functionName="tmp.getTemperature()"
  description="Retrieves the most recent temperature measurement from the TMP117 sensor."
  returnDescription="float, Temperature value in degrees Celsius"
/>


<CenteredImage src="/img/tmp117/connection.jpg" alt="SPK0641HT4H-1 Pinout" caption="Dasduino CONNECTPLUS connected to TMP117 temperature sensor via Qwiic connector." width="800px"/>

<br></br>

<CenteredImage src="/img/tmp117/simpleread.png" alt="Serial Monitor output" caption="Simple periodic temperature readout." width="700"/>

## Full example

<QuickLink 
  title="simpleReading.ino" 
  description="Example that reads TMP117 temperature every 100 ms"  
  url="https://github.com/SolderedElectronics/Soldered-Temperature-Sensor-TMP117-Arduino-Library/blob/main/examples/simpleReading/simpleReading.ino"  
/>  