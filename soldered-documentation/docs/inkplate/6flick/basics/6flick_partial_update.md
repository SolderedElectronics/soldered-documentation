---
slug: /inkplate/6flick/basics/partial-update
title: Inkplate 6FLICK – Partial update
sidebar_label: Partial update
id: 6flick-partial-update
hide_title: true
---

<SectionTitle title="Partial updates" />

Instead of `display.display()`, you can use `display.partialUpdate()` for a faster display refresh. This prevents full-screen flickering by updating only the pixels that have changed in the frame buffer.

---

## Partial update

Partial updates in black-and-white (1-bit) mode offer the fastest e-Paper update available on Inkplate.

<WarningBox>It is recommended to perform a full update after a certain number of partial updates to maintain the lifespan and image quality of the e-Paper display. Around 50 partial updates should still look good, depending on the content being displayed. Use `display.setFullUpdateThreshold()` to automate this process.</WarningBox>
<InfoBox>Partial updates are also supported in grayscale (3-bit) mode, but they are much faster and cleaner in black-and-white mode. In grayscale mode, their primary benefit is reducing full-screen flickering.</InfoBox>

```cpp
#include "Inkplate.h"            //Include Inkplate library to the sketch
Inkplate display(INKPLATE_1BIT); // Create an object on Inkplate library and also set library into 1-bit mode (BW)

// Char array where you can store your text that will be scrolled.
const char text[] = "This is partial update on Inkplate 6FLICK e-paper display! :)";

// This variable is used for moving the text (scrolling)
int offset = 800;

//This variable is used to define the number of partial updates before doing a full update
int partialUpdates=9;

void setup()
{
    display.begin();                    // Init Inkplate library (you should call this function ONLY ONCE)
    display.clearDisplay();             // Clear frame buffer of display
    display.display();                  // Put clear image on display
    display.setTextColor(BLACK, WHITE); // Set text color to be black and background color to be white
    display.setTextSize(4);             // Set text to be 4 times bigger than classic 5x7 px text
    display.setTextWrap(false);         // Disable text wraping
    /*
    Set the number of partial updates before doing a full update
    This function forces a full update as the next update to ensure that the cycle of partial 
    updates starts from a fully updated screen.
    The Inkplate class keeps a internal counter that increments every time partialUpdate() gets called.
    */
    display.setFullUpdateThreshold(partialUpdates); 
}

void loop()
{
    // BASIC USAGE

    display.clearDisplay();         // Clear content in frame buffer
    display.setCursor(offset, 300); // Set new position for text
    display.print(text);            // Write text at new position
    
    /*
    //Updates changes parts of the screen without the need to refresh the whole display
    //partialUpdate(bool _forced, bool leaveOn)
	    _forced		Can force partial update in deep sleep (for advanced use)
	    leaveOn 	If set to 1, it will disable turning power supply for eink after display update in order to increase refresh time
    */
    display.partialUpdate(false, true);
    offset -= 20; // Move text into new position
    if (offset < 0)
        offset = 800; // Text is scrolled till the end of the screen? Get it back on the start!
    delay(500);       // Delay between refreshes.
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
  title="Inkplate6FLICK_Partial_Update.ino" 
  description="Example demonstrating the use of partialUpdate for fast display refreshes on Inkplate 6FLICK."
  url="https://github.com/SolderedElectronics/Inkplate-Arduino-library/blob/master/examples/Inkplate6FLICK/Basic/Inkplate6FLICK_Partial_Update/Inkplate6FLICK_Partial_Update.ino" 
/>