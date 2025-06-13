---
slug: /apds-9960/arduino/proximity-sensor
title: Apds 9960 - Proximity Sensor
sidebar_label: Proximity Sensor
id: apds-9960-arduino-4
hide_title: false
---

This page contains simple examples of initialization and proximity detection with the APDS-9960 sensor.

---

## Proximity Sensor

In this code snippet, the `loop()` function continuously checks if a proximity reading is available from the APDS-9960 sensor using the `proximityAvailable()` function. If a reading is available, the `readProximity()` function is called to retrieve the proximity value.

To avoid constantly querying the sensor and overwhelming the Serial Monitor, the `delay(100)` function is used to pause for 100 milliseconds before the next reading is taken.

```cpp
void loop()
{
    // check if a proximity reading is available
    if (APDS.proximityAvailable())
    {

        int proximity = APDS.readProximity();

        // print value to the Serial Monitor
        Serial.println(proximity);
    }

    // wait a bit before reading again
    delay(100);
}
```

<FunctionDocumentation
  functionName="APDS.proximityAvailable()"
  description="Enables the proximity sensor and verifies the sensor's status."
  returnDescription="An integer: 1 if proximity data is available, 0 otherwise."
  parameters={[]}
/>

<FunctionDocumentation
  functionName="APDS.readProximity()"
  description="Reads the proximity data from the APDS9960 sensor and returns the proximity value after processing."
  returnDescription="An integer representing the processed proximity value. If an error occurs while retrieving the data, it returns -1. The proximity value is calculated as 255 - r, where r is the raw proximity data retrieved from the sensor."
  parameters={[]}
/>

| Integer | Proximity |
| :-----: | :-------: |
|    0    |   close   |
|   255   |    far    |
|   -1    |   error   |

---

## Full example

Open the Serial Monitor at 115200 baud to observe the detected proximity values.

```cpp
// Include the library
#include "APDS9960-SOLDERED.h"

// Create an APDS-9960 object
APDS_9960 APDS;

// Setup function that runs once
void setup()
{
    Serial.begin(115200); // Begin serial communication with PC
    while (!Serial) // Wait until serial becomes active
        ;

    if (!APDS.begin())  // Begin communication with sensor
    {
        Serial.println("Error initializing APDS-9960 sensor!");
        while(1); // Loop forever if sensor is not available
    }

    Serial.println("Sensor initialized.");
}
void loop()
{
    // check if a proximity reading is available
    if (APDS.proximityAvailable())
    {

        int proximity = APDS.readProximity();

        // print value to the Serial Monitor
        Serial.println(proximity);
    }

    // wait a bit before reading again
    delay(100);
}
```

<InfoBox>When reading open-air proximity, the sensor reaches the maximum value of 255.</InfoBox>

<CenteredImage src="/img/apds-9960/open_air_prox.png" alt="Serial Monitor" width="700px"/>
<CenteredImage src="/img/apds-9960/open_air_proximity.png" alt="Serial Monitor" caption="Proximity Sensor Serial Monitor output" width="700px"/>

<CenteredImage src="/img/apds-9960/hand_prox.png" alt="Serial Monitor" width="700px"/>
<CenteredImage src="/img/apds-9960/hand_proximity.png" alt="Serial Monitor" caption="Proximity Sensor Serial Monitor output" width="700px"/>

<QuickLink 
  title="ProximitySensor.ino" 
  description="Example file for using the APDS-9960 sensor with easyC/Qwiic/I2C"
  url="https://github.com/SolderedElectronics/Soldered-APDS9960-Light-Gesture-Color-Sensor-Arduino-Library/blob/main/examples/ProximitySensor/ProximitySensor.ino" 
/>