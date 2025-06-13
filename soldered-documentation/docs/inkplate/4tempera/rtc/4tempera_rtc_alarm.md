---  
slug: /inkplate/4tempera/rtc/alarm  
title: Inkplate 4TEMPERA – RTC alarm
id: 4tempera-rtc-alarm  
hide_title: true
---

<SectionTitle title="RTC Alarm" backgroundImage="/img/inkplate_2/hardware.png" />

The onboard RTC supports creating an alarm that triggers at a specific time, allowing the firmware to detect and respond accordingly. Alarms can be configured to trigger once per day, per hour, or per minute.

---

## Simple alarm

This section demonstrates how to set a simple RTC alarm that is checked using polling. The firmware continuously checks the alarm flag and responds when it is triggered.

```cpp
#include "Inkplate.h"            // Include the Inkplate library in the sketch
Inkplate inkplate(INKPLATE_1BIT); // Create an Inkplate object and set the library to 1-bit mode (BW)

#define REFRESH_DELAY 1000 // Delay between refreshes
unsigned long time1;       // Variable for measuring refresh time in millis

// Set clock
uint8_t hour = 12;
uint8_t minutes = 50;
uint8_t seconds = 30;

// Set date and weekday (NOTE: In weekdays, 0 means Sunday, 1 means Monday, etc.)
uint8_t weekday = 1;
uint8_t day = 20;
uint8_t month = 2;
uint8_t year = 23;

// Set alarm time and date (the alarm will be generated 10 seconds after board power-up)
uint8_t alarmHour = 12;
uint8_t alarmMinutes = 50;
uint8_t alarmSeconds = 40;
uint8_t alarmWeekday = 1;
uint8_t alarmDay = 20;

void setup()
{
    inkplate.begin();        // Initialize the Inkplate library (call this function ONLY ONCE)
    inkplate.clearDisplay(); // Clear the frame buffer of Inkplate
    inkplate.display();      // Display the cleared image on Inkplate
    inkplate.setTextSize(5); // Set text to be 5 times larger than the classic 5x7 px text

    inkplate.rtcSetTime(hour, minutes, seconds);                                         // Send time to RTC
    inkplate.rtcSetDate(weekday, day, month, year);                                      // Send date to RTC
    inkplate.rtcSetAlarm(alarmSeconds, alarmMinutes, alarmHour, alarmDay, alarmWeekday); // Set alarm
}

// Variable that keeps count of how many times the screen has been partially updated
int n = 0;
void loop()
{
    if ((unsigned long)(millis() - time1) > REFRESH_DELAY)
    {
        inkplate.rtcGetRtcData();           // Get the time and date from RTC
        seconds = inkplate.rtcGetSecond();  // Store seconds in a variable
        minutes = inkplate.rtcGetMinute();  // Store minutes in a variable
        hour = inkplate.rtcGetHour();       // Store hours in a variable
        day = inkplate.rtcGetDay();         // Store the day of the month in a variable
        weekday = inkplate.rtcGetWeekday(); // Store the day of the week in a variable
        month = inkplate.rtcGetMonth();     // Store month in a variable
        year = inkplate.rtcGetYear();       // Store year in a variable

        inkplate.clearDisplay();                                       // Clear content in the frame buffer
        inkplate.setCursor(100, 300);                                  // Set the position of the text
        printTime(hour, minutes, seconds, day, weekday, month, year); // Print the time on the screen

        if (inkplate.rtcCheckAlarmFlag()) // Check if the alarm has occurred
        {
            inkplate.rtcClearAlarmFlag(); // It is recommended to clear the alarm flag after the alarm occurs
            inkplate.setCursor(400, 400); // Set a new cursor position
            inkplate.print("ALARM!");
        }

        if (n > 9) // Check if a full refresh is required or if a partial update is sufficient
        {
            inkplate.display(true); // Perform a full refresh
            n = 0;
        }
        else
        {
            inkplate.partialUpdate(false, true); // Perform a partial update and keep the e-paper power supply on
            n++;                                // Increment the count of partial updates
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
    description="Sets the alarm with all the provided parameters."
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
  description="Checks if the alarm flag is set"
  returnDescription="Returns true if the alarm flag is set"
  returnType="bool"
/>

---

## Interrupt Alarm
The RTC alarm can also generate an **interrupt** instead of requiring polling. The alarm event can wake up the MCU from sleep or trigger an action immediately. To use this, you will need to globally declare a `volatile bool` (or an appropriate type) to use as the alarm flag and create a function to modify this flag:

```cpp
#include "Inkplate.h"             // Include the Inkplate library in the sketch
Inkplate inkplate(INKPLATE_1BIT);  // Create an Inkplate object and set the library to 1-bit mode (BW)

volatile int _alarmFlag = 0;      // Variable to store the alarm flag

void IRAM_ATTR alarmISR()         // This function will be called when the alarm interrupt event occurs
{                                 // NOTE: This function must be declared above setup() and loop()!
  _alarmFlag = 1;                 // Set the alarm flag
}

void setup()
{
    pinMode(39, INPUT_PULLUP);      // Set the RTC INT pin on ESP32 GPIO39 as input with pullup resistor enabled

    inkplate.begin();        // Initialize the Inkplate library (call this function ONLY ONCE)
    inkplate.clearDisplay(); // Clear the frame buffer of Inkplate
    inkplate.display();      // Display the cleared image on Inkplate
    inkplate.setTextSize(5); // Set text to be 5 times larger than the classic 5x7 px text
  
    inkplate.rtcSetEpoch(1589610300);
    inkplate.rtcSetAlarmEpoch(inkplate.rtcGetEpoch() + 10, RTC_ALARM_MATCH_DHHMMSS);

    // inkplate.rtcSetTime(6, 25, 0);        // Alternatively, you can set the time and date in another way
    // inkplate.rtcSetDate(6, 16, 5, 2020);
    // inkplate.rtcSetAlarm(10, 25, 6, 16, 6); // Set an alarm 10 seconds from now
  
    attachInterrupt(39, alarmISR, FALLING); // Set the interrupt function and mode
}

// Variable that keeps count of how many times the screen has been partially updated
int n = 0;
void loop()
{
    inkplate.clearDisplay();         // Clear the frame buffer of Inkplate
    inkplate.setCursor(100, 100);    // Set the position of the text
    inkplate.rtcGetRtcData();          // Get the time and date from the RTC

    // Print the time on the screen
    printTime(inkplate.rtcGetHour(), inkplate.rtcGetMinute(), inkplate.rtcGetSecond(), inkplate.rtcGetDay(), inkplate.rtcGetWeekday(), inkplate.rtcGetMonth(), inkplate.rtcGetYear());
    
    if (_alarmFlag)     // Check the alarm flag
    {
        // _alarmFlag = 0;              // Uncomment this line if you want to clear the flag
        inkplate.rtcClearAlarmFlag();    // It is recommended to clear the alarm flag after the alarm occurs
        inkplate.setCursor(200, 200);    // Set the position of the text
        inkplate.print("ALARM");         // Print the "ALARM" text
    }
    
    if (n > 9) // Check if a full refresh is required or if a partial update is sufficient
    {
        inkplate.display(true); // Perform a full refresh
        n = 0;
    }
    else
    {
        inkplate.partialUpdate(false, true); // Perform a partial update and keep the e-paper power supply on
        n++;                                // Increment the count of partial updates
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

For full working code examples that provide a great overview, a real-world use scenario, and **code comments**, see the links below:

<QuickLink 
  title="Inkplate4TEMPERA_RTC_Alarm.ino" 
  description="This example shows how to set the time and date, how to set up an alarm, how to read time, how to print time on Inkplate using partial updates, and how to handle interrupts."
  url="https://github.com/SolderedElectronics/Inkplate-Arduino-library/tree/master/examples/Inkplate4TEMPERA/Advanced/RTC/Inkplate4TEMPERA_RTC_Alarm" 
/>

<QuickLink 
  title="Inkplate4TEMPERA_RTC_Interrupt_Alarm.ino" 
  description="This example shows how to set the time and date, how to set up an alarm, how to read time, how to print time on Inkplate using partial updates, and how to handle interrupts."
  url="https://github.com/SolderedElectronics/Inkplate-Arduino-library/blob/master/examples/Inkplate4TEMPERA/Advanced/RTC/Inkplate4TEMPERA_RTC_Interrupt_Alarm/Inkplate4TEMPERA_RTC_Interrupt_Alarm.ino" 
/>