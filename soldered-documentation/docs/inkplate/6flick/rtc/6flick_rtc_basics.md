---
slug: /inkplate/6flick/rtc/basics
title: Inkplate 6FLICK – RTC basics
sidebar_label: RTC basics
id: 6flick-rtc-basics
hide_title: true
---
<SectionTitle title="RTC basics" backgroundImage="/img/rtc.png" />

The real time clock on Inkplate 10 is the **onboard PCF85063 RTC**. The RTC uses an external clock source, an external XTAL of 32.768kHz.

---

## Setting time and date

Setting the current time and date is the most basic RTC usage. Once you set the time, it will keep "ticking" and you will be able to get the current time later, and it will be accurate. Of course, the RTC isn't perfect, so during one day it will drift off a couple of seconds early or late. If you're using the RTC, **it's recommended to set it approx. once per day**.

```cpp
#include "Inkplate.h"            // Include Inkplate library in the sketch
Inkplate inkplate(INKPLATE_1BIT); // Create an Inkplate object and set the library into 1-bit mode (BW)

#define REFRESH_DELAY 1000 // Delay between refreshes
unsigned long time1;       // Time for measuring refresh in millis

// Set clock
uint8_t hour = 14;
uint8_t minutes = 30;
uint8_t seconds = 00;

// Set date and weekday (NOTE: In weekdays 0 means Sunday, 1 means Monday, ...)
uint8_t weekday = 4;
uint8_t day = 11;
uint8_t month = 11;
uint8_t year = 21;

void setup()
{
    inkplate.begin();        // Init Inkplate library (you should call this function ONLY ONCE)
    inkplate.clearDisplay(); // Clear frame buffer of display
    inkplate.display();      // Put clear image on display
    inkplate.setTextSize(5); // Set text to be 5 times bigger than classic 5x7 px text
    inkplate.rtcSetTime(hour, minutes, seconds);    // Send time to RTC
    inkplate.rtcSetDate(weekday, day, month, year);   // Send date to RTC
}

// Variable that keeps count on how many times the screen has been partially updated
int n = 0;
void loop()
{
    if ((unsigned long)(millis() - time1) > REFRESH_DELAY)
    {
        inkplate.rtcGetRtcData();           // Get the time and date from RTC
        seconds = inkplate.rtcGetSecond();  // Store seconds in a variable
        minutes = inkplate.rtcGetMinute();  // Store minutes in a variable
        hour = inkplate.rtcGetHour();       // Store hours in a variable
        day = inkplate.rtcGetDay();         // Store day of month in a variable
        weekday = inkplate.rtcGetWeekday(); // Store day of week in a variable
        month = inkplate.rtcGetMonth();     // Store month in a variable
        year = inkplate.rtcGetYear();       // Store year in a variable

        inkplate.clearDisplay();                                       // Clear content in frame buffer
        inkplate.setCursor(100, 300);                                  // Set position of the text
        printTime(hour, minutes, seconds, day, weekday, month, year);   // Print the time on screen

        if (n > 9) // Check if you need to do a full refresh or you can do a partial update
        {
            inkplate.display(true); // Do a full refresh
            n = 0;
        }
        else
        {
            inkplate.partialUpdate(false, true); // Do a partial update and keep the e-paper power supply on
            n++;                                // Keep track of how many times the screen has been partially updated
        }

        time1 = millis(); // Store current millis
    }
}

void printTime(uint8_t _hour, uint8_t _minutes, uint8_t _seconds, uint8_t _day, uint8_t _weekday, uint8_t _month,
               uint16_t _year)
{
    // Write time and date info on screen
    char *wday[] = {"Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"};

    print2Digits(_hour);
    inkplate.print(':');
    print2Digits(_minutes);
    inkplate.print(':');
    print2Digits(_seconds);

    inkplate.print(' ');

    inkplate.print(wday[_weekday]);
    inkplate.print(", ");
    print2Digits(_day);
    inkplate.print('/');
    print2Digits(_month);
    inkplate.print('/');
    inkplate.print(_year, DEC);
}

void print2Digits(uint8_t _d)
{
    if (_d < 10)
        inkplate.print('0');
    inkplate.print(_d, DEC);
}
```

<FunctionDocumentation
  functionName="inkplate.rtcSetTime()"
  description="Method for setting time."
  returnType="void"
  parameters={[ 
    { type: 'uint8_t', name: 'rtcHour', description: "RTC Hour value." },
    { type: 'uint8_t', name: 'rtcMinute', description: "RTC Minute value." },
    { type: 'uint8_t', name: 'rtcSecond', description: "RTC Seconds value." },
  ]}
/>

<FunctionDocumentation
  functionName="inkplate.rtcSetDate()"
  description="Method for setting date."
  returnDescription="void"
  parameters={[ 
    { type: 'uint8_t', name: 'rtcWeekday', description: "Weekday value." },
    { type: 'uint8_t', name: 'rtcDay', description: "Day of the month." },
    { type: 'uint16_t', name: 'rtcMonth', description: "Month value." },
    { type: 'uint8_t', name: 'yr', description: "Year value." }
  ]}
/>

<FunctionDocumentation
  functionName="inkplate.rtcGetRtcData()"
  description="Reads time and date from the RTC, and stores them in their corresponding variables."
  returnDescription="void"
/>

## Full example

For full working code examples, which provide a great overview, a real-world use scenario, and **code comments**, see the links below:

<QuickLink 
  title="Inkplate6FLICK_RTC_Simple.ino" 
  description="This example will show how to set time and date, how to read time, and how to print time on Inkplate using partial updates."
  url="https://github.com/SolderedElectronics/Inkplate-Arduino-library/blob/dev/examples/Inkplate6FLICK/Advanced/RTC/Inkplate6FLICK_RTC_Simple/Inkplate6FLICK_RTC_Simple.ino" 
/>