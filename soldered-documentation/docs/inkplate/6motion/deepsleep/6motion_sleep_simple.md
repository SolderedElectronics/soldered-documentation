---
slug: /inkplate/6motion/low-power/deep-sleep
title: "Inkplate \u2013 6Motion Low Power Deep Sleep"
id: 6motion-deep-sleep
hide_title: true
---
<SectionTitle title="Deep sleep" backgroundImage="/img/deepsleep.jpg" />

Using deep sleep on Inkplate 6 MOTION is key to writing a sketch which maximizes battery efficiency. Since e-Paper does not need any kind of power to retain the image displayed - Inkplate 6 MOTION can use little to no current while in deep sleep mode, and have a sketch running for months on battery.

<InfoBox>If all peripherals are in sleep mode, deep sleep current will be around **20-30µA**</InfoBox>

---

## Simple deep sleep

The function below is a compound of all function calls required to put Inkplate 6 MOTION in deep sleep mode:

```cpp
void deepSleep()
{
    // Disable all peripherals including WiFi, microSD card, SDRAM, sensors etc
    inkplate.peripheralState(INKPLATE_PERIPHERAL_ALL, false);
    // Disable USB voltage detection on USB OTG (This causes high current consumption in sleep!)
    HAL_PWREx_DisableUSBVoltageDetector();
    // Use different voltage scale for internal voltage regulator (lower current consumption in sleep mode)
    HAL_PWREx_ControlStopModeVoltageScaling(PWR_REGULATOR_SVOS_SCALE5);
    // Put every domain into standby mode
    HAL_PWREx_EnterSTANDBYMode(PWR_D3_DOMAIN);
    HAL_PWREx_EnterSTANDBYMode(PWR_D2_DOMAIN);
    HAL_PWREx_EnterSTANDBYMode(PWR_D1_DOMAIN);
    // Code does not continue past this point!
}
```
<WarningBox>**Code will not continue after the final call to `HAL_PWREx_EnterSTANDBYMode`!**</WarningBox>

<InfoBox>For more information on turning off peripherals via `peripheralState`, see [**this**](/inkplate/6motion/peripherals/introduction#powering-off/) page</InfoBox>

To create a sketch which uses deep sleep - it's common practice to put all code in the `setup` function, and then at the end put Inkplate into deep sleep.

---

## Wake on button press

To wake on button press of the `WAKE` button, use the STM32 function `HAL_PWR_EnableWakeUpPin` after resetting the wakeup flags. Setting wakeup reasons  
```cpp
// Check if the wake up from sleep did reset the board. If so, clear the flags
if (__HAL_PWR_GET_FLAG(PWR_FLAG_SB) != RESET)
{
    // Clear Standby flag
    __HAL_PWR_CLEAR_FLAG(PWR_FLAG_SB);
    // Wake-up button on Inkplate 6 Motion is PC13 = WAKEUP PIN 4.
    HAL_PWR_DisableWakeUpPin(PWR_WAKEUP_PIN4);
}
// Enable wake up button. By setting PC13 to low (button press), Inkplate will wake up
HAL_PWR_EnableWakeUpPin(PWR_WAKEUP_PIN4_LOW);
```

## Wake on timer

The most common usage of deep sleep is to periodically wake Inkplate to refresh the display with new data, this is documented in the RTC section of the documentation:
<QuickLink 
  title="RTC deep sleep wakeup" 
  description="How to use the built-in RTC to set a timer wake up from deep sleep"
  url="https://github.com/SolderedElectronics/Inkplate_Motion_Arduino_Library/blob/main/examples/Inkplate6Motion/Advanced/DeepSleep/Inkplate_6_Motion_Deep_Sleep/Inkplate_6_Motion_Deep_Sleep.ino" 
/>

## Full examples

<QuickLink 
  title="Inkplate 6 MOTION deep sleep example" 
  description="This example demonstrates a sketch structured around deep sleep, it's an overview of all the deep sleep possibilies on Inkplate 6 MOTION, with waking on timer or pushbutton"
  url="https://github.com/SolderedElectronics/Inkplate_Motion_Arduino_Library/blob/main/examples/Inkplate6Motion/Advanced/DeepSleep/Inkplate_6_Motion_Deep_Sleep/Inkplate_6_Motion_Deep_Sleep.ino" 
/>
