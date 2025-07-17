---
slug: /ad8495/hardware 
title: Hardware details
id: ad8495-hardware 
hide_title: False
---

## Pinout

<ErrorBox>The pinout image for this board has not been generated yet! We're working on it!</ErrorBox>

| Pin Marking | Pin Name | Description                             |
| ----------- | -------- | --------------------------------------- |
| **GND**     | Ground   | Common ground for power and signals.    |
| **VCC**     | Power    | Supply voltage.                         |
| **OUT**     | Data     | Output data pin.                        |

---

## Dimensions

- **Board Dimensions:** Under development.
- **Header Pin Holes:** 1.5 mm  
- **Screw Holes:** Designed for M3 screws (3.2 mm diameter)  
- Soldered boards are LEGO compatible! 🧱 

---

## Hardware repository

<QuickLink 
  title="Thermocouple sensor AD8495 breakout Hardware Design" 
  description="Hardware design, BOM, Gerbers, and 3D files for the Thermocouple-sensor-AD8495-breakout designed by Soldered Electronics."
  url="https://github.com/SolderedElectronics/Thermocouple-sensor-AD8495-breakout-hardware-design" 
/> 

The hardware repository contains everything you need to understand, modify, or manufacture the board. The different output folders are versioned. You can determine which board version you have by locating the version mark on the PCB.

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