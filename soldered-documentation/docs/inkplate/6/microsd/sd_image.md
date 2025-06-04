---  
slug: /inkplate/6/microsd/sd-image  
title: Image from microSD  
id: microsd-image  
---  

To draw images from the microSD card, use the `drawImage()` function.

<InfoBox>Supported formats are: JPG, BMP and PNG.</InfoBox>

<WarningBox>JPG files **without** progressive encoding are supported.</WarningBox>

---  

## Drawing PNG, JPG and BMP files from the microSD card

Let's draw example images of different formats on Inkplate. Download them from the [**Inkplate library**](https://github.com/SolderedElectronics/Inkplate-Arduino-library/tree/master/examples/Inkplate6/Advanced/SD/Inkplate6_SD_Pictures) and place them in the root folder of the microSD card:

```cpp
/*
   Inkplate6_SD_Pictures example for Soldered Inkplate 6
   For this example you will need a micro USB cable, an Inkplate6, and an SD card loaded with
   image1.bmp and image2.bmp files that can be found inside the folder of this example.
   Select "e-radionica Inkplate6" or "Soldered Inkplate6" from Tools -> Board menu.
   Don't see the "e-radionica Inkplate6" or "Soldered Inkplate6" option? Follow our tutorial and add it:
   https://soldered.com/learn/add-inkplate-6-board-definition-to-arduino-ide/

   You can open .bmp, .jpeg, or .png files (but there are some limitations imposed by the library) that have 
   a color depth of 1-bit (BW bitmap), 4-bit, 8-bit, or 24-bit and have a resolution smaller than 800x600,
   or else they won't fit on the screen. Format your SD card using the standard FAT file format.

   This example will show you how to read .bmp and .jpeg files (pictures) from the SD card and
   display the image on the e-paper display.

   Want to learn more about Inkplate? Visit www.inkplate.io
   Looking to get support? Write on our forums: https://forum.soldered.com/
   17 February 2023 by Soldered
*/

// Next three lines are a precaution; you can ignore these, and the example would also work without them
#if !defined(ARDUINO_ESP32_DEV) && !defined(ARDUINO_INKPLATE6V2)
#error "Wrong board selection for this example, please select e-radionica Inkplate6 or Soldered Inkplate6 in the boards menu."
#endif

#include "Inkplate.h"            // Include the Inkplate library in the sketch
Inkplate display(INKPLATE_3BIT); // Create an object from the Inkplate library and set the library to 3-bit mode
SdFile file;                   // Create an SdFile object used for accessing files on the SD card

void setup()
{
    display.begin();             // Initialize the Inkplate library (you should call this function ONLY ONCE)
    display.clearDisplay();      // Clear the frame buffer of the display
    display.setTextColor(BLACK); // Set text color to black
    display.setTextSize(3);      // Set font size to 3

    // Initialize the SD card. Display whether the SD card is initialized properly or not.
    if (display.sdCardInit())
    {
        display.println("SD Card OK! Reading image...");
        display.display();

        // If the card is initialized properly, try to load the image and display it on the e-paper at position X=0, Y=0
        // NOTE: Both drawImage methods allow for an optional fifth "invert" parameter. Setting this parameter
        // to true will flip all colors on the image, making black white and white black. This may be necessary when
        // exporting bitmaps from certain software.
        if (!display.drawImage("image1.bmp", 0, 0, 1))
        {
            // If something failed (wrong filename or wrong bitmap format), write an error message on the screen.
            // REMEMBER! You can only use Windows Bitmap files with a color depth of 1, 4, 8, or 24 bits with no
            // compression! You can turn off dithering for a somewhat faster image load by changing the last parameter
            // from 1 to 0, or by removing the 1 argument completely.
            display.println("Image open error");
        }
        display.display();
        delay(5000);

        // Now try to load the image using the SdFat library class (for more advanced users) and display the image on the e-paper.
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
    
        // Now draw a JPEG
        display.clearDisplay();
        if (!display.drawImage("pyramid.jpg", 100, 0, true, false))
        {
            // If something fails (wrong filename or wrong format), write an error message on the screen.
            // You can turn off dithering for a somewhat faster image load by changing the fifth parameter to false, or
            // by removing the parameter completely.
            display.println("Image open error");
        }       
        display.display();
    }
    else
    {
        // If the SD card fails to initialize, display an error on the screen
        display.println("SD Card error!");        
        display.display();
    }

    // Turn off the MOSFET that powers the SD card
    display.sdCardSleep();
}

void loop()
{
    // Nothing...
}
```

<CenteredImage src="/img/6/image1.jpg" alt="Expected output on Inkplate display" caption="Example image 1" width="1000px" />

<CenteredImage src="/img/6/image2.jpg" alt="Expected output on Inkplate display" caption="Example image 2" width="1000px" />

<CenteredImage src="/img/6/image3.jpg" alt="Expected output on Inkplate display" caption="Example image 3" width="1000px" />

<FunctionDocumentation
    functionName="inkplate.drawImage()"
    description="The function draws an image from the given path."
    returnDescription="Returns true if the image was successfully drawn, otherwise false."
    parameters={[  
    { type: "const char*", name: "path", description: "The path and filename of the image. Can be a URL (for web images) or a file path (on the microSD card)." },
    { type: "int", name: "x", description: "The X-coordinate of the image's upper-left corner in the framebuffer." },
    { type: "int", name: "y", description: "The Y-coordinate of the image's upper-left corner in the framebuffer." },
    { type: "uint8_t", name: "dither", description: "Dithering mode: 0 (disabled), 1 (enabled)." },
    { type: "bool", name: "invert", description: "If true, inverts colors." },
    ]}
/>

---  

## Full example

<QuickLink 
  title="Inkplate6_SD_Pictures.ino" 
  description="This example shows you how to read .bmp and .jpeg files (pictures) from the SD card and display them on the e-paper display."
  url="https://github.com/SolderedElectronics/Inkplate-Arduino-library/blob/master/examples/Inkplate6/Advanced/SD/Inkplate6_SD_Pictures/Inkplate6_SD_Pictures.ino" 
/>