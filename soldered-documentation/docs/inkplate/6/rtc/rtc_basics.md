---  
slug: /inkplate/6/rtc/basics  
title: Inkplate 6 – RTC basics
sidebar_label: RTC basics
id: rtc-basics  
hide_title: true  
---  

<SectionTitle title="RTC basics" />

## Setting time and date

Setting the current time and date is the most basic RTC usage. Once you set the time, it will continue ticking, allowing you to retrieve the current time accurately. Of course, the RTC isn't perfect, so over the course of a day it may drift by a couple of seconds, either early or late. The drift comes from the 32.768 kHz crystal rather than the RTC chip: at a typical ±20 ppm that works out to under two seconds a day. If you're using the RTC, **it's recommended to set it approximately once per day**.

<InfoBox>If you would rather correct the drift than re-set the clock, the PCF85063A has an offset register for exactly this. Use `display.rtc.setClockOffset()`, and see the [**Inkplate6_RTC_Calibration**](https://github.com/SolderedElectronics/Inkplate-Arduino-library/blob/master/examples/Inkplate6/Diagnostics/Inkplate6_RTC_Calibration/Inkplate6_RTC_Calibration.ino) example for how to measure and apply the correction.</InfoBox>

```cpp
#include "Inkplate.h"            // Include Inkplate library to the sketch
Inkplate display(INKPLATE_1BIT); // Create an object on Inkplate library and also set library into 1-bit mode (BW)

#define REFRESH_DELAY 1000 // Delay between refreshes
unsigned long time1;       // Time for measuring refresh in millis

// Set clock
uint8_t hour = 8;
uint8_t minutes = 25;
uint8_t seconds = 0;

// Set date and weekday (NOTE: In weekdays 0 means Sunday, 1 means Monday, ...)
uint8_t weekday = 4;
uint8_t day = 16;
uint8_t month = 12;
uint8_t year = 21;

void setup()
{
    display.begin();        // Init Inkplate library (you should call this function ONLY ONCE)
    display.clearDisplay(); // Clear frame buffer of display
    display.display();      // Put clear image on display
    display.setTextSize(4); // Set text to be 4 times bigger than classic 5x7 px text

    display.rtc.setTime(hour, minutes, seconds);    // Send time to RTC
    display.rtc.setDate(weekday, day, month, year); // Send date to RTC
}

// Variable that keeps count on how much screen has been partially updated
int n = 0;

void loop()
{
    if ((unsigned long)(millis() - time1) > REFRESH_DELAY)
    {
        display.rtc.getRtcData();           // Get the time and date from RTC
        seconds = display.rtc.getSecond();  // Store senconds in a variable
        minutes = display.rtc.getMinute();  // Store minutes in a variable
        hour = display.rtc.getHour();       // Store hours in a variable
        day = display.rtc.getDay();         // Store day of month in a variable
        weekday = display.rtc.getWeekday(); // Store day of week in a variable
        month = display.rtc.getMonth();     // Store month in a variable
        year = display.rtc.getYear();       // Store year in a variable

        display.clearDisplay();                                       // Clear content in frame buffer
        display.setCursor(100, 300);                                  // Set position of the text
        printTime(hour, minutes, seconds, day, weekday, month, year); // Print the time on screen

        if (n > 9) // Check if you need to do full refresh or you can do partial update
        {
            display.display(true); // Do a full refresh
            n = 0;
        }
        else
        {
            display.partialUpdate(false, true); // Do partial update and keep e-papr power supply on
            n++;                                // Keep track on how many times screen has been partially updated
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
    display.print(':');
    print2Digits(_minutes);
    display.print(':');
    print2Digits(_seconds);

    display.print(' ');

    display.print(wday[_weekday]);
    display.print(", ");
    print2Digits(_day);
    display.print('/');
    print2Digits(_month);
    display.print('/');
    display.print(_year, DEC);
}

void print2Digits(uint8_t _d)
{
    if (_d < 10)
        display.print('0');
    display.print(_d, DEC);
}
```

<FunctionDocumentation
  functionName="display.rtc.setTime()"
  description="Method for setting time."
  returnType="void"
  parameters={[ 
    { type: 'uint8_t', name: 'rtcHour', description: "RTC Hour value." },
    { type: 'uint8_t', name: 'rtcMinute', description: "RTC Minute value." },
    { type: 'uint8_t', name: 'rtcSecond', description: "RTC Seconds value." },
  ]}
/>

<FunctionDocumentation
  functionName="display.rtc.setDate()"
  description="Method for setting date."
  returnType="void"
  parameters={[ 
    { type: 'uint8_t', name: 'rtcWeekday', description: "Weekday value. 0 means Sunday, 1 means Monday, and so on." },
    { type: 'uint8_t', name: 'rtcDay', description: "Day of the month." },
    { type: 'uint8_t', name: 'rtcMonth', description: "Month value." },
    { type: 'uint16_t', name: 'yr', description: "Year value." }
  ]}
/>

<FunctionDocumentation
  functionName="display.rtc.getRtcData()"
  description="Reads time and date from the RTC and stores them in their corresponding variables."
  returnType="void"
/>