---
slug: /mcp2518/overview
title: CAN Transceiver MCP2518 - Overview
id: mcp2518-overview 
hide_title: false
sidebar_label: Overview
pagination_prev: null
---

## CAN Transceiver MCP2518 board

The Controller Area Network (CAN) bus is a communication standard designed for reliable data exchange between microcontrollers without a central host, and is the dominant network protocol in automotive electronics. This breakout board uses the **MCP2518FD** CAN controller, which connects to any microcontroller via **SPI** and supports both classic **CAN 2.0B** (up to 1 Mbps, 8-byte payload) and the newer **CAN FD** (up to 8 Mbps, 64-byte payload). The CAN bus is accessible via the **CANH** and **CANL** screw terminal pins on the board. A 120 Ω termination resistor is included and can be switched in via a jumper (see the Jumper Details section of the Hardware Details page).

<CenteredImage src="/img/mcp2518/333020.jpg" alt="CAN Transceiver MCP2518 Breakout" caption="CAN Transceiver MCP2518 Breakout"/>

## Which product is this documentation for?

<QuickLink 
  title="CAN Transceiver MCP2518 board" 
  description="333030"
  url="https://soldered.com/product/can-transceiver-mcp2518-board/"
  image="/img/mcp2518/333020.jpg" 
/>

---

## Key features

- **Supported standards:** CAN 2.0B and CAN FD
- **Operating voltage:** 2.7 V to 5 V
- **Supply current:** 10 µA (standby) to 12 mA (active)
- **Data bit rate:** up to 8 Mbps (CAN FD), up to 1 Mbps (CAN 2.0B)
- **Payload size:** up to 64 bytes (CAN FD), up to 8 bytes (CAN 2.0B)
- **Hardware CRC noise detection**
- **SPI interface** for connection to any microcontroller
- **Onboard 120 Ω termination resistor** switchable via jumper (JP1)
- **Screw terminal** for CANH and CANL bus connections
- **Header pins** for SPI, interrupt, and clock signals