---
slug: /rs-232/hardware
title: Rs 232 - Hardware details
sidebar_label: Hardware details
id: rs-232-hardware
hide_title: false
---

## Pinout

<CenteredImage src="/img/rs-232/pinout.jpg" alt="RS-232 transceiver pinout diagram" caption="RS-232 transceiver pinout diagram"/>

Click [**here**](/img/rs-232/pinout.jpg) for a high-resolution image of the pinout.

---

## Pin Details

| **Pin Marking** | **Pin Name**   | **Description**                                                                 |
|-----------------|----------------|---------------------------------------------------------------------------------|
| **ROUT2**       | RS-232 Receive | Receives data from the RS-232 device (Channel 2).                               |
| **DIN2**        | TTL Transmit   | Sends data from the microcontroller to the RS-232 device (Channel 2).           |
| **ROUT1**       | RS-232 Receive | Receives data from the RS-232 device (Channel 1).                               |
| **DIN1**        | TTL Transmit   | Sends data from the microcontroller to the RS-232 device (Channel 1).           |
| **5V**          | Supply Voltage | Power input for the board (3.3V to 5.5V).                                       |
| **GND**         | Ground         | Common ground for both RS-232 and TTL/CMOS sides.                               |

<InfoBox> 
- **VCC Range**: 3.3V - 5.5V 
- **RS-232 Voltage Levels**: ±3V to ±15V 
</InfoBox>

<WarningBox>Ensure that GND is connected between both the RS-232 device and TTL/CMOS device to establish a common reference for signals.</WarningBox>

---

## Jumper Details

This board contains a hardware jumper; see below for its location and function:

<CenteredImage src="/img/rs-232/JP1.png" alt="RS-232 jumper 1" caption="JP1"/>

| Jumper  | Default State            | Function                                                                                                      |
| ------- | ------------------------ | ------------------------------------------------------------------------------------------------------------- |
| **JP1** | **NC** (Normally closed) | Controls the power LED by **connecting** or **disconnecting** it from the **5V** power supply.                |

---

## Dimensions

- **Board Dimensions:** 22 × 22 mm (0.9 × 0.9 inch)  
- **Header Pin Holes:** 1.5 mm  
- **Screw Holes:** Designed for M3 screws (3.2 mm diameter)  
- Soldered boards are LEGO-compatible! 🧱 

---

## Hardware repository

Schematics, KiCad files, Gerber files, and more can be found in the GitHub repository:

<QuickLink 
  title="RS-232 transceiver board Hardware design" 
  description="GitHub hardware repository for this product"
  url="https://github.com/SolderedElectronics/RS-232-Transceiver-breakout-hardware-design" 
/> 

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