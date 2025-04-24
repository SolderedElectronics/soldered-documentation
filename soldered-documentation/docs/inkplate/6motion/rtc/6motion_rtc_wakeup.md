---
slug: /inkplate/6motion/rtc/wakeup
title: RTC wakeup
id: 6motion-rtc-wakeup
---


Other than just measuring time while Inkplate is running, it's possible to use the built-in RTC to wake Inkplate up from deep sleep at a certain time.

<InfoBox>For more info on deep sleep on Inkplate 6 MOTION, see [**this**](/inkplate/6motion/low-power/deep-sleep) page.</InfoBox>

<WarningBox>If you want to keep RTC data between sleeps and power-offs, place a **CR2032 battery** in the battery holder.</WarningBox>

---

## Wake from deep sleep at a certain time

To wake the Inkplate from deep sleep at a predefined time, use the RTC's built-in alarm functionality. This allows the device to enter deep sleep mode and automatically wake up at a set time, reducing power consumption.

To configure the RTC alarm for deep sleep wake-up, initialize the RTC and set an alarm using `enableAlarm`. Then, enable the alarm interrupt to allow waking from deep sleep.

```cpp
// Initialize RTC library and set it to 24-hour format
inkplate.rtc.begin(RTC_HOURFORMAT_24);

// Clear any previous alarm flags
inkplate.rtc.checkForAlarm(true);

// Set the RTC time and date if not already set
if (!inkplate.rtc.isRTCSet())
{
    inkplate.rtc.setTime(hours, minutes, seconds, subSeconds);
    inkplate.rtc.setDate(day, month, year, weekday);

    // Enable alarm on RTC Alarm A
    inkplate.rtc.enableAlarm(alarmDay, alarmHour, alarmMinute, alarmSeconds, RTC_ALARM_A, alarmMask);

    // Enable interrupt on alarm event (also used for wake-up)
    inkplate.rtc.enableAlarmInterrupt(NULL);
}
```

<FunctionDocumentation functionName="inkplate.rtc.enableAlarm()" 
  description="Sets an RTC alarm that can wake the Inkplate from deep sleep at a specific time." 
  returnDescription="Returns true if the alarm was successfully enabled, false otherwise." 
  parameters={[
    { type: 'uint8_t', name: 'day', description: "Day of the month for the RTC alarm." }, 
    { type: 'uint8_t', name: 'hour', description: "Hour of the alarm time (24-hour format)." }, 
    { type: 'uint8_t', name: 'minute', description: "Minute of the alarm time." }, 
    { type: 'uint8_t', name: 'second', description: "Second of the alarm time." }, 
    { type: 'uint32_t', name: 'alarmType', description: "Select the alarm type, RTC_ALARM_A or RTC_ALARM_B. Note: Alarm B has limited functionality." }, 
    { type: 'uint32_t', name: 'alarmMask', description: "Bitmask defining which fields must match for the alarm to trigger. Options include RTC_ALARMMASK_DATEWEEKDAY (daily), RTC_ALARMMASK_HOURS (hourly), RTC_ALARMMASK_MINUTES (every minute), RTC_ALARMMASK_SECONDS (every second), and RTC_ALARMMASK_ALL (always triggers)." }, 
    { type: 'uint8_t', name: 'pmAm', description: "PM/AM indicator, used only if 12-hour mode is enabled. Options: RTC_HOURFORMAT12_AM, RTC_HOURFORMAT12_PM." }, 
    { type: 'uint32_t', name: 'dayLightSaving', description: "Daylight saving time adjustment. Options: RTC_DAYLIGHTSAVING_SUB1H (subtract 1 hour), RTC_DAYLIGHTSAVING_ADD1H (add 1 hour), RTC_DAYLIGHTSAVING_NONE (no adjustment)." }
  ]} 
/>


For more info on `alarmMask` check the [**RTC alarm**](/inkplate/6motion/rtc/alarm) page.


<FunctionDocumentation functionName="inkplate.rtc.enableAlarmInterrupt()" 
  description="Enables an interrupt for the RTC alarm event. This allows Inkplate to wake up from deep sleep when the alarm triggers." 
  returnDescription="Returns true if the interrupt was successfully enabled, false otherwise." 
  parameters={[
    { type: 'void(*)()', name: 'callback', description: "Pointer to a function that executes when the alarm triggers. Use NULL if no callback function is required." }
  ]} 
/>


---

## Full example

For a complete example that demonstrates how to use RTC alarms to wake Inkplate from deep sleep, see the link below:

<QuickLink 
  title="Inkplate_6_Motion_RTC_Alarm_Interrupt.ino" 
  description="Full example demonstrating how to configure RTC wake-up from deep sleep." 
  url="https://github.com/SolderedElectronics/Inkplate_Motion_Arduino_Library/blob/main/examples/Inkplate6Motion/Advanced/RTC/Inkplate_6_Motion_RTC_Deep_Sleep_Wakeup/Inkplate_6_Motion_RTC_Deep_Sleep_Wakeup.ino" 
/>