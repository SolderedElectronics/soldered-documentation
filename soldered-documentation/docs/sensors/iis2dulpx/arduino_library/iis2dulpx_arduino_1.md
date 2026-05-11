---
slug: /iis2dulpx/arduino/geting-started 
title: Getting started
id: iis2dulpx-arduino-1 
hide_title: False
---

## Arduino library

To install the Arduino library, you can use the **Arduino Library Manager** or download it directly from the GitHub repository:

<QuickLink
  title="IIS2DULPX Accelerometer breakout Arduino library"
  description="Soldered-IIS2DULPXTR-Accelerometer-Arduino-Library"
  url="https://github.com/SolderedElectronics/Soldered-IIS2DULPXTR-Accelerometer-Arduino-Library"
/>

<InfoBox>

**First time Arduino user?** For a detailed tutorial on how to get started with Arduino, see this section of our docs:

<QuickLink
  title="Getting started with Arduino"
  description="A full, comprehensive tutorial on how to fully set up and upload code for the first time on an Arduino board, from scratch!"
  url="https://docs.soldered.com/arduino/quick-start-guide/"
/>

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

<WarningBox>The **IO21** and **IO22** pins can differ for your personally used board, so **make sure to validate** the information before you start working!</WarningBox>

If you also want to use interrupt-based features (wake-up, tap detection, etc.), connect one of the interrupt pins:

| **Dasduino CONNECTPLUS** | **Breakout Board** |
| ------------------------ | ------------------ |
| Any digital input pin    | INT1 or INT2       |
