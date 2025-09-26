---
slug: /inkplate/5v2/micropython/basics/init-and-display-update
title: Inkplate 5v2 MicroPython - Initialization and display update
sidebar_label: Initialization and display update
id: init-and-display-update
---

## Initializing Inkplate

Here is a basic Inkplate object creation and display initialization which we will use in every example in following tutorials:

```python
from inkplate5v2 import Inkplate

# Create Inkplate object
inkplate=Inkplate(Inkplate.INKPLATE_1BIT)

# Initialize the display, needs to be called only once
inkplate.begin()

# Clear the display buffer
inkplte.clearDisplay()

# Draw what is currently stored in frame buffer, needs to be called to update the display
inkplate.display()
```

<FunctionDocumentation
    functionName="inkplate=Inkplate()"
    description="Creates the Inkplate object, in this example we are using enum Inkplate.INKPLATE_1BIT to set the display mode in Black and White mode."
    parameters={[
        {type: 'Number', name: 'mode', description: 'Enum representation of a integer value that sets the display mode as either Black-White or Grayscale.' }
    ]}
/>

<InfoBox> To learn more about Grayscale mode, check [this documentation](/documentation/inkplate/5v2/micropython/basics/printing-text/#displaying-text-in-grayscale-and-more-text-parameters)</InfoBox>

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
    functionName="inkplate.clearDisplay()"
    description="Clears the internal frame buffer (does not change the panel until you update)."

/>

<FunctionDocumentation
    functionName="inkplate.display()"
    description="Performs a full-screen refresh, sending the current frame buffer to the panel."
/>