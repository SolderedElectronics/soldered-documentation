---  
slug: /inkplate/6color/rtc/alarm  
title: RTC alarm  
id: rtc-alarm  
---  

The onboard RTC supports creating an alarm that triggers at a specific time, allowing the firmware to detect and respond accordingly. Alarms can be configured to trigger once per day, per hour, or per minute.

---  

## Simple alarm

This section demonstrates setting a simple RTC alarm that is checked using polling. The firmware continuously checks the alarm flag and responds when it is triggered.

```cpp
#include "Inkplate.h" // Include Inkplate library to the sketch
Inkplate display;     // Create an object on Inkplate library

// Set clock
uint8_t hour = 12;
uint8_t minutes = 51;
uint8_t seconds = 0;

// Set date and weekday (NOTE: In weekdays 0 means Sunday, 1 means Monday, ...)
uint8_t weekday = 1;
uint8_t day = 20;
uint8_t month = 2;
uint8_t year = 23;

// Set alarm time and date (alarm will be generated 60 seconds after board power up)
uint8_t alarmHour = 12;
uint8_t alarmMinutes = 52;
uint8_t alarmSeconds = 0;
uint8_t alarmWeekday = 1;
uint8_t alarmDay = 20;

void setup()
{
    display.begin();        // Init Inkplate library (you should call this function ONLY ONCE)
    display.rtcReset();     // Reset RTC if there is some data in it
    display.clearDisplay(); // Clear frame buffer of display
    display.setTextSize(3); // Set text to be 3 times bigger than classic 5x7 px text

    display.rtcSetTime(hour, minutes, seconds);    // Send time to RTC
    display.rtcSetDate(weekday, day, month, year);   // Send date to RTC
    display.rtcSetAlarm(alarmSeconds, alarmMinutes, alarmHour, alarmDay, alarmWeekday); // Set alarm
}

void loop()
{
    display.rtcGetRtcData();              // Get the time and date from RTC
    seconds = display.rtcGetSecond();     // Store seconds in a variable
    minutes = display.rtcGetMinute();     // Store minutes in a variable
    hour = display.rtcGetHour();          // Store hours in a variable
    day = display.rtcGetDay();            // Store day of month in a variable
    weekday = display.rtcGetWeekday();    // Store day of week in a variable
    month = display.rtcGetMonth();        // Store month in a variable
    year = display.rtcGetYear();          // Store year in a variable

    display.clearDisplay();                                       // Clear content in frame buffer
    display.setCursor(100, 300);                                  // Set position of the text
    display.setTextColor(INKPLATE_GREEN, INKPLATE_WHITE);         // Set text color and background
    printTime(hour, minutes, seconds, day, weekday, month, year);  // Print the time on screen

    if (display.rtcCheckAlarmFlag())  // Check if alarm has occurred
    {
      display.rtcClearAlarmFlag();    // It's recommended to clear alarm flag after alarm has occurred
      display.setCursor(400, 400);      // Set new position for cursor
      display.print("ALARM!");
    }

    display.display(); // Do a full refresh

    delay(60000); // Delay between refreshes one minute
}

void printTime(uint8_t _hour, uint8_t _minutes, uint8_t _seconds, uint8_t _day, uint8_t _weekday, uint16_t _month,
               uint8_t _year)
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
    functionName="inkplate.rtcSetAlarm()"
    description="Sets the alarm to all the parameters."
    returnType="void"
    parameters={[ 
    { type: 'uint8_t', name: 'rtcAlarmSecond', description: 'Set the alarm seconds.' },
    { type: 'uint8_t', name: 'rtcAlarmminute', description: 'Set the alarm minutes.' },
    { type: 'uint8_t', name: 'rtcAlarmHour', description: 'Set the alarm hours.' },
    { type: 'uint8_t', name: 'rtcAlarmDay', description: 'Set the alarm rtcDay.' },
    { type: 'uint8_t', name: 'rtcAlarmWeekday', description: 'Set the alarm rtcWeekday.' },
    ]}
/>

<FunctionDocumentation
  functionName="inkplate.rtcCheckAlarmFlag()"
  description="Checks if the alarm flag is on"
  returnDescription="Returns true if the alarm flag is on"
  returnType="bool"
/>

---  

## Interrupt Alarm
The RTC alarm can also generate an **interrupt** instead of requiring polling. The alarm event can wake up the MCU from sleep or trigger an action immediately. To use this, you will need to globally declare a `volatile bool` to use as the alarm flag and a function that modifies this flag:

```cpp
#include "Inkplate.h"             // Include Inkplate library to the sketch
Inkplate display;  // Create an object on Inkplate library and also set library into 1-bit mode (BW)

volatile int _alarmFlag = 0;      // Variable to store alarm flag

void IRAM_ATTR alarmISR()         // This function will be called when the alarm interrupt event happens
{                                 // NOTE: Function must be above setup() and loop()!
  _alarmFlag = 1;                 // Set alarm flag
}

void setup()
{
    pinMode(39, INPUT_PULLUP);      // Set RTC INT pin on ESP32 GPIO39 as input with pullup resistor enabled

    display.begin();            // Init Inkplate library (you should call this function ONLY ONCE)
    display.rtcReset();         // Reset RTC if there is some data in it
    display.clearDisplay();     // Clear frame buffer of display
    display.display();          // Put clear image on display
    display.setTextSize(3);     // Set text to be 4 times bigger than classic 5x7 px text
  
    display.rtcSetEpoch(1650000000);
    display.rtcSetAlarmEpoch(display.rtcGetEpoch() + 60, RTC_ALARM_MATCH_DHHMMSS);

    // display.rtcSetTime(6, 25, 0);        // Or you can use another way to set the time and date
    // display.rtcSetDate(6, 16, 5, 2020);
    // display.rtcSetAlarm(10, 25, 6, 16, 6); // Set alarm 10 seconds from now
  
    attachInterrupt(39, alarmISR, FALLING); // Set interrupt function and interrupt mode
}

void loop()
{
    display.clearDisplay();         // Clear frame buffer of display
    display.setCursor(60, 100);       // Set position of the text
    display.setTextColor(INKPLATE_RED, INKPLATE_WHITE);         // Set text color and background
    display.rtcGetRtcData();          // Get the time and date from RTC

    // Print the time on screen
    printTime(display.rtcGetHour(), display.rtcGetMinute(), display.rtcGetSecond(), display.rtcGetDay(), display.rtcGetWeekday(), display.rtcGetMonth(), display.rtcGetYear());
    
    if (_alarmFlag)     // Check alarm flag
    {
        // _alarmFlag = 0;              // Uncomment if you want to clear this flag
        display.rtcClearAlarmFlag();    // It's recommended to clear the alarm flag after the alarm has occurred
        display.setCursor(200, 200);      // Set position of the text
        display.print("ALARM");           // Print text
    }
    
    display.display(); // Do a full refresh

    delay(60000); // Wait one minute
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

---  

## Full examples

For full working code examples, which provide a great overview, a real-world use scenario, and **code comments**, see the links below:

<QuickLink 
  title="Inkplate6COLOR_RTC_Simple.ino" 
  description="This example will show how to set time and date, how to read the time, and how to print the time on Inkplate"
  url="https://github.com/SolderedElectronics/Inkplate-Arduino-library/blob/master/examples/Inkplate6COLOR/Advanced/RTC/Inkplate6COLOR_RTC_Simple/Inkplate6COLOR_RTC_Simple.ino" 
/>

<QuickLink 
  title="Inkplate6COLOR_RTC_Interrupt_Alarm.ino" 
  description="This example will show how to set time and date, how to set up an alarm, how to read the time, how to print the time on Inkplate, and how to handle an interrupt."
  url="https://github.com/SolderedElectronics/Inkplate-Arduino-library/blob/master/examples/Inkplate6COLOR/Advanced/RTC/Inkplate6COLOR_RTC_Interrupt_Alarm/Inkplate6COLOR_RTC_Interrupt_Alarm.ino" 
/>