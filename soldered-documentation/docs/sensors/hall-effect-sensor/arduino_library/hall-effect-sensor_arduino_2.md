---
slug: /hall-effect-sensor/arduino/examples 
title: Measuring strength and presence of magnetic field (examples)
id: hall-effect-sensor-arduino-2 
hide_title: False
---
This page contains some simple examples with function documentation on how to take measurements using the SI7211-B-00-IV temperature and humidity sensor.

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
  description="Instantiates digital sensor object"
  parameters={[
    { type: 'uint16_t', name: 'pin', description: "digital pin number for data communication" }
  ]}
  
/>
<FunctionDocumentation
  functionName="hall.getReading()"
  description="Requests a new reading from the SI7211-B-00-IV sensor. "
  returnDescription="Returns 1 (True) if magnet is detected and 0 (False) for no magnet detected. "
  
/>

---

## Analog output example

```cpp
#include "Hall-Effect-SOLDERED.h"
#define HALL_EFFECT_PIN A0

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
  description="Instantiates analog sensor object"
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
  description="calculates the value of magnetic induction from current reading"
  returnDescription="Returns float value that represents magnetic induction in milli Teslas"
  
/>

---

## Qwiic Digital output example
```cpp
#include "Hall-Effect-SOLDERED.h"

HallEffect_Digital_EasyC hall;

void setup()
{
    // Initialize serial communication
    Serial.begin(115200);

    // Initialize sensor via EasyC (required!)
    hall.begin();
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
  functionName="HallEffect_Digital_EasyC hall()"
  description="Instantiates digital sensor object"
/>

<FunctionDocumentation
  functionName="hall.begin()"
  description="Instantiates digital sensor object"
  parameters={[
    { type: 'uint16_t', name: 'address', description: "Optional, used for changing breakout address, default is 0x30" }
  ]}
/>

<FunctionDocumentation
  functionName="hall.getReading()"
  description="Requests a new reading from the SI7211-B-00-IV sensor. "
  returnDescription="Returns 1 (True) if magnet is detected and 0 (False) for no magnet detected. "
  
/>

---

## Qwiic Analog output example
```cpp
#include "Hall-Effect-SOLDERED.h"

// To change the reading, place a magnet in front of the sensor

// Declare sensor object on default address
HallEffect_Analog_EasyC hall;

void setup()
{
    // Initialize serial communication
    Serial.begin(115200);

    // Initialize sensor via EasyC (required!)
    hall.begin();

    // If you wish to use a custom address (e.g. 0x33), use
    // hall.begin(0x33);
}

void loop()
{
    // Read raw measurement
    uint16_t hallRawReading = hall.getRawReading();
    
    // Read milli Teslas
    float hallMilliTeslas = hall.getMilliTeslas();

    // Print sensor values to serial
    Serial.print("Analog Hall Effect raw sensor reading: ");
    Serial.println(hallRawReading);
    Serial.print("Which is: ");
    Serial.print(hallMilliTeslas);
    Serial.println(" mT\n");
    
    // Wait a bit until next measurement
    delay(1000);
}
```

<FunctionDocumentation
  functionName="HallEffect_Analog_EasyC hall()"
  description="Instantiates analog sensor object"
/>

<FunctionDocumentation
  functionName="hall.begin()"
  description="Instantiates digital sensor object"
  parameters={[
    { type: 'uint16_t', name: 'address', description: "Optional, used for changing breakout address, default is 0x30" }
  ]}
/>

<FunctionDocumentation
  functionName="hall.getRawReading()"
  description="Requests a new reading from the SI7211-B-00-IV sensor."
  returnDescription="Returns int value from output pin"

/>

<FunctionDocumentation
  functionName="hall.getMilliTeslas()"
  description="calculates the value of magnetic induction from current reading"
  returnDescription="Returns float value that represents magnetic induction in milli Teslas"
  
/>