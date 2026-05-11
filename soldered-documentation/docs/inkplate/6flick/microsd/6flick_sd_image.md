---  
slug: /inkplate/6flick/microsd/sd-image  
title: Inkplate 6FLICK – Image from microSD
sidebar_label: Image from microSD
id: 6flick-microsd-image  
hide_title: true  
---

<SectionTitle title="Display Images from SD Card" backgroundImage="img/sd_picture.jpg" />

The `Inkplate6FLICK_SD_Pictures` example demonstrates how to load and display image files from a microSD card on the Inkplate 6Flick. This is ideal for dynamic content such as photo slideshows or interface elements loaded at runtime.

---

## SD Card Image Display

The Inkplate library can render BMP and JPG images directly from an SD card. This allows you to present rich graphical content without hardcoding images into your firmware.

<WarningBox>Ensure your SD card is formatted as FAT32 and that image filenames use the 8.3 filename format (e.g., `image1.bmp`, `photo.jpg`). Only baseline JPEGs and uncompressed 24-bit BMPs are supported.</WarningBox>

<InfoBox>By default, the SD card must be inserted before power-up or reset. If hot-swapping is necessary, reinitialize the SD card interface using `SD.begin()`.</InfoBox>

```cpp
#include "Inkplate.h"            // Include the Inkplate library in the sketch
Inkplate display(INKPLATE_3BIT); // Create an Inkplate object and set the library to 3-bit mode
SdFile file;                   // Create an SdFile object for accessing files on the SD card

void setup()
{
    display.begin();           // Initialize the Inkplate library (you should call this function ONLY ONCE)
    display.clearDisplay();    // Clear the display's frame buffer
    display.setTextColor(BLACK); // Set the text color to black
    display.setTextSize(3);    // Set font size to 3

    // Initialize SD card. Display whether the SD card is initialized properly or not.
    if (display.sdCardInit())
    {
        display.println("SD Card OK! Reading image...");
        display.display();

        // If the card is properly initialized, try to load an image and display it on the e-paper at position X=0, Y=0.
        // NOTE: Both drawImage methods allow for an optional fifth "invert" parameter. Setting this parameter
        // to true will invert all colors in the image, making black white and white black. This may be necessary when
        // exporting bitmaps from certain software.
        if (!display.drawImage("image1.bmp", 0, 0, 1))
        {
            // If something fails (wrong filename or incorrect bitmap format), write an error message on the screen.
            // REMEMBER! You can only use Windows Bitmap files with color depths of 1, 4, 8, or 24 bits with no
            // compression! You can turn off dithering for somewhat faster image loading by changing the last 1 to 0, or
            // by removing the 1 argument completely.
            display.println("Image open error");
        }
        display.display();
        delay(5000);

        // Now try to load an image using the SdFat library class (for more advanced users) and display the image on the e-paper.
        display.clearDisplay();
        if (file.open("image2.bmp", O_RDONLY))
        {
            display.drawBitmapFromSd(&file, 0, 0);
        }
        else
        {
            display.println("Image open error");
        }   
        display.display();
        delay(5000);
    
        // Now draw a JPEG.
        display.clearDisplay();
        if (!display.drawImage("pyramid.jpg", 100, 0, true, false))
        {
            // If something fails (wrong filename or incorrect format), write an error message on the screen.
            // You can turn off dithering for somewhat faster image loading by changing the fifth parameter to false, or
            // by removing the parameter completely.
            display.println("Image open error");
        }       
        display.display();
    }
    else
    {
        // If SD card initialization is not successful, display an error on the screen.
        display.println("SD Card error!");        
        display.display();
    }

    // Turn off the MOSFET that powers the SD card.
    display.sdCardSleep();
}

void loop()
{
    // Nothing...
}
```

<CenteredImage src="/img/inkplate_6_flick/img_from_sd.png" alt="Example Image" caption="Example Image" />

<FunctionDocumentation
    functionName="inkplate.drawImage()"
    description="This function draws an image from a char path."
    returnDescription="Returns true if the image was successfully drawn, otherwise false."
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
  title="Inkplate6FLICK_SD_Pictures.ino" 
  description="This example will show you how to read .bmp and .jpeg files (pictures) from an SD card and display the image on an e-paper display."
  url="https://github.com/SolderedElectronics/Inkplate-Arduino-library/tree/dev/examples/Inkplate6FLICK/Advanced/SD/Inkplate6FLICK_SD_Pictures" 
/>