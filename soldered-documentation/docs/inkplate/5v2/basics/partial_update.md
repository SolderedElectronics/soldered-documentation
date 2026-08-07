---
slug: /inkplate/5v2/basics/partial-update
title: Inkplate 5V2 – Partial Update
sidebar_label: Partial Update
id: partial-update
hide_title: true
---

<SectionTitle title="Partial Updates" />

Instead of `inkplate.display()`, you can use `inkplate.partialUpdate()` for a faster display refresh. It only redraws the pixels that changed in the frame buffer, so the whole screen doesn't flicker.

---

## Partial update

Partial updates in black-and-white (1-bit) mode are the fastest e-Paper update available on Inkplate.

<WarningBox>Do a full update after a certain number of partial updates to keep the image quality and the lifespan of the e-Paper display. The library performs a full refresh every 10 partial updates by default, and 5 to 10 is the recommended range. Use `inkplate.setFullUpdateThreshold()` to change it.</WarningBox>
<WarningBox>Partial update works **only** in black-and-white (`INKPLATE_1BIT`) mode. Calling `partialUpdate()` while the display is in grayscale (`INKPLATE_3BIT`) mode does nothing: the function returns immediately without touching the panel.</WarningBox>

```cpp
#include "Inkplate.h"
Inkplate inkplate(INKPLATE_1BIT);
void setup(){
  inkplate.begin();
  inkplate.clearDisplay();
  inkplate.display(); // Do one full refresh first, so the panel starts from a known state
  inkplate.setTextSize(3);
  inkplate.setTextColor(BLACK);
  inkplate.setTextWrap(false); // Keep the text on one line while it scrolls
  inkplate.setFullUpdateThreshold(10);
}
void loop(){
  int x = -300; // Start from the left of the screen border
    while (x < 1280)
    {
        inkplate.clearDisplay();
        inkplate.setCursor(x, 300); // Set cursor position
        inkplate.print("Partial updates!"); // Print scrolling text
        inkplate.partialUpdate(false, true); // Partial update, leave the panel powered for the next one
        x += 15; // Move 15 pixels to the right
    }
    inkplate.display(); // Perform a full update
    delay(1000); // Pause before next update
}
```

<FunctionDocumentation
  functionName="inkplate.partialUpdate()"
  description="Performs a partial (fast) update on Inkplate. Only the changed pixels are refreshed, which avoids full-screen flicker."
  returnType="uint32_t"
  parameters={[ 
    { type: 'bool', name: '_forced', description: "Optional. Forces a partial update even when the library has flagged that a full refresh is due. Intended for advanced use, mainly deep sleep workflows." },
    { type: 'bool', name: 'leaveOn', description: "Optional. If set to true, the e-Paper power supply remains on after the update. This speeds up consecutive partial updates but requires a full refresh afterward to prevent prolonged power draw." }
  ]}
/>
<FunctionDocumentation
  functionName="inkplate.setFullUpdateThreshold()"
  description="Sets the number of partial updates after which a full update is automatically performed."
  returnType="void"
  parameters={[ 
    { type: 'uint16_t', name: '_numberOfPartialUpdates', description: "The number of partial updates before a full update (inkplate.display()) is triggered automatically." }
  ]}
/>

---

## Full examples

<QuickLink 
  title="Inkplate5V2_Partial_Update.ino" 
  description="Example demonstrating the use of partialUpdate for fast display refreshes on Inkplate 5V2."
  url="https://github.com/SolderedElectronics/Inkplate-Arduino-library/tree/master/examples/Inkplate5V2/Basic/Inkplate5V2_Partial_Update" 
/>