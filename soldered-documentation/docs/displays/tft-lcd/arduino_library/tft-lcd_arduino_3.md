---
slug: /tft-lcd/arduino/touchscreen-raw
title: TFT LCD - Touchscreen Raw
sidebar_label: Touchscreen raw
id: tft-lcd-arduino-3
hide_title: false
---

This example helps you understand how to read **raw X, Y coordinates and pressure values** from the **touchscreen controller** on the 2.4" TFT LCD breakout.

It’s useful for diagnosing touch issues or performing **touchscreen calibration**.

---

## TouchScreenRaw.ino

<InfoBox>
This example only reads touch values – it does **not render anything** on the screen.
</InfoBox>

```cpp
#include "SPI.h"
#include "TFT-LCD-Breakout-2.4-With-Touch-SOLDERED.h"

TFTTouch ts(5); // Replace with the correct CST pin

void setup() {
    Serial.begin(115200);
    ts.begin();
}

void loop() {
    ts.service(); // Refresh touch status

    if (ts.getPressure()) {
        Serial.print("X: ");
        Serial.print(ts.getX());
        Serial.print(" | Y: ");
        Serial.print(ts.getY());
        Serial.print(" | Pressure: ");
        Serial.println(ts.getPressure());
    }

    delay(100); // Small delay to avoid flooding serial monitor
}
```

---

## Output Format

When you touch the display, you’ll see a stream like this in your Serial Monitor:

```
X: 714 | Y: 412 | Pressure: 315
X: 718 | Y: 417 | Pressure: 310
...
```

---

## Use Case

Use this sketch to determine the **minimum and maximum raw values** for both X and Y axes. These values are essential for proper touchscreen calibration with the `calibrate()` function.

```cpp
ts.calibrate(x_max, x_min, y_max, y_min);
```

---

## Full Example

<QuickLink 
  title="TouchScreenRaw.ino"
  description="Example sketch to read raw X, Y, and pressure values from the TFT touchscreen."
  url="https://github.com/SolderedElectronics/Soldered-TFT-LCD-Breakout-2.4-With-Touch-Arduino-Library/blob/main/examples/TouchScreenRaw/TouchScreenRaw.ino" 
/>
