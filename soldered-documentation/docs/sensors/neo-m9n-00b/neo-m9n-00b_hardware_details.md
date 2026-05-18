---
slug: /neo-m9n-00b/hardware 
title: Hardware details
id: neo-m9n-00b-hardware 
hide_title: False
---

## Pinout

<CenteredImage src="/img/neo-m9n-00b/NEO-M9N-00_Pinout.png" alt="NEO-M9N-00B pinout diagram" caption="NEO-M9N-00B pinout diagram"/>

Click [**here**](/img/neo-m9n-00b/NEO-M9N-00_Pinout.png) for a high resolution image of the pinout.

---

## Pin Details

| Pin Marking | Pin Name | Description |
| ----------- | -------- | ----------- |
| **GND** | Ground | Common ground reference for the module. |
| **VCC** | Power | Main power input for the board. |
| **3V3** | Power | 3.3V regulated power output/input. |
| **SDA** | Data | I2C serial data line. |
| **SCL** | Clock | I2C serial clock line. |
| **TX** | UART TX | UART transmit pin for sending serial data. |
| **RX** | UART RX | UART receive pin for receiving serial data. |
| **RESET** | Control | Resets the GNSS module. |
| **INT** | Interrupt | Interrupt output pin for event notifications. |
| **PPS** | Timing | Pulse-per-second timing output for precise synchronization applications. |
| **SAFEBOOT** | Control | Forces the module into safe boot mode for firmware recovery or updates. |

<InfoBox>This breakout board operates at **3.3V logic level** and includes onboard power regulation for compatibility with both **3.3V and 5V systems**.</InfoBox>

---

## Qwiic (formerly easyC)

<CenteredImage src="/img/easyc_transparent.png" alt="EasyC/qwiic cable" width="550px" />

<InfoBox>This board is fully **Qwiic-compatible**! Just plug it into your board using a **Qwiic/easyC/STEMMA QT cable** and start coding!</InfoBox>

<QuickLink 
  title="Qwiic (formerly easyC) details and specifications" 
  description="Learn about hardware specifications, compatibility, and usage of the Qwiic connector." 
  url="/qwiic" 
/>

---

## Power Consumption

- **Backup mode:** Ultra-low power operation for maintaining GNSS data and RTC functionality.
- **Active tracking mode:** Power consumption depends on enabled GNSS constellations and update rate settings.

<InfoBox>For lower power consumption, reduce the navigation update rate and disable unused GNSS constellations when possible.</InfoBox>

---


## Dimensions

- **Board Dimensions:** 38 × 54 mm (1.5 × 2.1 inch)
- **Header Pin Holes:** 1.5 mm
- **Screw Holes:** Designed for M3 screws (3.2 mm diameter)
- Soldered boards are LEGO compatible! 🧱

---

## Jumper Details

This board contains hardware jumpers; see below for their locations and functions:

| Jumper | Default State | Function |
| ------- | ------------------------ | -------- |
| **JP1** | **NO** (Normally open) | Enables the onboard power LED when shorted. |
| **JP2** | **NC** (Normally closed) | Connects SDA/SCL pull-up resistors to 3.3V for I2C communication. |
| **JP3** | **NO** (Normally open) | Enables the PPS status LED when shorted. |
| **JP4** | **NC** (Normally closed) | Sets the D_SEL pin to its default configuration state. |
| **JP5** | **NC** (Normally closed) | Connects the backup battery circuit to the GNSS module. |

---

## Hardware repository

Schematics, KiCad files, Gerber files and more can be found in the GitHub repository:



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
- **Safety Instructions** – Safety guidelines and precautions in English and in German.
- **Info.txt** – Contains product details such as SKU, country of origin, HS tariff code, and barcode.