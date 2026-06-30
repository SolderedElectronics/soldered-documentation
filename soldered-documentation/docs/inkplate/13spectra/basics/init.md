---  
slug: /inkplate/13spectra/basics/initialization  
title: Inkplate 13SPECTRA – Initialization
sidebar_label: Initialization
id: 13spectra-init  
hide_title: true  
---

<SectionTitle title="Initialization" backgroundImage="img/arduino_bg.jpg" />

Let's get started writing our first Inkplate sketch! Before using Inkplate in Arduino code, it must be initialized in the `setup()` function of your sketch. This page contains details on how to do that.

---

## Initializing Inkplate and updating the display

The most basic sketch on Inkplate 13SPECRA is as follows. It initializes Inkplate in memory and lears the e-paper display:

```cpp
#include <Inkplate.h>
Inkplate display;   // Create Inkplate object

void setup(){
    // Initialize Inkplate
    display.begin();    
    // Update the display
    display.display()
    // As the frame buffer is empty upon initialization, this will display a blank screen
}
void loop(){
    // Do nothing here
}
```

<FunctionDocumentation
    functionName="Inkpate display"
    description="Creates an Inkplate object from the Inkplate class."
    returnType="none"
/>

<FunctionDocumentation
    functionName="display.begin()"
    description="In short, this function initializes the Inkplate object. It starts I2C, allocates the required memory for the frame buffer, and initializes the onboard peripherals."
    returnType="none"
/>

---

## Display rotation

In case you want to use Inkplate in portrait mpde or in any 90-degree rotation, use `inkplate.setRotation()`:

<FunctionDocumentation
    functionName="display.setRotation()"
    description="Sets the cardinal rotation of the display. This automatically adjusts the (0, 0) x-y coordinate origin point."
    returnDescription="none"
    parameters={[
    { type: 'uint8_t', name: '_rotation', decription:"Ranges from 0 to 270. 0 is the default rotation; 1 rotates by 90 degrees, 2 by 180 degrees, and 3 by 270 degrees." },
    ]}
/>