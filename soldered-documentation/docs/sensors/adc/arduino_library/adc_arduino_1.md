---
slug: /adc/arduino/getting-started
title: "Analog to Digital Converter \u2013 Arduino getting started"
id: adc-arduino-1
hide_title: false
---
## Arduino library

To install the Arduino library, you can use the **Arduino Library Manager** or download it from the GitHub repository:
<QuickLink  
  title="SOLDERED ADS1015 ADS1115 ADC Arduino library"  
  description="ADC Arduino library by Soldered"  
  url="https://github.com/SolderedElectronics/Soldered-ADS1015-ADS1115-ADC-Arduino-Library/tree/main"  
/>  

<InfoBox>

**First time Arduino user?** For a detailed tutorial on how to get started with Arduino, see this section of our docs:

<QuickLink  
  title="Getting started with Arduino"  
  description="A full, comprehensive tutorial on how to set up and upload code for the first time on an Arduino board, from scratch!"  
  url="/documentation/arduino/quick-start-guide"  
/>  

</InfoBox>

---

## Connections

Below is an example connection diagram for the **Dasduino CONNECTPLUS**. These pins will be used in the examples throughout this documentation.

| **Dasduino CONNECTPLUS** | **Breakout Board** |
| ------------------------ | ------------------ |
| Qwiic                    | Qwiic              |

<InfoBox>

If you prefer, you can use I2C pins to manually connect:

| **Dasduino CONNECTPLUS**     | **Breakout Board** |
| ---------------------------- | ------------------ |
| IO21 (Default SDA pin)       | SDA                |
| IO22 (Default SCL pin)       | SCL                |
| VCC                          | VCC                |
| GND                          | GND                |

<WarningBox>For the ALERT functionality, you can also connect the **ALERT** pin to an available IO pin if you plan to use the comparator feature.</WarningBox>

| **Dasduino CONNECTPLUS**     | **Breakout Board** |
| ---------------------------- | ------------------ |
| IO25 (any digital pin works) | ALERT              |

</InfoBox>