---
slug: /apds-9960/arduino/initialization-and-gesture-detection
title: Gesture Detection
id: apds-9960-arduino-2 
hide_title: False
---

This page contains simple examples of initialization and gesture detection with the APDS-9960 sensor.

---

## Initialization

To use the APDS-9960 sensor, first, include the required library, create the sensor object and initialize the sensor in the `setup()` function. You can use the return of `begin()` to check if everything is connected correctly:

```cpp
// Include the library
#include "APDS9960-SOLDERED.h"

// Create an APDS-9960 object
APDS_9960 APDS;

// Setup function, runs once
void setup()
{
    Serial.begin(115200); //Begin serial communication with PC
    while (!Serial) //Wait until serial becomes active
        ;

    if (!APDS.begin())  //Begin communication with sensor
    {
        Serial.println("Error initializing APDS-9960 sensor!");
      while(1); //Loop forever if sensor is not available
    }

    Serial.println("Sensor initialized.");
}

// ...
```

<FunctionDocumentation
  functionName="APDS.begin()"
  description="Initializes the APDS-9960 sensor, setting up communication over I2C and verifying its presence."
  returnDescription="True if initialization is successful, false otherwise."
  parameters={[]}
/>

---

## Gesture Detection

```cpp
void loop()
{
    if (APDS.gestureAvailable())
    {
        // a gesture was detected, read and print to Serial Monitor
        int gesture = APDS.readGesture();

        switch (gesture)  //Determine which gesture was captured
        {
        case GESTURE_UP:
            Serial.println("Detected UP gesture");
            break;

        case GESTURE_DOWN:
            Serial.println("Detected DOWN gesture");
            break;

        case GESTURE_LEFT:
            Serial.println("Detected LEFT gesture");
            break;

        case GESTURE_RIGHT:
            Serial.println("Detected RIGHT gesture");
            break;

        default:
            // ignore
            break;
        }
    }
}
```

<FunctionDocumentation
  functionName="APDS.gestureAvailable()"
  description="Checks if there is a detected gesture."
  returnDescription="True if a gesture is detected, false otherwise."
  parameters={[]}
/>

<FunctionDocumentation
  functionName="APDS.readGesture()"
  description="Reads the detected gesture."
  returnDescription="An integer corresponding to a detected gesture."
  parameters={[]}
/>

| Integer |    Gesture    |
| :-----: | :-----------: |
|   -1    | GESTURE_NONE  |
|    0    |  GESTURE_UP   |
|    1    | GESTURE_DOWN  |
|    2    | GESTURE_LEFT  |
|    3    | GESTURE_RIGHT |
---

## Full example

Open the Serial Monitor at 115200 baud to observe detected gestures.

```cpp
// Include the library
#include "APDS9960-SOLDERED.h"

// Create an APDS-9960 object
APDS_9960 APDS;

// Setup function, runs once
void setup()
{
    Serial.begin(115200); //Begin serial communication with PC
    while (!Serial) //Wait until serial becomes active
        ;

    if (!APDS.begin())  //Begin communication with sensor
    {
        Serial.println("Error initializing APDS-9960 sensor!");
      while(1); //Loop forever if sensor is not available
    }

    Serial.println("Sensor initialized.");
}

void loop()
{
    if (APDS.gestureAvailable())
    {
        // a gesture was detected, read and print to Serial Monitor
        int gesture = APDS.readGesture();

        switch (gesture)  //Determine which gesture was captured
        {
        case GESTURE_UP:
            Serial.println("Detected UP gesture");
            break;

        case GESTURE_DOWN:
            Serial.println("Detected DOWN gesture");
            break;

        case GESTURE_LEFT:
            Serial.println("Detected LEFT gesture");
            break;

        case GESTURE_RIGHT:
            Serial.println("Detected RIGHT gesture");
            break;

        default:
            // ignore
            break;
        }
    }
}
```

<QuickLink 
  title="GestureSensor.ino" 
  description="Example file for using the APDS-9960 sensor with easyC/Qwiic/I2C"
  url="https://github.com/SolderedElectronics/Soldered-APDS9960-Light-Gesture-Color-Sensor-Arduino-Library/blob/main/examples/GestureSensor/GestureSensor.ino" 
/>
