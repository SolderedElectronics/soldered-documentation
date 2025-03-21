---
slug: /microsd-reader/arduino/reading-info-data-from-sd-card
title: Reading info data from SD Card (example)
id: microsd-reader-arduino-2 
hide_title: False
---

This page contains a deep dive into the [**SdInfo library example**](https://github.com/SolderedElectronics/Soldered-SdFat-Arduino-Library/blob/master/examples/SdInfo/SdInfo.ino) and how to get it working

---

## Defining the CS pin

At the start of the example file, we have to define on what pin Chip Select (CS) is connected by changing the `SD_CS_PIN variable`, in this tutorial we picked `GPIO5`:

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

In the setup function, we are initializing a Serial connection with the PC and when it is established, we print out the current library version and we print out the SPI configuration (If the SD card reader is the only SPI device connected or not):

```cpp
//...
void setup()
{
  //Initialize a serial connection
  Serial.begin(115200);
  // Wait for USB Serial
  while (!Serial)
  {
    SysCall::yield();
  }
  //Prints out the version of the library
  cout << F("SdFat version: ") << SD_FAT_VERSION_STR << endl;

  //Prints out the SD SPI configuration (local function) 
  printConfig(SD_CONFIG);
}
//...
```
<CenteredImage src="/img/microsd-reader/setup.png" alt="Setup() function output on serial monitor" caption="Setup() function output on serial monitor" width="100%" />

## Loop() function

In the loop function, we wait for user input, then we try to initialize an SPI connection with the card reader, if it failed we get informed via the Serial monitor and are given some troubleshooting ideas:

```cpp
//Inside loop() function

  // Read any existing Serial data.
  clearSerialInput();

  // F stores strings in flash to save RAM
  cout << F("\ntype any character to start\n");

  //Wait for user input
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
    errorPrint();
    return;
  }
//Inside loop() function
```

<CenteredImage src="/img/microsd-reader/error_output.png" alt="Initialization error output on serial monitor" caption="Initialization error output on serial monitor" width="100%" />

<FunctionDocumentation
  functionName="sd.cardBegin(SdSpiConfig spiConfig)"
  description="Initializes the SD card in SPI mode"
  returnDescription="Boolean value, true for success and false for failure"
  parameters={[{ type: 'SdSpiConfig (object)', name: 'spiConfig', description: "An object of the current SPI configuration, including the CS pin" },]}
/>

Next, we read the CSD, OCR and CID data from the SD card and print the values to the Serial monitor:

```cpp
//Inside loop() function
//Get time it took to initialize SPI connection
  t = millis() - t;
  cout << F("init time: ") << t << " ms" << endl;
//Try reading SD card info
  if (!sd.card()->readCID(&m_cid) ||
      !sd.card()->readCSD(&m_csd) ||
      !sd.card()->readOCR(&m_ocr))
  {
    cout << F("readInfo failed\n");
    errorPrint();
    return;
  }
  //Print the Manufacturer and general information about the card
  printCardType();
  //Get register data
  cidDmp();
  csdDmp();
  cout << F("\nOCR: ") << uppercase << showbase;
  cout << hex << m_ocr << dec << endl;


  if (!mbrDmp())
  {
    return;
  }
  //Try getting volume data from SD 
  if (!sd.volumeBegin())
  {
    cout << F("\nvolumeBegin failed. Is the card formatted?\n");
    errorPrint();
    return;
  }
  dmpVol();
//Inside loop() function
```
<FunctionDocumentation
  functionName="sd.cardBegin(SdSpiConfig spiConfig)"
  description="Initializes the SD card in SPI mode"
  returnDescription="Boolean value, true for success and false for failure"
  parameters={[{ type: 'SdSpiConfig (object)', name: 'spiConfig', description: "An object of the current SPI configuration, including the CS pin" },]}
/>





