---
slug: /inkplate/13spectra/microsd/sd-basics
title: Inkplate 13SPECTRA – MicroSD basics
sidebar_label: MicroSD basics
id: 13spectra-microsd-basics
hide_title: true
---

<SectionTitle title="MicroSD basics" backgroundImage="/img/microsd.jpg" />

The built-in microSD card slot on Inkplate 13SPECTRA can be a great asset for your project. It can store a very large number of high-quality image files to be displayed, and it can also read and write data between deep sleep cycles. This page contains basic examples that will help you quickly get started with using the built-in microSD card slot.

[IMAGE PLACEHOLDER - microsd card slot highlighted on spectra]

<InfoBox>Inkplate 13SPECTRA uses the [**SdFat library**](https://github.com/greiman/SdFat)</InfoBox>
<WarningBox>All supported card formats are: **FAT16, FAT32, exFAT**</WarningBox>
<WarningBox>All supported card types are: **SD, SDHC and SDXC**</WarningBox>

---

## Preparing the microSD card before usage

For best results, use the [**official SD card formatter**](https://www.sdcard.org/downloads/formatter/) to format the card to **FAT32** before usage.

<CenteredImage src="/img/inkplate10/sdcard_formatter.png" alt="Official SD card formatter" caption="The official SD Card formatter" width="400px" />

---

## Initializing
Before the microSD card can be used in code, it must first be initialized. This powers on the microSD card circuitry and performs all the necessary memory allocations. In this code snippet, the microSD card is initialized and the result of the initialization is checked:

```cpp
#include "Inkplate.h" // Include the Inkplate library in the sketch
Inkplate display;     // Create an object of the Inkplate library
SdFile file;          // Create SdFile object used for accessing files on the SD card

void setup()
{
    Serial.begin(115200); // Initialize serial communication
    display.begin();      // Initialize the Inkplate library (you should call this function ONLY ONCE)

    // Initialize SD card. Display if the SD card is initialized properly or not.
    if (display.sdCardInit())
    {
        Serial.println("SD Card ok!");
    }
    else
    { // If card initialization was not successful, display an error on the screen, put the SD card in sleep mode, and stop the program
      // (using an infinite loop)
        Serial.println("SD Card error!");
        display.sdCardSleep();
        while (true)
            ;
    }
}
void loop(){
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
Place a sample `text.txt` file on the microSD card and write something in it. This code snippet will read the file and print its contents to the e-Paper display:
```cpp
#include "Inkplate.h" //Include Inkplate library to the sketch
Inkplate display;     // Create an object on Inkplate library
SdFile file;          // Create SdFile object used for accessing files on SD card

void setup()
{
    display.begin();        // Init Inkplate library (you should call this function ONLY ONCE)
    display.clearDisplay(); // Clear frame buffer of display
    display.display();      // Put clear image on display
    display.setCursor(0, 0);
    display.setTextColor(INKPLATE_BLACK);
    display.setTextSize(2);
    // Init SD card. Display if SD card is init propery or not.
    if (display.sdCardInit())
    {
        display.println("SD Card ok! Reading data...");
        display.display();

        // Try to load text with max lenght of 200 chars.
        if (!file.open("/text.txt", O_RDONLY))
        { // If it fails to open, send error message to display, otherwise read the file.
            display.println("File open error");
            display.display();
        }
        else
        {
            display.clearDisplay();    // Clear everything that is stored in frame buffer of epaper
            display.setCursor(0, 0);   // Set print position at the begining of the screen
            char text[3001];           // Array where data from SD card is stored (max 200 chars here)
            int len = file.fileSize(); // Read how big is file that we are opening
            if (len > 3000)
                len = 3000;        // If it's more than 200 bytes (200 chars), limit to max 200 bytes
            file.read(text, len);  // Read data from file and save it in text array
            text[len] = 0;         // Put null terminating char at the and of data
            display.print(text);   // Print data/text
            display.sdCardSleep(); // Put sd card in sleep mode
            display.display();     // Do a full refresh of display
        }
    }
    else
    { // If card init was not successful, display error on screen, put sd card in sleep mode, and stop the program
      // (using infinite loop)
        display.println("SD Card error!");
        display.display();
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

[IMAGE PLACEHOLDER - 13spectra example output]

<FunctionDocumentation
    functionName="file.open()"
    description="Opens a file in the current working directory."
    returnDescription="Returns true if opening is successful, otherwise returns false."
    parameters={[ 
      { type: 'const char *', name: 'path', description: "The path to the file which is being opened; if it's in the root folder, just write the filename." },
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
  description="Reads data from the file into the provided buffer. The function attempts to read up to a given number of bytes starting from the current file pointer."
  returnDescription="Returns the number of bytes read, or -1 if an error occurs."
  parameters={[ 
    { type: 'void *', name: 'buf', description: "A pointer to the buffer where the read file data will be stored." },
    { type: 'size_t', name: 'count', description: "The maximum number of bytes to read from the file." }
  ]}
 />
 <InfoBox>In the above-mentioned functions, the file pointer acts as a marker where you continue reading the file from, so subsequent calls to `file.print()` will continue from where you left off.</InfoBox>

<InfoBox>Using this method, it's possible to write to a .csv file, making it easy to store a table or log of events!</InfoBox>

[LINK PLACEHOLDER - 13spectra txt read example]

[LINK PLACEHOLDER - 13spectra txt write example]