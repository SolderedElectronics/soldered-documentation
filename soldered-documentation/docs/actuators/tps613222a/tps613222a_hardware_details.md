---
slug: /tps613222a/hardware
title: TPS61322A - Hardware details
id: tps613222a-hardware
sidebar_label: Hardware details
hide_title: false
---

## Pinout

<CenteredImage src="/img/tps613222a/pinout.png" alt="TPS613222A boost converter pinout diagram" caption="TPS613222A boost converter pinout diagram"/>

| Pin Marking | Pin Name  | Description                        |
|-------------|-----------|------------------------------------|
| **3V3**    | Positive  | Positive terminal for 3.3V         |
| **GND**    | Negative  | Negative terminal for 3.3V         |
| **5V**     | Positive  | Positive terminal for 5V           |
| **GND**    | Negative  | Negative terminal for 5V           |

---

## Dimensions

- **Board Dimensions:** 38 × 22 mm (1.5 × 0.9 inch)  
- **Header Pin Holes:** 1.5 mm  
- **Screw Holes:** Designed for M3 screws (3.2 mm diameter)  
- Soldered boards are LEGO compatible! 🧱 

---

## Jumper Details

This board contains hardware jumpers; see below for their locations and functions:

<CenteredImage src="/img/tps613222a/jp1_highlighted.png" alt="jp1" caption="JP1" width="600px"/>

| Jumper  | Default State            | Function          |
|---------|--------------------------|-------------------|
| **JP1** | **NC** (Normally closed) | Connects PWR LED. |

---

## Hardware repository

Schematics, KiCad files, Gerber files, and more can be found in the GitHub repository:

<QuickLink 
  title="Mini low-power TPS613222A boost converter Hardware design" 
  description="GitHub hardware repository for this product"
  url="https://github.com/SolderedElectronics/Mini-low-power-TPS613222A-boost-converter-hardware-design" 
/> 

The hardware repository contains everything you need to understand, modify, or manufacture the board. The output folders are versioned. You can check your board version by locating the version mark on the PCB.

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

The **Compliance** section contains important regulatory and safety documentation for this product. These files ensure compliance with relevant industry standards and legal requirements.

- **CE** – Certification document confirming compliance with EU safety, health, and environmental requirements.  
- **UKCA** – UKCA (UK Conformity Assessed) certification for the UK market.  
- **Safety Instructions** – Safety guidelines and precautions are provided in English and German.  
- **Info.txt** – Contains product details such as SKU, country of origin, HS tariff code, and barcode.