---
slug: /espflash-programmer/how-it-works 
title: ESPFlash Programmer - How it works
sidebar_label: How it works
id: espflash-programmer-how-it-works 
hide_title: False
pagination_next: null
---

The ESPFlash Programmer uses the onboard **CH340C chip** by [**WCH**](https://www.lcsc.com/product-detail/USB-ICs_WCH-Jiangsu-Qin-Heng-CH340C_C84681.html) to convert the USB protocol into serial communication.

<CenteredImage src="/img/espflash-programmer/chip.png" alt="CH340C chip on the ESPFlash Programmer board" caption="CH340C chip on the ESPFlash Programmer board" width="500px" />

---

## Datasheet

For an in-depth look at the technical specifications, refer to the official CH340C Datasheet:  

<QuickLink  
  title="USB to serial chip CH340C Datasheet"  
  description="Detailed technical documentation for the CH340C converter"  
  url="https://www.lcsc.com/datasheet/C84681.pdf"  
/>

---

## How it Works

The CH340C works by converting **USB signals** into **serial communication** signals and vice versa. It essentially translates data from the computer’s USB interface and passes it on to the ESP board.

1. **USB Data Transfer**: The USB interface sends data to the CH340C chip, where it is converted into UART signals. These UART signals are then sent to the TXD (Transmit) and RXD (Receive) pins, enabling data transmission to and from the connected device.

2. **Signal Conversion**: The CH340C handles the conversion between the **USB protocol** and the **UART protocol**. It supports standard baud rates from 50 bps up to 2 Mbps, and your computer's serial driver picks the rate to match what your code or flashing tool requests.

<InfoBox>The CH340C supports a wide range of standard baud rates, so it works with whatever rate your sketch or flashing tool requests without any manual configuration.</InfoBox>

The breakout board also supplies the ESP with 3V3 and can place it into **Bootloader mode** using the **IO0 pin**.

Programming the ESP with the ESPFlash Programmer works the same as when you connect the USB cable directly to the ESP.

---

## **USB Plug-and-Play Functionality**

The **ESPFlash Programmer** is designed for **plug-and-play** operation with minimal setup. It supports various operating systems, including **Windows**, **macOS**, and **Linux**, and is recognized by the system immediately after connection.

When connected to a computer via USB, the board is powered by the USB port, and data can be transmitted seamlessly to the connected serial device.

<InfoBox>The **USB-to-UART conversion** provided by the CH340C chip allows seamless communication between a computer and embedded devices without needing additional drivers in most cases.</InfoBox>

---

## How to Connect It?

| **ESPFlash Programmer** | **ESP Board** |
| ------------------------ | ------------------------- |
| IO0  | IO0          |
| RESET  | RESET          |
| TXD  | RXD          |
| RXD  | TXD          |
| 3V3  | 3V3          |
| GND  | GND |