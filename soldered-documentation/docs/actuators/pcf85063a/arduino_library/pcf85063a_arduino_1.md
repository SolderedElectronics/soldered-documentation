---
slug: /pcf85063a/arduino/geting-started
title: "PCF85063A RTC \u2013 Arduino Getting Started"
id: pcf85063a-arduino-1
hide_title: false
---
This page provides the essential information for getting started, including board and library installation and wiring the breakout board to your microcontroller.

---

## Arduino library

To install the Arduino library, you can download it from the GitHub repository:
<QuickLink  
  title="Real time clock PCF85063A breakout Arduino library"  
  description="PCF85063A RTC Arduino library by Soldered"  
  url="https://github.com/SolderedElectronics/Soldered-PCF85063A-RTC-Module-Arduino-Library"  
/>  


<InfoBox>

**First time Arduino user?** For a detailed tutorial on how to get started with Arduino, see this section of our docs:

<QuickLink  
  title="Getting started with Arduino"  
  description="A full, comprehensive tutorial on how to fully set up and upload code for the first time on an Arduino board, from scratch!"  
  url="/documentation/arduino/quick-start-guide"  
/>  

</InfoBox>

---

## Connections

Below is an example connection diagram for **Dasduino CONNECTPLUS**. These pins will be used in the examples throughout this documentation.

| **Dasduino CONNECTPLUS** | **Breakout Board** |
| ------------------------ | ------------------ |
| Qwiic                    | Qwiic              |
| GPIO4                    | INT                |

<InfoBox>

If you prefer, you can use I2C pins to manually connect:

</InfoBox>