---
slug: /inputronic-grid/hardware 
title: Hardware details
id: inputronic-grid-hardware 
hide_title: False
---
## Pinout


<CenteredImage
  src="/img/inputronic-grid/pinout.png"
  alt="Pinout"
/>


---

## Pin Details

| Pin Marking | Pin Name        | Description                                                               |
| ----------- | --------------- | ------------------------------------------------------------------------- |
| **3V3**     | Debug Power     | 3.3V power supply for debugging purposes.                                 |
| **UPDI**    | Debug Interface | Used for debugging and programming the onboard ATTiny404 microcontroller. |
| **GND**     | Debug Ground    | Ground pin for debugging purposes.                                        |

---

## Power Consumption
The power consumption of the Inputronic GRID depends heavily on the state and brightness of the 16 onboard RGB LEDs. The board operates on a **3.3V** supply. 
 
When all 16 RGB LEDs are turned on at full brightness (pure white) and the microcontroller is actively scanning:
- **16x WS2812B-2020 LEDs:** ~160mA (approx. 10mA per LED)
- **ATtiny404 Microcontroller:** ~5mA
- **Total Current:** **~165mA**
---
## Dimensions

- **Board Dimensions:** **60mm x 60mm** (2.36 x 2.36 inch)
- **Header Pin Holes:** 1.5 mm

---
## Hardware repository

Schematics, KiCad files, Gerber files, and more can be found in the GitHub repository:

<ErrorBox>The link for this repository has not been generated yet! We're working on it!</ErrorBox>

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

- **Copper layers** (`.Cu.gbr`) - Defines the traces and pads on the board.  
- **Solder mask layers** (`.Mask.gbr`) - Specifies the protective solder mask.  
- **Silkscreen layers** (`.Silkscreen.gbr`) - Contains text and component markings.  
- **Paste layers** (`.Paste.gbr`) - Used for stencil fabrication in SMD assembly.  
- **Drill files** (`.drl`) - Provides drilling coordinates for vias and holes.  
- **Board outline** (`.Edge_Cuts.gbr`) - Defines the shape of the PCB.  
- **Gerber job file** (`.gbrjob`) - Describes the set of Gerber files used for production.  

These files are ready for fabrication and can be used in PCB manufacturing.

#### Compliance

The **Compliance** section includes important regulatory and safety documentation for this product. These files ensure compliance with relevant industry standards and legal requirements.

- **CE** - Certification document confirming compliance with EU safety, health, and environmental requirements.  
- **UKCA** - UKCA (UK Conformity Assessed) certification for the UK market.  
- **Safety Instructions** - Safety guidelines and precautions in English and in German.  
- **Info.txt** - Contains product details such as SKU, country of origin, HS tariff code, and barcode.