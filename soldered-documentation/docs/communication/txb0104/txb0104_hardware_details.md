---
slug: /txb0104/hardware 
title: Hardware details
id: txb0104-hardware 
hide_title: False
---

## Pinout

<CenteredImage src="/img/txb0104/pinout.png" alt="Logic Level Converter pinout diagram" caption="Logic Level Converter TXB0104 pinout diagram"/>

Click [**here**](/img/txb0104/pinout.png) for a high reoslution image of the pinout.

## Pin Details

| Pin Marking | Pin Name           | Description                                                                                       |
| ----------- | ------------------ | ------------------------------------------------------------------------------------------------- |
| **GND**     | Ground             | Common ground for both high and low voltage sides.                                                |
| **VCCH**    | High Voltage Power | Supply voltage for the high-voltage side (typically 5V).                                          |
| **VCCL**    | Low Voltage Power  | Supply voltage for the low-voltage side (typically 3.3V).                                         |
| **B1 - B4** | High Voltage Pins  | High-voltage side signal pins (typically 5V logic).                                               |
| **A1 - A4** | Low Voltage Pins   | Low-voltage side signal pins (typically 3.3V logic).                                              |
| **OE**      | Output Enable Pin  | Enables or disables output, switching between active (HIGH/LOW) and high-impedance (Hi-Z) states. |

<InfoBox>
- VCCH: 2.3V - 5V
- VCCL: 1.65V - 3.6V 
</InfoBox>

<WarningBox>**VCCL must be lower than VCCH!**</WarningBox>

<WarningBox>Ensure that **GND** is connected to both the high and low voltage grounds to establish a common reference for signals.</WarningBox>

---

## Dimensions

- **Board Dimensions:** 22 × 22 mm (0.9 × 0.9 inch)  
- **Header Pin Holes:** 1.5 mm  
- **Screw Holes:** Designed for M3 screws (3.2 mm diameter)  
- Soldered boards are LEGO compatible! 🧱 

---

## Hardware repository

Schematics, KiCad files, Gerber files and more can be found in the GitHub repository:

<QuickLink 
  title="Logic Level Converter TXB0104 board Hardware design" 
  description="GitHub hardware repository for this product"
  url="https://github.com/SolderedElectronics/Logic-level-converter-generic-TXB0104-breakout-hardware-design" 
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
- **Safety Instructions** – Safety guidelines and precautions in English and in German.
- **Info.txt** – Contains product details such as SKU, country of origin, HS tariff code, and barcode.  
