---
slug: /hall-effect-sensor/arduino/regular-analog-example
title: Hall Effect Sensor - Measuring strength of magnetic field with regular analog
sidebar_label: Measuring strength of magnetic field with regular analog
  sensor (example)
id: hall-effect-sensor-arduino-3
hide_title: false
---
This page contains a simple example with function documentation on how to take measurements using the SI7211-B-00-IV Hall effect sensor.



## Analog output example

```cpp
#include "Hall-Effect-SOLDERED.h"
#define HALL_EFFECT_PIN 12

// To change the reading, place a magnet in front of the sensor
// The sensor outputs a value approximately in the middle of your analogRead range
// A higher number indicates a stronger positive magnetic force
// A lower number indicates a stronger negative magnetic force

HallEffect_Analog hall(HALL_EFFECT_PIN);

void setup()
{
    // Initialize serial communication
    Serial.begin(115200);
}

void loop()
{
    // Read sensor and store to variable
    uint16_t hallReading = hall.getReading();
    float hallMilliTeslas = hall.getMilliTeslas();

    // Print sensor values to serial
    Serial.print("Analog Hall Effect raw sensor reading: ");
    Serial.println(hallReading);
    Serial.print("Analog Hall Effect sensor reading in milli Teslas: ");
    Serial.print(hallMilliTeslas);
    Serial.println(" mT\n");

    // Wait a bit until next measurement
    delay(1000);
}
```

<FunctionDocumentation
  functionName="HallEffect_Analog hall()"
  description="Creates analog sensor object"
  parameters={[
    { type: 'uint16_t', name: 'pin', description: "Analog pin number for data communication" }
  ]}
/>

<FunctionDocumentation
  functionName="hall.getReading()"
  description="Requests a new reading from the SI7211-B-00-IV sensor."
  returnDescription="Returns int value from output pin"

/>

<FunctionDocumentation
  functionName="hall.getMilliTeslas()"
  description="Calculates the value of magnetic induction from current reading"
  returnDescription="Returns float value that represents magnetic induction in milli Teslas"
  
/>

<CenteredImage src="/img/hall-effect-sensor/analog_no_magnet.png" alt="Sensor when magnet is not present" caption="Sensor when magnet is not present" width="700px" />
<CenteredImage src="/img/hall-effect-sensor/analog_serial_no_magnet.jpg" alt="Serial Monitor output" caption="Serial Monitor output" width="700px" />
<CenteredImage src="/img/hall-effect-sensor/analog_magnet.png" alt="Sensor when magnet is present" caption="Sensor when magnet is present" width="700px" />
<CenteredImage src="/img/hall-effect-sensor/analog_serial_magnet.jpg" alt="Serial Monitor output" caption="Serial Monitor output" width="700px" />

---

## Full example

Try all of the above mentioned functions in this full example which measures the strenght of magnetic field.

<QuickLink 
  title="analogRead.ino" 
  description="Example file for using analog Hall effect sensor"
  url="https://github.com/SolderedElectronics/Soldered-Hall-Effect-Sensor-Arduino-Library/blob/main/examples/analogRead/analogRead.ino" 
/>