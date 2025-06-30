---
slug: /connect-programmer/how-it-works 
title: CONNECT Programmer - How it works
sidebar_label: How it works
id: connect-programmer-how-it-works 
hide_title: False
pagination_next: null
---

The CONNECT programmer uses the onboard **CH340 chip** by [**WCH**](https://www.wch-ic.com/products/CH340.html) to convert the USB protocol into serial communication.

<CenteredImage src="/img/connect-programmer/onboard.jpg" alt="ch340onboard" caption="USB-UART CH340 Converter on the board" width="500px" />

---

## Datasheet

For an in-depth look at the technical specifications, refer to the official CH340 Datasheet:  

<QuickLink  
  title="USB to serial chip CH340 Datasheet"  
  description="Detailed technical documentation for the CH340 converter"  
  url="https://soldered.com/productdata/2020/02/Soldered_CH340_datasheet.pdf"  
/>

---

## How it Works

The CH340 works by converting **USB signals** into **serial communication** signals and vice versa. It essentially translates data from the computer’s USB interface and passes it on to the ESP board.

1. **USB Data Transfer**: The USB interface sends data to the CH340 chip, where it is converted into UART signals. These UART signals are then sent to the TXD (Transmit) and RXD (Receive) pins, enabling data transmission to and from the connected device.

2. **Signal Conversion**: The CH340 handles the conversion between the **USB protocol** and the **UART protocol**. The chip automatically detects the **baud rate** and **flow control** settings, making it easy to set up and use.

<InfoBox>The CH340 chip ensures automatic baud rate detection and adjusts communication parameters dynamically, simplifying the setup process for users.</InfoBox>

The breakout board also supplies the ESP with 3V3 and can place it into **Bootloader mode** using the **IO0 pin**.

Programming the ESP with the CONNECT programmer works the same as when you connect the USB cable directly to the ESP.

---

## **USB Plug-and-Play Functionality**

The **CH340 Converter Board** is designed for **plug-and-play** operation with minimal setup. It supports various operating systems, including **Windows**, **macOS**, and **Linux**, and is recognized by the system immediately after connection.

When connected to a computer via USB, the board is powered by the USB port, and data can be transmitted seamlessly to the connected serial device.

<InfoBox>The **USB-to-UART conversion** provided by the CH340 chip allows seamless communication between a computer and embedded devices without needing additional drivers in most cases.</InfoBox>

---

## How to Connect It?

| **CONNECT Programmer** | **ESP Board** |
| ------------------------ | ------------------------- |
| IO0  | IO0          |
| RESET  | RESET          |
| TXD  | RXD          |
| RXD  | TXD          |
| 3V3  | 3V3          |
| GND  | GND |

<CenteredImage src="/img/connect-programmer/connection.jpg" alt="How to connect it" caption="Connections" width="500px" />