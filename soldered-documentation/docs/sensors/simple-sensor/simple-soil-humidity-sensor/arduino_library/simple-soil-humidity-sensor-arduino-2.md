---
slug: /simple-sensor/simple-soil-humidity-sensor/arduino_library/ragular-example
title: Measuring and detectiing humidity with regular sensor (example)
id: simple-soil-humidity-sensor-arduino-2
hide_title: False
---

This page contains a simple example with function documentation on how to detect and measure humidity of the soil using the sensor.

---

## Initialization
To use the sensor, first include the required library, create the sensor object (SimpleRainSensor), and initialize it in the `setup()` function. You can use the return value of `begin()` to check if everything is connected correctly.

```cpp
#include "Simple-soil-sensor-easyC-SOLDERED.h"
#define ANALOG_PIN 15

SimpleSoilSensor sensor(ANALOG_PIN);

void setup(){
  sensor.begin();
}
//...
```
<FunctionDocumentation
  functionName="SimpleSoilSensor sensor"
  description="Creates SimpleSoilSensor object"
  returnDescription="none"
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
#include "Simple-soil-sensor-easyC-SOLDERED.h"
#define ANALOG_PIN 15

SimpleSoilSensor sensor(ANALOG_PIN);

#define CALIBRATION_RESISTANCE_TIP_IN_WATER  15000
#define CALIBRATION_RESISTANCE_FULL_IN_WATER 7000


void setup(){
  Serial.begin(115200);

    // Initialize the sensor
    sensor.begin();

    // Sensor will work just fine if it is not calibrated
    // but since it is relying on resistance of water and
    // and water significantly changes resistance if it is
    // filled with particles, it smart idea to calibrate sometimes.
    // For calibration it is needed to measure resistance of sensor
    // when only tip is in water(about 5mm of sensor) and when
    // pads are completely in water and write them in
    // CALIBRATION_RESISTANCE_TIP_IN_WATER and CALIBRATION_RESISTANCE_FULL_IN_WATER
    sensor.calibrate(CALIBRATION_RESISTANCE_TIP_IN_WATER, CALIBRATION_RESISTANCE_FULL_IN_WATER);

    // If different microcontroller with different bit width
    // is used, it should be set using this function
    sensor.setADCWidth(12);
}

void loop(){
  Serial.print("Raw value of sensor: "); // Print information message
    Serial.print(sensor.getValue());       // Prints percent value of soil sensor
    Serial.print("% ");
    Serial.println(sensor.getRawValue()); // Prints raw value of soil sensor

    Serial.print("Resistance of sensor: "); // Print information message
    Serial.print(sensor.getResistance());   // Prints resistance of soil sensor
    Serial.println(" Ohms.");               // Print information message

    Serial.print("Humidity: ");         // Print information message
    Serial.print(sensor.getHumidity()); // Prints raw value of soil sensor
    Serial.println(" %.");              // Print information message

    // Wait a bit before next reading
    delay(500);
}
```
<FunctionDocumentation
  functionName="sensor.getValue()"
  description="Returns the percent value of the soil humidity sensor."
  returnDescription="Returns a float representation of the rain humidity sensor value in percentage."
/>
<FunctionDocumentation
  functionName="sensor.getRawValue()"
  description="Returns the raw ADC value."
  returnDescription="Returns an integer representation of the rain sensor value."
/>
<FunctionDocumentation
  functionName="sensor.getResistance()"
  description="Returns the calculated resistance."
  returnDescription="Returns a float representation of the rain sensor resistance."
/>
<FunctionDocumentation
  functionName="sensor.getHumidity()"
  description="Returns the percent value of the soil humidity."
  returnDescription="Returns a float representation of the soil humidity in percentage."
/>

<CenteredImage src="/img/simple-sensor/simple-soil-humidity-sensor/water_not_detected.png" alt="Sensor when water is not present" caption="Sensor when water is not present" width="700px" />

<CenteredImage src="/img/simple-sensor/simple-soil-humidity-sensor/water_not_detected_serial.jpg" alt="Serial Monitor output" caption="Serial Monitor output" width="700px" />

<CenteredImage src="/img/simple-sensor/simple-soil-humidity-sensor/water_detected.png" alt="Sensor when rain is present" caption="Sensor when rain is present" width="700px" />

<CenteredImage src="/img/simple-sensor/simple-soil-humidity-sensor/water_detected_serial.jpg" alt="Serial Monitor output" caption="Serial Monitor output" width="700px" />

---

## Full example
Try all of the functions mentioned above in the full example below:

<QuickLink 
  title="Read_values_native.ino" 
  description="Example for using the digital and analog read functions for Simple soil humidity sensor."
  url="https://github.com/SolderedElectronics/Soldered-Simple-Soil-Humidity-Sensor-Arduino-Library/blob/main/examples/Read_values_native/Read_values_native.ino" 
/>