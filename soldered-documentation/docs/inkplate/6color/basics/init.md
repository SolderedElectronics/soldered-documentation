---  
slug: /inkplate/6color/basics/initialization  
title: Inkplate 6COLOR – Initialization
sidebar_label: Initialization
id: init  
hide_title: true  
---  
<SectionTitle title="Initialization" />

Before using Inkplate in Arduino code, it must be initialized in the `setup()` function of your sketch. This page covers how to do that.

---

## Initializing Inkplate and updating the display

The most basic sketch on Inkplate 6COLOR is as follows. It initializes Inkplate in memory and clears the e-paper display:

```cpp
#include <Inkplate.h>
Inkplate display; // Create Inkplate object
void setup() 
{
  // Initialize Inkplate
  display.begin();
  // Update the display
  display.display();
  // As the frame buffer is empty upon initialization, this will display a blank screen
}
void loop() 
{
  // Do nothing here
}
```
<FunctionDocumentation
  functionName="Inkplate display"
  description="Creates an Inkplate object from the Inkplate class."
  returnType="none"
/>
<FunctionDocumentation
  functionName="display.begin()"
  description="In short, this function initializes the Inkplate object. It starts I2C, allocates the required memory for the frame buffer, and initializes the onboard peripherals."
  returnType="none"
/>
<FunctionDocumentation
  functionName="display.display()"
  description="This function refreshes the display and draws what is currently in the frame buffer. To update the display, this function must be called. This is a full refresh that completely wipes the e-Paper and then draws everything from the frame buffer."
  returnType="none"
  parameters={[ 
    { type: 'bool', name: '_leaveOn', description: "Optional. If set to true, the e-paper power supply is left on after the refresh." },
  ]}
/>

<InfoBox>Inkplate 6COLOR has no partial update. The color panel can only do a full refresh, which takes about 12 seconds, so `display()` is the only way to get the frame buffer onto the screen.</InfoBox>

---

## Display rotation

In case you want to use Inkplate in portrait mode or in any 90-degree rotation, use `display.setRotation()`:
<FunctionDocumentation
  functionName="display.setRotation()"
  description="Sets the cardinal rotation of the display. This automatically adjusts the (0, 0) x-y coordinate origin point."
  returnType="none"
  parameters={[ 
    { type: 'uint8_t ', name: '_rotation', description: "Accepts 0 to 3. 0 is the default rotation, 1 is 90 degrees, 2 is 180 degrees, and 3 is 270 degrees. The value is masked with & 3, so passing 90, 180 or 270 will not do what you expect." },
  ]}
/>