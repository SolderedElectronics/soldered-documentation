---
slug: /microsd-reader/arduino/reading-files
title: Microsd Reader - Reading files (example)
id: microsd-reader-arduino-5
hide_title: false
---

On this page, we will read data from the file we created in the previous example.

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

We also have to create instances of objects for the SD card and the file we will create, as well as a buffer for the string we are reading:

```cpp
//Create an instance of the SD card
SdFs sd;

//Create an instance of the file system file object
FsFile file;

//Create a char buffer for the text we will read
char line[40];
```

---

## Reading from a file
Since we want to read the file only once, the entire program is placed in the `setup()` function.
First, we initialize the Serial communication, then we initialize the SD card and its volume so that we can write and read data from it. Finally, we read data from the SD card using the FsFile object:

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
  if (!file.open("hello.txt", FILE_READ))
  {
    Serial.println("Failed to open file!");
    return;
  }
  // Read data from file line by line
  while(file.available())
  {
    int n = file.fgets(line, sizeof(line));
    //Check if there was an error getting the line from text
    if (n <= 0)
    {
      Serial.println("fgets failed");
    }
    //Check if the line was longer than the buffer
    if (line[n - 1] != '\n' && n == (sizeof(line) - 1))
    {
      Serial.println("line too long");
    }
    Serial.println(line);
  }
  // Close the file we were reading from.
  file.close();

  Serial.println("Reading from file done!");
}
```

If everything works as it should, you should get an output like this:

<CenteredImage src="/img/microsd-reader/file_read.png" alt="Successful file read" caption="Successful file read" width="100%" />

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

//Create a char buffer for the text we will read
char line[40];
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
  if (!file.open("hello.txt", FILE_READ))
  {
    Serial.println("Failed to open file!");
    return;
  }
  while(file.available())
  {
    int n = file.fgets(line, sizeof(line));
    //Check if there was an error getting the line from text
    if (n <= 0)
    {
      Serial.println("fgets failed");
    }
    //Check if the line was longer than the buffer
    if (line[n - 1] != '\n' && n == (sizeof(line) - 1))
    {
      Serial.println("line too long");
    }
    Serial.println(line);
  }
  // Close the file we were reading from.
  file.close();

  Serial.println("Reading from file done!");
}

void loop()
{
}
```