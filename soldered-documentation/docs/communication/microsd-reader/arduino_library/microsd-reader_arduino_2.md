---
slug: /microsd-reader/arduino/initializing-the-SD-Card
title: Initializing the SD Card (example)
id: microsd-reader-arduino-2 
hide_title: False
---

This page contains an example of initializing the SD card.

---

## Connecting to the board

<CenteredImage src="/img/microsd-reader/connections.png" alt="Connections" />

---

## Defining the CS pin

At the beginning of the example file, we define the pin to which the Chip Select (CS) is connected by changing the `SD_CS_PIN variable`. In this tutorial, we picked `GPIO5`:

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

## Setup() function

In the setup function, we initialize a Serial connection to the PC; once it is established, we print out the current library version.

```cpp
//...
void setup()
{
  //Initialize serial communication
  Serial.begin(115200);
  // Wait for USB Serial
  while (!Serial)
  {
    SysCall::yield();
  }
}
//...
```

---

## Loop() function

In the loop function, we wait for user input and then attempt to initialize an SPI connection with the card reader. If it fails, a message is printed via the Serial monitor along with some troubleshooting ideas:

```cpp
void loop()
{
  // Read any existing Serial data.
    clearSerialInput();
  // F stores strings in flash to save RAM
  cout << F("\ntype any character to start\n");
  while (!Serial.available())
  {
    SysCall::yield();
  }
  uint32_t t = millis();
  if (!sd.cardBegin(SD_CONFIG))
  {
    cout << F(
        "\nSD initialization failed.\n"
        "Do not reformat the card!\n"
        "Is the card correctly inserted?\n"
        "Is there a wiring/soldering problem?\n");
    if (isSpi(SD_CONFIG))
    {
      cout << F(
          "Is SD_CS_PIN set to the correct value?\n"
          "Does another SPI device need to be disabled?\n");
    }
    return;
  }

  
  cout << F("SD Card successfully initialized!") << endl;
  
  return;


}
```

<CenteredImage src="/img/microsd-reader/error_output.png" alt="Initialization error output on serial monitor" caption="Initialization error output on serial monitor" width="100%" />

<CenteredImage src="/img/microsd-reader/success_output.png" alt="Initialization success output on serial monitor" caption="Initialization success output on serial monitor" width="100%" />

<FunctionDocumentation
  functionName="sd.cardBegin(SdSpiConfig spiConfig)"
  description="Initializes the SD card in SPI mode"
  returnDescription="Boolean value, true for success and false for failure"
  parameters={[{ type: 'SdSpiConfig (object)', name: 'spiConfig', description: "An object of the current SPI configuration, including the CS pin" },]}
/>

---

## Full example
Below you can find the full example:

```cpp
/*
 * This program attempts to initialize an SD card
 */
#include "SdFat.h"
#include "sdios.h"
/*
  Set DISABLE_CS_PIN to disable a second SPI device.
  For example, with the Ethernet shield, set DISABLE_CS_PIN
  to 10 to disable the Ethernet controller.
*/
const int8_t DISABLE_CS_PIN = -1;
/*
  Change the value of SD_CS_PIN if you are using SPI
  and your hardware does not use the default value, SS.
  Common values are:
  Arduino Ethernet shield: pin 4
  Sparkfun SD shield: pin 8
  Adafruit SD shields and modules: pin 10
*/
// SDCARD_SS_PIN is defined for the built-in SD on some boards.
#ifndef SDCARD_SS_PIN
const uint8_t SD_CS_PIN = SS;
#else  // SDCARD_SS_PIN
const uint8_t SD_CS_PIN = 5;
#endif // SDCARD_SS_PIN

// Try to select the best SD card configuration.
#if HAS_SDIO_CLASS
#define SD_CONFIG SdioConfig(FIFO_SDIO)
#elif ENABLE_DEDICATED_SPI
#define SD_CONFIG SdSpiConfig(SD_CS_PIN, DEDICATED_SPI, SD_SCK_MHZ(16))
#else // HAS_SDIO_CLASS
#define SD_CONFIG SdSpiConfig(SD_CS_PIN, SHARED_SPI, SD_SCK_MHZ(16))
#endif // HAS_SDIO_CLASS

//------------------------------------------------------------------------------

//Create an instance of the SD card
SdFs sd;
static ArduinoOutStream cout(Serial);


//------------------------------------------------------------------------------

void clearSerialInput()
{
  uint32_t m = micros();
  do
  {
    if (Serial.read() >= 0)
    {
      m = micros();
    }
  } while (micros() - m < 10000);
}



void setup()
{
  
  
}
//------------------------------------------------------------------------------
void loop()
{
  // Read any existing Serial data.
    clearSerialInput();
  // F stores strings in flash to save RAM
  cout << F("\ntype any character to start\n");
  while (!Serial.available())
  {
    SysCall::yield();
  }
  uint32_t t = millis();
  if (!sd.cardBegin(SD_CONFIG))
  {
    cout << F(
        "\nSD initialization failed.\n"
        "Do not reformat the card!\n"
        "Is the card correctly inserted?\n"
        "Is there a wiring/soldering problem?\n");
    if (isSpi(SD_CONFIG))
    {
      cout << F(
          "Is SD_CS_PIN set to the correct value?\n"
          "Does another SPI device need to be disabled?\n");
    }
    return;
  }

  
  cout << F("SD Card successfully initialized!") << endl;
  
  return;


}
```