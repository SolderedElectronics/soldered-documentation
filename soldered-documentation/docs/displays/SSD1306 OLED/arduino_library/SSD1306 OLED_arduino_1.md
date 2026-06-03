---
slug: /ssd1306-new/arduino/getting-started
title: SSD1306 - Getting started
sidebar_label: Getting started
id: ssd1306-new-arduino-1
hide_title: false
---

This page provides the essential information for getting started, including board and library installation and wiring the breakout board to your microcontroller.

---

## Acknowledgement

<InfoBox> The Soldered OLED Display Arduino library is based on the [**Adafruit_SSD1306** library](https://github.com/adafruit/Adafruit_SSD1306/tree/master) by [Adafruit](https://www.adafruit.com/). As such, its source code is licensed under the **MIT License**. For more details, see the [**MIT License**](https://opensource.org/license/mit).</InfoBox>

<CenteredImage src="/img/license/MIT.png" alt="MIT license" width="250px" />

---

## Arduino library

To install the Arduino library, you can download it from the GitHub repository:
<QuickLink  
  title="OLED Display Arduino library"  
  description="OLED Display Arduino library by Soldered"  
  url="https://github.com/SolderedElectronics/Soldered-OLED-Display-Arduino-Library/tree/main"  
/>  

<InfoBox>

**First time Arduino user?** For a detailed tutorial on how to get started with Arduino, see this section of our docs:

<QuickLink  
  title="Getting started with Arduino"  
  description="A full, comprehensive tutorial on how to fully set up and upload code for the first time on an Arduino board, from scratch!"  
  url="/arduino/quick-start-guide"  
/>  

</InfoBox>

---

## Connections

Below is an example connection diagram for **NULA DeepSleep ESP32 S3**. These pins will be used in the examples throughout this documentation.

| **NULA DeepSleep ESP32 S3** | **Breakout Board** |
| --------------------------- | ------------------ |
| Qwiic (formerly easyC)      | Qwiic (formerly easyC) |
