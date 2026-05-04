---
slug: /digital-compass/arduino/geting-started 
title: Digital Compass - Getting started
id: digital-compass-arduino-1 
sidebar_label: Getting started
hide_title: False
---


## Arduino library

To install the Arduino library, you can use the **Arduino library manager** or download it from the GitHub repository:

<QuickLink  
  title="Soldered Compass AK09918 Arduino Library"  
  description="3-Axis Digital Compass Breakout Arduino library by Soldered"  
  url="https://github.com/SolderedElectronics/Soldered-Compass-AK09918-Arduino-Library"  
/>  
<InfoBox>

**First time Arduino user?** For a detailed tutorial on how to get started with Arduino, see this section of our docs:

<QuickLink  
  title="Getting started with Arduino"  
  description="A full, comprehensive tutorial on how to fully set up and upload code for the first time on an Arduino board, from scratch!"  
  url="/arduino/quick-start-guide"  
/>  

</InfoBox>

## Connections
Below is an example connection diagram for **NULA MINI**. These pins will be used in the examples throughout this documentation.

| **NULA MINI** | **Breakout Board** |
| --- | --- |
| Qwiic | Qwiic |

<WarningBox>
Due to the limited number of available pins on the NULA MINI, its default i2c pins are not exposed.
</WarningBox>