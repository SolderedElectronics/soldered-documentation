---
slug: /pcf85063a/arduino/initialization
title: PCF85063A - Initialization
id: pcf85063a-arduino-2
hide_title: false
---

## Connections for this example

<CenteredImage src="/img/pcf85063a/connections.png" alt="connections"/>

---

## Initializing

For first-time use, we must initialize the RTC by providing it with the current time and date. First, include the library and create an instance of the RTC object, then initialize it in the `setup()` function:

```cpp
// Include the library
#include "PCF85063A-SOLDERED.h"

// Create an instance of the RTC
PCF85063A rtc; 


void setup()
{
    Serial.begin(115200); // Start serial communication with the PC using a baud rate of 115200
    rtc.begin();  // Initialize RTC module

    //  setTime(hour, minute, sec);
    rtc.setTime(11, 53, 00); // 24-hour mode, e.g., 11:53:00
    //  setDate(weekday, day, month, yr);
    rtc.setDate(1, 31, 3, 2025); // 0 for Sunday, e.g., Monday, 31.3.2025.
}
```

<FunctionDocumentation
  functionName="rtc.begin()"
  description="Initializes the RTC, setting up communication over I2C"
  returnDescription="None"
  parameters={[]}
/>

<FunctionDocumentation
  functionName="rtc.setTime(uint8_t hour, uint8_t minute, uint8_t second)"
  description="Sets the time on the RTC"
  returnDescription="None"
  parameters={[
  { type: 'uint8_t', name: 'hour', description: "What hour you want to set" },
  { type: 'uint8_t', name: 'minute', description: "What minute you want to set" },
  { type: 'uint8_t', name: 'second', description: "What second you want to set" },
  ]}
/>

<FunctionDocumentation
  functionName="rtc.setDate(uint8_t weekday, uint8_t day, uint8_t month, uint16_t yr)"
  description="Sets the date on the RTC"
  returnDescription="None"
  parameters={[
  { type: 'uint8_t', name: 'weekday', description: "What weekday you want to set" },
  { type: 'uint8_t', name: 'day', description: "What day you want to set" },
  { type: 'uint8_t', name: 'month', description: "What month you want to set" },
  { type: 'uint16_t', name: 'year', description: "What year you want to set" },
  ]}
/>