---
slug: /inkplate/6motion/rtc/alarm
title: "Inkplate \u2013 6Motion RTC Alarm"
id: 6motion-rtc-alarm
---
The built-in RTC supports creating an alarm that triggers at a specific time, allowing the firmware to detect and respond accordingly. Alarms can be configured to trigger once per day, per hour, or per minute.

---

## Simple alarm

This section demonstrates setting a simple RTC alarm that is checked using polling. The firmware continuously checks the alarm flag and responds when it is triggered.

```cpp
// Initialize RTC in 24-hour format and reset it
inkplate.rtc.begin(RTC_HOURFORMAT_24, true);

// Set the time and date
inkplate.rtc.setTime(12, 24, 25, 0); // Set time to 12:24:25
inkplate.rtc.setDate(29, 5, 24, RTC_WEEKDAY_MONDAY); // Set date to 29/5/2024, Monday

// Enable an alarm at 12:24:35 on the same day
inkplate.rtc.enableSimpleAlarm(29, 12, 24, 35, RTC_ALARM_A, RTC_ALARMMASK_DATEWEEKDAY | RTC_ALARMMASK_HOURS | RTC_ALARMMASK_MINUTES);

// Use polling method to detect alarm event
while(true)
{
    // Check the RTC
    if (inkplate.rtc.checkForAlarm())
    {
        // Alarm is detected!
        // Print out the message
        inkplate.setCursor(320, 450);
        inkplate.println("ALARM EVENT!");
        // Let's display the message and halt the code here
        inkplate.display();

        // You can of course continue the code from here in any other use case
        // Use inkplate.rtc.checkForAlarm(true) to clear the alarm flag
    }
    delay(1000); // Wait a second between polling the RTC
}
```

<FunctionDocumentation functionName="inkplate.rtc.enableSimpleAlarm()" description="Enables a simple RTC alarm without interrupts. The alarm must be checked using polling." returnDescription="none" parameters={[ { type: 'uint8_t', name: '_d', description: "Day of the month to trigger the alarm." }, { type: 'uint8_t', name: '_h', description: "Hour value for the alarm." }, { type: 'uint8_t', name: '_m', description: "Minute value for the alarm." }, { type: 'uint8_t', name: '_s', description: "Second value for the alarm." }, { type: 'uint32_t', name: '_alarm', description: "Select which alarm to use. Use RTC_ALARM_A or RTC_ALARM_B (limited support for Alarm B)." }, { type: 'uint32_t', name: '_alarmMask', description: "Defines when the alarm should trigger. See the table below." }, { type: 'uint8_t', name: '_pmAm', description: "Optional. PM/AM indicator (only relevant in 12-hour mode)." }, { type: 'uint32_t', name: '_dayLightSaving', description: "Optional. Daylight saving setting: RTC_DAYLIGHTSAVING_SUB1H, RTC_DAYLIGHTSAVING_ADD1H, or RTC_DAYLIGHTSAVING_NONE." } ]} />

The alarm masks essentially can filter out certain information for the alarm, making it easy to tirgger it always at a certain time. If you want to use multiple flags, they have to be `OR`'d together:

| Alarm Frequency     | Mask Definition                                                 |
| ------------------- | --------------------------------------------------------------- |
| **Once per day**    | RTC_ALARMMASK_DATEWEEKDAY                                       |
| **Once per hour**   | RTC_ALARMMASK_DATEWEEKDAY                                       | RTC_ALARMMASK_HOURS |
| **Once per minute** | RTC_ALARMMASK_DATEWEEKDAY                                       | RTC_ALARMMASK_HOURS | RTC_ALARMMASK_MINUTES |
| **Every second**    | RTC_ALARMMASK_ALL *(ignores all fields, triggers continuously)* |

<FunctionDocumentation functionName="inkplate.rtc.checkForAlarm()" description="Checks if an RTC alarm has been triggered." returnDescription="Returns true if the alarm was triggered, otherwise false." parameters={[ { type: 'bool', name: '_clearFlag', description: "Set to true to clear the alarm flag immediately, false to keep it active." } ]} />

---

## Interrupt Alarm

The RTC alarm can also generate an **interrupt** instead of requiring polling. The alarm event can wake up the MCU from sleep or trigger an action immediately. To use this, you will need to globally declare a `volatile bool` to use as the alarm flag and a function which modifies this flag:

```cpp
volatile bool alarmFlag = false;
// Function will be called on every alarm event
void alarmFunction()
{
    alarmFlag = true;
}
```
And then, in the body of the sketch:
```cpp
// Initialize RTC in 24-hour format and reset it
inkplate.rtc.begin(RTC_HOURFORMAT_24, true);

// Set the time and date
inkplate.rtc.setTime(12, 24, 25, 0); // Set time to 12:24:25
inkplate.rtc.setDate(29, 5, 24, RTC_WEEKDAY_MONDAY); // Set date to 29/5/2024, Monday

// Enable an alarm at 12:24:35 on the same day
inkplate.rtc.enableAlarm(29, 12, 24, 35, RTC_ALARM_A, RTC_ALARMMASK_DATEWEEKDAY | RTC_ALARMMASK_HOURS | RTC_ALARMMASK_MINUTES);

// Enable the alarm interrupt
inkplate.rtc.enableAlarmInterrupt(alarmFunction);

// Let's periodically check for the interrupt  flag
while(true)
{
    // Check for alarm event
    if (alarmFlag)
    {
        // Clear the flag
        alarmFlag = false;
        // Print out the message
        inkplate.print("Interrupt alarm!");
        inkplate.display();
        // Continue alarm-handling code here as you wish
        // In this example, just stop the sketch
        while(true)
            delay(100);
    }
}
```

<FunctionDocumentation
  functionName="inkplate.rtc.enableAlarmInterrupt()"
  description="Enables an RTC alarm interrupt, triggering a callback function when the alarm occurs."
  returnDescription="none"
  parameters={[
    { type: 'void(*)()', name: '_f', description: "Pointer to callback function that will be executed when the alarm triggers." }
  ]}
/>

<FunctionDocumentation
  functionName="inkplate.rtc.disableAlarmInterrupt()"
  description="Disables the RTC alarm interrupt, preventing further callback executions."
  returnDescription="none"
/>

---

## Alarm output

Other than just being detected internally within Inkplate, it's possible to output a pulse output the STM32 pin `PC13` by calling `inkplate.rtc.setAlarmOutput()`:

```cpp
inkplate.rtc.setAlarmOutput(true, RTC_OUTPUT_ALARMA);
```

<FunctionDocumentation functionName="inkplate.rtc.setAlarmOutput()" description="Routes the RTC alarm signal to a GPIO pin, allowing external hardware to detect the alarm event." returnDescription="none" parameters={[ { type: 'bool', name: '_outEn', description: "Set to true to enable the RTC Alarm Output on the GPIO pin, or false to disable it." }, { type: 'uint32_t', name: '_alarm', description: "Select which alarm output to use: RTC_OUTPUT_ALARMA (pin PC13), RTC_OUTPUT_ALARMB, or RTC_OUTPUT_DISABLE." } ]} />

<WarningBox>Using **RTC_OUTPUT_ALARMB** is not yet implemented!</WarningBox>

---

## Full examples

For full working code examples, which provide a great overwiew, a real-world use scenario and **code comments**, see the links below:

<QuickLink 
  title="Inkplate_6_Motion_Simple_Alarm.ino" 
  description="How to set a polling alarm with the internal RTC on Inkplate 6 MOTION"
  url="https://github.com/SolderedElectronics/Inkplate_Motion_Arduino_Library/blob/main/examples/Inkplate6Motion/Advanced/RTC/Inkplate_6_Motion_Simple_Alarm/Inkplate_6_Motion_Simple_Alarm.ino" 
/>

<QuickLink 
  title="Inkplate_6_Motion_RTC_Alarm_Interrupt.ino" 
  description="Full example on how to detect alarm via interrupt"
  url="https://github.com/SolderedElectronics/Inkplate_Motion_Arduino_Library/blob/main/examples/Inkplate6Motion/Advanced/RTC/Inkplate_6_Motion_RTC_Alarm_Interrupt/Inkplate_6_Motion_RTC_Alarm_Interrupt.ino" 
/>

<QuickLink 
  title="Inkplate_6_Motion_RTC_Alarm_Output.ino" 
  description="Pulse an external LED when the alarm is triggered"
  url="https://github.com/SolderedElectronics/Inkplate_Motion_Arduino_Library/blob/main/examples/Inkplate6Motion/Advanced/RTC/Inkplate_6_Motion_RTC_Alarm_Output/Inkplate_6_Motion_RTC_Alarm_Output.ino" 
/>