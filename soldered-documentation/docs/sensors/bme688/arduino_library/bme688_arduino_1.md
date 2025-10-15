---
slug: /bme688/arduino/geting-started 
title: Arduino -  Getting started
sidebar_label: Getting started
id: bme688-arduino-1 
hide_title: False
---

## Arduino library

To install the Arduino library, you can use the **Arduino library manager** or download it from the GitHub repository:
<QuickLink
    title="BME688 Sensor Arduino library"
    description="BME688 Arduino library by Soldered"
    url="https://github.com/SolderedElectronics/Soldered-BME688-Sensor-Arduino-Library/tree/main"
/>

<InfoBox>
**First time Arduino user?** For a detailed tutorial on how to get started with Arduino, see this section of our docs:

<QuickLink
    title="Getting started with Arduino"
    description="A full, comprehensive tutorial on how to fully set up and upload code for the first time on an Arduino board, from scratch!"
    url="/documentation/arduino/quick-start-guide"
/>
</InfoBox>

--

## Connections

Below is an example connection diagram for **Dasduino CONNECTPLUS**. These pins will be used in the examples throughout this documentation.

|**Dasduino CONNECTPLUS**|**Breakout Board**|
|---|---|
|Qwiic|Qwiic|

<InfoBox>

If you prefer, you can use I2C pins to malually connect:

| **Dasduino CONNECTPLUS** | **Breakout Board** |
|---|---|
|IO21 (Default SDA pin) | SDA |
|IO22 (Default SCL pin) | SCL |
|VCC | VCC|
|GND | GND|

</InfoBox>