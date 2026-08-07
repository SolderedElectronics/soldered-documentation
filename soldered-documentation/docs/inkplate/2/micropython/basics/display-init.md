---  
slug: /inkplate/2/micropython/basics/display-initialization
title: Inkplate 2 – Initialization and display
sidebar_label: Initialization and display
id: display-initialization
hide_title: false  
---

## Initializing Inkplate

Here is a basic Inkplate object creation and display initialization, which we'll use in every example in the following tutorials:

```python
# Include inkplate library
from inkplate2 import Inkplate

# Create Inkplate object
inkplate = Inkplate()

# Initialize the display, needs to be called only once
inkplate.begin()

# Draw what is currently stored in frame buffer, needs to be called to update the display
inkplate.display()
```

<FunctionDocumentation
  functionName="inkplate.Inkplate()"
  description="Creates an Inkplate object from the Inkplate class."
  returnType="none"
/>
<FunctionDocumentation
  functionName="inkplate.begin()"
  description="Initializes the Inkplate object. It starts I2C, allocates the required memory for the frame buffer, and initializes the onboard peripherals."
  returnType="none"
/>
<FunctionDocumentation
  functionName="inkplate.display()"
  description="This function refreshes the display and draws what is currently in the frame buffer. It must be called to update the display. This is a full refresh that completely wipes the e-Paper and then draws everything from the frame buffer."
  returnType="none"
/>

## Clear display

<FunctionDocumentation
  functionName="inkplate.clear_display()"
  description="This function clears everything stored in display buffer."
  returnType="none"
/>

<InfoBox> Screen refresh time takes about **12 - 15 seconds**. The screen may flicker while updating, which is normal.</InfoBox>

---

## Full example

<QuickLink title="hello_world.py" 
description="Displays 'Hello world!' text on the Inkplate 2 screen." 
url="https://github.com/SolderedElectronics/Inkplate-micropython/blob/master/examples/inkplate2/hello_world.py" />
