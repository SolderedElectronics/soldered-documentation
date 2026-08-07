---
slug: /inkplate/6motion/basics/image-converter
title: Inkplate 6MOTION - Soldered Image Converter
sidebar_label: Soldered Image Converter
id: 6motion-image-converter
---

<CenteredImage src="/img/image_converter_web.png" alt="Soldered Image Converter" caption="Soldered Image Converter web tool" width="1000px" />

The Soldered Image Converter is a free web tool that converts images into `.h` header files ready to include in your Arduino sketch and display on Inkplate.

<QuickLink 
  title="Soldered Image Converter" 
  description="Open the web-based image converter tool."
  url="https://tools.soldered.com/tools/image-converter/" 
/>

After converting images, export the .h files and save them in your Inkplate sketch's project folder. To find this folder, go to `Sketch -> Show Sketch Folder` in Arduino.

Place the exported .h files in that folder, then include them in the sketch and draw them with `drawBitmap()` for 1-bit images or `drawBitmap4Bit()` for 4-bit grayscale ones.

---

## Black and white bitmap

```cpp
// Include Inkplate Motion library
#include <InkplateMotion.h>
// Include converted image, make sure to use 1-bit mode in conversion
#include "images/imageBW.h"
Inkplate inkplate; // Create Inkplate object
void setup()
{
    // Initialize Inkplate in black and white mode
    inkplate.begin(INKPLATE_BLACKWHITE);

    // Draw the black and white image at (0, 0)
    // The last parameter determines the color of the bitmap
    // The image is pre-dithered using Floyd-Steinberg in the image converter
    inkplate.drawBitmap(0, 0, imageBW, imageBW_w, imageBW_h, BLACK);
    inkplate.display(); // Update the display
}
void loop()
{
  // Do nothing here
}
```

<FunctionDocumentation
  functionName="inkplate.drawBitmap()"
  description="Draws a 1-bit image stored in RAM that was converted by the Soldered Image Converter. The function places the image into the framebuffer at the specified (x, y) position. A call to display() or partialUpdate() is required to render it on the screen. This function stamps the bitmap in the specified color, while unset bits remain transparent. It is recommended to call clearDisplay() before drawing a full-screen image to prevent artifacts."
  returnDescription="None"
  parameters={[ 
    { type: 'int16_t', name: 'x', description: 'Top-left x-coordinate.' },
    { type: 'int16_t', name: 'y', description: 'Top-left y-coordinate.' },
    { type: 'const uint8_t[]', name: 'bitmap', description: 'Byte array containing the monochrome bitmap.' },
    { type: 'int16_t', name: 'w', description: 'Width of the bitmap in pixels.' },
    { type: 'int16_t', name: 'h', description: 'Height of the bitmap in pixels.' },
    { type: 'uint16_t', name: 'color', description: "Color used for drawing the bitmap pixels. Can be BLACK or WHITE." }
  ]}
/>

---

## Grayscale image

```cpp
// Include Inkplate Motion library
#include <InkplateMotion.h>
// Include converted image, make sure to use 4-bit mode in conversion
#include "images/imageGrayscale.h"
Inkplate inkplate; // Create Inkplate object
void setup()
{
    // Initialize Inkplate in grayscale mode - required for 4-bit images
    inkplate.begin(INKPLATE_GRAYSCALE); 

    // Draw the grayscale image at (0, 0)
    // The image is pre-dithered using Floyd-Steinberg in the image converter
    inkplate.drawBitmap4Bit(0, 0, imageGrayscale, imageGrayscale_w, imageGrayscale_h);
    inkplate.display(); // Update the display
}
void loop()
{
  // Do nothing here
}
```
<FunctionDocumentation
  functionName="inkplate.drawBitmap4Bit()"
  description="Draws a 4-bit grayscale bitmap at the specified (x, y) position. The bitmap should be stored in memory and formatted as a 4-bit grayscale image, where each pixel is represented by 4 bits (16 grayscale levels). The function places the image into the framebuffer, and display() or partialUpdate() must be called to render it on the screen."
  returnDescription="None"
  parameters={[ 
    { type: 'int16_t', name: '_x', description: 'Top-left x-coordinate.' },
    { type: 'int16_t', name: '_y', description: 'Top-left y-coordinate.' },
    { type: 'const unsigned char*', name: '_p', description: 'Pointer to the byte array containing the 4-bit grayscale bitmap data.' },
    { type: 'int16_t', name: '_w', description: 'Width of the bitmap in pixels.' },
    { type: 'int16_t', name: '_h', description: 'Height of the bitmap in pixels.' }
  ]}
/>

---

## Full example

<QuickLink 
  title="Inkplate_6_Motion_Image_Converter.ino" 
  description="The full example for drawing images using the Soldered Image Converter."
  url="https://github.com/SolderedElectronics/Inkplate_Motion_Arduino_Library/blob/main/examples/Inkplate6Motion/Basic/Inkplate_6_Motion_Image_Converter/Inkplate_6_Motion_Image_Converter.ino" 
/>