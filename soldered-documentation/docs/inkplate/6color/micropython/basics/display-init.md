---  
slug: /inkplate/6color/micropython/basics/display-initialization
title: Inkplate 6COLOR – Initialization and display
sidebar_label: Initialization and display
id: display-initialization
hide_title: false  
---

## Initializing Inkplate

Here is a basic Inkplate object creation and display initialization which we will use in every example in following tutorials:

```python
# Include inkplate library
from inkplate6COLOR import Inkplate

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
  description="In short, this function initializes the Inkplate object. It starts I2C, allocates the required memory for the frame buffer, and initializes the onboard peripherals."
  returnType="none"
/>
<FunctionDocumentation
  functionName="inkplate.display()"
  description="This function refreshes the display and draws what is currently in the frame buffer, this function must be called to update the display. This is a full refresh that completely wipes the e-Paper and then draws everything from the frame buffer."
  returnType="none"
/>

<InfoBox> Screen refresh time takes about **12 seconds** which is expected for this kind of display. You may also see it flicker in multiple colors during refresh but that is normal behaviour. </InfoBox>