---
slug: /inkplate/2/rtc/alarm
title: RTC alarm
id: 2-rtc-alarm
hide_title: true
---

<SectionTitle title="RTC Alarm" backgroundImage="/img/inkplate_2/hardware.png" />

This page provides two key examples for using the **real-time clock (RTC)** on the Inkplate 2. The examples demonstrate how to retrieve the current time from the internet and how to set a periodic wake-up alarm using Inkplate's RTC functionality.

---

## Example 1: Fetching Time from the Internet

This example shows how to use the **`Network`** object to retrieve the current date and time from an NTP server and display it on the screen.

```cpp
#include "Inkplate.h"
#include "Network.h"

Inkplate display;
Network network;

char ssid[] = "your-ssid";
char pass[] = "your-password";
int timeZone = 2;

struct tm currentTime;
#define DELAY_TIME 40 * 1000

void setup() {
    Serial.begin(115200);
    network.begin(ssid, pass);
    display.begin();
    display.setTextColor(INKPLATE2_BLACK);
}

void loop() {
    network.getTime(&currentTime, timeZone);

    display.clearDisplay();
    display.setCursor(0, 10);
    display.setTextSize(7);
    display.printf("%2.1d:%02d\n", currentTime.tm_hour, currentTime.tm_min);
    display.setTextSize(3);
    display.printf(" %2.1d.%2.1d.%04d\n", currentTime.tm_mday, currentTime.tm_mon + 1, currentTime.tm_year + 1900);
    display.display();

    delay(DELAY_TIME);
}
```

This will print the current time and date based on your time zone, updated approximately every 40 seconds.

---

## Example 2: Periodic Alarm Wake-Up

This example sets an RTC alarm that triggers periodically (every 1 hour and 30 minutes) and checks whether the target date/time has been reached.

```cpp
#include "Inkplate.h"
#include "Network.h"
#include "RTC.h"

Inkplate display;
Network network;
RTC rtc;

char ssid[] = "your-ssid";
char pass[] = "your-password";
int timeZone = 1;

int alarmHour = 8, alarmMins = 0, alarmSecs = 0, alarmDay = 25, alarmMon = 12;
int wakeHours = 1, wakeMinutes = 30;

struct tm currentTime;

void setup() {
    Serial.begin(115200);
    network.begin(ssid, pass);
    network.getTime(&currentTime, timeZone);

    display.begin();
    display.clearDisplay();
    display.setTextColor(INKPLATE2_BLACK);

    int timeUntilAlarmInSeconds = rtc.secondsUntilAlarm(alarmHour, alarmMins, alarmSecs, alarmDay, alarmMon, currentTime);

    if (timeUntilAlarmInSeconds <= 0) {
        alarmScreen();
        while (1) delay(100);
    } else {
        waitingScreen();
        rtc.setWakeUpTimer(wakeHours, wakeMinutes, currentTime);
        esp_deep_sleep_start();
    }
}

void loop() {}

void waitingScreen() {
    display.setTextSize(1);
    display.printf("
           Waiting for: ");
    display.setTextSize(4);
    display.setCursor(0, 33);
    display.printf("  %2.1d:%02d", alarmHour, alarmMins);
    display.setCursor(0, 65);
    display.setTextSize(2);
    display.printf("    on %2.1d.%2.1d.", alarmDay, alarmMon);
    display.display();
}

void alarmScreen() {
    display.setTextSize(2);
    display.setCursor(9, 30);
    display.printf("ALARM!\n");
    display.setTextSize(1);
    display.display();
}
```

This will keep the Inkplate in deep sleep, waking every 1.5 hours to check if the set alarm time has arrived.

---

## Full Examples

<QuickLink 
  title="Inkplate2_RTC_Alarm.ino" 
  description="Displays time and date fetched from an NTP server"
  url="https://github.com/SolderedElectronics/Inkplate-Arduino-library/blob/master/examples/Inkplate2/Advanced/RTC/Inkplate2_RTC_Alarm/Inkplate2_RTC_Alarm.ino" 
/>
<QuickLink 
  title="Inkplate2_RTC_Alarm_Periodic.ino" 
  description="Periodically checks for a predefined alarm time and triggers a screen update"
  url="https://github.com/SolderedElectronics/Inkplate-Arduino-library/blob/master/examples/Inkplate2/Advanced/RTC/Inkplate2_RTC_Alarm_Periodic/Inkplate2_RTC_Alarm_Periodic.ino" 
/>