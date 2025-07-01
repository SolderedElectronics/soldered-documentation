---
slug: /mcp2518/hardware 
title: CAN Transciever MCP2518 - Hardware details
id: mcp2518-hardware 
hide_title: False
sidebar_label: Hardware details
---

## Pinout

<CenteredImage src="/img/mcp2518/pinout.png" alt="LIN Transceiver NCV7329 Breakout pinout diagram" caption="LIN Transceiver NCV7329 Breakout pinout diagram"/>

## Pin Details

| PIn Marking 	| Pin Name 	| Description 	|
|---	|---	|---	|
| **NCS** 	| Chip Select 	| SPI chip select input 	|
| **SDI** 	| Data input 	| SPI data input 	|
| **SDO** 	| Data output 	| SPI data output 	|
| **SCK** 	| Clock input 	| SPI clock input 	|
| **GND** 	| Ground 	| Common ground for the module 	|
| **VCC**  	| Supply voltage 	| Operating voltage input 	|
| **INT1** 	| Interrupt 	| RX interrupt output(active low) 	|
| **INT0** 	| Interrupt 	| TX interrupt output(active low) 	|
| **INT** 	| Interrupt 	| Interrupt output (active low) 	|
| **CLKO** 	| Clock output 	| Clock output/Start of frame output 	|

---

## Jumper Details

This board contains hardware jumpers See below for their locations and functions:

<FlickityCarousel
  images={[
    { src: '/img/mcp2518/jp1.png', alt: 'mcp2518-jp1', caption: 'JP1' },
    { src: '/img/mcp2518/jp2.png', alt: 'mcp2518-jp2', caption: 'JP2' },
  ]}
  jumpers={true}
/>

| Jumper 	| Default State 	| Function 	|
|---	|---	|---	|
| **JP1** 	| **NO** (Normally open) 	| When closed it adds Termination Resistor 	|
| **JP2** 	| **NC** (Normally closed) 	| Connect/Disconnect PWR LED 	|

---

## Hardware repository

Schematics, KiCad files, Gerber files, and more can be found in the GitHub repository:

<QuickLink 
  title="CAN Transceiver MCP2518 board Hardware Design" 
  description="Hardware design, BOM, gerbers and 3D files for CAN-Transceiver-MCP2518-board designed by Soldered Electronics."
  url="https://github.com/SolderedElectronics/CAN-Transceiver-MCP2518-board-hardware-design" 
/> 

The hardware repository contains everything you need to understand, modify, or manufacture the board. The different output folders are versioned. You can check which board version you have by finding the version mark on the PCB.

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
- **Safety Instructions** – Safety guidelines and precautions in English and in German.  
- **Info.txt** – Contains product details such as SKU, country of origin, HS tariff code, and barcode.