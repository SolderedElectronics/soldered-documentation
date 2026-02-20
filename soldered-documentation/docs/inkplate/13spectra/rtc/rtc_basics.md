---  
slug: /inkplate/13spectra/rtc/basics 
title: Inkplate 13SPECTRA – RTC blasics
sidebar_label: RTC basics
id: 13spectra-rtc-basics 
---  

<SectionTitle title="RTC basics" backgroundImage="/img/rtc.png" />

The real-time clock on Inkplate 13SPECTRA is the **onboard PCF85063A RTC**. The RTC uses an external clock source, an external XTAL of 32.768kHz.

---

## Setting time and date

Setting the current time and date is the most basic RTC usage. Once you set the time, it will continue ticking, and you will be able to retrieve the current time later accurately. Of course, the RTC isn't perfect, so over the course of a day it may drift a couple of seconds early or late. If you're using the RTC, **it's recommended to set it approximately once per day**.

```cpp
#include "Inkplate.h" // Include Inkplate library to the sketch

Inkplate inkplate;     // Create an object on Inkplate library

#define REFRESH_DELAY 60000 // Delay between refreshes one minute
unsigned long time1;        // Time for measuring refresh in millis

// Set clock
uint8_t hour = 13;
uint8_t minutes = 0;
uint8_t seconds = 10;

// Set date and weekday (NOTE: In weekdays 0 means Sunday, 1 means Monday, ...)
uint8_t weekday = 1;
uint8_t day = 2;
uint8_t month = 2;
uint8_t year = 26;

void setup()
{
  inkplate.begin();          // Init Inkplate library (you should call this function ONLY ONCE)
  inkplate.rtc.Reset();      // Reset RTC if there is some data in it
  inkplate.clearDisplay();   // Clear frame buffer of display
  inkplate.setTextSize(4);   // Set text to be 4 times bigger than classic 5x7 px text
  inkplate.setTextColor(INKPLATE_BLACK, INKPLATE_WHITE); // Set text color and background

  inkplate.rtc.SetTime(hour, minutes, seconds);    // Send time to RTC
  inkplate.rtc.SetDate(weekday, day, month, year); // Send date to RTC
  getAndDisplayTime();                            // Display time on the screen
}

void loop()
{
  // Refresh screen every one minute
  if ((unsigned long)(millis() - time1) > REFRESH_DELAY)
  {
    // Display time on the screen
    getAndDisplayTime();

    // Store current millis
    time1 = millis();
  }
}

void getAndDisplayTime()
{
  inkplate.rtc.GetRtcData(); // Get the time and date from RTC

  seconds = inkplate.rtc.GetSecond();  // Store senconds in a variable
  minutes = inkplate.rtc.GetMinute();  // Store minutes in a variable
  hour = inkplate.rtc.GetHour();       // Store hours in a variable
  day = inkplate.rtc.GetDay();         // Store day of month in a variable
  weekday = inkplate.rtc.GetWeekday(); // Store day of week in a variable
  month = inkplate.rtc.GetMonth();     // Store month in a variable
  year = inkplate.rtc.GetYear();       // Store year in a variable

  inkplate.clearDisplay();                                       // Clear content in frame buffer
  inkplate.setCursor(80, 300);                                   // Set position of the text
  printTime(hour, minutes, seconds, day, weekday, month, year); // Print the time on screen
  inkplate.display();                                            // Refresh the screen
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

<CenteredImage src="/img/13spectra/DSC00703.jpg" alt="Example output displayed on e-paper display" caption="Example output displayed on e-paper display" width="1200px" />

<FunctionDocumentation
  functionName="inkplate.rtc.SetTime()"
  description="Method for setting time."
  returnType="void"
  parameters={[  
    { type: 'uint8_t', name: 'rtcHour', description: "RTC Hour value." },  
    { type: 'uint8_t', name: 'rtcMinute', description: "RTC Minute value." },  
    { type: 'uint8_t', name: 'rtcSecond', description: "RTC Seconds value." }  
  ]}
/>

<FunctionDocumentation
  functionName="inkplate.rtc.SetDate()"
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
  functionName="inkplate.rtc.GetRtcData()"
  description="Reads time and date from the RTC and stores them in their corresponding variables."
  returnDescription="void"
/>

