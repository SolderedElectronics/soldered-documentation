---
slug: /inkplate/5v2/micropython/basics/init-and-display-update
title: Inkplate 5v2 MicroPython - Initialization and display update
sidebar_label: Initialization and display update
id: init-and-display-update
---

## Initializing Inkplate

Every example in the following tutorials starts the same way: create an Inkplate object and initialize the display.

```python
from inkplate5v2 import Inkplate

# Create Inkplate object
inkplate=Inkplate(Inkplate.INKPLATE_1BIT)

# Initialize the display, needs to be called only once
inkplate.begin()

# Clear the display buffer
inkplate.clear_display()

# Draw what is currently stored in frame buffer, needs to be called to update the display
inkplate.display()
```

<FunctionDocumentation
    functionName="Inkplate()"
    description="Creates the Inkplate object. This example uses the enum Inkplate.INKPLATE_1BIT to set the display to black and white mode."
    parameters={[
        {type: 'Number', name: 'mode', description: 'Enum representation of an integer value that sets the display mode to either black-white or grayscale.' }
    ]}
/>

<InfoBox> To learn more about grayscale mode, see [this page](/inkplate/5v2/micropython/basics/printing-text/#displaying-text-in-grayscale-and-more-text-parameters)</InfoBox>

<InfoBox>
| **VALUE** 	| **ENUM** 	|
|---	|---	|
| Black-White mode 	| `INKPLATE_1BIT`	|
| Grayscale 	| `INKPLATE_2BIT` 	|
</InfoBox>

<FunctionDocumentation
    functionName="inkplate.begin()"
    description="Initializes the display, this must be called only once after creating the Inkplate object."
/>

<FunctionDocumentation
    functionName="inkplate.clear_display()"
    description="Clears the internal frame buffer (does not change the panel until you update)."

/>

<FunctionDocumentation
    functionName="inkplate.display()"
    description="Performs a full-screen refresh, sending the current frame buffer to the panel."
/>