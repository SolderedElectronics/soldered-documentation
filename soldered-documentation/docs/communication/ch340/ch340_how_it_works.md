---
slug: /ch340/how-it-works 
title: How it works
id: ch340-how-it-works 
hide_title: False
---  

The USB-UART CH340 Converter Board by [**Soldered**](https://soldered.com/product/usb-uart-ch340-converter-board/) enables communication between a computer and microcontroller or other embedded devices through USB to UART conversion. Featuring the **CH340G chip**, this board supports **asynchronous serial communication** with baud rates **up to 2 Mbps**, making it ideal for programming, debugging, and data transfer. It provides **5V and 3.3V compatibility**.

<CenteredImage src="/img/ch340/ch340onboard.png" alt="ch340onboard" caption="USB-UART CH340 Converter on the board" width="500px" />

---

## Datasheet

For an in-depth look at technical specifications, refer to the official CH340 Datasheet:  

<QuickLink  
  title="USB to serial chip CH340 Datasheet"  
  description="Detailed technical documentation for the CH340 converter"  
  url="https://soldered.com/productdata/2020/02/Soldered_CH340_datasheet.pdf"  
/>  

---

## **How it Works**

The CH340G works by converting **USB signals** into **serial communication** signals and vice versa. It essentially translates data from the computer’s USB interface to a format that can be understood by microcontrollers, sensors, and other serial devices.

1. **USB Data Transfer**: The USB interface sends data to the CH340G chip, where it is converted into UART signals. These UART signals are then sent to the TXD (Transmit) and RXD (Receive) pins, enabling data transmission to/from the connected device.

2. **Signal Conversion**: The CH340G handles the conversion between the **USB protocol** and the **UART protocol**. The chip automatically detects the **baud rate** and **flow control** settings, making it easy to set up and use.

3. **Baud Rate Control**: The CH340G supports a wide range of baud rates, which ensures flexibility when connecting to various devices. The default baud rate can be adjusted using software settings or tools like **Arduino IDE** or other terminal programs.

4. **Flow Control**: For more advanced serial communication, the CH340G supports hardware flow control pins like **CTS, RTS, DTR, DSR**, and **DCD**. These pins help manage the data flow, preventing data loss during communication.

<InfoBox>The CH340G chip ensures automatic baud rate detection and adjusts communication parameters dynamically, simplifying the setup process for users.</InfoBox>

---

## **USB Plug-and-Play Functionality**

The **CH340 Converter Board** is designed for **plug-and-play** operation with minimal setup. It supports various operating systems, including **Windows**, **macOS**, and **Linux**, and is recognized by the system immediately after connection.  

When connected to a computer via USB, the board is powered by the USB port, and data can be transmitted seamlessly to the connected serial device.

<InfoBox>The **USB to UART conversion** provided by the CH340G chip allows seamless communication between a computer and embedded devices without needing additional drivers in most cases.</InfoBox>

---

## How to Connect the CH340 Converter Board

- **Connect Power**:
   - Connect the **VCC** pin to the **5V power supply** (typically from the USB port).
   - Connect **GND** to the ground of both the computer and the connected device.
- **Wiring the Signals**:
   - Connect **TXD** from the CH340 to the **RXD** pin of the target device.
   - Connect **RXD** from the CH340 to the **TXD** pin of the target device.
   - For **flow control**, connect the corresponding **CTS, RTS, DTR, DSR, DCD** pins between devices as needed.
- **Verify Connections**:
   - Ensure the **TXD** and **RXD** are properly connected for data transfer.
   - Confirm that the **GND** pin is common across both devices.

<InfoBox>Make sure you have installed the necessary **CH340 drivers** if the device isn't automatically recognized, especially on older versions of **Windows**.</InfoBox>