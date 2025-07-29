---  
slug: /ncv7329/hardware  
title: NCV7329 – Hardware details
sidebar_label: Hardware details
id: ncv7329-hardware  
hide_title: False  
---

## Pinout

<CenteredImage src="/img/ncv7329/pinout.png" alt="LIN Transceiver NCV7329 Breakout pinout diagram" caption="LIN Transceiver NCV7329 Breakout pinout diagram"/>

Click [**here**](/img/ncv7329/pinout.png) for a high-resolution image of the pinout.

## Pin Details

| Pin Marking | Pin Name       | Description                                                                 |
| ----------- | -------------- | --------------------------------------------------------------------------- |
| **GND**     | Ground         | Common ground for the module.                                               |
| **VCC**     | Supply Voltage | Operating voltage input (typically 5V to 18V).                              |
| **LIN**     | LIN Bus I/O    | Connection to the LIN bus for data transmission and reception.              |
| **EN**      | Enable         | Controls the transceiver's operating mode; high to enable normal operation. |
| **TXD**     | Transmit Data  | Input for data to be transmitted over the LIN bus.                          |
| **RXD**     | Receive Data   | Output for data received from the LIN bus.                                  |

<WarningBox>Ensure that **GND** is connected to the common ground of your system to establish a proper reference for signals.</WarningBox>

---

## Jumper Details (Qwiic version)

This board contains hardware jumpers. See below for their locations and functions:

<CenteredImage src="/img/ncv7329/jp1.png" alt="jp1" caption="JP1" width="600px"/>

| Jumper  | Default State            | Function                                                                                   |
| ------- | ------------------------ | ------------------------------------------------------------------------------------------ |
| **JP1** | **NC** (Normally closed) | Controls the **PWR LED**.                                                                    |

---

## Dimensions

- **Board Dimensions:** 21.3 × 22.6 × 12.3 mm (0.8 × 0.9 × 0.5 inches)
- **Header Pin Holes:** 1.5 mm  
- **Screw Holes:** Designed for M3 screws (3.2 mm diameter)  
- Soldered boards are LEGO compatible! 🧱

---

## Hardware Repository

Schematics, PCB layouts, and other design files are available in the GitHub repository:

<QuickLink 
  title="LIN Transceiver NCV7329 Breakout Hardware Design" 
  description="GitHub hardware repository for this product"
  url="https://github.com/SolderedElectronics/LIN-Transceiver-NCV7329-MASTER-breakout-hardware-design/tree/main"
  image="/img/ncv7329/333026.png" 
/>

The hardware repository contains everything you need to understand, modify, or manufacture the board. The various output folders are versioned. You can identify your board version by locating the version mark on the PCB.

Below is an overview of the available files.

#### CAD files

We use KiCad, an open-source PCB design tool. You can open and edit the `.kicad_pro` project file, which includes both the schematic and PCB layout.

The `PANEL` files are used internally for production.

#### Schematic

The **OUTPUTS** folder contains the schematic in `.pdf` format, exported from KiCad.

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