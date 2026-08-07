---
slug: /inkplate/10/basics/partial-update
title: Inkplate 10 – Partial update
sidebar_label: Partial update
id: 10-partial-update
hide_title: true
---

<SectionTitle title="Partial updates" />

Instead of `display.display()`, you can use `display.partialUpdate()` for a faster display refresh. This prevents full-screen flickering, updating only the pixels that have changed in the frame buffer.

---

## Partial update

Partial updates in black-and-white (1-bit) mode offer the fastest e-Paper update available on Inkplate.

<WarningBox>It is recommended to perform a full update after a certain number of partial updates to maintain the lifespan and image quality of the e-Paper display. Around 50 partial updates should still look good, depending on the content being displayed. Use `display.setFullUpdateThreshold()` to automate this process.</WarningBox>
<InfoBox>Partial updates are also supported in grayscale (3-bit) mode, but they are significantly faster and more effective in black-and-white mode. In grayscale mode, their primary benefit is reducing full-screen flickering.</InfoBox>

```cpp
#include "Inkplate.h"
Inkplate display(INKPLATE_1BIT);
void setup(){
  display.begin();
  display.setTextSize(3);
  display.setTextColor(BLACK);
  display.setFullUpdateThreshold(40);
}
void loop(){
  int x = -500; // Start from the left of the screen border
    while (x < 1200)
    {
        display.clearDisplay();
        display.setCursor(x, 300); // Set cursor position
        display.print("Partial updates!"); // Print scrolling text
        display.partialUpdate(true); // Perform a partial update
        x += 15; // Move 15 pixels to the right
    }
    display.display(); // Perform a full update
    delay(1000); // Pause before next update
}
```

<FunctionDocumentation
  functionName="display.partialUpdate()"
  description="Performs a partial (fast) update on Inkplate, refreshing only changed pixels to prevent full-screen flickering."
  returnDescription="None"
  parameters={[ 
    { type: 'uint8_t', name: '_leaveOn', description: "Optional. If set to 1, the e-Paper power supply remains on after the update. This speeds up consecutive partial updates but requires a full refresh afterward to prevent prolonged power draw." }
  ]}
/>
<FunctionDocumentation
  functionName="display.setFullUpdateThreshold()"
  description="Sets the number of partial updates after which a full update is automatically performed."
  returnDescription="None"
  parameters={[ 
    { type: 'uint16_t', name: '_numberOfPartialUpdates', description: "The number of partial updates before a full update (display.display()) is triggered automatically." }
  ]}
/>

---

## Full examples

<QuickLink 
  title="Inkplate10_Partial_Update.ino" 
  description="Example demonstrating the use of partialUpdate for fast display refreshes on Inkplate 10."
  url="https://github.com/SolderedElectronics/Inkplate-Arduino-library/blob/master/examples/Inkplate10/Basic/Inkplate10_Partial_Update/Inkplate10_Partial_Update.ino" 
/>