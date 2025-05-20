---
slug: /simple-sensor/simple-fire-sensor/arduino_library/regular-example
title: Simple Sensor - Detecting and maesuring fire with regular fire sensor (example)
id: simple-fire-sensor-arduino-2
hide_title: false
---
This page contains a simple example with function documentation on how to detect and measure intensity of fire with the sensor.

---

## Initialization
To use the sensor, first include the required library, create the sensor object and SimpleFireSensor object, and initialize it in the `setup()` function. You can use the return value of `begin()` to check if everything is connected correctly.

```cpp
#include "Simple-fire-sensor-easyC-SOLDERED.h"

#define ANALOG_PIN 14
#define DIGITAL_PIN 15

SimpleFireSensor sensor(ANALOG_PIN);
void setup() {
  sensor.begin();
}
//...
```
<FunctionDocumentation
  functionName="SimpleFireSensor sensor()"
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
In this library, there are two options for displaying the analog value: for a percentage value, call the `getValue()` function, and for the raw value, call the `getRawValue()` function.

```cpp
#include "Simple-fire-sensor-easyC-SOLDERED.h"

#define ANALOG_PIN 14
#define DIGITAL_PIN 15

SimpleFireSensor sensor(ANALOG_PIN);
void setup() {
  Serial.begin(115200);
  sensor.begin();
}

void loop() {
  Serial.print("IR light sensor reading: "); // Print information message
  Serial.print(sensor.getValue());           // Prints percentage value of fire sensor
  Serial.print("% ");
  Serial.println(sensor.getRawValue());        // Prints raw value of fire sensor

  if (digitalRead(DIGITAL_PIN)) // Potentiometer on breakout board is used to
                                // set threshold value. This function checks if
                                // the threshold value is passed and determines if there
                                // is a fire nearby.
  {
      Serial.println("Fire is not detected.");
  }

  else
  {
      Serial.println("Fire is detected!!");
  }

  // You can also use thresholds (except threshold for LED) like in the Read_values_easyC example to detect fire.

  // Wait a bit before the next reading
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

<CenteredImage src="/img/simple-sensor/simple-fire-sensor/fire_not_detected.png" alt="Sensor when fire is not present" caption="Sensor when fire is not present" width="700px" />

<CenteredImage src="/img/simple-sensor/simple-fire-sensor/fire_not_detected_serial.jpg" alt="Serial Monitor output" caption="Serial Monitor output" width="700px" />

<CenteredImage src="/img/simple-sensor/simple-fire-sensor/fire_detected.png" alt="Sensor when fire is present" caption="Sensor when fire is present" width="700px" />

<CenteredImage src="/img/simple-sensor/simple-fire-sensor/fire_detected_serial.jpg" alt="Serial Monitor output" caption="Serial Monitor output" width="700px" />

---

## Full example

Try all of the functions mentioned above in the full example below:

<QuickLink 
  title="Read_values_native.ino" 
  description="Example for using the digital and analog read functions for Simple fire sensor."
  url="https://github.com/SolderedElectronics/Soldered-Simple-Fire-Sensor-Arduino-library/blob/main/examples/Read_values_native/Read_values_native.ino" 
/>