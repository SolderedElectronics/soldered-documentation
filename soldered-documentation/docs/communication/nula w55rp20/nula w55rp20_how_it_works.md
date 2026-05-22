---
slug: /nula_w55rp20/how-it-works
title: NULA W55RP20 - How it works
sidebar_label: How it works
id: nula_w55rp20-how-it-works
hide_title: False
---

## How It Works

The **NULA W55RP20** is a development board designed and manufactured by {/* [Soldered Electronics](https://soldered.com/product/nula-w55rp20/) */}**Soldered Electronics**, built around the **WIZnet W55RP20** — a **System-in-Package (SiP)** created by **WIZnet** that integrates two chips into a single module: the **Raspberry Pi RP2040** dual-core microcontroller and the **WIZnet W5500** hardwired TCP/IP Ethernet controller. This combination means the board can run user firmware on the RP2040 and handle full Ethernet networking through the W5500, all without needing any external networking chips or software TCP/IP stacks.

The RP2040 communicates with the W5500 internally over a dedicated **SPI bus** (GPIO16–GPIO21), which is wired inside the SiP package. From the user's perspective, the Ethernet controller behaves exactly like a standalone W5500 — the same libraries and socket API apply.

---

## Datasheets

<QuickLink
  title="W55RP20 Datasheet"
  description="Complete technical documentation for the WIZnet W55RP20 SiP"
  url="https://docs.wiznet.io/Product/ioNIC/W55RP20/documents_and_downloads"
/>

<QuickLink
  title="RP2040 Datasheet"
  description="Complete technical documentation for the Raspberry Pi RP2040 microcontroller"
  url="https://datasheets.raspberrypi.com/rp2040/rp2040-datasheet.pdf"
/>

---

## RP2040 Microcontroller

The **RP2040** is the processing core of the board. It features:

- **Dual Arm Cortex-M0+** cores running at up to **133 MHz**
- **264 KB** of on-chip SRAM
- **2 MB** of external flash memory
- Rich peripheral set: **UART, SPI, I²C, PWM, ADC, PIO**
- **Programmable I/O (PIO)** — state machines that can implement custom digital interfaces in hardware

The RP2040 runs the application firmware and drives all board peripherals, including the microSD card, the WS2812B RGB LED, the Qwiic connector, and the Ethernet controller.

---

## W5500 Hardwired TCP/IP

The **W5500** handles all Ethernet communication using a **hardwired TCP/IP stack** — meaning the protocol logic (TCP, UDP, IP, ARP, ICMP, IGMP, PPPoE) runs in dedicated silicon rather than in software on the RP2040. This offloads network processing entirely from the main processor and makes the Ethernet connection deterministic and reliable.

Key W5500 features available on this board:

- Up to **8 independent hardware sockets** open simultaneously
- **32 KB** internal TX/RX buffer memory
- **10/100 Mbps** Ethernet with auto-negotiation (configurable via JP10–JP12)
- Hardwired support for **TCP, UDP, IPv4, ICMP, ARP, IGMP, PPPoE**

The W5500 connects to the physical Ethernet network through an external **HR913550A isolation transformer**, which provides the required galvanic isolation on the RJ45 port.

---

## MicroSD Card

The board includes a **microSD card slot** connected to the RP2040 via SPI (GPIO10–GPIO13). The microSD power rail (**3V3_MICROSD**) is controlled by a PMOS transistor switch driven by **GPIO09**, allowing the firmware to power-cycle the card for low-power applications. JP4 can bypass this switch to keep the card always powered.

---

## WS2812B RGB LED

A single **WS2812B addressable RGB LED** (D3) is connected to **GPIO01**. It uses a single-wire protocol and can display any colour, making it useful as a status indicator.

---

## Qwiic / easyC

The **Qwiic connector** exposes the RP2040's I²C bus (**GPIO02 = SDA, GPIO03 = SCL**) with onboard 10 kΩ pull-up resistors (enabled by default via JP2). This allows any Qwiic/easyC-compatible sensor or module to be connected without soldering.

---

## Power

The board accepts power via **USB-C** (5 V). An onboard **TPS7A2633DRVR** regulator steps this down to a stable **3.3 V** rail for all logic. A **TP4056M** battery charger and automatic source-selection circuit (PMOS Q1) allow a **Li-Ion/Li-Poly battery** to be connected via the JST connector — the board will switch to battery power automatically when USB is disconnected.
