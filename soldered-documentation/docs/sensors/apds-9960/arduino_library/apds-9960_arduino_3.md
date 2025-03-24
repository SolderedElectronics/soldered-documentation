---
slug: /apds-9960/arduino/gesture-detection
title: Gesture Detection
id: apds-9960-arduino-3
hide_title: False
---

This page contains simple examples of initialization and gesture detection with the APDS-9960 sensor.

---

## Gesture Detection

In this code snippet, the `loop()` function continuously checks if a gesture has been detected by the APDS-9960 sensor. The `gestureAvailable()` function is used to determine if a gesture is ready to be read. If a gesture is detected, the `readGesture()` function is called to retrieve the gesture.

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
  description="Enables the gesture sensor and checks if a gesture is available for reading."
  returnDescription="An integer: 1 if a gesture was detected, 0 otherwise."
  parameters={[]}
/>

<FunctionDocumentation
  functionName="APDS.readGesture()"
  description="Reads the detected gesture."
  returnDescription="An integer corresponding to a detected gesture (check table below)."
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

<CenteredImage src="/img/apds-9960/apds9960_gesture.png" alt="Serial Monitor" caption="Gesture Detection Serial Monitor output"/>

<QuickLink 
  title="GestureSensor.ino" 
  description="Example file for using the APDS-9960 sensor with easyC/Qwiic/I2C"
  url="https://github.com/SolderedElectronics/Soldered-APDS9960-Light-Gesture-Color-Sensor-Arduino-Library/blob/main/examples/GestureSensor/GestureSensor.ino" 
/>
