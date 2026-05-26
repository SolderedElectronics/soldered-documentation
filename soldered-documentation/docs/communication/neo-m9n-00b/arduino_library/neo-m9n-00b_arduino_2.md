---
slug: /neo-m9n-00b/arduino/examples 
title: NEO-M9N-00B - Get Position
sidebar_label: Get Position
id: neo-m9n-00b-arduino-2 
hide_title: False
---

This page contains a simple example of reading GPS position data (latitude, longitude, altitude, and satellites in view) with the NEO-M9N-00B module.

---

---

## Initialization

To read position data from the NEO-M9N-00B, first include the required libraries and create the module object:

```cpp
#include <Wire.h>
#include <Soldered-GNSS.h>

Soldered_GNSS myGNSS;

long lastTime = 0;
```

Next, in the `setup()` function, initialize and configure the module:

```cpp
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
```

<FunctionDocumentation
  functionName="myGNSS.begin()"
  description="Initializes the GNSS module and establishes I2C communication"
  returnDescription="Boolean value, true if the module is detected and communication succeeds, false otherwise"
  parameters={[]}
/>

<FunctionDocumentation
  functionName="myGNSS.setI2COutput(uint8_t comSettings)"
  description="Sets the communication protocol output over I2C. Using COM_TYPE_UBX disables NMEA output and reduces I2C traffic"
  returnDescription="Boolean value, true if successful, false for error"
  parameters={[
  { type: 'uint8_t', name: 'comSettings', description: "Communication type flag, e.g. COM_TYPE_UBX for UBX-only output" },
  ]}
/>

<FunctionDocumentation
  functionName="myGNSS.saveConfigSelective(uint32_t configMask)"
  description="Saves a selective subset of the current configuration to the module's flash memory"
  returnDescription="Boolean value, true if successful, false for error"
  parameters={[
  { type: 'uint32_t', name: 'configMask', description: "Bitmask specifying which configuration subsections to save, e.g. VAL_CFG_SUBSEC_IOPORT" },
  ]}
/>

---

## Taking measurements

In the `loop()` function, the module is polled once per second to read the current position:

```cpp
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

<CenteredImage src="/img/neo-m9n-00b/readings.png" alt="Serial monitor sensor readings" caption="Serial monitor" width="100%" />

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

<FunctionDocumentation
  functionName="myGNSS.getAltitude()"
  description="Reads the current altitude from the GNSS module"
  returnDescription="Long value, altitude in millimeters"
  parameters={[]}
/>

<FunctionDocumentation
  functionName="myGNSS.getSIV()"
  description="Reads the number of satellites currently in view"
  returnDescription="Byte value, number of satellites in view"
  parameters={[]}
/>

---

## Full example

You can find the full sketch below:

<QuickLink  
  title="GetPosition.ino"  
  description="An example of reading GPS position data with the NEO-M9N-00B module"  
  url="https://github.com/SolderedElectronics/Soldered-u-blox-GPS-GNSS-Arduino-Library/blob/main/examples/GetPosition/GetPosition.ino"  
/>
