---
slug: /inkplate/2/basics/initialization
title: Inkplate 2 – Initialization
sidebar_label: Initialization
id: 2-init
hide_title: true
---
<SectionTitle title="Initialization" backgroundImage="img/arduino_bg.jpg" />

Let's get started writing our first Inkplate sketch! Before using Inkplate in Arduino code, it must be initialized in the `setup()` function of your sketch. This page contains details on how to do that.

---

## Initializing Inkplate and updating the display

The most basic sketch for Inkplate 10 is as follows: it initializes Inkplate in memory and clears the e-paper display:

```cpp
// Include Inkplate Arduino Library.
#include <Inkplate.h>
Inkplate inkplate; // Create Inkplate object
void setup() 
{
  // Initialize Inkplate
  inkplate.begin();
  // Update the display
  inkplate.display();
  // As the frame buffer is empty upon initialization, this will display a blank screen
}
void loop() 
{
  // Do nothing here
}
```
<FunctionDocumentation
  FunctionName="Inkplate inkplate()"
  description="Creates an Inkplate object from the Inkplate class."
  returnType="none"
  parameters={[
    { type: 'uint8_t ', name: '_mode', description: 'The display mode to be initialized. INKPLATE_1BIT is BW, INKPLATE_3BIT is Grayscale.' },
  ]}
/>
<FunctionDocumentation
  functionName="inkplate.begin()"
  description="In short, this function initializes the Inkplate object. This starts I2C, allocates the required memory for the frame buffer, and initializes the onboard peripherals."
  returnType="none"
/>
<FunctionDocumentation
  functionName="inkplate.display()"
  description="This function refreshes the display and draws what’s currently in the frame buffer. To update the display, this function must be called. This is a full refresh, completely wiping the e-Paper and then drawing what’s in the frame buffer."
  returnType="none"
  parameters={[
    { type: 'uint8_t ', name: '_leaveOn', description: "Optional. If set to true, the e-Paper won't be turned off after the refresh. This speeds up consecutive refreshes. It's best to use this with partialUpdate and not with this function." },
  ]}
/>

---

## Display rotation

If you want to use Inkplate in portrait mode or with any 90-degree rotation, use `inkplate.setRotation()`:
<FunctionDocumentation
  functionName="inkplate.setRotation()"
  description="Sets the cardinal rotation of the display. This automatically adjusts the (0, 0) x-y coordinate origin point."
  returnDescription="none"
  parameters={[
    { type: 'uint8_t ', name: '_rotation', description: "Ranges from 0-270. 0 is the default rotation, 1 is rotated by 90, 2 by 180, and 3 by 270 degrees." },
  ]}
/>