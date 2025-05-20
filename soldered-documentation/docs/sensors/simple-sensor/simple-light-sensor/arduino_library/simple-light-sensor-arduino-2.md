---
slug: /simple-sensor/simple-light-sensor/arduino_library/regular-example
title: Simple Sensor - Detecting and measuring light with regular light sensor (example)
id: simple-light-sensor-arduino-2
hide_title: false
---
This page contains a simple example with function documentation on how to detect and measure intensity of present light with the sensor.

---

## initialization
To use the sensor, first include the required library, create the sensor object and SimpleFireSensor object, and initialize it in the `setup()` function. You can use the return value of `begin()` to check if everything is connected correctly.

```cpp
#include "Simple-light-sensor-easyC-SOLDERED.h"

#define ANALOG_PIN
#define DIGITAL_PIN

SimpleLightSensor sensor(ANALOG_PIN);

void setup(){
  sensor.begin();
}
//...
```
<FunctionDocumentation
  functionName="SimpleLightSensor sensor()"
  description="Creates SimpleLightSensor object"
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
In this library, there are two options for displaying the analog value: for a percentage value, call the `getResistance()` function, and for the raw value, call the `getLux()` function.

```cpp
#include "Simple-light-sensor-easyC-SOLDERED.h"

#define ANALOG_PIN 14
#define DIGITAL_PIN 15

SimpleLightSensor sensor(ANALOG_PIN);

void setup(){
    Serial.begin(115200);
    sensor.begin();
}

void loop(){
  Serial.print("Resistance of a LDR: "); // Print information message
    Serial.print(sensor.getResistance());  // Prints percent value of light sensor
    Serial.println(" Ohms.");              // Print information message

    Serial.print("Light intensity: "); // Print information message
    Serial.print(sensor.getLux());     // Prints raw value of light sensor
    Serial.println(" lux.");           // Print information message

    // You can adjust treshold light intesity using potentiometer on breakout board
    Serial.println(digitalRead(DIGITAL_PIN) ? "Treshold light intesity is past." : "Treshold intensity is not past.");

    // Wait a bit before next reading
    delay(500);
}
```

<FunctionDocumentation
  functionName="sensor.getResistance()"
  description="Returns the measurement in percentage."
  returnDescription="Returns float representation of fire chance percentage."
/>

<FunctionDocumentation
  functionName="sensor.getLux()"
  description="Returns the raw ADC value."
  returnDescription="Returns integer representation of fire value"
/>
<CenteredImage src="/img/simple-sensor/simple-light-sensor/light_not_detected.png" alt="Sensor when light is not present" caption="Sensor when light is not present" width="700px" />

<CenteredImage src="/img/simple-sensor/simple-light-sensor/light_not_detected_serial.jpg" alt="Serial Monitor output" caption="Serial Monitor output" width="700px" />

<CenteredImage src="/img/simple-sensor/simple-light-sensor/light_detected.png" alt="Sensor when light is present" caption="Sensor when light is present" width="700px" />

<CenteredImage src="/img/simple-sensor/simple-light-sensor/light_detected_serial.jpg" alt="Serial Monitor output" caption="Serial Monitor output" width="700px" />

---

## Full example
Try all of the functions mentioned above in the full example below:

<QuickLink 
  title="Read_values_native.ino" 
  description="Example for using the digital and analog read functions for Simple light sensor."
  url="https://github.com/SolderedElectronics/Soldered-Simple-Light-Sensor-Arduino-Library/blob/main/examples/Read_values_native/Read_values_native.ino" 
/>