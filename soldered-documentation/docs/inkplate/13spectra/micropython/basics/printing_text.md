---
slug: /inkplate/13spectra/micropython/basics/printing-text
title: Inkplate 13SPECTRA MicroPython - Printing text
sidebar_label: Printing text
id: 13spectra-printing-text
---

Inkplate 13SPECTRA allows you to print text on a **1600 x 1200px canvass**.

## Displaying basic information

Below is a simple example demonstrating the simple way of displaying the information on the Inkplate display.

```python
from inkplate13SPECTRA import Inkplate
import time

inkplate = Inkplate()
inkplate.begin()
inkplate.clearDisplay()
inkplate.display()

# Putting the text in display buffer
inkplate.printText("Hello World!")
inkplate.display()
```

<FunctionDocumentation
  functionName="inkplate.print()"
  description="Puts the text in display buffer at the current position on display"
  parameters={[
    { type: 'String', name: 'text', description: 'String to render.' }
  ]}
/>

[IMAGE PLACEHOLDER]

---

## Displaying text in different colors and more text parameters

Inkplate 13SPECTRA also lets you render color graphics on its canvas. You can also modify different text parameters, such as text color, text size and text wrapping. Below is a simple example demonstrating different text colors and different text styles:

