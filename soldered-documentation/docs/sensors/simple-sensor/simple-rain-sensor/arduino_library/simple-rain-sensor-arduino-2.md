---
slug: /simple-sensor/simple-rain-sensor/arduino_library/regular-example
title: Simple Sensor - Measuring and detecting moisture with regular rain sensor (example)
id: simple-rain-sensor-arduino-2
hide_title: false
---
This page contains a simple example with function documentation on how to detect and measure the intensity of the present light using the sensor.

---

## Initialization
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
  functionName="SimpleRainSensor sensor()"
  description="Creates SimplerainSensor object"
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
#include "Simple-rain-sensor-easyC-SOLDERED.h"

// Connecting diagram
// Breakout      Arduino

// |-------------|
// D0------------9
// A0------------A0
// GND-----------GND
// VCC-----------5V

// Define your pins
#define ANALOG_PIN  14
#define DIGITAL_PIN 15

// Declare the sensor object and specify the pin to which the sensor is connected
SimpleRainSensor sensor(ANALOG_PIN);

void setup()
{
    // Initialize the serial communication via UART
    Serial.begin(115200);

    // Initialize the sensor
    sensor.begin();
    sensor.setADCWidth(12);
    // You can use a potentiometer on the breakout board to set the threshold to sense rain.
    pinMode(DIGITAL_PIN, INPUT_PULLUP);
}

void loop()
{
    Serial.print("Raw value of sensor: "); // Print information message
    Serial.print(sensor.getValue());       // Prints percent value of rain sensor
    Serial.print("% ");
    Serial.println(sensor.getRawValue());    // Prints raw value of rain sensor

    Serial.print("Resistance of sensor: "); // Print information message
    Serial.print(sensor.getResistance());    // Prints resistance of rain sensor
    Serial.println(" Ohms.");                // Print information message
    if (digitalRead(DIGITAL_PIN))
    {
        Serial.println("Rain is not detected");
    }
    else
    {
        Serial.println("Rain is detected");
    }
    Serial.println();

    // Wait a bit before next reading
    delay(500);
}
```

<FunctionDocumentation
  functionName="sensor.setADCWidth()"
  description="Sets the ADC resolution for used MCU."
  returnDescription="None"
  parameters={[
    { type: 'uint8_t', name: 'resolution', description: "ADC resolution" }
  ]}
/>
<FunctionDocumentation
  functionName="sensor.getValue()"
  description="Returns the percent value of rain sensor."
  returnDescription="Returns float representation of rain sensor value in percentage."
/>
<FunctionDocumentation
  functionName="sensor.getRawValue()"
  description="Returns the raw ADC value."
  returnDescription="Returns integer representation of rain value."
/>
<FunctionDocumentation
  functionName="sensor.getResistance()"
  description="Returns the calculated resistance."
  returnDescription="Returns float representation of rain sensor resistance."
/>

<CenteredImage src="/img/simple-sensor/simple-rain-sensor/rain_not_detected.png" alt="Sensor when rain is not present" caption="Sensor when rain is not present" width="700px" />

<CenteredImage src="/img/simple-sensor/simple-rain-sensor/rain_not_detected_serial.jpg" alt="Serial Monitor output" caption="Serial Monitor output" width="700px" />

<CenteredImage src="/img/simple-sensor/simple-rain-sensor/rain_detected.png" alt="Sensor when rain is present" caption="Sensor when rain is present" width="700px" />

<CenteredImage src="/img/simple-sensor/simple-rain-sensor/rain_detected_serial.jpg" alt="Serial Monitor output" caption="Serial Monitor output" width="700px" />

---

## Full example
Try all of the functions mentioned above in the full example below:

<QuickLink 
  title="Read_values_native.ino" 
  description="Example for using the digital and analog read functions for the simple rain sensor."
  url="https://github.com/SolderedElectronics/Soldered-Simple-Light-Sensor-Arduino-Library/blob/main/examples/Read_values_native/Read_values_native.ino" 
/>