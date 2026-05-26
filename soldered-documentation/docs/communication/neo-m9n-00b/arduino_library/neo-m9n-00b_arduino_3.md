---
slug: /neo-m9n-00b/arduino/date-time
title: NEO-M9N-00B - Get Date and Time
sidebar_label: Get Date and Time
id: neo-m9n-00b-arduino-3 
hide_title: False
---

This page contains an example of reading GPS position alongside date and time data from the NEO-M9N-00B module, including validity checks for both.

---

---

## Initialization

Include the required libraries and create the module object:

```cpp
#include <Wire.h>
#include <Soldered-GNSS.h>

Soldered_GNSS myGNSS;

long lastTime = 0;
```

In the `setup()` function, initialize and configure the module:

```cpp
void setup()
{
    Serial.begin(115200);
    while (!Serial);
    Serial.println("Soldered u-blox GNSS Example 3 - Get Date and Time");

    Wire.begin();

    if (myGNSS.begin() == false)
    {
        Serial.println(F("u-blox GNSS not detected at default I2C address. Please check wiring. Freezing."));
        while (1);
    }

    // Set the I2C port to output UBX only (turn off NMEA noise)
    myGNSS.setI2COutput(COM_TYPE_UBX);
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

---

## Taking measurements

In the `loop()` function, the module is polled once per second to read position and date/time data:

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
        Serial.print(SIV);

        Serial.println();
        Serial.print(myGNSS.getYear());
        Serial.print("-");
        Serial.print(myGNSS.getMonth());
        Serial.print("-");
        Serial.print(myGNSS.getDay());
        Serial.print(" ");
        Serial.print(myGNSS.getHour());
        Serial.print(":");
        Serial.print(myGNSS.getMinute());
        Serial.print(":");
        Serial.print(myGNSS.getSecond());

        Serial.print("  Time is ");
        if (myGNSS.getTimeValid() == false)
        {
            Serial.print("not ");
        }
        Serial.print("valid  Date is ");
        if (myGNSS.getDateValid() == false)
        {
            Serial.print("not ");
        }
        Serial.print("valid");

        Serial.println();
    }
}
```

<CenteredImage src="/img/neo-m9n-00b/readings_datetime.png" alt="Serial monitor sensor readings" caption="Serial monitor" width="100%" />

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
  functionName="myGNSS.getYear()"
  description="Reads the current year from the GNSS module's UTC time"
  returnDescription="uint16_t value, the current year (e.g. 2025)"
  parameters={[]}
/>

<FunctionDocumentation
  functionName="myGNSS.getMonth()"
  description="Reads the current month from the GNSS module's UTC time"
  returnDescription="uint8_t value, the current month (1–12)"
  parameters={[]}
/>

<FunctionDocumentation
  functionName="myGNSS.getDay()"
  description="Reads the current day from the GNSS module's UTC time"
  returnDescription="uint8_t value, the current day of the month (1–31)"
  parameters={[]}
/>

<FunctionDocumentation
  functionName="myGNSS.getHour()"
  description="Reads the current hour from the GNSS module's UTC time"
  returnDescription="uint8_t value, the current hour (0–23)"
  parameters={[]}
/>

<FunctionDocumentation
  functionName="myGNSS.getMinute()"
  description="Reads the current minute from the GNSS module's UTC time"
  returnDescription="uint8_t value, the current minute (0–59)"
  parameters={[]}
/>

<FunctionDocumentation
  functionName="myGNSS.getSecond()"
  description="Reads the current second from the GNSS module's UTC time"
  returnDescription="uint8_t value, the current second (0–59)"
  parameters={[]}
/>

<FunctionDocumentation
  functionName="myGNSS.getTimeValid()"
  description="Checks whether the current time reported by the GNSS module is valid and confirmed"
  returnDescription="Boolean value, true if the time is valid, false if not yet confirmed"
  parameters={[]}
/>

<FunctionDocumentation
  functionName="myGNSS.getDateValid()"
  description="Checks whether the current date reported by the GNSS module is valid and confirmed"
  returnDescription="Boolean value, true if the date is valid, false if not yet confirmed"
  parameters={[]}
/>

---

## Full example

You can find the full sketch below:

<QuickLink  
  title="GetDateTime.ino"  
  description="An example of reading GPS date/time data with the NEO-M9N-00B module"  
  url="https://github.com/SolderedElectronics/Soldered-u-blox-GPS-GNSS-Arduino-Library/blob/main/examples/GetDateTime/GetDateTime.ino"  
/>
