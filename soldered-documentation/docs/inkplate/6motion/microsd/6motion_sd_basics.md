---
slug: /inkplate/6motion/microsd/sd-basics
title: "Inkplate \u2013 6Motion MicroSD SD Basics"
id: 6motion-microsd-basics
hide_title: true
---
<SectionTitle title="MicroSD basics" backgroundImage="/img/microsd.jpg" />

The built-in microSD card slot on Inkplate 6 MOTION can be of great use for your project. It can store a very large number of quality image files to be displayed and read and write data between deep sleeps. This page contains basic examples which will help you quickly get started with using the built-in microSDs card slot.

<CenteredImage src="/img/inkplate_6_motion/6motion_sdcard.jpg" alt="MicroSD card in Inkplate 6 MOTION" caption="8GB microSD card inserted in Inkplate 6 MOTION" width="600px" />

<InfoBox>Inkplate 6 MOTION uses the [**SdFat library**](https://github.com/greiman/SdFat)</InfoBox>
<WarningBox>All supported card formats are: **FAT16, FAT32, exFAT**</WarningBox>
<WarningBox>All supported card types are: **SD, SDHC and SDXC**</WarningBox>

---

## Preparing the microSD card before usage

For best results, use the [**official SD card formatter**](https://www.sdcard.org/downloads/formatter/) to format the card to **FAT32** before usage.

<CenteredImage src="/img/inkplate_6_motion/sdcard_formatter.png" alt="Official SD card formatter" caption="The official SD Card formatter" width="400px" />

---

## Initializing

Before the microSD card can be used in code, it must first be initialized, this powers on the microSD card circuitry and does all the nescessary memory allocations. In this code snippet, the microSD card is initialized and the result of the initialization is checked:
```cpp
// Inkplate must be initialized before this

// Let's init the microSD card
if (!inkplate.microSDCardInit())
{
    // Print error message if the card could not be initialized
    inkplate.print("Couldn't init microSD card!");
    inkplate.partialUpdate();
    // Go to infinite loop - stop code
    while (1)
        ;
}
inkplate.print("MicroSD init success!");
inkplate.partialUpdate();
```
<FunctionDocumentation
  functionName="inkplate.microSDCardInit()"
  description="Initializes the microSD card on the Inkplate 6MOTION. Powers up the card, configures the necessary pins, and attempts to initialize the card interface."
  returnDescription="Returns true if the initialization was successful, otherwise returns false."
/>

---

## Reading and writing

Place a sample `example.txt` file on the microSD card and write something in it, this code snippet will read it and print it to the e-Paper:
```cpp
// Make sure the microSD card is initialized by this point

File file; // Create a SdFile object
// This will only open the file in read only mode:
file = inkplate.sdFat.open("example.txt", O_RDONLY);
if (!file)
{
    // Print error message if the file couldn't be opened back
    inkplate.print("Couldn't open the created file!");
    inkplate.partialUpdate();
    // Go to infinite loop
    while (1)
        ;
}
// File is opened
// Read file contents to buffer
char buffer[128];
int bytesRead = file.read(buffer, sizeof(buffer) - 1);

file.close(); // Close the file, important!

// Bytes have been read
if (bytesRead > 0)
{
    buffer[bytesRead] = '\0'; // Null-terminate the c-style string
    // Let's print it to Inkplate!
    inkplate.println("\nFile contents:\n");
    inkplate.println(buffer);
}
else
{
    // Print error message if the file couldn't be opened
    inkplate.print("Couldn't read the test string!");
}
// Update the display with the result of the sketch
inkplate.partialUpdate();
```

Writing to a `writeFile.txt` file on the microSD card is similar:
```cpp
char * testString = "Hi Inkplate!"; 
// Let's create the .txt file and write to it
// This will create the file if it doesn't exist, and open it in read-write mode if it exists:
File file = inkplate.sdFat.open("writeFile.txt", O_CREAT | O_RDWR);
if (!file)
{
    // Print error message if the file couldn't be created
    inkplate.print("Couldn't create the file on SD card!");
    inkplate.partialUpdate();
    // Go to infinite loop
    while (1)
        ;
}
// Write to the file and close it
file.print(testString);
file.close();
```
Before diving into the function details, here is the full example which provides a great overview:
<QuickLink 
  title="SD Text read and write example" 
  description="A full example on how to initialize the microSD card, read and write data to it"
  url="https://github.com/SolderedElectronics/Inkplate_Motion_Arduino_Library/blob/main/examples/Inkplate6Motion/Advanced/SD/Inkplate_6_Motion_SD_Read_Write_Text/Inkplate_6_Motion_SD_Read_Write_Text.ino" 
/>
<FunctionDocumentation
  functionName="inkplate.sdFat.open()"
  description="Open a file from the SD card, this is a function from the SdFat library."
  returnDescription="Returns the SdFile object if it was successful, false if it failed"
  parameters={[
    { type: 'const char *', name: 'path', description: "The path to the file which is being opened, if it's in the root folder just write the filename." },
    { type: 'oflag_t', name: 'oflag', description: "The settings for opening the file. The different flags have to be OR'd, eg. O_CREAT | O_RDWR. Below is a table of these flags and what they mean." }
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
  functionName="file.print()"
  description="Prints the given c-style string to the file at the current file pointer position."
  returnDescription="Returns the number of characters successfully printed, or a negative value if an error occurs."
  parameters={[
    { type: 'const char *', name: 'str', description: "The c-style string to print to the file." }
  ]}
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

<InfoBox>In the above mentioned functions, the file pointer is like a marker where you continue reading the file from, so subsequent calls to `file.print()` and `file.print()` will continue from where you left off.</InfoBox>

<FunctionDocumentation
  functionName="file.close()"
  description="Closes the file, ensuring that any buffered data is flushed to the storage medium and that all resources associated with the file are freed."
  returnDescription="Returns true if the file was closed successfully, or false if an error occurred."
/>

<InfoBox>Using this method, it's possible to write to a .csv file, making it easy to store a table or log of events!</InfoBox>

---

## Full example

<QuickLink 
  title="Inkplate_6_Motion_SD_Read_Write_Text.ino" 
  description="Full example of reading and writing text to the microSD card."
  url="https://github.com/SolderedElectronics/Inkplate_Motion_Arduino_Library/blob/main/examples/Inkplate6Motion/Advanced/SD/Inkplate_6_Motion_SD_Read_Write_Text/Inkplate_6_Motion_SD_Read_Write_Text.ino" 
/>
