---
slug: /inkplate/10/low-power/deep-sleep
title: Deep sleep
id: 10-deep-sleep
hide_title: true
---

<SectionTitle title="Deep sleep" backgroundImage="/img/deepsleep.jpg" />

Using deep sleep on Inkplate 10 is key to writing a sketch which maximizes battery efficiency. Since e-Paper does not need any kind of power to retain the image displayed - Inkplate 10 can use little to no current while in deep sleep mode, and have a sketch running for months on battery.

<InfoBox>If all peripherals are in sleep mode, deep sleep current will be around **20-30µA**</InfoBox>

---

## Simple deep sleep
Check how the deep sleep works with the example below:

```cpp

#define uS_TO_S_FACTOR 1000000 // Conversion factor for micro seconds to seconds
#define TIME_TO_SLEEP  20 //How long ESP32 will be in deep sleep (in seconds)
void setup(){
    //your code
    ///...
    esp_sleep_enable_timer_wakeup(TIME_TO_SLEEP * uS_TO_S_FACTOR); //Activate wake-up timer -- wake up after 20s here
    esp_deep_sleep_start(); //Put ESP32 into deep sleep. Program stops here.
}
```

<FunctionDocumentation
  functionName="esp_sleep_enable_timer_wakeup()"
  description="This function enables wakeup by timer."
  returnDescription="Returns ESP error code"
  returnType="int"
  parameters={[
    { type: 'uint64_t', name: 'time_in_us', description: 'Wakeup time in microseconds.' },
  ]}
/>

<FunctionDocumentation
  functionName="esp_deep_sleep_start()"
  description="This function enters deep sleep wit the configured wakeup options."
  returnType="None"
/>

---

## Full examples
Check out the full examples from this page and many more usage options down below:

<QuickLink 
  title="Inkplate10_Simple_Deep_Sleep.ino" 
  description="This example will show you how you can use low power functionality of Inkplate board."
  url="https://github.com/SolderedElectronics/Inkplate-Arduino-library/tree/master/examples/Inkplate10/Advanced/DeepSleep/Inkplate10_Simple_Deep_Sleep" 
/>

<QuickLink 
  title="Inkplate10_Wake_Up_Button.ino" 
  description="Full example on how to implement WAKE UP button with deepsleep on Inkplate 10"
  url="https://github.com/SolderedElectronics/Inkplate-Arduino-library/blob/master/examples/Inkplate10/Advanced/DeepSleep/Inkplate10_Wake_Up_Button/Inkplate10_Wake_Up_Button.ino" 
/>

<QuickLink 
  title="Inkplate10_RTC_Alarm_With_Deep_Sleep.ino" 
  description="This example will show you how to use RTC alarm interrupt with deep sleep."
  url="https://github.com/SolderedElectronics/Inkplate-Arduino-library/tree/master/examples/Inkplate10/Advanced/DeepSleep/Inkplate10_RTC_Alarm_With_Deep_Sleep" 
  
/>