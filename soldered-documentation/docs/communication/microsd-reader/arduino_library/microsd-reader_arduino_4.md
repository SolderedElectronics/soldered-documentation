---
slug: /microsd-reader/arduino/writing-files
title: Writing files (example)
id: microsd-reader-arduino-4 
hide_title: False
---

This page contains an example of writing data to an SD card in the form of a text file

---

## Defining the CS pin and instances
To write data to the SD card, we must first define the CS pin used for SPI communication (GPIO 5 in our case):

```cpp
//...
// SDCARD_SS_PIN is defined for the built-in SD on some boards.
#ifndef SDCARD_SS_PIN
const uint8_t SD_CS_PIN = SS;
#else  // SDCARD_SS_PIN
const uint8_t SD_CS_PIN = 5; //SET THIS PIN
#endif // SDCARD_SS_PIN
//...
```

We also have to create instances of objects for the SD card and the file we will create:

```cpp
//Create an instance of the SD card
SdFs sd;

//Create an instance of the file system file object
FsFile file;
```

---

## Writing to the file
Since we want to create the file only once, the entire program is located in the `setup()` function. First, we initialize the Serial communication; next, we initialize the SD card and its volume so that we can write and read data from it. Finally, we write data to the SD card using the FsFile object:

```cpp
void setup()
{
  //Initialize the serial communication
  Serial.begin(115200);

  // Wait for USB Serial
  while (!Serial)
  {
    yield();
  }
  Serial.println("Type any character to start");
  while (!Serial.available())
  {
    yield();
  }
  // Initialize the SD.
  if (!sd.cardBegin(SD_CONFIG))
  {
    sd.initErrorHalt(&Serial);
    return;
  }
  if(!sd.volumeBegin())
  {
    Serial.println("Failed to initialize volume!");
    return;
  }

  // Create the file.
  if (!file.open("hello.txt", FILE_WRITE))
  {
    Serial.println("Failed to open file!");
    return;
  }
  // Write test data.
  file.print(F("Hello from Soldered!"));
  // Close the file we were writing to.
  file.close();

  Serial.println("Writing to file done!");
}
```
If the file creation and writing are successful, when connected to a computer, we can see and open the created file:

<CenteredImage src="/img/microsd-reader/file_created.png" alt="Successful file writing" caption="Successful file writing" width="100%" />

<FunctionDocumentation
  functionName="sd.volumeBegin()"
  description="Initialize the file system after a call to cardBegin"
  returnDescription="Boolean value, true for success and false for failure"
  parameters={[]}
/>

<FunctionDocumentation
  functionName="file.open(const char *path. oflag_t oflag)"
  description="Open a file by path"
  returnDescription="Boolean value, true for success and false for failure"
  parameters={[{ type: 'const char*', name: 'path', description: "Path and filename from working directory to specified file" },
  { type: 'oflag_t (enumerator)', name: 'oflag', description: "A flag that specifies what we intend to do with the file (read it, write to it etc.)" }
  ]}
/>

<FunctionDocumentation
  functionName="file.close()"
  description="Close a file and force cached data and directory information to be written to the storage device."
  returnDescription="None"
  parameters={[]}
/>

---

## Full example
Below you can find the full example:

```cpp
#include "SdFat.h"

//Set to one if there are more SPI devices connected to the bus
const int8_t DISABLE_CS_PIN = -1;

// SDCARD_SS_PIN is defined for the built-in SD on some boards.
#ifndef SDCARD_SS_PIN
const uint8_t SD_CS_PIN = 5;
#else  // SDCARD_SS_PIN
const uint8_t SD_CS_PIN = SDCARD_SS_PIN;
#endif // SDCARD_SS_PIN

// Try to select the best SD card configuration.
#if HAS_SDIO_CLASS
#define SD_CONFIG SdioConfig(FIFO_SDIO)
#elif ENABLE_DEDICATED_SPI
#define SD_CONFIG SdSpiConfig(SD_CS_PIN, DEDICATED_SPI, SD_SCK_MHZ(16))
#else // HAS_SDIO_CLASS
#define SD_CONFIG SdSpiConfig(SD_CS_PIN, SHARED_SPI, SD_SCK_MHZ(16))
#endif // HAS_SDIO_CLASS

//Create an instance of the SD card
SdFs sd;

//Create an instance of the file system file object
FsFile file;
//------------------------------------------------------------------------------
void setup()
{
  //Initialize the serial communication
  Serial.begin(115200);

  // Wait for USB Serial
  while (!Serial)
  {
    yield();
  }
  Serial.println("Type any character to start");
  while (!Serial.available())
  {
    yield();
  }
  // Initialize the SD.
  if (!sd.cardBegin(SD_CONFIG))
  {
    sd.initErrorHalt(&Serial);
    return;
  }
  if(!sd.volumeBegin())
  {
    Serial.println("Failed to initialize volume!");
    return;
  }

  // Create the file.
  if (!file.open("hello.txt", FILE_WRITE))
  {
    Serial.println("Failed to open file!");
    return;
  }
  // Write test data.
  file.print(F("Hello from Soldered!"));
  // Close the file we were writing to.
  file.close();

  Serial.println("Writing to file done!");
}

void loop()
{
}
```