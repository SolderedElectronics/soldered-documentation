---  
slug: /inkplate/6/rtc/alarm  
title: Inkplate 6 – RTC alarm
id: rtc-alarm  
---  

The onboard RTC supports creating an alarm that triggers at a specific time, allowing the firmware to detect and respond accordingly. Alarms can be configured to trigger once per day, per hour, or per minute.

---  

## Simple alarm

This section demonstrates setting a simple RTC alarm that is checked using polling. The firmware continuously checks the alarm flag and responds when it is triggered.

```cpp
#include "Inkplate.h"            // Include the Inkplate library in the sketch
Inkplate inkplate(INKPLATE_1BIT); // Create an Inkplate object and set the library to 1-bit mode (BW)

#define REFRESH_DELAY 1000 // Delay between refreshes
unsigned long time1;       // Time for measuring refresh in millis

// Set clock
uint8_t hour = 12;
uint8_t minutes = 50;
uint8_t seconds = 30;

// Set date and weekday (NOTE: For weekdays, 0 means Sunday, 1 means Monday, ...)
uint8_t weekday = 1;
uint8_t day = 20;
uint8_t month = 2;
uint8_t year = 23;

// Set alarm time and date (the alarm will be generated 10 seconds after board power up)
uint8_t alarmHour = 12;
uint8_t alarmMinutes = 50;
uint8_t alarmSeconds = 40;
uint8_t alarmWeekday = 1;
uint8_t alarmDay = 20;

void setup()
{
    inkplate.begin();        // Initialize the Inkplate library (you should call this function ONLY ONCE)
    inkplate.clearDisplay(); // Clear the frame buffer of Inkplate
    inkplate.display();      // Display the cleared image on Inkplate
    inkplate.setTextSize(3); // Set text to be three times larger than the classic 5x7 px text

    inkplate.rtcSetTime(hour, minutes, seconds);                                         // Send time to the RTC
    inkplate.rtcSetDate(weekday, day, month, year);                                      // Send date to the RTC
    inkplate.rtcSetAlarm(alarmSeconds, alarmMinutes, alarmHour, alarmDay, alarmWeekday); // Set the alarm
}

// Variable that keeps count of how many times the screen has been partially updated
int n = 0;
void loop()
{
    if ((unsigned long)(millis() - time1) > REFRESH_DELAY)
    {
        inkplate.rtcGetRtcData();           // Get the time and date from the RTC
        seconds = inkplate.rtcGetSecond();  // Store seconds in a variable
        minutes = inkplate.rtcGetMinute();  // Store minutes in a variable
        hour = inkplate.rtcGetHour();       // Store hours in a variable
        day = inkplate.rtcGetDay();         // Store day of the month in a variable
        weekday = inkplate.rtcGetWeekday(); // Store day of the week in a variable
        month = inkplate.rtcGetMonth();     // Store month in a variable
        year = inkplate.rtcGetYear();       // Store year in a variable

        inkplate.clearDisplay();                                       // Clear content in the frame buffer
        inkplate.setCursor(100, 300);                                  // Set the position of the text
        printTime(hour, minutes, seconds, day, weekday, month, year); // Print the time on the screen

        if (inkplate.rtcCheckAlarmFlag()) // Check if the alarm has occurred
        {
            inkplate.rtcClearAlarmFlag(); // It is recommended to clear the alarm flag after the alarm has occurred
            inkplate.setCursor(400, 400); // Set a new position for the cursor
            inkplate.print("ALARM!");
        }

        if (n > 9) // Check if a full refresh is needed or if a partial update is sufficient
        {
            inkplate.display(true); // Do a full refresh
            n = 0;
        }
        else
        {
            inkplate.partialUpdate(false, true); // Do a partial update and keep the e-paper power supply on
            n++;                                 // Keep track of how many times the screen has been partially updated
        }

        time1 = millis(); // Store the current millis
    }
}

void printTime(uint8_t _hour, uint8_t _minutes, uint8_t _seconds, uint8_t _day, uint8_t _weekday, uint16_t _month,
               uint8_t _year)
{
    // Write time and date information on the screen
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
    functionName="inkplate.rtcSetAlarm()"
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
  functionName="inkplate.rtcCheckAlarmFlag()"
  description="Checks if the alarm flag is on"
  returnDescription="Returns true if the alarm flag is on"
  returnType="bool"
/>

---  

## Interrupt Alarm
The RTC alarm can also generate an **interrupt** instead of requiring polling. The alarm event can wake up the MCU from sleep or trigger an action immediately. To use this, you will need to globally declare a volatile flag variable (for example, volatile int _alarmFlag) to use as the alarm flag and a function that modifies this flag:

```cpp
#include "Inkplate.h"             // Include the Inkplate library in the sketch
Inkplate inkplate(INKPLATE_1BIT);  // Create an Inkplate object and set the library to 1-bit mode (BW)

volatile int _alarmFlag = 0;      // Variable to store the alarm flag

void IRAM_ATTR alarmISR()         // This function will be called when an alarm interrupt event occurs
{                                 // NOTE: The function must be declared before setup() and loop()!
  _alarmFlag = 1;                 // Set the alarm flag
}

void setup()
{
    pinMode(39, INPUT_PULLUP);      // Set the RTC INT pin on ESP32 GPIO39 as input with the pull-up resistor enabled

    inkplate.begin();        // Initialize the Inkplate library (you should call this function ONLY ONCE)
    inkplate.clearDisplay(); // Clear the frame buffer of Inkplate
    inkplate.display();      // Display the cleared image on Inkplate
    inkplate.setTextSize(3); // Set text to be three times larger than the classic 5x7 px text
  
    inkplate.rtcSetEpoch(1589610300);
    inkplate.rtcSetAlarmEpoch(inkplate.rtcGetEpoch() + 10, RTC_ALARM_MATCH_DHHMMSS);

    // inkplate.rtcSetTime(6, 25, 0);        // Or you can use another method to set the time and date
    // inkplate.rtcSetDate(6, 16, 5, 2020);
    // inkplate.rtcSetAlarm(10, 25, 6, 16, 6); // Set an alarm 10 seconds from now
  
    attachInterrupt(39, alarmISR, FALLING); // Set the interrupt function and interrupt mode
}

// Variable that keeps count of how many times the screen has been partially updated
int n = 0;
void loop()
{
    inkplate.clearDisplay();         // Clear the frame buffer of Inkplate
    inkplate.setCursor(100, 100);      // Set the position of the text
    inkplate.rtcGetRtcData();          // Get the time and date from the RTC

    // Print the time on the screen
    printTime(inkplate.rtcGetHour(), inkplate.rtcGetMinute(), inkplate.rtcGetSecond(), inkplate.rtcGetDay(), inkplate.rtcGetWeekday(), inkplate.rtcGetMonth(), inkplate.rtcGetYear());
    
    if (_alarmFlag)     // Check the alarm flag
    {
        // _alarmFlag = 0;              // Uncomment if you want to clear this flag
        inkplate.rtcClearAlarmFlag();    // It is recommended to clear the alarm flag after the alarm has occurred
        inkplate.setCursor(200, 200);    // Set the position of the text
        inkplate.print("ALARM");         // Print the text
    }
    
    if (n > 9) // Check if a full refresh is needed or if a partial update is sufficient
    {
        inkplate.display(true); // Do a full refresh
        n = 0;
    }
    else
    {
        inkplate.partialUpdate(false, true); // Do a partial update and keep the e-paper power supply on
        n++;                                 // Keep track of how many times the screen has been partially updated
    }

    delay(700);                             // Delay between refreshes.
}

void printTime(uint8_t _hour, uint8_t _minutes, uint8_t _seconds, uint8_t _day, uint8_t _weekday, uint8_t _month,
               uint16_t _year)
{
    // Write time and date information on the screen
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