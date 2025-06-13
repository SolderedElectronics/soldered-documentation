---  
slug: /inkplate/6color/rtc/basics  
title: Inkplate 6COLOR – RTC basics
id: rtc-basics  
hide_title: true  
---  
<SectionTitle title="RTC basics" backgroundImage="/img/rtc.png" />

The real-time clock on Inkplate 6COLOR is the **onboard PCF85063A RTC**. The RTC uses an external clock source, an external XTAL of 32.768kHz.

---

## Setting time and date

Setting the current time and date is the most basic RTC usage. Once you set the time, it will continue ticking, and you will be able to retrieve the current time later accurately. Of course, the RTC isn't perfect, so over the course of a day it may drift a couple of seconds early or late. If you're using the RTC, **it's recommended to set it approximately once per day**.

```cpp
#include "Inkplate.h" // Include Inkplate library in the sketch
Inkplate display;     // Create an object of the Inkplate library

#define REFRESH_DELAY 60000 // Delay between refreshes: one minute
unsigned long time1;      // Time for measuring refresh in millis

// Set clock
uint8_t hour = 12;
uint8_t minutes = 50;
uint8_t seconds = 0;

// Set date and weekday (NOTE: In weekdays 0 means Sunday, 1 means Monday, ...)
uint8_t weekday = 1;
uint8_t day = 20;
uint8_t month = 2;
uint8_t year = 23;

void setup()
{
    display.begin();        // Init Inkplate library (you should call this function ONLY ONCE)
    display.rtcReset();     // Reset RTC if there is some data in it
    display.clearDisplay(); // Clear frame buffer of display
    display.setTextSize(3); // Set text to be 3 times bigger than classic 5x7 px text
    display.setTextColor(INKPLATE_BLACK, INKPLATE_WHITE); // Set text color and background

    display.rtcSetTime(hour, minutes, seconds);    // Send time to RTC
    display.rtcSetDate(weekday, day, month, year);   // Send date to RTC
    getAndDisplayTime();                             // Display time on the screen
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
    display.rtcGetRtcData(); // Get the time and date from the RTC

    seconds = display.rtcGetSecond();  // Store seconds in a variable
    minutes = display.rtcGetMinute();    // Store minutes in a variable
    hour = display.rtcGetHour();         // Store hours in a variable
    day = display.rtcGetDay();           // Store day of month in a variable
    weekday = display.rtcGetWeekday();   // Store day of week in a variable
    month = display.rtcGetMonth();       // Store month in a variable
    year = display.rtcGetYear();         // Store year in a variable

    display.clearDisplay();                                        // Clear content in frame buffer
    display.setCursor(80, 300);                                    // Set position of the text
    printTime(hour, minutes, seconds, day, weekday, month, year);  // Print the time on screen
    display.display();                                             // Refresh the screen
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
  functionName="inkplate.rtcSetTime()"
  description="Method for setting time."
  returnType="void"
  parameters={[  
    { type: 'uint8_t', name: 'rtcHour', description: "RTC Hour value." },  
    { type: 'uint8_t', name: 'rtcMinute', description: "RTC Minute value." },  
    { type: 'uint8_t', name: 'rtcSecond', description: "RTC Seconds value." }  
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
  description="Reads time and date from the RTC and stores them in their corresponding variables."
  returnDescription="void"
/>