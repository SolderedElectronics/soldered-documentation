---
slug: /hall-effect-sensor/arduino/regular-digital-example
title: "Hall Effect Sensor \u2013 Arduino regular digital example"
id: hall-effect-sensor-arduino-2
hide_title: false
---
This page contains a simple example with function documentation on how to take measurements using the SI7211-B-06-IV Hall effect sensor.

## Digital output example

```cpp
#include "Hall-Effect-SOLDERED.h"
#define HALL_EFFECT_PIN 5

// To change the reading, place a magnet in front of the sensor
// getReading returns 1 (True) for a detected magnet and 0 (False) for no magnet detected
// If it's always reading 0, check connections

// Declare sensor object
HallEffect_Digital hall(HALL_EFFECT_PIN);

void setup()
{
    // Initialize serial communication
    Serial.begin(115200);
}

void loop()
{
    // Read sensor
    bool hallReading = hall.getReading();

    // Print sensor value to serial
    Serial.print("Digital Hall Effect Sensor reading: ");
    Serial.println(hallReading);

    // Print a string depending on the measurement result
    if(hallReading)
    {
        Serial.println("Magnet detected!\n");
    }
    else
    {
        Serial.println("No magnet detected.\n");
    }
    
    // Wait a bit until next measurement
    delay(1000);
}
```
<FunctionDocumentation
  functionName="HallEffect_Digital hall()"
  description="Creates digital sensor object"
  returnDescription="none "
  parameters={[
    { type: 'uint16_t', name: 'pin', description: "Digital pin number for data communication" }
  ]}
  
/>
<FunctionDocumentation
  functionName="hall.getReading()"
  description="Requests a new reading from the SI7211-B-00-IV sensor. "
  returnDescription="Returns bool value, true if magnet is detected and false for no magnet detected. "
  
/>

<CenteredImage src="/img/hall-effect-sensor/digital_no_magnet.png" alt="Sensor when magnet is not present" caption="Sensor when magnet is not present" width="700px" />
<CenteredImage src="/img/hall-effect-sensor/digital_serial_no_magnet.jpg" alt="Serial Monitor output" caption="Serial Monitor output" width="700px" />
<CenteredImage src="/img/hall-effect-sensor/digital_magnet.png" alt="Sensor when magnet is present" caption="Sensor when magnet is present" width="700px" />
<CenteredImage src="/img/hall-effect-sensor/digital_serial_magnet.jpg" alt="Serial Monitor output" caption="Serial Monitor output" width="700px" />


---

## Full example

Try all of the above mentioned functions in this full example which detects presence of magnetic object.

<QuickLink 
  title="digitalRead.ino" 
  description="Example file for using digital Hall effect sensor."
  url="https://github.com/SolderedElectronics/Soldered-Hall-Effect-Sensor-Arduino-Library/blob/main/examples/digitalRead/digitalRead.ino" 
/>