---
slug: /inkplate/6flick/basics/partial-update
title: Inkplate 6FLICK – Partial Update
id: 6flick-partial-update
hide_title: true
---

<SectionTitle title="Partial Updates" backgroundImage="img/partial_update.jpg" />

Instead of `inkplate.update()`, you can use `inkplate.partialUpdate()` for a faster display refresh. This prevents full-screen flickering by updating only the pixels that have changed in the frame buffer.

---

## Partial Update

Partial updates in black-and-white (1-bit) mode offer the fastest e-Paper update available on Inkplate.

<WarningBox>It is recommended to perform a full update after a certain number of partial updates to maintain the lifespan and image quality of the e-Paper display. Around 50 partial updates should still look good, depending on the content being displayed. Use `inkplate.setFullUpdateThreshold()` to automate this process.</WarningBox>
<InfoBox>Partial updates are also supported in grayscale (3-bit) mode, but they are significantly faster and more effective in black-and-white mode. In grayscale mode, their primary benefit is reducing full-screen flickering.</InfoBox>

```cpp
#include "Inkplate.h"
Inkplate inkplate(INKPLATE_1BIT);
void setup(){
  inkplate.begin();
  inkplate.setTextSize(3);
  inkplate.setTextColor(BLACK);
  inkplate.setFullUpdateThreshold(40);
}
void loop(){
  int x = -500; // Start from the left of the screen border
    while (x < 1024)
    {
        inkplate.clearDisplay();
        inkplate.setCursor(x, 300); // Set cursor position
        inkplate.print("Partial updates!"); // Print scrolling text
        inkplate.partialUpdate(true); // Perform a partial update
        x += 15; // Move 15 pixels to the right
    }
    inkplate.display(); // Perform a full update
    delay(1000); // Pause before next update
}
```

<FunctionDocumentation
  functionName="inkplate.partialUpdate()"
  description="Performs a partial (fast) update on Inkplate, refreshing only changed pixels to prevent full-screen flickering."
  returnDescription="None"
  parameters={[ 
    { type: 'uint8_t', name: '_leaveOn', description: "Optional. If set to 1, the e-Paper power supply remains on after the update. This speeds up consecutive partial updates but requires a full refresh afterward to prevent prolonged power draw." }
  ]}
/>
<FunctionDocumentation
  functionName="inkplate.setFullUpdateThreshold()"
  description="Sets the number of partial updates after which a full update is automatically performed."
  returnDescription="None"
  parameters={[ 
    { type: 'uint16_t', name: '_numberOfPartialUpdates', description: "The number of partial updates before a full update (inkplate.display()) is triggered automatically." }
  ]}
/>

---

## Full Examples

<QuickLink 
  title="Inkplate6FLICK_Partial_Update.ino" 
  description="Example demonstrating the use of partialUpdate for fast display refreshes on Inkplate 6FLICK."
  url="https://github.com/SolderedElectronics/Inkplate-Arduino-library/blob/master/examples/Inkplate6FLICK/Basic/Inkplate6FLICK_Partial_Update/Inkplate6FLICK_Partial_Update.ino" 
/>