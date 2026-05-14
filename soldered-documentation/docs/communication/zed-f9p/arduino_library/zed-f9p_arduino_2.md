---
slug: /zed-f9p/arduino/examples 
title: ZED-F9P - Initialization and Readings
sidebar_label: Initialization and Readings
id: zed-f9p-arduino-2 
hide_title: False
---

This page provides a simple example on how to initialize and use the u-blox ZED-F9P GPS GNSS sensor with NULA MINI.

[image placeholder - connections]

<WarningBox> **The antenna may take a couple of mnutes to start reading proper data - this is normal.**</WarningBox>

---

## Initialization
To use the ZED-F9P sensor with the NULA MINI, you need to include the `Soldered-GNSS.h` and `Wire.h` libraries, create an instance of the GNSS object, and initialize it within the `setup()` function. This ensures proper communication between NULA MINI and the GNSS module. The `begin()` function is used to set up the sensor, allowing it to start receiving satelite data.

Here is an example of how to initialize the ZED-F9P sensor:

```cpp
// Include the required libraries
#include <Wire.h>
#include <Soldered-GNSS.h>

// Create an object for the GNSS library
Soldered_GNSS myGNSS;

void setup()
{
    Serial.begin(115200);

    Wire.begin();

    if(myGNSS.begin()==false)
    {
        Serial.println("u-blox GNSS not detected at default I2C address. Please check wiring. Freezing.");
    }
}
```

<FunctionDocumentation
functionName="myGNSS.begin()"
description="Initializes the ZED-F9P module, setting up communication over default I2C pins."
returnDescription="Bool, Returns true is initialization is successful, false otherwise."
parameters={[]}
/>

---

## Getting Basic Readings
This snippet provides an example of how to retrieve and display GNSS data using the ZED-F9P module. To get readings for **Latitude**, **Longitude**, **Altitude** and **SIV**, call functions `getLatitude()`, `getLongitude()`, `getAltitude()` and `getSIV()`. It is recommended to Query the module once per second.

```cpp
long lastTime=0;
void loop()
{
    if(millis() - lastTime > 1000)
    {
        lastTime=millis();
        long latitude = myGNSS.getLatitude();
        Serial.print(F("Lat: "));
        Serial.print(latitude);

        long longitude = myGNSS.getLongitude();
        Serial.print(F(" Long: "));
        Serial.print(longitude);
        Serial.print(F(" (degrees * 10^-7)"));

        long altitude = myGNSS.getAltitude();
        Serial.print(F(" Alt: "));
        Serial.print(altitude);
        Serial.print(F(" (mm)"));

        byte SIV = myGNSS.getSIV();
        Serial.print(F(" SIV: "));
        Serial.println(SIV);
    }
}
```

<FunctionDocumentation
functionName="myGNSS.getLatitude()"
description="Get the current latitude in degrees."
returnDescription="Returns a long representing the number of degrees *10^7."
parameters={[]}
/>

<FunctionDocumentation
functionName="myGNSS.getLongitude()"
description="Get the current longitude in degrees."
returnDescription="Returns a long representing the number of degrees *10^7."
parameters={[]}
/>

<FunctionDocumentation
functionName="myGNSS.getAltitude()"
description="Get the current altitude in mlimeters according to ellipsoid model."
returnDescription="Returns a long representing the altitude in milimeters."
parameters={[]}
/>

<FunctionDocumentation
functionName="myGNSS.getSIV()"
description="Get the number of satelites used in fix."
returnDescription="Returns a int representing the number of satelites that were used for fix."
/>
---

## Full Example

Open the Serial Monitor at 115200 to observe the detected data.

```cpp
#include <Wire.h>
#include <Soldered-GNSS.h>

Soldered_GNSS myGNSS;

long lastTime = 0;

void setup()
{
    Serial.begin(115200);
    while (!Serial);
    Serial.println("Soldered u-blox GNSS Example 2 - Get Position");

    Wire.begin();

    if (myGNSS.begin() == false)
    {
        Serial.println("u-blox GNSS not detected at default I2C address. Please check wiring. Freezing.");
        while (1);
    }

    // Use UBX-only output to reduce I2C traffic
    myGNSS.setI2COutput(COM_TYPE_UBX);
    myGNSS.saveConfigSelective(VAL_CFG_SUBSEC_IOPORT);
}

void loop()
{
    // Query the module only once per second
    if (millis() - lastTime > 1000)
    {
        lastTime = millis();

        long latitude = myGNSS.getLatitude();
        Serial.print(F("Lat: "));
        Serial.print(latitude);

        long longitude = myGNSS.getLongitude();
        Serial.print(F(" Long: "));
        Serial.print(longitude);
        Serial.print(F(" (degrees * 10^-7)"));

        long altitude = myGNSS.getAltitude();
        Serial.print(F(" Alt: "));
        Serial.print(altitude);
        Serial.print(F(" (mm)"));

        byte SIV = myGNSS.getSIV();
        Serial.print(F(" SIV: "));
        Serial.println(SIV);
    }
}
```

[Image placeholder - serial monitor output]

