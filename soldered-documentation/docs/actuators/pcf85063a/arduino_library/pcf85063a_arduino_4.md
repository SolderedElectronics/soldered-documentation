---
slug: /pcf85063a/arduino/reading-the-time-and-date
title: Reading the time and date
id: pcf85063a-arduino-4 
hide_title: False
---

In the `loop()` function, we will read the time on the RTC every second:

```cpp

//Include the library
#include "PCF85063A-SOLDERED.h"

//Create an instance ov the RTC
PCF85063A rtc; 


void setup()
{
    Serial.begin(115200); //Start serial communication with PC using 115200 baudrate
    rtc.begin();  //Initialize RTC module

    //  setTime(hour, minute, sec);
    rtc.setTime(11, 53, 00); // 24H mode, ex. 11:53:00
    //  setDate(weekday, day, month, yr);
    rtc.setDate(1, 31, 3, 2025); // 0 for Sunday, ex. Monday, 31.3.2025.
}

void loop()
{
    switch (rtc.getWeekday()) // Get weekday, 0 is Sunday
                              // and decode to string
    {
    case 0:                   
        Serial.print("Sunday , ");
        break;
    case 1:
        Serial.print("Monday , ");
        break;
    case 2:
        Serial.print("Tuesday , ");
        break;
    case 3:
        Serial.print("Wednesday , ");
        break;
    case 4:
        Serial.print("Thursday , ");
        break;
    case 5:
        Serial.print("Friday , ");
        break;
    case 6:
        Serial.print("Saturday , ");
        break;
    }

    Serial.print(rtc.getDay()); //Function for getting day in month
    Serial.print(".");
    Serial.print(rtc.getMonth()); //Function for getting month
    Serial.print(".");
    Serial.print(rtc.getYear()); //Function for getting year
    Serial.print(". ");
    Serial.print(rtc.getHour()); //Function for getting hours
    Serial.print(":");
    Serial.print(rtc.getMinute()); //Function for getting minutes
    Serial.print(":");
    Serial.println(rtc.getSecond()); //Function for getting seconds

    delay(1000); //Delay for 1s
}

```

<CenteredImage src="/img/pcf85063a/datetime.png" alt="Serial monitor date & time readings" caption="Serial monitor date & time readings" width="100%" />


<FunctionDocumentation
  functionName="rtc.getWeekday()"
  description="Returns the current weekday"
  returnDescription="uint8_t value, the current weekday id (0 for sunday, 6 for saturday)"
  parameters={[]}
/>

<FunctionDocumentation
  functionName="rtc.getDay()"
  description="Returns the current day"
  returnDescription="uint8_t value, the current day"
  parameters={[]}
/>

<FunctionDocumentation
  functionName="rtc.getMonth()"
  description="Returns the current month"
  returnDescription="uint8_t value, the current month"
  parameters={[]}
/>

<FunctionDocumentation
  functionName="rtc.getYear()"
  description="Returns the current year"
  returnDescription="uint16_t value, the current year"
  parameters={[]}
/>

<FunctionDocumentation
  functionName="rtc.getHour()"
  description="Returns the current hour"
  returnDescription="uint8_t value, the current hour"
  parameters={[]}
/>

<FunctionDocumentation
  functionName="rtc.getMinute()"
  description="Returns the current minute"
  returnDescription="uint8_t value, the current minutes"
  parameters={[]}
/>

<FunctionDocumentation
  functionName="rtc.getSecond()"
  description="Returns the current seconds"
  returnDescription="uint8_t value, the current hour"
  parameters={[]}
/>

---

## Full example 

The full example is listed below:

```cpp


void loop()
{
    switch (rtc.getWeekday()) // Get weekday, 0 is Sunday
                              // and decode to string
    {
    case 0:                   
        Serial.print("Sunday , ");
        break;
    case 1:
        Serial.print("Monday , ");
        break;
    case 2:
        Serial.print("Tuesday , ");
        break;
    case 3:
        Serial.print("Wednesday , ");
        break;
    case 4:
        Serial.print("Thursday , ");
        break;
    case 5:
        Serial.print("Friday , ");
        break;
    case 6:
        Serial.print("Saturday , ");
        break;
    }

    Serial.print(rtc.getDay()); //Function for getting day in month
    Serial.print(".");
    Serial.print(rtc.getMonth()); //Function for getting month
    Serial.print(".");
    Serial.print(rtc.getYear()); //Function for getting year
    Serial.print(". ");
    Serial.print(rtc.getHour()); //Function for getting hours
    Serial.print(":");
    Serial.print(rtc.getMinute()); //Function for getting minutes
    Serial.print(":");
    Serial.println(rtc.getSecond()); //Function for getting seconds

    delay(1000); //Delay for 1s
}


```
