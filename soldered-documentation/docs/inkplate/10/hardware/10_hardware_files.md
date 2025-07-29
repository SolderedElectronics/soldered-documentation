---
slug: /inkplate/10/hardware/open-source-files
title: Inkplate 10 – Hardware files
sidebar_label: Hardware files
id: 10-hardware-files
---

The **hardware repositories** for Inkplate 10 hardware files can be found on these links:

<QuickLink 
  title="Soldered Inkplate 10 hardware design" 
  description="Hardware design, BOM, gerbers and 3D files for Soldered Inkplate 10, designed by Soldered Electronics"
  url="https://github.com/SolderedElectronics/Soldered-Inkplate-10-hardware-design" 
/>

<QuickLink 
  title="E-Radionica Inkplate 10 hardware design" 
  description="Hardware design, BOM, gerbers and 3D files for E-Radionica Inkplate 10, designed by Soldered Electronics"
  url="https://github.com/SolderedElectronics/Inkplate-10-hardware" 
/>

## Repository contents  

The Inkplate 10 hardware repository contains everything you need to understand, modify, or manufacture the board. Below is an overview of the available files.  

### CAD files

We use [**KiCad**](https://www.kicad.org/), an open-source PCB design tool. You can open and edit the `.kicad_pro` project file, which includes both the schematic and PCB layout.  

The `PANEL` files are used internally for production.  

<CenteredImage src="/img/inkplate10/inkplate_10_cad_files.png" alt="Inkplate 10 KiCad project" caption="Inkplate 10 KiCad project" />

---

### Schematic

The **OUTPUTS** folder contains the **schematic** in `.pdf` format, exported from Kicad. The schematic is divided into sections based on functionality, making it easy to navigate.

<CenteredImage src="/img/inkplate10/inkplate_10_schematic0.png" alt="Inkplate 10 schematic" caption="Inkplate 10 schematic 1/6" />  
        

---

### BOM (Bill of Materials)

The bill of materials (BOM) is provided in two formats:  

- A **standard `.csv` table**, listing all components, part numbers, and values.  
- An **interactive BOM (`.html`)** that visually highlights each component on the PCB, making it easy to locate and reference parts.  

<CenteredImage src="/img/inkplate10/inkplate_10_ibom.png" alt="Inkplate 10 interactive BOM" caption="IBOM for 10" />

---

### 3D files

A **3D model** of the PCB is available in `.step` format, allowing you to inspect the board design in CAD software.

---

### Gerber files 

Gerber files are essential for PCB manufacturing, as they contain precise instructions for each layer of the board. The repository includes standard Gerber outputs in a .zip file, such as:  

- **Copper layers** (`.Cu.gbr`) – Defines the traces and pads on the board.  
- **Solder mask layers** (`.Mask.gbr`) – Specifies the protective solder mask.  
- **Silkscreen layers** (`.Silkscreen.gbr`) – Contains text and component markings.  
- **Paste layers** (`.Paste.gbr`) – Used for stencil fabrication in SMD assembly.  
- **Drill files** (`.drl`) – Provides drilling coordinates for vias and holes.  
- **Board outline** (`.Edge_Cuts.gbr`) – Defines the shape of the PCB.  
- **Gerber job file** (`.gbrjob`) – Describes the set of Gerber files used for production.  

These files are ready for fabrication and can be used in PCB manufacturing.  