---
slug: /nula_w55rp20/overview
title: NULA Ethernet W55RP20 - Overview
sidebar_label: Overview
id: nula_w55rp20-overview
hide_title: True
pagination_prev: null
---

{/*
  TODO - pending items before this product page can go fully live:
  - Onboard chip photo for how-it-works
  - Jumper photos for hardware details
  - Hardware repository link (KiCad/Gerbers/BOM) once available
*/}

# Overview

## NULA Ethernet W55RP20

The **NULA Ethernet W55RP20** is a development board built around the **WIZnet W55RP20** - a chip that combines the **Raspberry Pi RP2040** with a **hardwired W5500 Ethernet controller** in a single package. The board has a built-in **RJ45 Ethernet port**, **USB-C** for programming and power, a **Qwiic connector** for I2C peripherals, an onboard **microSD card reader**, and a **JST battery connector** for running off a single-cell Li-Ion/Li-Po battery.

Because the TCP/IP stack runs in hardware on the W5500, the RP2040 cores are free for your application code rather than managing network overhead in software.

<CenteredImage src="/img/nula_w55rp20/NULA_W55RP20.png" alt="NULA Ethernet W55RP20" caption="NULA Ethernet W55RP20"/>

---

## Which product is this documentation for?

<QuickLink
title="NULA Ethernet W55RP20"
description="RP2040 development board with hardwired W5500 Ethernet, RJ45, microSD and Qwiic."
url="https://soldered.com/products/soldered-nula-ethernet-w55rp20"
image="/img/nula_w55rp20/333407.png"
/>

---

## Key features

- **SiP:** WIZnet W55RP20 (RP2040 + W5500 in one package)
- **Processor:** Dual-core ARM Cortex-M0+ @ 133 MHz
- **SRAM:** 264 KB on-chip
- **Flash:** 2 MB external
- **Ethernet:** 10/100 Mbit/s, hardwired TCP/IP - TCP, UDP, IPv4, ICMP, ARP, IGMP, PPPoE
- **Simultaneous sockets:** Up to **8** independent hardware sockets
- **Ethernet buffers:** 32 KB internal TX/RX
- **USB-C:** Programming, power, and serial communication
- **Qwiic:** Plug-and-play I2C sensor integration
- **MicroSD card reader:** Onboard slot with card-detect, wired over SPI1
- **Battery support:** JST connector and onboard TP4056M charger for single-cell Li-Ion/Li-Po batteries
- **GPIO:** Access to RP2040 I/O pins (UART, SPI, I2C, PWM, ADC) - a handful of pins are reserved internally for the W5500, see the [hardware details](/nula_w55rp20/hardware) page
- **Logic level:** 3.3 V
- **ADC:** 12-bit, 0-3.3 V range
- **Development support:** Arduino IDE, MicroPython, C/C++ SDK
- **In the box:** USB-A to USB-C cable

---

## You may also need

<QuickLink
  title="Qwiic cable"
  description="Qwiic compatible cables with connectors on both ends, available in various lengths."
  url="https://soldered.com/product/easyc-cable/"
  image="/img/333311.webp"
/>
