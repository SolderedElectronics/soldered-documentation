---
slug: /nula_w55rp20/overview
title: NULA Ether W55RP20 - Overview
sidebar_label: Overview
id: nula_w55rp20-overview
hide_title: True
pagination_prev: null
---

# Overview

## NULA Dual ESP32-C5

The **Soldered NULA Dual ESP32-C5** is a development board featuring **two Espressif ESP32-C5 modules**, enabling a wide range of dual-radio and multi-role embedded applications. Each ESP32-C5 integrates a **32-bit RISC-V core**, **Wi-Fi 6 (2.4 GHz & 5 GHz)**, and **Bluetooth 5 (LE)**, making this board ideal for projects that require simultaneous multi-network connectivity, protocol bridging, or independent parallel processing.

The two modules can operate **independently** or work in tandem - one handling the main application while the other manages communication, or each connected to a different network. The board follows the familiar **Soldered NULA form factor**, with an **easyC (Qwiic) connector** for sensor integration and a **USB-C** port for programming and power.

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

- **Modules:** Two independent **ESP32-C5** modules
- **Processor:** 32-bit RISC-V single-core @ up to **240 MHz** (per module)
- **Wi-Fi:** Wi-Fi 6 (802.11ax) - **2.4 GHz and 5 GHz** dual-band (per module)
- **Bluetooth:** Bluetooth 5 (LE) (per module)
- **USB-C:** Programming, power, and serial communication
- **easyC / Qwiic:** Plug-and-play I²C sensor integration
- **GPIO:** Full access to both modules' I/O pins (UART, SPI, I²C, PWM, ADC)
- **Logic level:** 3.3 V
- **Development support:** Arduino IDE, ESP-IDF, MicroPython compatible

---

---
slug: /nula_w55rp20/overview
title: NULA Ether W55RP20 - Overview
sidebar_label: Overview
id: nula_w55rp20-overview
hide_title: True
pagination_prev: null
---

# Overview

## NULA Ether W55RP20

The **Soldered NULA Ether W55RP20** is a compact development board built around the **WIZnet W55RP20** - a System-in-Package (SiP) that combines the **Raspberry Pi RP2040** dual-core microcontroller with a **hardwired W5500 TCP/IP Ethernet controller** in a single chip.

This integration makes the NULA Ether W55RP20 an ideal platform for **wired Ethernet-connected embedded systems** without the overhead of a software TCP/IP stack. The board exposes the RP2040's GPIO pins alongside a built-in **RJ45 Ethernet port**, **USB-C** for programming and power, and a **Qwiic connector** for quick sensor integration.

Whether you're building an **IoT gateway**, a **network data logger**, or an **Ethernet-enabled controller**, the NULA Ether W55RP20 delivers reliable, deterministic networking with the familiar RP2040 ecosystem.

{/* <CenteredImage src="/img/nula w55rp20/NULA_W55RP20.png" alt="NULA Ether W55RP20" caption="NULA Ether W55RP20 Development Board"/> */}

<br></br>

---

## Which product is this documentation for?

{/* <QuickLink
  title="NULA Ether W55RP20"
  description="RP2040 + W5500 hardwired TCP/IP Ethernet development board"
  url="https://soldered.com/product/nula-w55rp20/"
  image="/img/nula w55rp20/NULA_W55RP20.png"
/> */}

---

## Key Features

- **SiP:** WIZnet W55RP20 (RP2040 + W5500 in one package)
- **Processor:** Dual-core ARM Cortex-M0+ @ 133 MHz
- **SRAM:** 264 KB on-chip
- **Flash:** 2 MB external
- **Ethernet:** Hardwired TCP/IP stack - TCP, UDP, IPv4, ICMP, ARP, IGMP, PPPoE
- **Simultaneous sockets:** Up to **8** independent hardware sockets
- **Ethernet buffers:** 32 KB internal TX/RX
- **USB-C:** Programming, power, and serial communication
- **Qwiic:** Plug-and-play I2C sensor integration
- **GPIO:** Full access to RP2040 I/O pins (UART, SPI, I2C, PWM, ADC)
- **Logic level:** 3.3 V (not 5 V tolerant)
- **ADC:** 12-bit, 0-3.3 V range
- **Development support:** Arduino IDE, MicroPython, C/C++ SDK compatible

---

## You may also need

<QuickLink
  title="Qwiic cable"
  description="Qwiic compatible cables with connectors on both ends, available in various lengths."
  url="https://soldered.com/product/easyc-cable/"
  image="/img/333311.webp"
/>
