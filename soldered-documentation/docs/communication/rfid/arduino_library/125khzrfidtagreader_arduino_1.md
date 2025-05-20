---
slug: /rfid/arduino/geting-started
title: Rfid - Getting started
id: 125khzrfidtagreader-arduino-1
hide_title: false
---

# Arduino Library

To install the Arduino library, you can use the **Arduino Library Manager** or download it from the GitHub repository:
<QuickLink
  title="125kHz RFID tag reader board - I2C & UART Arduino library"  
  description="Soldered-RFID-Reader-125kHz-Arduino-Library"  
  url="https://github.com/SolderedElectronics/Soldered-RFID-Reader-125kHz-Arduino-Library/tree/main"  
/>

<InfoBox>

**First-time Arduino user?** For a detailed tutorial on how to get started with Arduino, see this section of our docs:

<QuickLink  
  title="Getting started with Arduino"  
  description="A full, comprehensive tutorial on how to fully set up and upload code for the first time on an Arduino board, from scratch!"  
  url="/documentation/arduino/quick-start-guide"  
/>  
</InfoBox>

---

## Connections

Below is an example connection diagram for **Dasduino CONNECTPLUS**. These pins will be used in the examples throughout this documentation.

### UART version

| **Dasduino CONNECTPLUS** | **Breakout Board** |
| ------------------------ | ------------------ |
| IO4 (User choice)        | TXD                |
| IO5 (User choice)        | RXD                |
| VCC                      | VCC                |
| GND                      | GND                |

---

### Qwiic version

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

<WarningBox> The **IO21** and **IO22** pins may differ for your board, so **make sure to validate** the information before you start working!</WarningBox>
