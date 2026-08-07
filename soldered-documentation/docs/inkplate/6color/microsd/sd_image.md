---
slug: /inkplate/6color/microsd/sd-image
title: Inkplate 6COLOR – Image from microSD
sidebar_label: Image from microSD
id: microsd-image
---

To draw images from the microSD card, use the `display.image.draw()` function.

<InfoBox>Supported formats are: JPG, BMP and PNG.</InfoBox>

<WarningBox>JPG files **without** progressive encoding are supported.</WarningBox>

---

## Drawing PNG, JPG and BMP files from the microSD card

Let's draw example images of different formats on Inkplate. Download them from the [**Inkplate library**](https://github.com/SolderedElectronics/Inkplate-Arduino-library/tree/master/examples/Inkplate6COLOR/Advanced/microSD/Inkplate6COLOR_microSD_Pictures) and place them in the root folder of the microSD card:

```cpp
#include "Inkplate.h" // Include Inkplate library to the sketch
Inkplate display;     // Create an object on Inkplate library and also set library into 3 Bit mode
SdFile file;          // Create SdFile object used for accessing files on SD card

void setup()
{
    // Init serial communication
    Serial.begin(115200);

    display.begin();             // Init Inkplate library (you should call this function ONLY ONCE)
    display.clearDisplay();      // Clear frame buffer of display
    display.setTextColor(BLACK); // Set text color to black
    display.setTextSize(3);      // Set font size to 3

    // Init SD card. Display if SD card is init propery or not.
    if (display.sdCardInit())
    {
        Serial.println("SD Card OK! Reading image...");

        // If card is properly init, try to load image and display it on e-paper at position X=0, Y=0
        // NOTE: Both drawImage methods allow for an optional fifth "invert" parameter. Setting this parameter
        // to true will flip all colors on the image, making black white and white black. This may be necessary when
        // exporting bitmaps from certain softwares.
        if (display.image.draw("image1.bmp", 0, 0, 1))
        {
            display.display();
            delay(5000);
        }
        else
        {
            // If is something failed (wrong filename or wrong bitmap format), write error message on the Serial
            // Monitor. REMEMBER! You can only use Windows Bitmap file with color depth of 1, 4, 8 or 24 bits with no
            // compression! You can turn of dithering for somewhat faster image load by changing the last 1 to 0, or
            // removing the 1 argument completely
            Serial.println("Image open error");
        }


        // Now try to load image using SdFat library class (for more advanced users) and display image on epaper.
        display.clearDisplay();
        if (file.open("image2.bmp", O_RDONLY))
        {
            display.image.drawBitmapFromSd(&file, 0, 0);
            display.display();
            delay(5000);
        }
        else
        {
            Serial.println("Image open error");
        }
    }
    else
    {
        // If SD card init not success, display error on screen
        Serial.println("SD Card error!");
    }

    // Turn off the MOSFET that powers the SD card
    display.sdCardSleep();
}

void loop()
{
    // Nothing...
}
```

<CenteredImage src="/img/6color/image1.png" alt="Expected output on Inkplate display" caption="Example image 1" width="1000px" />

<CenteredImage src="/img/6color/image2.png" alt="Expected output on Inkplate display" caption="Example image 2" width="1000px" />

<FunctionDocumentation
    functionName="display.image.draw()"
    description="The function draws an image from the given path."
    returnDescription="Returns true if the image was successfully drawn, otherwise false."
    parameters={[
    { type: "const char*", name: "path", description: "The path and filename of the image. Can be a URL (for web images) or a file path (on the microSD card)." },
    { type: "int", name: "x", description: "X-coordinate of the image's upper-left corner in the framebuffer." },
    { type: "int", name: "y", description: "Y-coordinate of the image's upper-left corner in the framebuffer." },
    { type: "bool", name: "dither", description: "Dithering mode: false (disabled), true (enabled). Defaults to true." },
    { type: "bool", name: "invert", description: "If true, inverts colors." },
    ]}
/>

---

## Full example

<QuickLink 
  title="Inkplate6COLOR_microSD_Pictures.ino" 
  description="This example shows you how to read .bmp and .jpeg files (pictures) from the SD card and display them on the e-paper display."
  url="https://github.com/SolderedElectronics/Inkplate-Arduino-library/blob/master/examples/Inkplate6COLOR/Advanced/microSD/Inkplate6COLOR_microSD_Pictures/Inkplate6COLOR_microSD_Pictures.ino" 
/>