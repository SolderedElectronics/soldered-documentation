---
slug: /slider-potentiometer/arduino-1 
title: Getting Started
id: slider-potentiometer-arduino-1 
hide_title: False
---

## Arduino library

To install the Arduino library, you can use the **Arduino library manager** or download it from the GitHub repository:
<QuickLink  
  title="Slider-Potentiometer-with-easyC Arduino Library"  
  description="Soldered-Slider-Potentiometer-with-easyC-Arduino-Library"  
  url="https://github.com/SolderedElectronics/Soldered-Slider-Potentiometer-with-easyC-Arduino-Library/tree/main"  
/>  

<InfoBox>

**First time Arduino user?** For a detailed tutorial on getting started with Arduino, see this section of our docs:

<QuickLink  
  title="Getting started with Arduino"  
  description="A full, comprehensive tutorial on how to fully set up and upload code for the first time on an Arduino board, from scratch!"  
  url="/documentation/arduino/quick-start-guide"  
/>  

**Note:** The library is only required for the Qwiic version of the product.

</InfoBox>

---

## Connections

Below is an example connection diagram for **Dasduino CONNECTPLUS**. These pins will be used in the examples throughout this documentation.

| **Dasduino CONNECTPLUS** | **Breakout Board** |
| ------------------------ | ------------------ |
| Qwiic                    | Qwiic              |

<InfoBox>

If you prefer, you can use I2C pins to manually connect:

| **Dasduino CONNECTPLUS** | **Breakout Board** |
| ------------------------ | ------------------ |
| IO21 (Default SDA pin)   | SDA                |
| IO22 (Default SCL pin)   | SCL                |
| VCC                      | VCC                |
| GND                      | GND                |

</InfoBox>

<WarningBox> The **IO21** and **IO22** pins may differ depending on the board you are using, so **make sure to validate** the information before you start working! </WarningBox>