---
slug: /inkplate/13spectra/micropython/basics/init-and-display-update
title: Inkplate 13SPECTRA MicroPython - Initialization and display update
sidebar_label: Initialization and display update
id: 13spectra-init-and-display-update
---

## Initializing Inkplate

Here is a basic Inkplate object creation and display initialization which we will use in every example in following tutorials:

```python
# Include all the required libraries
from inkplate13SPECTRA import Inkplate

# Create Inkplate object
display = Inkplate()

# Initialize the display, needs to be called only once
display.begin()

# Clear the display buffer
display.clearDisplay()

# Draw what is currently in frame buffer, needs to be called to update the display
inkplate.display()
```

<FunctionDocumentation
    functionName="inkplate=Inkplate()"
    description="Creates the Inkplate object."
/>

<FunctionDocumentation
    functionName="inkplate.begin()"
    description="Initializes the display, this must be called only once after creating the Inkplate object."
/>

<FunctionDocumentation
    functionName="inkplate.clearDisplay()"
    description="Clears the internal frame buffer (does not change the panel until you update)."

/>

<FunctionDocumentation
    functionName="inkplate.display()"
    description="Performs a full-screen refresh, sending the current frame buffer to the panel."
/>