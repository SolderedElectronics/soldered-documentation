---
slug: /hall-effect-sensor/arduino/Qwiic-digital-example 
title: Detecting magnetic presence with Qwiic digital sensor (example)
id: hall-effect-sensor-arduino-4 
hide_title: False
---

This page contains some simple examples with function documentation on how to take measurements using the SI7211-B-06-IV Hall effect sensor and Qwiic connection.

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
  description="Creates digital sensor object"
/>

<FunctionDocumentation
  functionName="hall.begin()"
  description="Initialises digital sensor object"
  returnDescription="Returns true if initialization is successful, false otherwise."
  parameters={[
    { type: 'uint16_t', name: 'address', description: "Optional, used for changing breakout address, default is 0x30" }
  ]}
/>

<FunctionDocumentation
  functionName="hall.getReading()"
  description="Requests a new reading from the SI7211-B-00-IV sensor. "
  returnDescription="Returns bool value, true if magnet is detected and false for no magnet detected. "
  
/>

---

## Serial Monitor output
<CenteredImage src="/img/hall-effect-sensor/hall-effect-sensor_digital_serial_monitor.jpg" alt="SI7211-B-00-IV sensor on board" caption="output from Serial Monitor" width="400px" />

---

## Full example

Try all of the above mentioned functions in this full example which detects presence of magnetic object.

<QuickLink 
  title="digitalReadEasyC.ino" 
  description="Example file for using Digital Hall effect sensor with easyC/Qwiic/I2C"
  url="https://github.com/SolderedElectronics/Soldered-Hall-Effect-Sensor-Arduino-Library/blob/main/examples/digitalReadEasyC/digitalReadEasyC.ino" 
/>