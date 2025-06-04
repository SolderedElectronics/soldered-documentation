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

## Wake on button press

To wake on button press of the `Wake` button, use the ESP32 function `esp_sleep_enable_ext0_wakeup()` before putting it to sleep.

```cpp
// Go to sleep for TIME_TO_SLEEP seconds
esp_sleep_enable_timer_wakeup(TIME_TO_SLEEP * uS_TO_S_FACTOR);

// Enable wakeup from deep sleep on gpio 36 (wake button)
esp_sleep_enable_ext0_wakeup(GPIO_NUM_36, LOW);

// Go to sleep
esp_deep_sleep_start();

```

<FunctionDocumentation
  functionName="esp_sleep_enable_ext0_wakeup()"
  description="This function uses external wakeup feature of RTC_IO peripheral."
  returnDescription="Returns ESP error constant"
  returnType="int"
  parameters={[
    { type: 'gpio_num_t', name: 'gpio_num', description: 'GPIO number used as wakeup source. Only GPIOs which are have RTC functionality can be used.' },
    { type: 'int', name: 'level', description: 'Input level which will trigger wakeup.' },
  ]}
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