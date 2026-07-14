---
slug: /neo-m9n-00b/arduino/power-save-mode
title: NEO-M9N-00B - Power Save Mode
sidebar_label: Power Save Mode
id: neo-m9n-00b-arduino-6
hide_title: False
---

This page contains an example of toggling the module's power save mode from the Serial Monitor. Power save mode trades off fix rate and responsiveness for lower average current draw, useful for battery-powered projects.

---

## Initialization

Include the required libraries and create the module object:

```cpp
#include <Wire.h>
#include <Soldered-GNSS.h>

Soldered_GNSS myGNSS;

long lastTime = 0;
```

In the `setup()` function, initialize the module:

```cpp
void setup()
{
    Serial.begin(115200);
    while (!Serial);
    Serial.println("Soldered u-blox GNSS Example - Power Save Mode");

    Wire.begin();

    if (myGNSS.begin() == false)
    {
        Serial.println(F("u-blox GNSS not detected at default I2C address. Please check wiring. Freezing."));
        while (1);
    }

    myGNSS.setI2COutput(COM_TYPE_UBX);

    Serial.println("Power save example.");
    Serial.println("Send '1' to enable power saving, '2' to disable it.");
}
```

<FunctionDocumentation
  functionName="myGNSS.begin()"
  description="Initializes the GNSS module and establishes I2C communication"
  returnDescription="Boolean value, true if the module is detected and communication succeeds, false otherwise"
  parameters={[]}
/>

---

## Toggling power save mode

In the `loop()` function, sending `1` or `2` over Serial enables or disables power save mode. Position and fix type are also printed every 10 seconds so you can observe the effect on fix behavior:

```cpp
void loop()
{
    if (Serial.available())
    {
        byte incoming = Serial.read();

        if (incoming == '1')
        {
            if (myGNSS.powerSaveMode())
                Serial.println(F("Power Save Mode enabled."));
            else
                Serial.println(F("*** Power Save Mode FAILED ***"));
        }
        else if (incoming == '2')
        {
            if (myGNSS.powerSaveMode(false))
                Serial.println(F("Power Save Mode disabled."));
            else
                Serial.println(F("*** Power Save Disable FAILED ***"));
        }

        uint8_t lowPowerMode = myGNSS.getPowerSaveMode();
        Serial.print(F("The low power mode is: "));
        Serial.println(lowPowerMode); // 0 or 4 = Continuous, 1 = Power Save
    }

    // Query the module every 10 seconds so it's easier to observe the current draw
    if (millis() - lastTime > 10000)
    {
        lastTime = millis();

        byte fixType = myGNSS.getFixType();
        Serial.print(F("Fix: "));
        Serial.print(fixType);

        long latitude = myGNSS.getLatitude();
        Serial.print(F(" Lat: "));
        Serial.print(latitude);

        long longitude = myGNSS.getLongitude();
        Serial.print(F(" Long: "));
        Serial.print(longitude);
        Serial.print(F(" (degrees * 10^-7)"));

        long altitude = myGNSS.getAltitude();
        Serial.print(F(" Alt: "));
        Serial.print(altitude);
        Serial.println(F(" (mm)"));
    }
}
```

<FunctionDocumentation
  functionName="myGNSS.powerSaveMode()"
  description="Enables or disables the module's power save mode"
  returnDescription="Boolean value, true if successful, false for error"
  parameters={[
  { type: 'bool', name: 'power_save', description: "Optional. True enables power save mode, false switches back to continuous mode. Defaults to true" },
  ]}
/>

<FunctionDocumentation
  functionName="myGNSS.getPowerSaveMode()"
  description="Reads back the module's current low power mode setting"
  returnDescription="Byte value: 0 or 4 = Continuous mode, 1 = Power save mode, 255 = error reading the setting"
  parameters={[]}
/>

<FunctionDocumentation
  functionName="myGNSS.getFixType()"
  description="Reads the current GNSS fix type"
  returnDescription="Byte value: 0 = no fix, 1 = dead reckoning, 2 = 2D, 3 = 3D, 4 = GNSS + dead reckoning, 5 = time only"
  parameters={[]}
/>

<InfoBox>In power save mode, the module fixes less frequently to save power, so expect slower position updates and a longer time to first fix compared to continuous mode.</InfoBox>

---

## Full example

You can find the full sketch below:

<QuickLink
  title="PowerSaveMode.ino"
  description="An example of toggling power save mode with the NEO-M9N-00B module"
  url="https://github.com/SolderedElectronics/Soldered-u-blox-GPS-GNSS-Arduino-Library/blob/main/examples/PowerSaveMode/PowerSaveMode.ino"
/>
