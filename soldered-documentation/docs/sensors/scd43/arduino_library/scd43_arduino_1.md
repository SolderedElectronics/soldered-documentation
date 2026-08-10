---
slug: /scd43/arduino/geting-started
title: SCD43 - Getting started
sidebar_label: Getting started
id: scd43-arduino-1
hide_title: false
---

## Arduino library

To install the Arduino library, you can use the **Arduino library manager** or download it from the GitHub repository:

<QuickLink
  title="SCD43 Arduino library"
  description="Arduino library for the SCD43 CO2, temperature and humidity sensor by Soldered"
  url="https://github.com/SolderedElectronics/Soldered-SCD43-Arduino-Library"
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

| **NULA Deepsleep** | **SCD43** |
| ------------------ | --------- |
| Qwiic              | Qwiic     |

If you'd rather wire the sensor directly instead of using a Qwiic cable, connect it to the **K1 header** like this:

| **NULA Deepsleep** | **SCD43 (K1 header)** |
| ------------------- | ----------------------- |
| 3V3                  | 3V3                     |
| GND                  | GND                     |
| SDA                  | SDA                     |
| SCL                  | SCL                     |

<InfoBox>The SCD43 communicates over I2C with a **fixed address of 0x62**. This address cannot be changed.</InfoBox>
