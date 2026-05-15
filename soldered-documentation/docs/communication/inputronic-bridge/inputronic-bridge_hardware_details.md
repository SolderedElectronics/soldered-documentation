---
slug: /inputronic-bridge/hardware 
title: Hardware details
id: inputronic-bridge-hardware 
hide_title: False
---
## Pinout

<CenteredImage src="/img/inputronic-bridge/pinout.png" alt="Inputronic BRIDGE pinout diagram" caption="Inputronic BRIDGE pinout diagram"/>

Click [**here**](/img/inputronic-bridge/pinout.png) for a high-resolution image of the pinout.

## Pin details

| Pin Marking | Pin Name              | Description                                                                 |
| ----------- | --------------------- | --------------------------------------------------------------------------- |
| **3V3** | 3.3V Power            | 3.3V power supply input for logic.                                          |
| **GND** | Ground                | Common ground for the module.                                               |
| **SDA** | I2C Data              | I2C data line for the default communication protocol.                       |
| **SCL** | I2C Clock             | I2C clock line for the default communication protocol.                      |
| **RX** | UART Receive          | UART receive pin (used when UART protocol is selected).                     |
| **TX** | UART Transmit         | UART transmit pin (used when UART protocol is selected).                    |
| **MISO** | SPI MISO              | SPI Master In Slave Out pin (used when SPI protocol is selected).           |
| **MOSI** | SPI MOSI              | SPI Master Out Slave In pin (used when SPI protocol is selected).           |
| **CLK** | SPI Clock             | SPI Clock pin (used when SPI protocol is selected).                         |
| **CS** | SPI Chip Select       | SPI Chip Select pin (used when SPI protocol is selected).                   |
| **INT** | Interrupt Output      | Signals the host MCU when new data is ready (avoids continuous polling).    |
| **IO0** | GPIO 0                | ESP32-S3 boot/strap pin, also available as general I/O.                     |
| **FAULT** | Fault Indicator       | Overcurrent fault output from the USB protection switch.                    |
| **RST** | Reset                 | Active-low reset pin for the onboard ESP32-S3.                              |

---


This board contains hardware jumpers, see below for their locations and functions:

<FlickityCarousel
images={[
{ src: '/img/inputronic-bridge/JP1.jpg', alt: 'Jumper JP1', caption: 'JP1' },
{ src: '/img/inputronic-bridge/JP2.jpg', alt: 'Jumper JP2', caption: 'JP2' },
{ src: '/img/inputronic-bridge/JP3.jpg', alt: 'Jumper JP3', caption: 'JP3' },
{ src: '/img/inputronic-bridge/JP4.jpg', alt: 'Jumper JP4', caption: 'JP4' },
]}
jumpers={true}
/>

| Jumper Marking | Default State            | Description                                                                                       |
| -------------- | ------------------------ | ------------------------------------------------------------------------------------------------- |
| **JP1**        | **NC** (Normally closed) | Cut the trace to disconnect the power LED and reduce overall current consumption.                 |
| **JP2**        | **NO** (Normally open)   | Connects onboard 3.3V pull-up resistors for the I2C bus (SDA and SCL).                            |
| **JP3**        | **NO** (Normally open)   | Configures the output protocol. Leave open for default I2C, or solder to select UART/SPI modes.   |
| **JP4**        | **NO** (Normally open)   | Configures the output protocol. Leave open for default I2C, or solder to select UART/SPI modes.   |


<InfoBox>
The table below shows how JP3 and JP4 configure the module's communication protocol.
| JP3               | JP4               | Active Protocol |
| ----------------- | ----------------- | --------------- |
| Not connected     | Not connected     | **I2C**         |
| Connected         | Not connected     | **UART**        |
| Not connected     | Connected         | **UART**        |
| Connected         | Connected         | **SPI**         |
</InfoBox>

---

## Dimensions

- **Board Dimensions:** 63 x 26 mm (2.48 x 1.02 inch)
- **Header Pin Holes:** 1.5 mm
- **Screw Holes:** Designed for M3 screws (3.2 mm diameter)
- Soldered boards are LEGO compatible! 🧱

---

## Hardware Repository

Schematics, KiCad files, Gerber files, and more can be found in the GitHub repository:

<QuickLink title="Inputronic Hardware Design" 
description="GitHub hardware repository for this product" 
url="https://github.com/SolderedElectronics/Inputronic-BRIDGE-hardware-design" />

The hardware repository contains everything you need to understand, modify, or manufacture the board. The different output folders are versioned. You can check which board version you have specifically by finding the version mark on the PCB.

Below is an overview of the available files.  

#### CAD files

We use KiCad, an open-source PCB design tool. You can open and edit the `.kicad_pro` project file, which includes both the schematic and PCB layout.  

The `PANEL` files are used internally for production.  

#### Schematic

The **OUTPUTS** folder contains the **schematic** in `.pdf` format, exported from KiCad.

#### BOM (Bill of Materials)

The bill of materials (BOM) is provided in two formats:  

- A **standard `.csv` table**, listing all components, part numbers, and values.  
- An **interactive BOM (`.html`)** that visually highlights each component on the PCB, making it easy to locate and reference parts.  

#### 3D files

A **3D model** of the PCB is available in `.step` format, allowing you to inspect the board design in CAD software.  

#### Gerber files 

Gerber files are essential for PCB manufacturing, as they contain precise instructions for each layer of the board. The repository includes standard Gerber outputs in a .zip file, such as:  

- **Copper layers** (`.Cu.gbr`) – Defines the traces and pads on the board.  
- **Solder mask layers** (`.Mask.gbr`) – Specifies the protective solder mask.  
- **Silkscreen layers** (`.Silkscreen.gbr`) – Contains text and component markings.  
- **Paste layers** (`.Paste.gbr`) – Used for stencil fabrication in SMD assembly.  
- **Drill files** (`.drl`) – Provides drilling coordinates for vias and holes.  
- **Board outline** (`.Edge_Cuts.gbr`) – Defines the shape of the PCB.  
- **Gerber job file** (`.gbrjob`) – Describes the set of Gerber files used for production.  

These files are ready for fabrication and can be used in PCB manufacturing.

#### Compliance  

The **Compliance** section includes important regulatory and safety documentation for this product. These files ensure compliance with relevant industry standards and legal requirements.  

- **CE** – Certification document confirming compliance with EU safety, health, and environmental requirements.  
- **UKCA** – UKCA (UK Conformity Assessed) certification for the UK market.  
- **Safety Instructions** – Safety guidelines and precautions in English and German.
- **Info.txt** – Contains product details such as SKU, country of origin, HS tariff code, and barcode.