---
slug: /microsd-reader/arduino/troubleshooting
title: "MicroSD Card Reader \u2013 Arduino troubleshooting"
id: microsd-reader-arduino-3
hide_title: false
pagination_next: null
---
This page contains some tips in case you are having problems using this product.

<ExpandableSection title="The SPI communication won't initialize!">

#### Check wiring
Make sure the SD card module is correctly wired to the ESP32 by following the wiring described [**here**](/microsd-reader/arduino/geting-started#connections/)

#### Set the CS pin value
When setting up the SPI communication in the code, ensure that you set the **SD_CS_PIN** variable to the pin to which CS is connected. If you're following our connections, the pin is **GPIO5**.

#### Connect the pins to VSPI
If not defined manually, the SPI.h library attempts to initialize on the VSPI (Very High-Speed SPI) pins. See the pinout for the Dasduino CONNECTPLUS [**here**](https://soldered.com/productdata/2022/06/Dasduino-CONNECTPLUS.png)

#### Try running our examples
If you are sure that the wiring is correct and that the module is connected via the **VSPI pins**, try our [**Initialization example**](/microsd-reader/arduino/initializing-the-SD-Card/)

</ExpandableSection>

<ExpandableSection title="I can't access the SD card!">

If the SPI connection has initialized successfully, but the SD card can't be accessed, here are some ways to fix it:

#### Format the card
The library only supports SD cards that are formatted as **FAT16/FAT32/exFAT**. For the card to be recognized, please format it into one of the aforementioned formats.

#### Connect VCC with 3.3V
While the breakout board supports a 5V supply, its onboard 3.3V regulator is disconnected by default with the shorted jumper **JP1**. To combat this, either connect 3.3V to the VCC pin or desolder the short on JP1 if your SD card expects 5V.

#### Make sure the card is less than 32GB
The reader only supports microSD cards up to 32GB, so larger cards won't be recognized.

#### Try a different card
If you've tried the previous tips, the problem may be with the SD card itself. Try a different one and see if the problem persists.

</ExpandableSection>

<ExpandableSection title="Reading/Writing data is so slow!">

#### Run in dedicated SPI mode
If the module is the only SPI device connected to the bus, use dedicated SPI mode by setting the **DISABLE_CS_PIN** variable to -1. This can improve transfer speeds by up to 10x in some cases.

</ExpandableSection>