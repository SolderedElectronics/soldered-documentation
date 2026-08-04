---
slug: /inkplate/4tempera/frontlight/simple-frontlight
title: Inkplate 4TEMPERA - Simple Frontlight
sidebar_label: Simple Frontlight
id: 4tempera-frontlight
hide_title: true
---

<SectionTitle title="Simple Frontlight Control" backgroundImage="/img/frontlight.jpg" />

Inkplate 4TEMPERA features a built-in frontlight, which allows the display to be visible in low-light environments. This page shows you how to control the frontlight using a simple sketch.

<InfoBox>The frontlight brightness is controlled through the `frontlight` object. Call `setState(true)` to enable the frontlight circuit, then use `setBrightness()` with a value between 0 (off) and 63 (full brightness) to set the intensity.</InfoBox>

---

## Frontlight example code

The following example demonstrates how to enable the frontlight and set it to roughly half brightness:

```cpp
/*
    Inkplate4TEMPERA_Simple_Frontlight example for Soldered Inkplate 4TEMPERA
    This example shows how to control the frontlight brightness.

    Make sure to select "Soldered Inkplate 4TEMPERA" from Tools -> Board menu.

    Want to learn more about Inkplate? Visit www.inkplate.io
    Looking to get support? Ask on the Soldered community: https://community.soldered.com/
*/

#include "Inkplate.h" // Include Inkplate library

Inkplate display; // Create Inkplate object

void setup()
{
    display.begin();                      // Initialize the display
    display.frontlight.setState(true);    // Enable the frontlight circuit
    display.frontlight.setBrightness(31); // Set frontlight brightness (0-63)
}

void loop()
{
    // Nothing here
}
```

---

<FunctionDocumentation
  functionName="display.frontlight.setBrightness()"
  description="Sets the frontlight brightness of the Inkplate 4TEMPERA."
  returnType="void"
  parameters={[
    { type: 'uint8_t', name: 'value', description: 'Brightness value (0-63).' }
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