---  
slug: /inkplate/6color/low-power/deep-sleep  
title: Deep sleep  
id: deep-sleep  
hide_title: true  
---

<SectionTitle title="Deep sleep" backgroundImage="/img/deepsleep.jpg" />

Using deep sleep on Inkplate 6COLOR is crucial for writing a sketch that maximizes battery efficiency. Since e-Paper does not require any power to retain the displayed image, Inkplate 6COLOR can consume little or no current while in deep sleep mode, enabling a sketch to run for months on battery.

<InfoBox>If all peripherals are in sleep mode, the deep sleep current will be around **20-30µA**</InfoBox>

---

## Simple deep sleep
Check how deep sleep works with the example below:

```cpp
#define uS_TO_S_FACTOR 1000000 // Conversion factor for micro seconds to seconds
#define TIME_TO_SLEEP  20 // How long ESP32 will be in deep sleep (in seconds)
void setup(){
    // your code
    ///...
    esp_sleep_enable_timer_wakeup(TIME_TO_SLEEP * uS_TO_S_FACTOR); // Activate wake-up timer -- wake up after 20s here
    esp_deep_sleep_start(); // Put ESP32 into deep sleep. Program stops here.
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
  description="This function enters deep sleep with the configured wakeup options."
  returnType="None"
/>

---

## Wake on button press

To wake up using the `Wake` button, call the ESP32 function `esp_sleep_enable_ext0_wakeup()` before putting it to sleep.

```cpp
// Go to sleep for TIME_TO_SLEEP seconds
esp_sleep_enable_timer_wakeup(TIME_TO_SLEEP * uS_TO_S_FACTOR);

// Enable wakeup from deep sleep on GPIO 36 (wake button)
esp_sleep_enable_ext0_wakeup(GPIO_NUM_36, LOW);

// Go to sleep
esp_deep_sleep_start();
```

<FunctionDocumentation
  functionName="esp_sleep_enable_ext0_wakeup()"
  description="This function uses the external wakeup feature of the RTC_IO peripheral."
  returnDescription="Returns ESP error constant"
  returnType="int"
  parameters={[
    { type: 'gpio_num_t', name: 'gpio_num', description: 'GPIO number used as wakeup source. Only GPIOs with RTC functionality can be used.' },
    { type: 'int', name: 'level', description: 'Input level which will trigger wakeup.' },
  ]}
/>

---

## Full examples
Check out the full examples from this page, along with many more usage options below:

<QuickLink 
  title="Inkplate6COLOR_Simple_Deep_Sleep.ino" 
  description="This example will show you how to use the low-power functionality of the Inkplate board."
  url="https://github.com/SolderedElectronics/Inkplate-Arduino-library/blob/master/examples/Inkplate6COLOR/Advanced/DeepSleep/Inkplate6COLOR_Simple_Deep_Sleep/Inkplate6COLOR_Simple_Deep_Sleep.ino" 
/>

<QuickLink 
  title="Inkplate6COLOR_Wake_Up_Button.ino" 
  description="Full example on how to implement the WAKE UP button with deep sleep on Inkplate 6COLOR."
  url="https://github.com/SolderedElectronics/Inkplate-Arduino-library/blob/master/examples/Inkplate6COLOR/Advanced/DeepSleep/Inkplate6COLOR_Wake_Up_Button/Inkplate6COLOR_Wake_Up_Button.ino" 
/>

<QuickLink 
  title="Inkplate6COLOR_RTC_Alarm_With_Deep_Sleep.ino" 
  description="This example will show you how to use the RTC alarm interrupt with deep sleep."
  url="https://github.com/SolderedElectronics/Inkplate-Arduino-library/tree/master/examples/Inkplate6COLOR/Advanced/DeepSleep/Inkplate6COLOR_RTC_Alarm_With_Deep_Sleep" 
/>