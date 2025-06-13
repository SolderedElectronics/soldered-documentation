---  
slug: /inkplate/4tempera/rtc/basics  
title: Inkplate 4TEMPERA – RTC basics
id: 4tempera-rtc-basics  
hide_title: true  
---  
<SectionTitle title="RTC basics" backgroundImage="/img/rtc.png" />

The real time clock on Inkplate is the **onboard PCF85063 RTC**. The RTC uses an external clock source—an external XTAL of 32.768kHz.

---

## Setting time and date

Setting the current time and date is the most basic RTC usage. Once you set the time, it will keep "ticking," and you will be able to retrieve the current time later with accuracy. Of course, the RTC is not perfect; it may drift by a couple of seconds each day. If you're using the RTC, **it's recommended to set it approximately once per day**.

```cpp
#include "Inkplate.h"            // Include the Inkplate library in the sketch
Inkplate inkplate(INKPLATE_1BIT); // Create an Inkplate object and set the library to 1-bit mode (BW)

#define REFRESH_DELAY 1000 // Delay between refreshes
unsigned long time1;       // Time for measuring refresh in millis

// Set clock
uint8_t hour = 14;
uint8_t minutes = 30;
uint8_t seconds = 0;

// Set date and weekday (NOTE: For weekdays, 0 represents Sunday, 1 represents Monday, etc.)
uint8_t weekday = 4;
uint8_t day = 11;
uint8_t month = 11;
uint8_t year = 21;

void setup()
{
    inkplate.begin();        // Initialize the Inkplate library (call this function only once)
    inkplate.clearDisplay(); // Clear the display's frame buffer
    inkplate.display();      // Put the clear image on display
    inkplate.setTextSize(5); // Set text to be 5 times larger than the classic 5x7 px text
    inkplate.rtcSetTime(hour, minutes, seconds);    // Send time to the RTC
    inkplate.rtcSetDate(weekday, day, month, year);   // Send date to the RTC
}

// Variable that counts how many times the screen has been partially updated
int n = 0;
void loop()
{
    if ((unsigned long)(millis() - time1) > REFRESH_DELAY)
    {
        inkplate.rtcGetRtcData();           // Get the time and date from the RTC
        seconds = inkplate.rtcGetSecond();  // Store seconds in a variable
        minutes = inkplate.rtcGetMinute();  // Store minutes in a variable
        hour = inkplate.rtcGetHour();       // Store hours in a variable
        day = inkplate.rtcGetDay();         // Store the day of the month in a variable
        weekday = inkplate.rtcGetWeekday(); // Store the day of the week in a variable
        month = inkplate.rtcGetMonth();     // Store the month in a variable
        year = inkplate.rtcGetYear();       // Store the year in a variable

        inkplate.clearDisplay();                                       // Clear content in the frame buffer
        inkplate.setCursor(100, 300);                                  // Set the position of the text
        printTime(hour, minutes, seconds, day, weekday, month, year);   // Print the time on screen

        if (n > 9) // Check if you need to do a full refresh or if you can do a partial update
        {
            inkplate.display(true); // Do a full refresh
            n = 0;
        }
        else
        {
            inkplate.partialUpdate(false, true); // Do a partial update and keep the e-paper power supply on
            n++;                                // Increment the count of partial updates
        }

        time1 = millis(); // Store the current millis value
    }
}

void printTime(uint8_t _hour, uint8_t _minutes, uint8_t _seconds, uint8_t _day, uint8_t _weekday, uint8_t _month,
               uint16_t _year)
{
    // Write time and date information on screen
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
  description="Reads time and date from the RTC and stores them in their corresponding variables."
  returnDescription="void"
/>

## Full example

For full working code examples that provide a great overview, a real-world use scenario, and **code comments**, see the links below:

<QuickLink 
  title="Inkplate4TEMPERA_RTC_Simple.ino" 
  description="This example shows how to set time and date, how to read time, and how to print time on Inkplate using partial updates."
  url="https://github.com/SolderedElectronics/Inkplate-Arduino-library/blob/master/examples/Inkplate4TEMPERA/Advanced/RTC/Inkplate4TEMPERA_RTC_Simple/Inkplate4TEMPERA_RTC_Simple.ino" 
/>