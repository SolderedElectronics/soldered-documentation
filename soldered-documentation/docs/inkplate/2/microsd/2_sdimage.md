---
slug: /inkplate/2/microsd/sd-image
title: Inkplate 2 – Image from microSD
sidebar_label: Image from microSD
id: 2-microsd-image
---

To draw images form the microSD card, use the `drawImage()` function.

<InfoBox>Supported formats are: JPG, BMP and BMP.</InfoBox>

<WarningBox>JPG files **without** progressive encoding are supported.</WarningBox>

---

## Drawing PNG, JPG and BMP files from the microSD card

Let's draw the example images of different formats on Inkplate, download them from the [**Inkplate library**](https://github.com/SolderedElectronics/Inkplate-Arduino-library/tree/7694c2963e95560dfc71d0b26bd8bf1960e08b6e/examples/Inkplate10/Advanced/SD/Inkplate10_SD_Pictures) and place them in the root folder of the microSD card:

Let's draw `image1.png` at coordinates 0, 0 and using the `display.drawImage()` function:

```cpp
// Make sure Inkplate and then the microSD card are initialized before this
if (!display.drawImage("image1.bmp", 0, 0, 1))
    {
        // If is something failed (wrong filename or wrong bitmap format), write error message on the screen.
        // REMEMBER! You can only use Windows Bitmap file with color depth of 1, 4, 8 or 24 bits with no
        // compression! You can turn of dithering for somewhat faster image load by changing the last 1 to 0, or
        // removing the 1 argument completely
        display.println("Image open error");
    }
display.display();
```
Now, lets draw `image2.bmp` by frst loading it using SdFat library class and then displaying it on epaper:

```cpp
if (file.open("image2.bmp", O_RDONLY))
        {
            display.drawBitmapFromSd(&file, 0, 0);
        }
        else
        {
            display.println("Image open error");
        }   
        display.display();
```

Lets try another file format, for example, jpg:
```cpp
if (!display.drawImage("pyramid.jpg", 100, 0, true, false))
        {
            // If is something failed (wrong filename or wrong format), write error message on the screen.
            // You can turn off dithering for somewhat faster image load by changing the fifth parameter to false, or
            // removing the parameter completely
            display.println("Image open error");
        }       
        display.display();
```
<FunctionDocumentation
    functionName="inkplate.drawImage()"
    description="Function draws image from char path."
    returnDescription="Returns true if image was successfully drawn, otherwise false."
    parameters={[
    { type: "const char*", name: "path", description: "Path and filename of the image. Can be a URL (for web images) or a file path (on the microSD card)." },
    { type: "int", name: "x", description: "X-coordinate of the image's upper-left corner in the framebuffer." },
    { type: "int", name: "y", description: "Y-coordinate of the image's upper-left corner in the framebuffer." },
    { type: "uint8_t", name: "dither", description: "Dithering mode: 0 (disabled), 1 (enabled)." },
    { type: "bool", name: "invert", description: "If true, inverts colors." },
    ]}
/>

---

## Full example

<QuickLink 
  title="Inkplate10_SD_Pictures.ino" 
  description="This example will show you how you can read .bmp and .jpeg files (pictures) from SD card and display that image on e-paper display."
  url="https://github.com/SolderedElectronics/Inkplate-Arduino-library/blob/7694c2963e95560dfc71d0b26bd8bf1960e08b6e/examples/Inkplate10/Advanced/SD/Inkplate10_SD_Pictures/Inkplate10_SD_Pictures.ino" 
/>