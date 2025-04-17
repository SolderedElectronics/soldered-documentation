---
slug: /inkplate/6motion/peripherals/buttons
title: User Buttons
id: 6motion-periph-buttons
---

The **Inkplate 6 MOTION** features **three onboard buttons** that can be used for **user interaction** or to wake the device from deep sleep. These buttons are:

- **USER1** (`INKPLATE_USER1`)
- **USER2** (`INKPLATE_USER2`)
- **WAKE** (`INKPLATE_WAKE`)

The **WAKE** button has a special function - it can be used to wake up the Inkplate 6 MOTION from deep sleep. See [**here**](/inkplate/6motion/low-power/deep-sleep#wake-on-button-press) for more info on waking via **WAKE** button.

---

## Configuration

The buttons need to be configured as **input pull-ups**, meaning they are normally HIGH and go LOW when pressed:

```cpp
// Configure button pin modes
pinMode(INKPLATE_USER1, INPUT_PULLUP);
pinMode(INKPLATE_USER2, INPUT_PULLUP);
pinMode(INKPLATE_WAKE, INPUT_PULLUP);
```

---

## Reading Button Presses

A simple way to detect button presses is using `digitalRead()`. The example below waits for a button press and identifies which button was pressed by returning an integer:

```cpp
int getButtonPress() {
  // Wait for button press and return which button was pressed accordingly
  while (true) {
    if (digitalRead(INKPLATE_USER1) == LOW)
      return 1;
    if (digitalRead(INKPLATE_USER2) == LOW)
      return 2;
    if (digitalRead(INKPLATE_WAKE) == LOW)
      return 3;
    
    delay(5);  // Short debounce delay
  }
}
```

---

## Full example

For an all-in-one demonstration, the Inkplate library provides an example:

<QuickLink title="Inkplate_6_MOTION_Buttons.ino"
description="Full example with pressing buttons and printing out which one was pressed"
url="https://github.com/SolderedElectronics/Inkplate_Motion_Arduino_Library/blob/main/examples/Inkplate6Motion/Advanced/Sensors_Other/Inkplate_6_MOTION_Buttons/Inkplate_6_MOTION_Buttons.ino"
/>

