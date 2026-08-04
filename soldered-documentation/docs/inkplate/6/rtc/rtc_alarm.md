---  
slug: /inkplate/6/rtc/alarm  
title: Inkplate 6 – RTC alarm
sidebar_label: RTC alarm
id: rtc-alarm  
---  

The onboard RTC supports creating an alarm that triggers at a specific time, allowing the firmware to detect and respond accordingly. Alarms can be configured to trigger once per day, per hour, or per minute.

---  

## Simple alarm

This section demonstrates setting a simple RTC alarm that is checked using polling. The firmware continuously checks the alarm flag and responds when it is triggered.

```cpp
#include "Inkplate.h"            // Include Inkplate library to the sketch
Inkplate display(INKPLATE_1BIT); // Create an object on Inkplate library and also set library into 1-bit mode (BW)

#define REFRESH_DELAY 1000 // Delay between refreshes
unsigned long time1;       // Time for measuring refresh in millis

// Set clock
uint8_t hour = 12;
uint8_t minutes = 50;
uint8_t seconds = 30;

// Set date and weekday (NOTE: In weekdays 0 means Sunday, 1 means Monday, ...)
uint8_t weekday = 1;
uint8_t day = 20;
uint8_t month = 2;
uint8_t year = 23;

// Set alarm time and date (alarm will be generated 10 seconds after board power up)
uint8_t alarmHour = 12;
uint8_t alarmMinutes = 50;
uint8_t alarmSeconds = 40;
uint8_t alarmWeekday = 1;
uint8_t alarmDay = 20;

void setup()
{
    display.begin();        // Init Inkplate library (you should call this function ONLY ONCE)
    display.clearDisplay(); // Clear frame buffer of display
    display.display();      // Put clear image on display
    display.setTextSize(4); // Set text to be 4 times bigger than classic 5x7 px text

    display.rtc.setTime(hour, minutes, seconds);                                         // Send time to RTC
    display.rtc.setDate(weekday, day, month, year);                                      // Send date to RTC
    display.rtc.setAlarm(alarmSeconds, alarmMinutes, alarmHour, alarmDay, alarmWeekday); // Set alarm
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

        if (display.rtc.checkAlarmFlag()) // Check if alarm has occurred
        {
            display.rtc.clearAlarmFlag(); // It's recommended to clear alarm flag after alarm has occurred
            display.setCursor(400, 400); // Set new position for cursor
            display.print("ALARM!");
        }

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
    functionName="display.rtc.setAlarm()"
    description="Sets the alarm using the provided parameters."
    returnType="void"
    parameters={[ 
    { type: 'uint8_t', name: 'rtcAlarmSecond', description: 'Set the alarm seconds.' },
    { type: 'uint8_t', name: 'rtcAlarmminute', description: 'Set the alarm minutes.' },
    { type: 'uint8_t', name: 'rtcAlarmHour', description: 'Set the alarm hours.' },
    { type: 'uint8_t', name: 'rtcAlarmDay', description: 'Set the alarm day.' },
    { type: 'uint8_t', name: 'rtcAlarmWeekday', description: 'Set the alarm weekday.' },
    ]}
 />

<FunctionDocumentation
  functionName="display.rtc.checkAlarmFlag()"
  description="Checks if the alarm flag is on"
  returnDescription="Returns true if the alarm flag is on"
  returnType="bool"
/>

---  

## Interrupt alarm
The RTC alarm can also generate an **interrupt** instead of requiring polling. The alarm event can wake up the MCU from sleep or trigger an action immediately. To use this, you will need to globally declare a volatile flag variable (for example, volatile int _alarmFlag) to use as the alarm flag and a function that modifies this flag:

```cpp
#include "Inkplate.h"             // Include Inkplate library to the sketch
Inkplate display(INKPLATE_1BIT);  // Create an object on Inkplate library and also set library into 1-bit mode (BW)

volatile int _alarmFlag = 0;      // Variable to store alarm flag

void IRAM_ATTR alarmISR()         // This function will be called when alarm interrupt event happens
{                                 // NOTE: Function must be above setup() and loop()!
  _alarmFlag = 1;                 // Set alarm flag
}

void setup()
{
    pinMode(39, INPUT_PULLUP);      // Set RTC INT pin on ESP32 GPIO39 as input with pullup resistor enabled

    display.begin();        // Init Inkplate library (you should call this function ONLY ONCE)
    display.clearDisplay(); // Clear frame buffer of display
    display.display();      // Put clear image on display
    display.setTextSize(4); // Set text to be 4 times bigger than classic 5x7 px text
  
    display.rtc.setEpoch(1589610300);
    display.rtc.setAlarmEpoch(display.rtc.getEpoch() + 10, RTC_ALARM_MATCH_DHHMMSS);

    // display.rtc.setTime(6, 25, 0);        // Or you can use other way to set the time and date
    // display.rtc.setDate(6, 16, 5, 2020);
    // display.rtc.setAlarm(10, 25, 6, 16, 6); // Set alarm 10 seconds from now
  
    attachInterrupt(39, alarmISR, FALLING); // Set interrupt function and interrupt mode
}

// Variable that keeps count on how much screen has been partially updated
int n = 0;
void loop()
{
    display.clearDisplay();         // Clear frame buffer of display
    display.setCursor(100, 100);    // Set position of the text
    display.rtc.getRtcData();          // Get the time and date from RTC

    // Print the time on screen
    printTime(display.rtc.getHour(), display.rtc.getMinute(), display.rtc.getSecond(), display.rtc.getDay(), display.rtc.getWeekday(), display.rtc.getMonth(), display.rtc.getYear());
    
    if (_alarmFlag)     // Check alarm flag
    {
        // _alarmFlag = 0;              // Uncomment if you want to clear this flag
        display.rtc.clearAlarmFlag();    // It's recommended to clear alarm flag after alarm has occurred
        display.setCursor(200, 200);    // Set position of the text
        display.print("ALARM");         // Print text
    }
    
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

    delay(700);                             // Delay between refreshes.
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

For full working code examples, which provide an excellent overview, a real-world use scenario, and **code comments**, see the links below:

<QuickLink 
  title="Inkplate6_RTC_Simple.ino" 
  description="This example shows how to set the time and date, how to read the time, and how to print the time on Inkplate using partial updates."
  url="https://github.com/SolderedElectronics/Inkplate-Arduino-library/blob/master/examples/Inkplate6/Advanced/RTC/Inkplate6_RTC_Simple/Inkplate6_RTC_Simple.ino" 
/>

<QuickLink 
  title="Inkplate6_RTC_Interrupt_Alarm.ino" 
  description="This example shows how to set the time and date, set up an alarm, read the time, print the time on Inkplate using partial updates, and handle an interrupt."
  url="https://github.com/SolderedElectronics/Inkplate-Arduino-library/blob/master/examples/Inkplate6/Advanced/RTC/Inkplate6_RTC_Interrupt_Alarm/Inkplate6_RTC_Interrupt_Alarm.ino" 
/>