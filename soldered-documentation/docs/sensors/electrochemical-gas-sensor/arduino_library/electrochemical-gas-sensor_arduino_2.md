---
slug: /electrochemical-gas-sensor/arduino/single-sensor-measurement-example
title: Electrochemical Gas Sensors – Single sensor measurement example
sidebar_label: Single sensor measurement example
id: electrochemical-gas-sensor-arduino-2 
hide_title: False
---

## Connections for this example

<CenteredImage src="/img/electrochemical-gas-sensor/connections1.png" />

<InfoBox>

When using a single sensor, make sure to connect the **LMPEN** pin to the **GND** pin on the board. This ensures that the pin is set to LOW and that the LMP91000 is always enabled. For more information, look [**here**](/documentation/electrochemical-gas-sensor/hardware/#lmpen-pin-functionality).

</InfoBox>

---

## Initializing the sensor

To initialize the sensor, we must first include the library and create an instance of the sensor object with a configuration for the appropriate type (for this example, we are using an ammonia sensor). You can find all of the pre-defined configurations [**here**](https://github.com/SolderedElectronics/Soldered-Electrochemical-Gas-Sensor-Arduino-Library/blob/main/src/sensorConfigData.h).

```cpp
// Include the library
#include "Electrochemical-Gas-Sensor-SOLDERED.h"

// Create the sensor object with the according type
ElectrochemicalGasSensor sensor(SENSOR_NH3);
```

Next, in the `setup()` function, we initialize the serial communication as well as the breakout board itself:

```cpp
void setup()
{
    // Initialize serial communication
    Serial.begin(115200); 

    // Initialize the breakout
    if (!sensor.begin())
    {
        // Can't initialize? Notify the user and enter an infinite loop
        Serial.println("ERROR: Can't init the sensor! Check connections!");
        while (true)
            delay(100);
    }

    Serial.println("Sensor initialized successfully!");
}
```

<FunctionDocumentation
  functionName="sensor.begin()"
  description="Initializes the LMP91000 and ADS1115 on the board and establishes an I2C connection"
  returnDescription="Boolean value, returns true if it was successful, false if it failed"
  parameters={[]}
/>

---

## Taking a measurement

Finally, in the `loop()` function, we get the reading from the breakout board and print it to serial:

```cpp
void loop()
{
    // Make the reading
    double reading = sensor.getPPM();

    // Print the reading with 5 digits of precision
    Serial.print("Sensor reading: ");
    Serial.print(reading, 5);
    Serial.println(" PPM");

    // Wait a bit before reading again
    delay(2500);
}
```

<CenteredImage src="/img/electrochemical-gas-sensor/reading_one.png" alt="Serial monitor" caption="Serial monitor"/>

<FunctionDocumentation
  functionName="sensor.getPPM()"
  description="Makes a measurement with the ADS1115 ADC and calculates the PPM value of the measured gas"
  returnDescription="Double value, gas measurement in PPM (parts per million)"
  parameters={[]}
/>

<FunctionDocumentation
  functionName="sensor.getPPB()"
  description="Make a measurement with the ADS1115 ADC and calculate the PPB value of the measured gas"
  returnDescription="Double value, gas measurement in PPB (parts per billion)"
  parameters={[]}
/>

---

## Full example

See the full example here:

```cpp
// Include the required library
#include "Electrochemical-Gas-Sensor-SOLDERED.h"

// Create the sensor object with the according type
ElectrochemicalGasSensor sensor(SENSOR_NH3);

void setup()
{
    Serial.begin(115200); // For debugging

    // Initialize the breakout
    if (!sensor.begin())
    {
        // Can't initialize? Notify the user and enter an infinite loop
        Serial.println("ERROR: Can't init the sensor! Check connections!");
        while (true)
            delay(100);
    }

    Serial.println("Sensor initialized successfully!");
}

void loop()
{
    // Make the reading
    double reading = sensor.getPPM();

    // Print the reading with 5 digits of precision
    Serial.print("Sensor reading: ");
    Serial.print(reading, 5);
    Serial.println(" PPM");

    // Wait a bit before reading again
    delay(2500);
}
```