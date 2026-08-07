---  
slug: /inkplate/6/microsd/sd-basics  
title: Inkplate 6 – MicroSD basics
sidebar_label: MicroSD basics
id: microsd-basics  
hide_title: true  
---

<SectionTitle title="MicroSD basics" />

The built-in microSD card slot on Inkplate 6 can be extremely useful for your project. It can store a large number of high-quality image files for display and also allows reading and writing data between deep sleep cycles. This page contains basic examples to help you quickly get started with using the built-in microSD card slot.

<CenteredImage src="/img/inkplate10/10_sdcard.jpg" alt="MicroSD card slot" caption="MicroSD card slot" width="600px" />

<InfoBox>Inkplate 6 uses the [**SdFat library**](https://github.com/greiman/SdFat)</InfoBox>
<WarningBox>All supported card formats are: **FAT16, FAT32, exFAT**</WarningBox>
<WarningBox>All supported card types are: **SD, SDHC, and SDXC**</WarningBox>

---

## Preparing the microSD card before use

For best results, use the [**official SD card formatter**](https://www.sdcard.org/downloads/formatter/) to format the card to **FAT32** before use.

<CenteredImage src="/img/inkplate10/sdcard_formatter.png" alt="Official SD card formatter" caption="The official SD Card formatter" width="400px" />

---

## Initializing

Before the microSD card can be used in code, it must first be initialized. This process powers on the microSD card circuitry and allocates the necessary memory. In this code snippet, the microSD card is initialized, and the result of the initialization is checked:
```cpp
#include "Inkplate.h"            // Include Inkplate library in the sketch
Inkplate display(INKPLATE_1BIT); // Create an Inkplate object and set the library to 1 Bit mode (BW)
SdFile file;                     // Create an SdFile object used for accessing files on the SD card

void setup()
{
    display.begin();        // Initialize the Inkplate library (you should call this function ONLY ONCE)
    display.clearDisplay(); // Clear the display's frame buffer
    display.display();      // Display the cleared image on the screen
    display.setTextSize(3);

    // Initialize SD card. Display whether the SD card was initialized properly or not.
    if (display.sdCardInit())
    {
        display.println("SD Card ok! Reading data...");
        display.partialUpdate();
    }
    else
    { // If card initialization was not successful, display an error on screen, put the SD card in sleep mode, and stop the program (using an infinite loop)
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
    functionName="display.sdCardInit()"
    description="Initializes the microSD card over SPI. This also powers on the microSD card circuitry."
    returnType="int16_t"
    returnDescription="Non-zero if the initialization was successful, 0 if it failed."
/>

---

## Reading and writing
Place a sample `text.txt` file on the microSD card with some content. This code snippet will read it and print it to the e-Paper display:
```cpp
#include "Inkplate.h"            //Include Inkplate library to the sketch
Inkplate display(INKPLATE_1BIT); // Create an object on Inkplate library and also set library into 1 Bit mode (BW)
SdFile file;                     // Create SdFile object used for accessing files on SD card

void setup()
{
    display.begin();        // Init Inkplate library (you should call this function ONLY ONCE)
    display.clearDisplay(); // Clear frame buffer of display
    display.display();      // Put clear image on display

    // Init SD card. Display if SD card is init propery or not.
    if (display.sdCardInit())
    {
        display.println("SD Card ok! Reading data...");
        display.partialUpdate();

        // Try to load text with max length of 200 chars.
        if (!file.open("/text.txt", O_RDONLY))
        { // If it fails to open, send error message to display and put sd card in sleep mode, otherwise read the file.
            display.println("File open error");            
            display.display();
            display.sdCardSleep();
        }
        else
        {
            display.clearDisplay();    // Clear everything that is stored in frame buffer of epaper
            display.setCursor(0, 0);   // Set print position at the begining of the screen
            char text[201];            // Array where data from SD card is stored (max 200 chars here)
            int len = file.fileSize(); // Read how big is file that we are opening
            if (len > 200)
                len = 200;         // If it's more than 200 bytes (200 chars), limit to max 200 bytes
            file.read(text, len);  // Read data from file and save it in text array
            text[len] = 0;         // Put null terminating char at the and of data
            display.print(text);   // Print data/text
            display.sdCardSleep(); // Put sd card in sleep mode
            display.display();     // Do a full refresh of display
        }
    }
    else
    { // If card init was not successful, display error on screen and stop the program (using infinite loop)
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
    returnDescription="Returns true if the file was opened successfully; otherwise, returns false."
    parameters={[ 
        { type: 'const char *', name: 'path', description: "The path to the file to be opened. If it's in the root folder, just write the filename." },
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
| O_CREAT  | 0x10      | Create the file if it does not exist.      |
| O_TRUNC  | 0x20      | Truncate the file to zero length.          |
| O_EXCL   | 0x40      | Fail if the file already exists.           |
| O_SYNC   | 0x80      | Synchronized write I/O operations.         |

<FunctionDocumentation
    functionName="file.fileSize()"
    description="Returns the total number of bytes in a file."
    returnType="uint32_t"
/>

<FunctionDocumentation
  functionName="file.read()"
  description="Reads data from the file into the provided buffer. The function attempts to read up to a specified number of bytes starting from the current file pointer."
  returnDescription="Returns the number of bytes read, or -1 if an error occurs."
  parameters={[ 
    { type: 'void *', name: 'buf', description: "A pointer to the buffer where the read file data will be stored." },
    { type: 'size_t', name: 'count', description: "The maximum number of bytes to read from the file." }
  ]}
/>

<InfoBox>In the above-mentioned functions, the file pointer acts as a marker indicating where reading resumes. Subsequent calls to `file.print()` will continue from where you left off.</InfoBox>

<InfoBox>Using this method, it's possible to write to a .csv file, making it easy to store a table or log of events!</InfoBox>

<QuickLink 
  title="Inkplate6_microSD_TXT_Read.ino" 
  description="This example shows you how to open .txt files and display their content on the Inkplate e-Paper display."
  url="https://github.com/SolderedElectronics/Inkplate-Arduino-library/tree/master/examples/Inkplate6/Advanced/microSD/Inkplate6_microSD_TXT_Read" 
/>

<QuickLink 
  title="Inkplate6_microSD_TXT_Write.ino" 
  description="This example shows you how to write to a .txt file."
  url="https://github.com/SolderedElectronics/Inkplate-Arduino-library/blob/master/examples/Inkplate6/Advanced/microSD/Inkplate6_microSD_TXT_Write/Inkplate6_microSD_TXT_Write.ino" 
/>