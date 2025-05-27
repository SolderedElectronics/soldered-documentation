---
slug: /obstacle-sensor/hardware
title: "Obstacle Sensor \u2013 Hardware details"
id: obstacle-sensor-hardware
hide_title: false
---
## Pinout
<CenteredImage src="/img/obstacle-sensor/333004_pinout.jpg" alt="Pinout" />
Click [**here**](/img/obstacle-sensor/333004_pinout.jpg) for a high resolution image of the pinout.

---

## Pin details

Connection is achived with Qwiic connector.

<InfoBox> This board also contains UPDI headers for preprogramming the onboard ATTINY404, they are used only for debugging purposes. </InfoBox>

---

## Qwiic (formerly easyC)  

<CenteredImage src="/img/easyc_transparent.png" alt="EasyC/qwiic cable" width="550px" />
 
<InfoBox> This board has **Qwiic-compatible** version! Just plug it into your board using a **Qwiic/easyC/STEMMA QT cable** and start coding! </InfoBox>

<QuickLink 
  title="Qwiic (formerly easyC) details and specifications" 
  description="Learn about hardware specifications, compatibility, and usage of the Qwiic connector." 
  url="/qwiic" 
/>

---

## Dimensions

- **Board Dimensions:** 38 × 22 mm (1.5 × 0.9 inch)  
- **Header Pin Holes:** 1.5 mm  
- **Screw Holes:** Designed for M3 screws (3.2 mm diameter)  
- Soldered boards are LEGO compatible! 🧱 

---

## Address selection

This board contains hardware address switches, see below how to change breakout board's address.

<CenteredImage src="/img/obstacle-sensor/333004_add_highlighted.jpg" alt="Address selection" />

| Address | SW3 | SW2 | SW1 |
|:---:|:---:|:---:|:---:|
| 0x30 | 0 | 0 | 0 |
| 0x31 | 0 | 0 | 1 |
| 0x32 | 0 | 1 | 0 |
| 0x33 | 0 | 1 | 1 |
| 0x34 | 1 | 0 | 0 |
| 0x35 | 1 | 0 | 1 |
| 0x36 | 1 | 1 | 0 |
| 0x37 | 1 | 1 | 1 |                  

---

## Hardware repository

Schematics, KiCad files, Gerber files and more can be found in the GitHub repository:

<QuickLink 
  title="Obstacle sensor qwiic Hardware Design" 
  description="Hardware design, BOM, gerbers and 3D files for Obstacle-sensor-qwiic designed by Soldered Electronics."
  url="https://github.com/SolderedElectronics/Obstacle-sensor-qwiic-hardware-design" 
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
