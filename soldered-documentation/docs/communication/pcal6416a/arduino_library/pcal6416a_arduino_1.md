---
slug: /pcal6416a/arduino/getting-started 
title: PCAL6416A - Getting started
sidebar_label: Getting started
id: pcal6416a-arduino-1 
hide_title: false
---

## Arduino library

This library isn't in the Arduino Library Manager yet, so download it directly from the GitHub repository:  
<QuickLink  
  title="PCAL6416A GPIO Expander Breakout Arduino library"  
  description="PCAL6416A Arduino library by Soldered"  
  url="https://github.com/SolderedElectronics/Soldered-PCAL6416A-IO-Expander-Arduino-Library"  
/>  

Click **Code → Download ZIP** on the repository page, then in the Arduino IDE go to **Sketch → Include Library → Add .ZIP Library...** and select the downloaded file.

<InfoBox>

**Are you a first-time Arduino user?** For a detailed tutorial on getting started with Arduino, see this section of our docs:

<QuickLink  
  title="Getting started with Arduino"  
  description="A comprehensive tutorial on how to set up and upload code to an Arduino board for the first time, from scratch!"  
  url="/arduino/quick-start-guide"  
/>  

</InfoBox>

---

## Connections

Below is an example connection diagram for **NULA Deepsleep**. These pins will be used in the examples throughout this documentation.

If your board has a Qwiic connector, connect it directly to the PCAL6416A board with a Qwiic cable:

| **NULA Deepsleep** | **PCAL6416A Board** |
| ------------------- | -------------------- |
| Qwiic                | Qwiic                 |

<InfoBox>

If you prefer, you can use I2C pins to manually connect:

| **NULA Deepsleep** | **PCAL6416A Board** |
| ------------------- | -------------------- |
| IO8 (Default SDA pin) | SDA                   |
| IO9 (Default SCL pin) | SCL                   |
| VCC                   | VCC                   |
| GND                   | GND                   |

</InfoBox>





