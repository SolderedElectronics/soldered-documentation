---
slug: /st67w611m1/how-it-works 
title: How it works
id: st67w611m1-how-it-works 
hide_title: false
sidebar_label: How it works
---  

The **ST67W611M1** is a Wi-Fi 6 and Bluetooth LE 5.4 co-processor module by STMicroelectronics. Your STM32 host MCU sends commands over SPI or UART, and the module handles all radio operations, protocol stacks, and security internally. The Soldered breakout integrates a PCB antenna, 4 MB NOR flash, and a 40 MHz crystal, so no external RF components are required.

<CenteredImage src="/img/st67w611m1/st67_highlighted.webp" alt="ST67W611M1 on the board" caption="ST67W611M1 on the board" width="500px" />

---

## Datasheet

For detailed technical specifications, please refer to the official ST67W611M1 Datasheet:

<QuickLink
    title="ST67W611M1 Datasheet"
    description="Complete technical documentation for the ST67W611M1 module"
    url="https://cdn.shopify.com/s/files/1/0990/5029/1549/files/st67w611m1.pdf?v=1775551766"
/>

---

## How the ST67W611M1 works

The ST67W611M1 contains a 2.4 GHz radio that supports **Wi-Fi 6 (IEEE 802.11b/g/n/ax)** and **Bluetooth LE 5.4** simultaneously. On the Wi-Fi side, it reaches up to **17 Mbps TCP throughput** and supports WPA3 security, STA mode, SoftAP mode, and concurrent STA+SoftAP. On the BLE side, it runs at up to **2 Mbps** and supports peer-to-peer, broadcast, and mesh topologies.

The host MCU does not run any wireless stack. Instead, it issues commands to the ST67W611M1 over **SPI** (up to 40 MHz, full-duplex) or **UART** (2 Mbps). The module processes those commands, manages the radio, and returns results. The **RDY** pin signals the host when the module has data to send; the host then asserts **CS** to start an SPI transfer. CS also doubles as a wake-up signal from the host when the module is in a low-power state.

The module has several power states. In deep sleep it draws **90 µA**, which makes it practical for battery-operated devices that connect periodically.

The **X-CUBE-ST67W61** expansion software package, pre-flashed on this board, abstracts all SPI/UART framing, Wi-Fi association, DHCP, TLS, and BLE pairing into higher-level APIs. You call functions to join a network or open a TCP/HTTPS connection rather than managing radio registers or packet buffers directly.

---

## SPI and UART communication

The ST67W611M1 operates as an **SPI slave**. The host MCU drives CLK and MOSI; the module drives MISO. The maximum clock frequency is **40 MHz**. The **RDY** pin works as an active-low interrupt: when the module has data ready for the host, it asserts RDY, the host responds by pulling CS low and reading the transfer. CS can also be held low by the host to wake the module from sleep before starting a transaction.

The **UART** interface is an alternative to SPI for hosts without available SPI peripherals. It runs at a fixed **2 Mbps**, 8N1, with no hardware flow control (RTS/CTS are not used).