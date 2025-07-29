---
slug: /inkplate/4tempera/microsd/sd-basics
title: Inkplate 4TEMPERA – MicroSD basics
sidebar_label: MicroSD basics
id: 4tempera-microsd-basics
hide_title: true
---

<SectionTitle title="MicroSD basics" backgroundImage="/img/microsd.jpg" />

The built-in microSD card slot on Inkplate 4TEMPERA can be extremely useful for your project. It can store a vast number of high-quality image files to be displayed, and it can also read and write data during deep sleep cycles. This page contains basic examples that will help you quickly get started with using the built-in microSD card slot.

<CenteredImage src="/img/inkplate10/10_sdcard.jpg" alt="MicroSD card slot on Inkplate 4TEMPERA" caption="MicroSD card slot on Inkplate 4TEMPERA" width="600px" />

<InfoBox>Inkplate 4TEMPERA uses the [**SdFat library**](https://github.com/greiman/SdFat)</InfoBox>
<WarningBox>All supported card formats are: **FAT16, FAT32, exFAT**</WarningBox>
<WarningBox>All supported card types are: **SD, SDHC and SDXC**</WarningBox>

---

## Preparing the microSD card before usage

For best results, use the [**official SD card formatter**](https://www.sdcard.org/downloads/formatter/) to format the card to **FAT32** before use.

<CenteredImage src="/img/inkplate10/sdcard_formatter.png" alt="Official SD card formatter" caption="The official SD Card formatter" width="400px" />

---

## Initializing

Before the microSD card can be used in code, it must first be initialized. This process powers on the microSD card circuitry and performs all the necessary memory allocations. In this code snippet, the microSD card is initialized, and the result of the initialization is checked:
```cpp
#include "Inkplate.h"            // Include Inkplate library to the sketch
#include "SdFat.h"               // Include library for SD card
Inkplate inkplate(INKPLATE_1BIT); // Create an object on Inkplate library and also set library into 1 Bit mode (BW)
SdFile file;                     // Create SdFile object used for accessing files on SD card

void setup()
{
    inkplate.begin();        // Initialize Inkplate library (you should call this function ONLY ONCE)
    inkplate.clearDisplay(); // Clear frame buffer of display
    inkplate.display();      // Put clear image on display
    inkplate.setTextSize(5);

    // Initialize SD card and display whether it was initialized properly.
    if (inkplate.sdCardInit())
    {
        inkplate.println("SD Card ok! Reading data...");
        inkplate.partialUpdate();
    }
    else
    { // If initialization fails, display an error on the screen, put the SD card in sleep mode, and stop the program (using an infinite loop)
        inkplate.println("SD Card error!");        
        inkplate.partialUpdate();
        inkplate.sdCardSleep();
        while (true)
            ;
    }
}
void loop()
{
    // Nothing...
}
```
<FunctionDocumentation
    functionname="inkplate.sdCardInit()"
    description="Initializes the SD card through SPI."
    returnDescription="Returns true if the initialization was successful, otherwise returns false."
/>

---

## Reading and writing
Place a sample `text.txt` file on the microSD card and add some content to it. This code snippet will read the file and print its contents to the e-Paper:
```cpp
/*
   Inkplate4TEMPERA_SD_TXT_Read example for Soldered Inkplate 4TEMPERA
   For this example you will need only a micro USB cable, Inkplate 4TEMPERA, and an SD card
   loaded with the text.txt file found inside the example folder.
   Select "Soldered Inkplate 4TEMPERA" from Tools -> Board menu.
   Don't see the "Inkplate 4TEMPERA(ESP32)" option? Follow our tutorial to add it:
   https://soldered.com/learn/add-inkplate-6-board-definition-to-arduino-ide/

   To work with the SD card on Inkplate, you will need to add one extra library.
   Download and install it from here: https://github.com/e-radionicacom/Inkplate-6-SDFat-Arduino-Library

   You can open your own .txt file, but to ensure this example works properly, the file should
   contain no more than 200 characters and must be named text.txt.

   This example will show you how to open .txt files and display the content of that file on the Inkplate e-Paper display.

   Want to learn more about Inkplate? Visit www.inkplate.io
   Looking to get support? Write on our forums: https://forum.soldered.com/
   15 March 2024 by Soldered
*/

// The next three lines are a precaution; you can ignore them, and the example will also work without them.
#ifndef ARDUINO_INKPLATE4TEMPERA
#error "Wrong board selection for this example, please select Soldered Inkplate 4TEMPERA"
#endif

#include "Inkplate.h"            // Include Inkplate library to the sketch
#include "SdFat.h"               // Include library for SD card
Inkplate display(INKPLATE_1BIT); // Create an object on Inkplate library and also set the library to 1 Bit mode (BW)
SdFile file;                     // Create SdFile object used for accessing files on SD card

void setup()
{
    display.begin();        // Initialize Inkplate library (you should call this function ONLY ONCE)
    display.clearDisplay(); // Clear frame buffer of display
    display.display();      // Put clear image on display
    display.setRotation(1);
    display.setFrontlight(15);
    // Initialize SD card and display whether it was initialized properly.
    if (display.sdCardInit())
    {
        display.println("SD Card ok! Reading data...");
        display.partialUpdate();

        // Try to load text with a maximum length of 200 characters.
        if (!file.open("/text.txt", O_RDONLY))
        { // If it fails to open, display an error message; otherwise, read the file.
            display.println("File open error");
            display.display();
        }
        else
        {
            display.clearDisplay();    // Clear everything stored in the frame buffer of the e-Paper
            display.setCursor(0, 0);   // Set the print position at the beginning of the screen
            char text[3001];           // Array where data from the SD card is stored (max 200 characters expected)
            int len = file.fileSize(); // Get the size of the file being opened
            if (len > 3000)
                len = 3000;       // If it's more than 3000 bytes, limit to a maximum of 3000 bytes
            file.read(text, len); // Read data from the file and save it in the text array
            text[len] = 0;        // Append a null-terminating character at the end of the data
            display.setTextSize(2);
            display.print(text);   // Print the text data
            display.sdCardSleep(); // Put the SD card in sleep mode
            display.display();     // Perform a full refresh of the display
        }
    }
    else
    { // If initialization fails, display an error on the screen, put the SD card in sleep mode, and stop the program
      // (using an infinite loop)
        display.println("SD Card error!");
        display.partialUpdate();
        display.sdCardSleep();
        while (true)
            ;
    }
}

void loop()
{
    // Nothing...
}

```

<FunctionDocumentation
    functionName="file.open()"
    description="Opens a file in the current working directory."
    returnDescription="Returns true if opening is successful, otherwise returns false."
    parameters={[ 
      { type: 'const char *', name: 'path', description: "The path to the file which is being opened. If it's in the root folder, just write the filename." },
      { type: 'oflag_t', name: 'oflag', description: "The settings for opening the file. The different flags have to be OR'd, e.g., O_CREAT | O_RDWR. Below is a table of these flags and what they mean." }
    ]}
 />

| Flag     | Hex Value | Description                                |
|----------|-----------|--------------------------------------------|
| O_RDONLY | 0x00      | Open for reading only.                     |
| O_WRONLY | 0x01      | Open for writing only.                     |
| O_RDWR   | 0x02      | Open for reading and writing.              |
| O_AT_END | 0x04      | Open at the end-of-file (EOF).             |
| O_APPEND | 0x08      | Set append mode (writes are added to EOF). |
| O_CREAT  | 0x10      | Create file if it does not exist.          |
| O_TRUNC  | 0x20      | Truncate file to zero length.              |
| O_EXCL   | 0x40      | Fail if the file already exists.           |
| O_SYNC   | 0x80      | Synchronized write I/O operations.         |

<FunctionDocumentation
    functionName="file.fileSize()"
    description="Returns the total number of bytes in a file."
    returnType="uint32_t"
/>

<FunctionDocumentation
  functionName="file.read()"
  description="Reads data from the file into the provided buffer. The function attempts to read up to a given number of bytes starting from the current file pointer."
  returnDescription="Returns the number of bytes read, or -1 if an error occurs."
  parameters={[ 
    { type: 'void *', name: 'buf', description: "A pointer to the buffer where the read file data will be stored." },
    { type: 'size_t', name: 'count', description: "The maximum number of bytes to read from the file." }
  ]}
 />

<InfoBox>In the functions mentioned above, the file pointer acts as a marker indicating where to continue reading the file, so subsequent calls to file.print() will continue from where you left off.</InfoBox>

<InfoBox>Using this method, it's possible to write to a .csv file, making it easy to store a table or log of events!</InfoBox>

<QuickLink 
  title="Inkplate4TEMPERA_SD_TXT_Read.ino" 
  description="This example shows you how to open .txt files and display the content of that file on the Inkplate e-Paper display."
  url="https://github.com/SolderedElectronics/Inkplate-Arduino-library/tree/master/examples/Inkplate4TEMPERA/Advanced/SD/Inkplate4TEMPERA_SD_TXT_Read" 
/>

<QuickLink 
  title="Inkplate4TEMPERA_SD_TXT_Write.ino" 
  description="This example shows you how to write to a .txt file."
  url="https://github.com/SolderedElectronics/Inkplate-Arduino-library/blob/master/examples/Inkplate4TEMPERA/Advanced/SD/Inkplate4TEMPERA_SD_TXT_Write/Inkplate4TEMPERA_SD_TXT_Write.ino" 
/>