---
slug: /simple-sensor/simple-fire-sensor/arduino_library/qwiic-example
title: Simple Fire Sensor - Detecting and maesuring fire with Qwiic fire sensor (example)
sidebar_label: Detecting and maesuring fire with Qwiic fire sensor (example)
id: simple-fire-sensor-arduino-3
hide_title: false
---
This page contains a simple example with function documentation on how to detect and measure intensity of fire with the sensor.

---

## initialization
To use the sensor, first, include the required library, create the sensor object and SimpleFireSensor object and initalize it in the `setup()` function. You can use the return of `begin()` to check if everything is connected correctly.

```cpp
#include "Simple-fire-sensor-easyC-SOLDERED.h"

SimpleFireSensor sensor;
void setup() {
  sensor.begin();
}
//...
```
<FunctionDocumentation
  functionName="SimpleFireSensor sensor"
  description="Creates SimpleFireSensor object"
  returnDescription="none"
  parameters={[
    { type: 'uint16_t', name: 'pin', description: "Analog pin number for data communication" }
  ]}
/>

<FunctionDocumentation
  functionName="sensor.begin()"
  description="Initializes the sensor."
  returnDescription="Returns true if initialization is successful, false otherwise."
/>

---

## Measuring with both digital and analog output
In this library, there are two options for displaying analog value, for percent value, call `getValue()` function and for raw value, call `getRawValue()` function. You should set the `setRawLowerTresh()` and `setRawUpperTresh()` values to use the digital output.

```cpp
#include "Simple-fire-sensor-easyC-SOLDERED.h"

// Declare the sensor object
SimpleFireSensor sensor;

void setup()
{
    // Initialize the serial communication via UART
    Serial.begin(115200);

    // Initialize the sensor
    // Start I2C communication on default address (0x30)
    sensor.begin();

    // If you want another I2C address, enter it in the bracket
    // You can set another I2C address (0x31 - 0x37) by changing address switches on the breakout
    // NOTE: You have to restart breakout to apply the address change by unplugging and plugging
    // the easyC or USB-c from the Dasduino 
    // sensor.begin(0x31);

    sensor.setRawLowerTresh(850);  // You should set these two values, this is value when fire is present (you can use
                                   // lighter at 1m distance)
    sensor.setRawUpperTresh(1000); // This is value when no fire is present

    // You can use percentage values by calling following functions:
    // sensor.setLowerTresh(85); // 85%
    // sensor.setUpperTresh(99); // 99%

    // Set threshold for LED on the breakout
    sensor.setRawThreshold(250); // or
    // sensor.setThreshold(25.1); // 25.1%
}

void loop()
{
    Serial.print("IR light sensor reading: "); // Print information message
    Serial.print(sensor.getValue());           // Prints percent value of fire sensor
    Serial.print("% ");
    Serial.println(sensor.getRawValue()); // Prints raw value of fire sensor

    // This function checks to which value is closer value that has been read from sensor
    if (abs(sensor.getValue() - sensor.getLowerTresh()) < abs(sensor.getValue() - sensor.getUpperTresh()))
    // You can also use raw values if you want:
    // if (abs(sensor.getRawValue() - sensor.getRawLowerTresh()) < abs(sensor.getRawValue() - sensor.getRawUpperTresh()))
    {
        Serial.println("Fire is detected!!");
    }
    else
    {
        Serial.println("Fire is not detected.");
    }

    // Wait a bit before next reading
    delay(500);
}
```
<FunctionDocumentation
  functionName="sensor.getValue()"
  description="Returns the measurement in percentage."
  returnDescription="Returns float representation of fire chance percentage"
/>

<FunctionDocumentation
  functionName="sensor.getRawValue()"
  description="Returns the raw ADC value."
  returnDescription="Returns integer representation of fire value"
/>

<FunctionDocumentation
  functionName="sensor.setRawLowerTresh()"
  description="Sets the value at which fire is present"
  returnDescription="none"
  parameters={[
    { type: 'uint16_t', name: 'value', description: "Value at which fire is present" }
  ]}
/>

<FunctionDocumentation
  functionName="sensor.setRawUpperTresh()"
  description="Sets the value at which fire is not present"
  returnDescription="none"
  parameters={[
    { type: 'uint16_t', name: 'value', description: "Value at which fire is not present" }
  ]}
/>

<CenteredImage src="/img/simple-sensor/simple-fire-sensor/fire_not_detected_qwiic.png" alt="Sensor when fire is not present" caption="Sensor when fire is not present" width="700px" />

<CenteredImage src="/img/simple-sensor/simple-fire-sensor/fire_not_detected_serial.jpg" alt="Serial Monitor output" caption="Serial Monitor output" width="700px" />

<CenteredImage src="/img/simple-sensor/simple-fire-sensor/fire_detected_qwiic.png" alt="Sensor when fire is present" caption="Sensor when fire is present" width="700px" />

<CenteredImage src="/img/simple-sensor/simple-fire-sensor/fire_detected_serial.jpg" alt="Serial Monitor output" caption="Serial Monitor output" width="700px" />

---

## Full example

Try all of the above mentioned functions in full example below:

<QuickLink 
  title="Read_values_native.ino" 
  description="Example for using the digital and analog read functions for Simple fire sensor."
  url="https://github.com/SolderedElectronics/Soldered-Simple-Fire-Sensor-Arduino-library/blob/main/examples/Read_values_native/Read_values_native.ino" 
/>