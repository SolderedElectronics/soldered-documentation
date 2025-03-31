---
slug: /ncv7329/hardware 
title: Hardware details
id: ncv7329-hardware 
hide_title: False
---

## Pinout

<CenteredImage src="/img/ncv7329/pinout.png" alt="LIN Transceiver NCV7329 Breakout pinout diagram" caption="LIN Transceiver NCV7329 Breakout pinout diagram"/>

Click [**here**](/img/lin-transceiver-ncv7329/lin_transceiver_pinout.png) for a high-resolution image of the pinout.

## Pin Details

| Pin Marking | Pin Name           | Description                                                                 |
| ----------- | ------------------ | --------------------------------------------------------------------------- |
| **GND**     | Ground             | Common ground for the module.                                               |
| **VCC**     | Supply Voltage     | Operating voltage input (typically 5V to 18V).                              |
| **LIN**     | LIN Bus I/O        | Connection to the LIN bus for data transmission and reception.              |
| **EN**      | Enable             | Controls the transceiver's operating mode; high to enable normal operation. |
| **TXD**     | Transmit Data      | Input for data to be transmitted over the LIN bus.                          |
| **RXD**     | Receive Data       | Output for data received from the LIN bus.                                  |

<WarningBox>Ensure that **GND** is connected to the common ground of your system to establish a proper reference for signals.</WarningBox>

---

## Jumper Configuration

The board includes a jumper labeled **LED_EN** that controls the power indicator LED:

- **Jumper Connected**: Power LED is enabled, indicating the presence of supply voltage.
- **Jumper Disconnected**: Power LED is disabled, reducing power consumption.

---

## Dimensions

- **Board Dimensions:** 21.3 × 22.6 × 12.3 mm (0.8 × 0.9 × 0.5 inches)
- **Mounting Holes:** Designed for secure attachment in various applications.

---

## Hardware Repository

Schematics, PCB layouts, and other design files are available in the GitHub repository:

<QuickLink 
  title="LIN Transceiver NCV7329 Breakout Hardware Design" 
  description="GitHub hardware repository for this product"
  url="https://github.com/SolderedElectronics/LIN-transceiver-NCV7329-breakout-hardware-design"
  image="/img/lin-transceiver-ncv7329/lin_transceiver_board.png" 
/>

The repository contains comprehensive resources to understand, modify, or manufacture the board. Below is an overview of the available files:

### CAD Files

The design files are created using KiCad, an open-source PCB design tool. The repository includes the complete project file (`.kicad_pro`), encompassing both the schematic and PCB layout.

### Schematic

The **OUTPUTS** folder contains the schematic in `.pdf` format, providing a detailed circuit diagram of the board.

### Bill of Materials (BOM)

The BOM is provided in two formats:

- A **standard `.csv` file**, listing all components, part numbers, and values.
- An **interactive BOM (`.html`)** that visually highlights each component on the PCB, facilitating easy identification.

### 3D Files

A **3D model** of the PCB is available in `.step` format, allowing inspection of the board design in compatible CAD software.

### Gerber Files

Gerber files are included for PCB manufacturing, containing precise instructions for each layer of the board. The repository provides these files in a `.zip` archive, ready for fabrication.

### Compliance

The repository also includes regulatory and safety documentation, ensuring compliance with relevant industry standards and legal requirements.

For detailed technical specifications and operational guidelines, refer to the [NCV7329 datasheet](https://soldered.com/productdata/2020/03/Soldered_NCV7329_datasheet.pdf).
