---
slug: /inkplate/6motion/basics/partial-update
title: 6Motion - Partial Update
id: 6motion-partial-update
hide_title: true
---

<SectionTitle title="Partial Updates" backgroundImage="img/partial_update.jpg" />

Instead of `inkplate.update()`, you can use `inkplate.partialUpdate()` for a faster display refresh. This prevents full-screen flickering, updating only the pixels that have changed in the frame buffer.

---

## Partial Update

Partial updates in black-and-white (1-bit) mode offer the fastest e-Paper update available on Inkplate.

<WarningBox>It is recommended to perform a full update after a certain number of partial updates to maintain the lifespan and image quality of the e-Paper display. Around 50 partial updates should still look good, depending on the content being displayed. Use `inkplate.setFullUpdateTreshold()` to automate this process.</WarningBox>
<InfoBox>Partial updates are also supported in grayscale (4-bit) mode, but they are significantly faster and more effective in black-and-white mode. In grayscale mode, their primary benefit is reducing full-screen flickering.</InfoBox>

```cpp
// Include Inkplate Motion library
#include <InkplateMotion.h>
Inkplate inkplate; // Create Inkplate object
void setup()
{
    inkplate.begin(INKPLATE_BLACKWHITE); // Initialize Inkplate in black and white mode
    
    // Set text options
    inkplate.setTextSize(3);
    inkplate.setTextColor(BLACK);
    inkplate.setTextWrap(false);

    // Set full update threshold
    inkplate.setFullUpdateTreshold(40);
    // This means a full update will occur after every 40 partial updates
}
void loop()
{
    // Scroll text from left to right with partial updates
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
  functionName="inkplate.setFullUpdateTreshold()"
  description="Sets the number of partial updates after which a full update is automatically performed."
  returnDescription="None"
  parameters={[ 
    { type: 'uint16_t', name: '_numberOfPartialUpdates', description: "The number of partial updates before a full update (inkplate.display()) is triggered automatically." }
  ]}
/>

---

## Drawing Fast Bitmaps

For the fastest bitmap rendering on Inkplate 6 MOTION, use `drawBitmapFast`. To convert images for displaying with this function, use the [**Soldered Image Converter**](/inkplate/6motion/basics/image-converter/). **For the moment, this function supports only bitmaps size 1024x758px**.

This efficiently fills the framebuffer with the provided bitmap data:

```cpp
inkplate.drawBitmapFast(&imageFrame);
```
<FunctionDocumentation
  functionName="inkplate.drawBitmapFast()"
  description="Draws a full-screen bitmap onto the framebuffer as quickly as possible. This function is optimized for high-speed rendering, particularly for 1-bit partial updates."
  returnDescription="None"
  parameters={[ 
    { type: 'const uint8_t *', name: '_p', description: "Pointer to the image bitmap data." }
  ]}
/>

<WarningBox>`drawBitmapFast` supports only exactly 1024x758px bitmaps for the moment!</WarningBox>

---

## Full Examples

<QuickLink 
  title="Inkplate_6_Motion_Partial_Update.ino" 
  description="Example demonstrating the use of partialUpdate for fast display refreshes on Inkplate 6 MOTION."
  url="https://github.com/SolderedElectronics/Inkplate_Motion_Arduino_Library/blob/main/examples/Inkplate6Motion/Basic/Inkplate_6_Motion_Partial_Update/Inkplate_6_Motion_Partial_Update.ino" 
/>
<QuickLink 
  title="Inkplate_6_Motion_Fast_Animation.ino" 
  description="Example demonstrating drawBitmapFast for rendering animations on Inkplate 6 MOTION. Review the included files in the sketch for more details."
  url="https://github.com/SolderedElectronics/Inkplate_Motion_Arduino_Library/blob/main/examples/Inkplate6Motion/Basic/Inkplate_6_Motion_Fast_Animation/Inkplate_6_Motion_Fast_Animation.ino" 
/>
<QuickLink 
  title="Soldered Image Converter" 
  description="Convert images to bitmaps for display on Inkplate 6 MOTION using the Soldered Image Converter."
  url="/inkplate/6motion/basics/image-converter" 
/>
