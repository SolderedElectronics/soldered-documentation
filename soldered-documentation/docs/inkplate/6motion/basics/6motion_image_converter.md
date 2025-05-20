---
slug: /inkplate/6motion/basics/image-converter
title: 6Motion - Soldered Image Converter
id: 6motion-image-converter
---

<CenteredImage src="/img/inkplate_6_motion/image_converter.png" alt="Soldered Image Converter" caption="Graphical user interface of the Soldered Image Converter" width="800px" />

Soldered Image Converter is an open-source Python program by Soldered. It is used to convert images for Inkplate boards into .h files, which can be included in Arduino sketches for Inkplate and then displayed.
<QuickLink 
  title="Soldered Image Converter Repository" 
  description="See the README in this repository for details on how to download and install the Soldered Image Converter."
  url="https://github.com/SolderedElectronics/Soldered-Image-Converter/" 
/>

After converting images, export the .h files and save them in your Inkplate sketch's project folder. To find this folder, go to `Sketch -> Show Sketch Folder` in Arduino.

Place the exported .h files in that folder, then include them in the sketch and use the `drawImage` function.

---

## Black and White Bitmap

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

## Grayscale Image

```cpp
// Include Inkplate Motion library
#include <InkplateMotion.h>
// Include converted image, make sure to use 4-bit mode in conversion
#include "images/imageGrayscale.h"
Inkplate inkplate; // Create Inkplate object
void setup()
{
    // Initialize Inkplate in black and white mode
    inkplate.begin(INKPLATE_BLACKWHITE); 

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

## Full Example

<QuickLink 
  title="Inkplate_6_Motion_Image_Converter.ino" 
  description="The full example for drawing images using the Soldered Image Converter."
  url="https://github.com/SolderedElectronics/Inkplate_Motion_Arduino_Library/blob/main/examples/Inkplate6Motion/Basic/Inkplate_6_Motion_Image_Converter/Inkplate_6_Motion_Image_Converter.ino" 
/>
