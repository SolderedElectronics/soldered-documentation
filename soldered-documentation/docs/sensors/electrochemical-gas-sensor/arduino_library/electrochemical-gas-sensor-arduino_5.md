---
slug: /electrochemical-gas-sensor/arduino/reading-from-multiple-sensors
title: Electrochemical Gas Sensors – Reading from multiple sensors
id: electrochemical-gas-sensor-arduino-5 
hide_title: False
---

In this example, we demonstrate how to read from multiple sensors over I2C. 


First, include the library and create the sensor objects by providing the configuration, the I2C address of the ADS1115, and the GPIO pin connected to the LMPEN pin on the breakout board:

```cpp
// Include the required library
#include "Electrochemical-Gas-Sensor-SOLDERED.h"

// Create two different sensor objects
// Through the constructor, give them the configuration, 
// ADC I2C address and GPIO pin connected to the LMPEN pin
ElectrochemicalGasSensor sensorCO(SENSOR_CO, 0x4A, 25);
ElectrochemicalGasSensor sensorNO2(SENSOR_NO2, 0x49, 32);
```
<InfoBox>We can change the I2C address of the ADS1115 ADC module by shorting jumpers on the breakout board. For more information on the jumpers look [**here**](/documentation/electrochemical-gas-sensor/hardware/#jumper-details)</InfoBox>

<InfoBox>While the LMP91000 has a non-configurable I2C address, we can distinguish them by setting the **LMPEN pin**. When we want to configure a specific one, we can disable all the others by setting their LMPEN pin to HIGH via the GPIO pins while the one we want to configure stays at a HIGH state. More information about this can be found [**here**](/documentation/electrochemical-gas-sensor/hardware/#lmpen-pin-functionality)</InfoBox>

Next, in the `setup()` function, both sensors are initialized, along with the serial communication:

```cpp
void setup()
{
    Serial.begin(115200); // For debugging

    // Init breakout #1
    if (!sensorCO.begin())
    {
        // Can't init? Notify the user and go to infinite loop
        Serial.println("ERROR: Can't init the sensor! Check connections!");
        while (true)
            delay(100);
    }

    Serial.println("CO sensor initialized successfully!");

    // Init breakout #2
    if (!sensorNO2.begin())
    {
        // Can't init? Notify the user and go to infinite loop
        Serial.println("ERROR: Can't init the sensor! Check connections!");
        while (true)
            delay(100);
    }

    Serial.println("NO2 sensor initialized successfully!");
}
```

<FunctionDocumentation
  functionName="sensor.begin()"
  description="Initializes the LMP91000 and ADS1115 on the board and establishes an I2C connection"
  returnDescription="Boolean value, returns true if it was successful, false if it failed"
  parameters={[]}
/>

---

## Getting readings

Finally, in the `loop()` function, we print the gas readings to the serial monitor:

```cpp
void loop()
{
    // Make the reading of CO and print it
    double COreading = sensorCO.getPPM();

    // Print the reading with 5 digits of precision
    Serial.print("CO sensor reading: ");
    Serial.print(COreading, 5);
    Serial.println(" PPM");

    // Make the reading of NO2 and print it
    double NO2reading = sensorNO2.getPPB();

    // Print the reading with 5 digits of precision
    Serial.print("NO2 sensor reading: ");
    Serial.print(NO2reading, 5);
    Serial.println(" PPB");

    // Wait a bit before reading again
    delay(2500);
}
```

<FunctionDocumentation
  functionName="sensorCO.getPPM()"
  description="Make a measurement with the ADS1115 ADC and calculate the PPM value of the measured gas"
  returnDescription="Double value, gas measurement in PPM (parts per million)"
  parameters={[]}
/>

<FunctionDocumentation
  functionName="sensorNO2.getPPB()"
  description="Make a measurement with the ADS1115 ADC and calculate the PPB value of the measured gas"
  returnDescription="Double value, gas measurement in PPB (parts per billion)"
  parameters={[]}
/>

---

## Full example

See the full example here:

<QuickLink  
  title="Measuring two sensors"  
  description="Example of getting measurements from two sensors"  
  url="https://github.com/SolderedElectronics/Soldered-Electrochemical-Gas-Sensor-Arduino-Library/blob/main/examples/twoSensors/twoSensors.ino"  
/>  

```cpp
// Include the required library
#include "Electrochemical-Gas-Sensor-SOLDERED.h"

// Create two different sensor objects
// Through the constructor, give them the configuration, 
// ADC I2C address and GPIO pin connected to the LMPEN pin
ElectrochemicalGasSensor sensorCO(SENSOR_CO, 0x4A, 25);
ElectrochemicalGasSensor sensorNO2(SENSOR_NO2, 0x49, 32);

void setup()
{
    Serial.begin(115200); // For debugging

    // Init breakout #1
    if (!sensorCO.begin())
    {
        // Can't init? Notify the user and go to infinite loop
        Serial.println("ERROR: Can't init the sensor! Check connections!");
        while (true)
            delay(100);
    }

    Serial.println("CO sensor initialized successfully!");

    // Init breakout #2
    if (!sensorNO2.begin())
    {
        // Can't init? Notify the user and go to infinite loop
        Serial.println("ERROR: Can't init the sensor! Check connections!");
        while (true)
            delay(100);
    }

    Serial.println("NO2 sensor initialized successfully!");
}

void loop()
{
    // Make the reading of CO and print it
    double COreading = sensorCO.getPPM();

    // Print the reading with 5 digits of precision
    Serial.print("CO sensor reading: ");
    Serial.print(COreading, 5);
    Serial.println(" PPM");

    // Make the reading of NO2 and print it
    double NO2reading = sensorNO2.getPPB();

    // Print the reading with 5 digits of precision
    Serial.print("NO2 sensor reading: ");
    Serial.print(NO2reading, 5);
    Serial.println(" PPB");

    // Wait a bit before reading again
    delay(2500);
}
```