---
slug: /simple-sensor/simple-soil-humidity-sensor/arduino_library/qwiic-example
title: Measuring and detectiing humidity with regular sensor (example)
id: simple-soil-humidity-sensor-arduino-3
hide_title: False
---
This page contains a simple example with function documentation on how to detect and measure humidity of the soil using the sensor.

---

## Initialization
To use the sensor, first include the required library, create the sensor object (SimpleRainSensor), and initialize it in the `setup()` function. You can use the return value of `begin()` to check if everything is connected correctly.

```cpp
#include "Simple-soil-sensor-easyC-SOLDERED.h"

SimpleSoilSensor sensor;

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

#define CALIBRATION_RESISTANCE_TIP_IN_WATER  30000
#define CALIBRATION_RESISTANCE_FULL_IN_WATER 10000

// Declare the sensor object
SimpleSoilSensor sensor;

void setup()
{
    // Initialize the serial communication via UART
    Serial.begin(115200);

    // Initialize the sensor
    // Start I2C communication on default address (0x30)
    sensor.begin();

    sensor.calibrate(CALIBRATION_RESISTANCE_TIP_IN_WATER, CALIBRATION_RESISTANCE_FULL_IN_WATER);
}

void loop()
{
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
    delay(200);
}
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

<CenteredImage src="/img/simple-sensor/simple-soil-humidity-sensor/water_not_detected_qwiic.png" alt="Sensor when water is not present" caption="Sensor when water is not present" width="700px" />

<CenteredImage src="/img/simple-sensor/simple-soil-humidity-sensor/water_not_detected_qwiic_serial.jpg" alt="Serial Monitor output" caption="Serial Monitor output" width="700px" />

<CenteredImage src="/img/simple-sensor/simple-soil-humidity-sensor/water_detected_qwiic.png" alt="Sensor when rain is present" caption="Sensor when rain is present" width="700px" />

<CenteredImage src="/img/simple-sensor/simple-soil-humidity-sensor/water_detected_qwiic_serial.jpg" alt="Serial Monitor output" caption="Serial Monitor output" width="700px" />

---

## Full example
Try all of the functions mentioned above in the full example below:

<QuickLink 
  title="Read_values_easyC.ino" 
  description="Example for using the digital and analog read functions for Simple soil humidity sensor with Qwiic."
  url="https://github.com/SolderedElectronics/Soldered-Simple-Soil-Humidity-Sensor-Arduino-Library/blob/main/examples/Read_values_native/Read_values_native.ino" 
/>