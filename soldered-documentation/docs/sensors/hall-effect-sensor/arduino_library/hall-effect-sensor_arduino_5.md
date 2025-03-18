---
slug: /hall-effect-sensor/arduino/Qwiic analog example 
title: Measuring strenght of magnetic field with Qwiic analog sensor (example)
id: hall-effect-sensor-arduino-5 
hide_title: False
pagination_next: null
---

This page contains some simple examples with function documentation on how to take measurements using the SI7211-B-00-IV Hall effect sensor and Qwiic connection.

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
  returnDescription="Returns true if initialization is successful, false otherwise."
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

---

## Serial Monitor output
<CenteredImage src="/img/hall-effect-sensor/hall-effect-sensor_analog_serial_monitor.jpg" alt="SI7211-B-00-IV sensor on board" caption="output from Serial Monitor" width="400px" />

---

## Full example

Try all of the above mentioned functions in this full example which measures the strenght of magnetic field.

<QuickLink 
  title="analogReadEasyC.ino" 
  description="Example file for using analog Hall effect sensor with easyC/Qwiic/I2C"
  url="https://github.com/SolderedElectronics/Soldered-Hall-Effect-Sensor-Arduino-Library/blob/main/examples/analogReadEasyC/analogReadEasyC.ino" 
/>