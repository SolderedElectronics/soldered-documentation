---
slug: /neo-m9n-00b/arduino/great-circle-distance
title: NEO-M9N-00B - Great Circle Distance
sidebar_label: Great Circle Distance
id: neo-m9n-00b-arduino-5
hide_title: False
---

This page contains an example of calculating the distance and bearing from the module's current position to a fixed target location, using a great-circle (Haversine-based) distance calculation.

---

## Initialization

Include the required libraries, create the module object, and add two helper functions for calculating distance and bearing between two coordinates:

```cpp
#include <Wire.h>
#include <Soldered-GNSS.h>

Soldered_GNSS myGNSS;

long lastTime = 0;

double distanceBetween(long lat1_l, long long1_l, long lat2_l, long long2_l)
{
    // Returns distance in meters between two positions using a great-circle
    // calculation on a sphere of radius 6372795 m. Rounding errors of up to
    // 0.5% are possible since Earth isn't a perfect sphere.
    double lat1 = (double)lat1_l / 10000000.0;
    double long1 = (double)long1_l / 10000000.0;
    double lat2 = (double)lat2_l / 10000000.0;
    double long2 = (double)long2_l / 10000000.0;

    double delta = radians(long1 - long2);
    double sdlong = sin(delta);
    double cdlong = cos(delta);
    lat1 = radians(lat1);
    lat2 = radians(lat2);
    double slat1 = sin(lat1);
    double clat1 = cos(lat1);
    double slat2 = sin(lat2);
    double clat2 = cos(lat2);
    delta = (clat1 * slat2) - (slat1 * clat2 * cdlong);
    delta = sq(delta);
    delta += sq(clat2 * sdlong);
    delta = sqrt(delta);
    double denom = (slat1 * slat2) + (clat1 * clat2 * cdlong);
    delta = atan2(delta, denom);
    return delta * 6372795;
}

double courseTo(long lat1_l, long long1_l, long lat2_l, long long2_l)
{
    // Returns course in degrees (North = 0, West = 270) from position 1 to position 2
    double lat1 = (double)lat1_l / 10000000.0;
    double long1 = (double)long1_l / 10000000.0;
    double lat2 = (double)lat2_l / 10000000.0;
    double long2 = (double)long2_l / 10000000.0;

    double dlon = radians(long2 - long1);
    lat1 = radians(lat1);
    lat2 = radians(lat2);
    double a1 = sin(dlon) * cos(lat2);
    double a2 = sin(lat1) * cos(lat2) * cos(dlon);
    a2 = cos(lat1) * sin(lat2) - a2;
    a2 = atan2(a1, a2);
    if (a2 < 0.0)
    {
        a2 += TWO_PI;
    }
    return degrees(a2);
}
```

In the `setup()` function, initialize the module:

```cpp
void setup()
{
    Serial.begin(115200);
    while (!Serial);
    Serial.println("Soldered u-blox GNSS Example - Great Circle Distance");

    Wire.begin();

    if (myGNSS.begin() == false)
    {
        Serial.println(F("u-blox GNSS not detected at default I2C address. Please check wiring. Freezing."));
        while (1);
    }

    myGNSS.setI2COutput(COM_TYPE_UBX);
    myGNSS.saveConfigSelective(VAL_CFG_SUBSEC_IOPORT);
}
```

<FunctionDocumentation
  functionName="myGNSS.begin()"
  description="Initializes the GNSS module and establishes I2C communication"
  returnDescription="Boolean value, true if the module is detected and communication succeeds, false otherwise"
  parameters={[]}
/>

---

## Taking measurements

Set your target coordinates, then in the `loop()` function the module is polled once per second to compute the distance and bearing to that target:

```cpp
static const long TARGET_LAT = 400909142, TARGET_LON = -1051849833; // Set your own target: degrees * 10^-7

void loop()
{
    if (millis() - lastTime > 1000)
    {
        lastTime = millis();

        long latitude = myGNSS.getLatitude();
        long longitude = myGNSS.getLongitude();

        Serial.print(F("Lat: "));
        Serial.print(latitude);
        Serial.print(F(" Long: "));
        Serial.println(longitude);

        double distanceToTarget = distanceBetween(latitude, longitude, TARGET_LAT, TARGET_LON);
        Serial.print(F("Distance to target: "));
        Serial.print(distanceToTarget, 2);
        Serial.print(F(" (m)  "));

        double courseToTarget = courseTo(latitude, longitude, TARGET_LAT, TARGET_LON);
        Serial.print(F("Course to target: "));
        Serial.print(courseToTarget, 1);
        Serial.println(F(" (degrees)"));
    }
}
```

<CenteredImage src="/img/neo-m9n-00b/circle.png" alt="Serial monitor great circle distance readings" caption="Serial monitor" width="100%" />

<FunctionDocumentation
  functionName="myGNSS.getLatitude()"
  description="Reads the current latitude from the GNSS module"
  returnDescription="Long value, latitude in degrees multiplied by 10^-7"
  parameters={[]}
/>

<FunctionDocumentation
  functionName="myGNSS.getLongitude()"
  description="Reads the current longitude from the GNSS module"
  returnDescription="Long value, longitude in degrees multiplied by 10^-7"
  parameters={[]}
/>

<InfoBox>The `distanceBetween()` and `courseTo()` helper functions aren't part of the library itself, they're plain C++ math included directly in the sketch, adapted from the widely-used TinyGPSPlus library.</InfoBox>

---

## Full example

You can find the full sketch below:

<QuickLink
  title="Great_Circle_Distance.ino"
  description="An example of calculating distance and bearing to a target location with the NEO-M9N-00B module"
  url="https://github.com/SolderedElectronics/Soldered-u-blox-GPS-GNSS-Arduino-Library/blob/main/examples/Great_Circle_Distance/Great_Circle_Distance.ino"
/>
