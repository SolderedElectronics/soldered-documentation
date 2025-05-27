---
slug: /simple-sensor/simple-rain-sensor/arduino_library/qwiic-example
title: "Simple Rain Sensor \u2013 Library Qwiic example"
id: simple-rain-sensor-arduino-3
hide_title: false
---
This page contains a simple example with function documentation on how to detect and measure moisture using the sensor.

---

## Initialization
To use the sensor, first include the required library, create the sensor object (SimpleRainSensor), and initialize it in the `setup()` function. You can use the return value of `begin()` to check if everything is connected correctly.

```cpp
#include "Simple-rain-sensor-easyC-SOLDERED.h"

SimpleRainSensor sensor;

void setup(){
  sensor.begin();
}
//...
```
<FunctionDocumentation
  functionName="SimpleRainSensor sensor"
  description="Creates SimpleRainSensor object"
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
#include "Simple-rain-sensor-easyC-SOLDERED.h"

SimpleRainSensor sensor;

#define CALIBRATION_VALUE_ON_DRY 1024
void setup(){
  // Initialize the serial communication via UART
  Serial.begin(115200);

  // Initialize the sensor
  // Start I2C communication on default address (0x30)
  sensor.begin();
  sensor.calibrate(CALIBRATION_VALUE_ON_DRY);

  // Set threshold for LED on the breakout by raw value
  // sensor.setRawThreshold(400); // or percentage:
  sensor.setThreshold(90); // 25.1%
  // If the sensor reads a value smaller than this, it means rain is detected

  // If you want the LED to turn OFF when rain is detected, use:
  // sensor.invertLED(true);
  // Usually, it's ON while rain is detected
}

void loop(){
  Serial.print("Rain reading from the sensor: ");
  Serial.print(sensor.getValue()); // Prints percent value of rain sensor
  Serial.print("%, and the raw value: ");
  Serial.println(sensor.getRawValue()); // Prints raw value of rain sensor

  Serial.print("Resistance of sensor: ");
  Serial.print(sensor.getResistance()); // Prints resistance of rain sensor
  Serial.println(" Ohms.");

  Serial.print("The set threshold is: ");
  Serial.print(sensor.getThreshold());
  Serial.println("%");

  // Detect if it's raining or not
  // And print information accordingly
  if (sensor.isRaining())
  {
    Serial.println("Rain is detected");
  }
  else
  {
    Serial.println("Rain is not detected");
  }
  Serial.println();

  // Wait a bit before next reading
  delay(1000);
}
```
<FunctionDocumentation
  functionName="sensor.getValue()"
  description="Returns the percent value of the rain sensor."
  returnDescription="Returns a float representation of the rain sensor value in percentage."
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

<CenteredImage src="/img/simple-sensor/simple-rain-sensor/rain_not_detected_qwiic.png" alt="Sensor when rain is not present" caption="Sensor when rain is not present" width="700px" />

<CenteredImage src="/img/simple-sensor/simple-rain-sensor/rain_not_detected_qwiic_serial.jpg" alt="Serial Monitor output" caption="Serial Monitor output" width="700px" />

<CenteredImage src="/img/simple-sensor/simple-rain-sensor/rain_detected_qwiic.png" alt="Sensor when rain is present" caption="Sensor when rain is present" width="700px" />

<CenteredImage src="/img/simple-sensor/simple-rain-sensor/rain_detected_qwiic_serial.jpg" alt="Serial Monitor output" caption="Serial Monitor output" width="700px" />

---

## Full example
Try all of the functions mentioned above in the full example below:

<QuickLink 
  title="Read_values_easyC.ino" 
  description="Example for using the digital and analog read functions for the simple rain sensor with Qwiic."
  url="https://github.com/SolderedElectronics/Soldered-Simple-Rain-Sensor-Arduino-Library/blob/main/examples/Read_values_easyC/Read_values_easyC.ino" 
/>