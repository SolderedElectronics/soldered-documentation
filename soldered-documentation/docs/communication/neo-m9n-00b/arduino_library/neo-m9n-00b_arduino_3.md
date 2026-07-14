---
slug: /neo-m9n-00b/arduino/debug-output
title: NEO-M9N-00B - Debug Output
sidebar_label: Debug Output
id: neo-m9n-00b-arduino-3
hide_title: False
---

This page contains an example of enabling the library's debug output, which prints the raw UBX packets and internal status messages the library sends and receives. Use this to troubleshoot communication issues or see what's actually happening under the hood.

---

## Initialization

Include the required libraries and create the module object:

```cpp
#include <Wire.h>
#include <Soldered-GNSS.h>

Soldered_GNSS myGNSS;

unsigned long lastTime = 0;
int counter = 0;
```

In the `setup()` function, initialize the module and turn on debugging:

```cpp
void setup()
{
    Serial.begin(115200);
    while (!Serial);
    Serial.println("Soldered u-blox GNSS Example - Debug Output");

    Wire.begin();

    if (myGNSS.begin() == false)
    {
        Serial.println(F("u-blox GNSS not detected at default I2C address. Please check wiring. Freezing."));
        while (1);
    }

    myGNSS.setI2COutput(COM_TYPE_UBX);

    myGNSS.enableDebugging(); // Print all debug messages to Serial
    // myGNSS.enableDebugging(Serial, true); // Or print only critical messages
}
```

<FunctionDocumentation
  functionName="myGNSS.begin()"
  description="Initializes the GNSS module and establishes I2C communication"
  returnDescription="Boolean value, true if the module is detected and communication succeeds, false otherwise"
  parameters={[]}
/>

<FunctionDocumentation
  functionName="myGNSS.enableDebugging()"
  description="Prints the library's internal debug messages (UBX packets sent/received, parsing status, errors) to a Serial port"
  returnDescription="None"
  parameters={[
  { type: 'Stream &', name: 'debugPort', description: "Optional. The Serial port to print debug messages to. Defaults to Serial" },
  { type: 'bool', name: 'printLimitedDebug', description: "Optional. When true, only critical messages are printed instead of everything. Defaults to false" },
  ]}
/>

---

## Taking measurements

In the `loop()` function, the module is polled once per second. Debug messages print alongside the readings, then automatically stop after 20 readings:

```cpp
void loop()
{
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

        counter++;
        if (counter == 20)
        {
            myGNSS.disableDebugging();
        }
    }
}
```

<CenteredImage src="/img/neo-m9n-00b/debug.png" alt="Serial monitor debug output" caption="Serial monitor" width="100%" />

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

<FunctionDocumentation
  functionName="myGNSS.disableDebugging()"
  description="Stops the library from printing debug messages"
  returnDescription="None"
  parameters={[]}
/>

---

## Full example

You can find the full sketch below:

<QuickLink
  title="DebugOutput.ino"
  description="An example of enabling debug output while reading GPS position data with the NEO-M9N-00B module"
  url="https://github.com/SolderedElectronics/Soldered-u-blox-GPS-GNSS-Arduino-Library/blob/main/examples/DebugOutput/DebugOutput.ino"
/>
