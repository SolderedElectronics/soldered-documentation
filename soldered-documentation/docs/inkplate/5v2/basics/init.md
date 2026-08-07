---  
slug: /inkplate/5v2/basics/initialization  
title: Inkplate 5V2 – Initialization
sidebar_label: Initialization
id: init  
hide_title: true  
---  
<SectionTitle title="Initialization" />

Let's write your first Inkplate sketch. Before you can use Inkplate in your Arduino code, it has to be initialized in the `setup()` function of your sketch. Here's how to do that.

---

## Initializing Inkplate and updating the display

Here's the most basic sketch for Inkplate 5V2. It initializes Inkplate in memory and clears the e-paper display:

```cpp
// Include Inkplate Arduino Library.
#include <Inkplate.h>
Inkplate inkplate(INKPLATE_1BIT); // Create Inkplate object
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
  functionName="Inkplate inkplate(INKPLATE_1BIT)"
  description="Creates an Inkplate object from the Inkplate class."
  returnType="none"
  parameters={[{ type: 'uint8_t ', name: '_mode', description: 'The display mode to be initialized. INKPLATE_1BIT is BW, INKPLATE_3BIT is Grayscale.' }]}
/>
<FunctionDocumentation
  functionName="inkplate.begin()"
  description="Initializes the Inkplate object. This starts I2C, allocates the required memory for the frame buffer, and initializes the on-board peripherals."
  returnType="none"
/>
<FunctionDocumentation
  functionName="inkplate.display()"
  description="This function refreshes the display and draws what's currently in the frame buffer. To update the display, this function must be called. This is a full refresh, completely wiping the e-paper and then drawing what's in the frame buffer."
  returnType="none"
  parameters={[{ type: 'uint8_t ', name: '_leaveOn', description: "Optional. If set to true, the e-paper won't get turned off after the refresh, which speeds up consecutive refreshes. It's best to use this with partialUpdate and not with this function." }]}
/>

---

## Display rotation

If you want to use Inkplate in portrait mode or any 90-degree rotation, use `inkplate.setRotation()`:
<FunctionDocumentation
  functionName="inkplate.setRotation()"
  description="Sets the cardinal rotation of the display. This automatically adjusts the (0, 0) x-y coordinate origin point."
  returnType="none"
  parameters={[{ type: 'uint8_t ', name: '_rotation', description: "Accepts 0 to 3. 0 is the default rotation, 1 is 90 degrees, 2 is 180 degrees, and 3 is 270 degrees. The value is masked with & 3, so passing 90, 180 or 270 will not do what you expect." }]}
/>