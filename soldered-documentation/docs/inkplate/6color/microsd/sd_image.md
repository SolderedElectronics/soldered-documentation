---
slug: /inkplate/6color/microsd/sd-image
title: Image from microSD
id: microsd-image
---

To draw images from the microSD card, use the `drawImage()` function.

<InfoBox>Supported formats are: JPG, BMP and PNG.</InfoBox>

<WarningBox>JPG files **without** progressive encoding are supported.</WarningBox>

---

## Drawing PNG, JPG and BMP files from the microSD card

Let's draw example images of different formats on Inkplate. Download them from the [**Inkplate library**](https://github.com/SolderedElectronics/Inkplate-Arduino-library/tree/master/examples/Inkplate6COLOR/Advanced/SD/Inkplate6COLOR_SD_Pictures) and place them in the root folder of the microSD card:

```cpp
#include "Inkplate.h" // Include the Inkplate library in the sketch
Inkplate display;     // Create an Inkplate object and set the library to 3-bit mode
SdFile file;          // Create an SdFile object used for accessing files on the SD card

void setup()
{
    // Initialize serial communication
    Serial.begin(115200);

    display.begin();             // Initialize the Inkplate library (you should call this function only once)
    display.clearDisplay();      // Clear the display's frame buffer
    display.setTextColor(BLACK); // Set text color to black
    display.setTextSize(3);      // Set the font size to 3

    // Initialize the SD card. Display whether the SD card is properly initialized or not.
    if (display.sdCardInit())
    {
        Serial.println("SD Card OK! Reading image...");

        // If the card is properly initialized, try to load the image and display it on the e-paper at position X=0, Y=0
        // NOTE: Both drawImage methods allow for an optional fifth "invert" parameter. Setting this parameter
        // to true will flip all colors on the image, making black white and white black. This may be necessary when
        // exporting bitmaps from certain software.
        if (display.drawImage("image1.bmp", 0, 0, 1))
        {
            display.display();
            delay(5000);
        }
        else
        {
            // If something fails (wrong filename or wrong bitmap format), write an error message on the Serial Monitor.
            // REMEMBER! You can only use Windows Bitmap files with color depths of 1, 4, 8 or 24 bits with no compression!
            // You can turn off dithering for somewhat faster image load by changing the last 1 to 0, or removing the '1' argument completely.
            Serial.println("Image open error");
        }

        // Now try to load the image using the SdFat library class (for more advanced users) and display the image on the e-paper.
        display.clearDisplay();
        if (file.open("image2.bmp", O_RDONLY))
        {
            display.drawBitmapFromSd(&file, 0, 0);
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
        // If the SD card initialization is unsuccessful, display an error on the screen
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
    functionName="inkplate.drawImage()"
    description="The function draws an image from the given path."
    returnDescription="Returns true if the image was successfully drawn, otherwise false."
    parameters={[
    { type: "const char*", name: "path", description: "The path and filename of the image. Can be a URL (for web images) or a file path (on the microSD card)." },
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
  description="This example shows you how to read .bmp and .jpeg files (pictures) from the SD card and display them on the e-paper display."
  url="https://github.com/SolderedElectronics/Inkplate-Arduino-library/blob/7694c2963e95560dfc71d0b26bd8bf1960e08b6e/examples/Inkplate10/Advanced/SD/Inkplate10_SD_Pictures/Inkplate10_SD_Pictures.ino" 
/>