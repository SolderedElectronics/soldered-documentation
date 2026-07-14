---
slug: /neo-m9n-00b/arduino/geofence
title: NEO-M9N-00B - Geofence
sidebar_label: Geofence
id: neo-m9n-00b-arduino-4
hide_title: False
---

This page contains an example of setting up geofences around the module's current position and monitoring whether it's still inside them. The module supports up to **4 concentric geofences**, each with its own radius and confidence level.

---

## Initialization

Include the required libraries, create the module object, and define which pin drives an LED to show the geofence state:

```cpp
#define LED LED_BUILTIN // Change this if your board's LED is on a different pin

#include <Wire.h>
#include <Soldered-GNSS.h>

Soldered_GNSS myGNSS;
```

In the `setup()` function, wait for a 3D fix, then define four geofences (5 m, 10 m, 15 m, and 20 m radius) centered on the current position:

```cpp
void setup()
{
    pinMode(LED, OUTPUT);

    Wire.begin();

    Serial.begin(115200);
    while (!Serial);
    Serial.println(F("NEO-M9N-00B geofence example"));

    if (myGNSS.begin() == false)
    {
        Serial.println(F("u-blox GNSS not detected at default I2C address. Please check wiring. Freezing."));
        while (1);
    }

    myGNSS.setI2COutput(COM_TYPE_UBX);

    Serial.println(F("Waiting for a 3D fix..."));

    byte fixType = 0;
    while (fixType < 3)
    {
        fixType = myGNSS.getFixType();
        Serial.print(F("Fix: "));
        Serial.println(fixType);
        delay(1000);
    }

    Serial.println(F("3D fix found!"));

    long latitude = myGNSS.getLatitude();
    long longitude = myGNSS.getLongitude();

    myGNSS.clearGeofences(); // Clear any existing geofences first

    byte confidence = 2; // 0 = none, 1 = 68%, 2 = 95%, 3 = 99.7%, 4 = 99.99%

    myGNSS.addGeofence(latitude, longitude, 500, confidence);  // 5 m radius (radius is in cm)
    myGNSS.addGeofence(latitude, longitude, 1000, confidence); // 10 m radius
    myGNSS.addGeofence(latitude, longitude, 1500, confidence); // 15 m radius
    myGNSS.addGeofence(latitude, longitude, 2000, confidence); // 20 m radius
}
```

<FunctionDocumentation
  functionName="myGNSS.getFixType()"
  description="Reads the current GNSS fix type"
  returnDescription="Byte value: 0 = no fix, 1 = dead reckoning, 2 = 2D, 3 = 3D, 4 = GNSS + dead reckoning, 5 = time only"
  parameters={[]}
/>

<FunctionDocumentation
  functionName="myGNSS.clearGeofences()"
  description="Removes all currently configured geofences from the module"
  returnDescription="Boolean value, true if successful, false for error"
  parameters={[]}
/>

<FunctionDocumentation
  functionName="myGNSS.addGeofence()"
  description="Adds a circular geofence around a given coordinate. Up to 4 geofences can be active at once"
  returnDescription="Boolean value, true if successful, false for error"
  parameters={[
  { type: 'int32_t', name: 'latitude', description: "Latitude of the geofence center, in degrees * 10^-7" },
  { type: 'int32_t', name: 'longitude', description: "Longitude of the geofence center, in degrees * 10^-7" },
  { type: 'uint32_t', name: 'radius', description: "Radius of the geofence, in centimeters" },
  { type: 'byte', name: 'confidence', description: "Confidence level: 0 = none, 1 = 68%, 2 = 95%, 3 = 99.7%, 4 = 99.99%" },
  ]}
/>

---

## Monitoring the geofence state

In the `loop()` function, the combined geofence state is checked once per second. The LED lights up while the module is inside the outermost (combined) geofence:

```cpp
void loop()
{
    geofenceState currentGeofenceState;

    if (myGNSS.getGeofenceState(currentGeofenceState) == false)
    {
        return;
    }

    Serial.print(F("Combined state: "));
    Serial.print(currentGeofenceState.combState);

    if (currentGeofenceState.combState == 1)
    {
        Serial.println(F(" (Inside)"));
        digitalWrite(LED, HIGH);
    }
    else if (currentGeofenceState.combState == 2)
    {
        Serial.println(F(" (Outside)"));
        digitalWrite(LED, LOW);
    }
    else
    {
        Serial.println(F(" (Unknown)"));
        digitalWrite(LED, LOW);
    }

    delay(1000);
}
```

<CenteredImage src="/img/neo-m9n-00b/geofence.png" alt="Serial monitor geofence readings" caption="Serial monitor" width="100%" />

<FunctionDocumentation
  functionName="myGNSS.getGeofenceState()"
  description="Reads the current state of all configured geofences into the provided struct"
  returnDescription="Boolean value, true if successful, false for error"
  parameters={[
  { type: 'geofenceState &', name: 'currentGeofenceState', description: "Struct that receives the combined state and the individual state of each configured geofence" },
  ]}
/>

<InfoBox>The combined state is **0 = Unknown**, **1 = Inside**, or **2 = Outside**, and reflects the outermost of the configured geofences. Each individual geofence's state is also available in `currentGeofenceState.states[]`.</InfoBox>

---

## Full example

You can find the full sketch below:

<QuickLink
  title="Geofence.ino"
  description="An example of setting up and monitoring geofences with the NEO-M9N-00B module"
  url="https://github.com/SolderedElectronics/Soldered-u-blox-GPS-GNSS-Arduino-Library/blob/main/examples/Geofence/Geofence.ino"
/>
