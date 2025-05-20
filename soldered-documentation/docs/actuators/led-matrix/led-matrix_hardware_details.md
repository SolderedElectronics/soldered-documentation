---
slug: /led-matrix/hardware
title: Hardware - Hardware details
id: led-matrix-hardware
hide_title: false
---

## Pinout

<CenteredImage src="/img/led-matrix/led-matrix_pinout.jpg" alt="Pinout" />
Click [**here**](/img/led-matrix/led-matrix_pinout.jpg) for a high resolution image of the pinout.

---

## Pin details

| Pin Marking | Pin Name | Description                                     |
| ----------- | -------- | ----------------------------------------------- |
| **VCC**     | Power    | 5V Supply voltage. |
| **GND**     | Ground   | Common ground for power and signals.            |
| **DOUT**     | Data     | Serial-Data Output. |
| **LOAD**     | Data     | Load-Data Input. |
| **DIN**     | Data     | Serial-Data input. |
| **CLK**     | Data     | Serial-Clock Input. |

---

## Dimensions

- **Board Dimensions:** 54 x 22 mm (2.1 x 0.9 inch)  
- **Header Pin Holes:** 1.5 mm  
- **Screw Holes:** Designed for M3 screws (3.2 mm diameter)  
- Soldered boards are LEGO compatible! 🧱 

---

## Hardware repository

Schematics, KiCad files, Gerber files and more can be found in the GitHub repository:

<QuickLink 
  title="8x8-LED-matrix-Blue-MAX7219-board-hardware-design" 
  description="Hardware design, BOM, gerbers and 3D files for 8x8-LED-matrix-Blue-MAX7219-board designed by Soldered Electronics."
  url="https://github.com/SolderedElectronics/8x8-LED-matrix-Blue-MAX7219-board-hardware-design" 
/>  

<QuickLink 
  title="8x8-LED-matrix-White-MAX7219-board-hardware-design" 
  description="Hardware design, BOM, gerbers and 3D files for 8x8-LED-matrix-White-MAX7219-board designed by Soldered Electronics."
  url="https://github.com/SolderedElectronics/8x8-LED-matrix-White-MAX7219-board-hardware-design" 
/> 

<QuickLink 
  title="8x8-LED-matrix-Red-MAX7219-board-hardware-design" 
  description="Hardware design, BOM, gerbers and 3D files for 8x8-LED-matrix-Red-MAX7219-board designed by Soldered Electronics."
  url="https://github.com/SolderedElectronics/8x8-LED-matrix-Red-MAX7219-board-hardware-design" 
/>

<QuickLink 
  title="8x8-LED-matrix-Purple-MAX7219-board-hardware-design" 
  description="Hardware design, BOM, gerbers and 3D files for 8x8-LED-matrix-Purple-MAX7219-board designed by Soldered Electronics."
  url="https://github.com/SolderedElectronics/8x8-LED-matrix-Purple-MAX7219-board-hardware-design" 
/>

<QuickLink 
  title="8x8-LED-matrix-Orange-MAX7219-board-hardware-design" 
  description="Hardware design, BOM, gerbers and 3D files for 8x8-LED-matrix-Orange-MAX7219-board designed by Soldered Electronics."
  url="https://github.com/SolderedElectronics/8x8-LED-matrix-Orange-MAX7219-board-hardware-design" 
/>

<QuickLink 
  title="8x8-LED-matrix-Green-MAX7219-board-hardware-design" 
  description="Hardware design, BOM, gerbers and 3D files for 8x8-LED-matrix-Green-MAX7219-board designed by Soldered Electronics."
  url="https://github.com/SolderedElectronics/8x8-LED-matrix-Green-MAX7219-board-hardware-design" 
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
