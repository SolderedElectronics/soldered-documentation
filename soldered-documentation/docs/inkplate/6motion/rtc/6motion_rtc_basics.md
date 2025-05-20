---
slug: /inkplate/6motion/rtc/basics
title: 6Motion - RTC basics
id: 6motion-rtc-basics
hide_title: true
---

<SectionTitle title="RTC basics" backgroundImage="/img/rtc.png" />

The real time clock on Inkplate 6 MOTION is the **internal RTC of the STM32H743ZIT6**. The RTC uses an external clock source, an external XTAL of 32.768kHz.

---

## Initializing

The RTC is initialized by calling `inkplate.rtc.begin()`:

```cpp
inkplate.rtc.begin(RTC_HOURFORMAT_24);
```
<FunctionDocumentation
  functionName="inkplate.rtc.begin()"
  description="Initializes the RTC inside the STM32."
  returnDescription="Returns an instance of RTC_HandleTypeDef, the STM32duino RTC object. This is not nescessary to use as the RTC can be interfaced with using our library, but it's returned in case you need it."
  parameters={[
    { type: 'uint8_t', name: '_format', description: "Clock format - RTC_HOURFORMAT_24 for 24-hour format or RTC_HOURFORMAT_12 for 12-hour format." },
    { type: 'bool', name: '_resetRtc', description: "Optional. If set to true, forces RTC reset, overriding the previously set RTC." },
  ]}
/>

---

## Setting time and date

Setting the current time and date is the most basic RTC usage. Once you set the time, it will keep 'ticking' and you will be able to get the current time later and it will be accurate. Of course, the RTC isn't perfect so during one day it will drift off a couple seconds early or late. If you're using the RTC, **it's reccomended to set it approx. once per day**.

```cpp

// Check if the time is already set. If not, set it!
if (!inkplate.rtc.isRTCSet()) {
    inkplate.rtc.setTime(12, 24, 25, 0); // Set time to 12:24:25
    inkplate.rtc.setDate(29, 5, 24, RTC_WEEKDAY_MONDAY); // Set date to 29/5/2024, Monday
}
```

<FunctionDocumentation
  functionName="inkplate.rtc.isRTCSet()"
  description="Checks whether the RTC is set. If not, the RTC needs to be manually configured."
  returnDescription="Returns true if the RTC is already set, otherwise false."
/>

<FunctionDocumentation
  functionName="inkplate.rtc.setTime()"
  description="Sets the time inside the STM32 RTC using a human-readable format."
  returnDescription="none"
  parameters={[
    { type: 'uint8_t', name: '_h', description: "RTC Hour value." },
    { type: 'uint8_t', name: '_m', description: "RTC Minute value." },
    { type: 'uint8_t', name: '_s', description: "RTC Seconds value." },
    { type: 'uint32_t', name: '_ss', description: "RTC Sub-Seconds value." },
    { type: 'uint8_t', name: '_pmAm', description: "Optional. PM/AM indicator. Use RTC_HOURFORMAT12_AM or RTC_HOURFORMAT12_PM." },
    { type: 'uint32_t', name: '_dayLightSaving', description: "Optional. Daylight saving setting. Possible values: RTC_DAYLIGHTSAVING_SUB1H (Subtract one hour), RTC_DAYLIGHTSAVING_ADD1H (Add one hour), RTC_DAYLIGHTSAVING_NONE (Disabled)." }
  ]}
/>

<FunctionDocumentation
  functionName="inkplate.rtc.setDate()"
  description="Sets the date inside the STM32 RTC."
  returnDescription="none"
  parameters={[
    { type: 'uint8_t', name: '_d', description: "Day of the month." },
    { type: 'uint8_t', name: '_m', description: "Month value." },
    { type: 'uint16_t', name: '_y', description: "Year value." },
    { type: 'uint8_t', name: '_weekday', description: "Weekday value." }
  ]}
/>

<WarningBox>In the current version of the Inkplate 6 MOTION library, you cannot use epoch to set the time in the RTC.</WarningBox>

---

## Getting time and date

To retrieve the time and date after setting them, use `inkplate.rtc.getTime()`. These functions take pointers to individual date/time components and store the retrieved values in the corresponding variables:

```cpp
// Variables for time and date
uint8_t h, m, s, d, mn, y, wk;
uint32_t ss;

// Get time and date data from STM32 internal RTC using pointers
inkplate.rtc.getTime(&h, &m, &s, &ss, NULL, NULL);
inkplate.rtc.getDate(&d, &mn, &y, &wk);
```

<FunctionDocumentation
functionName="inkplate.rtc.getTime()"
description="Gets the current time from the STM32 RTC in a human-readable format."
returnDescription="Returns an RTC_TimeTypeDef structure containing the current time. It's optional to further use this structure in your code."
parameters={[
{ type: 'uint8_t*', name: '_h', description: "Pointer to store the hour value." },
{ type: 'uint8_t*', name: '_m', description: "Pointer to store the minute value." },
{ type: 'uint8_t*', name: '_s', description: "Pointer to store the second value." },
{ type: 'uint32_t*', name: '_ss', description: "Pointer to store the sub-seconds value." },
{ type: 'uint8_t*', name: '_pmAm', description: "Optional. Pointer to store the PM/AM indicator." },
{ type: 'uint8_t*', name: '_dayLightSaving', description: "Optional. Pointer to store the daylight savings status." }
]}
/>

<FunctionDocumentation
functionName="inkplate.rtc.getDate()"
description="Gets the current date from the STM32 RTC."
returnDescription="Returns an RTC_DateTypeDef structure containing the current date. It's optional to further use this structure in your code."
parameters={[
{ type: 'uint8_t*', name: '_d', description: "Pointer to store the day of the month." },
{ type: 'uint8_t*', name: '_m', description: "Pointer to store the month value." },
{ type: 'uint16_t*', name: '_y', description: "Pointer to store the year value." },
{ type: 'uint8_t*', name: '_weekday', description: "Pointer to store the weekday value." }
]}
/>

---

## Full examples

<QuickLink 
  title="Inkplate_6_Motion_Fast_Animation.ino" 
  description="Full Arduino example on how to get and set time via the internal RTC on Inkplate 6 MOTION"
  url="https://github.com/SolderedElectronics/Inkplate_Motion_Arduino_Library/blob/main/examples/Inkplate6Motion/Advanced/RTC/Inkplate_6_Motion_Simple_RTC/Inkplate_6_Motion_Simple_RTC.ino" 
/>
