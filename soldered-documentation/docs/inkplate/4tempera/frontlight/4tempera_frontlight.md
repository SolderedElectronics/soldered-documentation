---
slug: /inkplate/4tempera/frontlight/simple-frontlight
title: Inkplate 4TEMPERA – Simple Frontlight
sidebar_label: Simple Frontlight
id: 4tempera-frontlight
hide_title: true
---

<SectionTitle title="Simple Frontlight Control" backgroundImage="/img/frontlight.jpg" />

Inkplate 4TEMPERA features a built-in frontlight, which allows the display to be visible in low-light environments. This page shows you how to control the frontlight using a simple sketch.

<InfoBox>The frontlight brightness can be controlled using PWM (Pulse Width Modulation) via the `setFrontlight()` function, which takes a value between 0 (off) and 100 (full brightness).</InfoBox>

---

## Frontlight Example Code

The following example demonstrates how to turn on the frontlight at 50% brightness and keep it running:

```cpp
/*
    Inkplate4TEMPERA_Simple_Frontlight example for Soldered Inkplate 4TEMPERA
    This example shows how to control the frontlight brightness.

    Make sure to select "Soldered Inkplate 4TEMPERA" from Tools -> Board menu.

    Want to learn more about Inkplate? Visit www.inkplate.io
    Looking to get support? Write on our forums: https://forum.soldered.com/
*/

#include "Inkplate.h" // Include Inkplate library

Inkplate display; // Create Inkplate object

void setup()
{
    display.begin();              // Initialize the display
    display.setFrontlight(50);   // Set frontlight brightness to 50%
    display.clearDisplay();      // Clear frame buffer
    display.setCursor(0, 20);    // Set cursor position
    display.setTextSize(2);      // Set text size
    display.setTextColor(BLACK); // Set text color
    display.print("Frontlight at 50%");
    display.display();           // Refresh display
}

void loop()
{
    // Nothing here
}
```

---

<FunctionDocumentation
  functionName="display.setFrontlight()"
  description="Sets the frontlight brightness of the Inkplate 4TEMPERA."
  returnType="void"
  parameters={[
    { type: 'uint8_t', name: 'value', description: 'Brightness value (0–100).' }
  ]}
/>

---

## Full example

Check out the full example on GitHub:

<QuickLink 
  title="Inkplate4TEMPERA_Simple_Frontlight" 
  description="Control the frontlight brightness of Inkplate 4TEMPERA." 
  url="https://github.com/SolderedElectronics/Inkplate-Arduino-library/blob/master/examples/Inkplate4TEMPERA/Basic/Inkplate4TEMPERA_Simple_Frontlight/Inkplate4TEMPERA_Simple_Frontlight.ino" 
/>