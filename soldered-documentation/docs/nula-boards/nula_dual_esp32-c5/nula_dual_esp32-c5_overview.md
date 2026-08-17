---
slug: /nula-dual-esp32-c5/overview
title: NULA Dual ESP32-C5 - Overview
sidebar_label: Overview
id: nula_dual_esp32-c5-overview
hide_title: True
pagination_prev: null
---

# Overview

## NULA Dual ESP32-C5

The **Soldered NULA Dual ESP32-C5** is a development board built around the **Espressif ESP32-C5-WROOM-1-N8R8** module. The "Dual" in its name refers to the chip's **dual-band Wi-Fi 6** radio, which works on both the **2.4 GHz and 5 GHz** bands - the radio uses one band at a time, so you simply pick whichever your network runs on. The ESP32-C5 also brings **Bluetooth 5 (LE)**, an **802.15.4** radio for Thread, Zigbee and Matter, and a 32-bit RISC-V high-performance core for your code, alongside a separate low-power core that can keep simple tasks running while the main core sleeps.

The board follows the familiar **Soldered NULA form factor**, with a **Qwiic connector** for sensor integration, a battery connector with onboard charging, and a **USB-C** port for programming and power.

{/* <CenteredImage src="/img/nula_dual_esp32-c5/NULA_Dual_ESP32-C5.png" alt="NULA Dual ESP32-C5" caption="NULA Dual ESP32-C5 Development Board"/> */}

<br></br>

---

## Which product is this documentation for?

{/* <QuickLink
  title="NULA Dual ESP32-C5"
  description="Dual ESP32-C5 development board with Wi-Fi 6 and Bluetooth 5"
  url="https://soldered.com/product/nula-dual-esp32-c5/"
  image="/img/nula_dual_esp32-c5/NULA_Dual_ESP32-C5.png"
/> */}

<WarningBox>The product page for this board is not available yet! We're working on it. In the meantime, please [**contact us**](https://soldered.com/contact/) for more information.</WarningBox>

---

## Key Features

- **Module:** Espressif **ESP32-C5-WROOM-1-N8R8**
- **Processor:** 32-bit RISC-V high-performance core @ up to **240 MHz**, plus a separate low-power (LP) RISC-V core for background tasks
- **Memory:** **8 MB flash** and **8 MB PSRAM** (PSRAM is disabled by default in Arduino - see the Arduino page)
- **Wi-Fi:** Wi-Fi 6 (802.11ax) - dual-band **2.4 GHz and 5 GHz**, one band at a time
- **Bluetooth:** Bluetooth 5 (LE)
- **802.15.4:** Thread, Zigbee and Matter
- **USB-C:** Programming, power, and serial communication through an onboard **CH340K** USB-to-UART bridge
- **Qwiic:** Plug-and-play I²C sensor integration
- **Battery support:** Onboard JST connector and **TP4056** charging circuit for a 3.7 V Li-Ion/Li-Poly battery, at roughly **400 mA** charge current
- **GPIO:** Broad access to the module's I/O pins (UART, SPI, I²C, PWM, ADC)
- **Logic level:** 3.3 V
- **Development support:** Arduino IDE, ESP-IDF, and MicroPython (v1.27 or newer, using the generic ESP32-C5 build)

---

## You may also need

<QuickLink
  title="Qwiic cable"
  description="Qwiic compatible cables with connectors on both ends, available in various lengths."
  url="https://soldered.com/product/easyc-cable/"
  image="/img/333311.webp"
/>

<QuickLink 
  title="Li-Ion Battery 3.7 V" 
  description="Rechargeable 3.7 V Li-Ion battery compatible with the NULA Dual ESP32-C5's JST connector."
  url="https://soldered.com/categories/power-sources-batteries/batteries/lithium-batteries/"
  image="/img/li-ion-battery/333284.jpg"
/>

