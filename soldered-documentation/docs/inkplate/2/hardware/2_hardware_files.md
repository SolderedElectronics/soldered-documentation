---  
slug: /inkplate/2/hardware/open-source-files  
title: Inkplate 2 – Hardware files
id: 2-hardware-files  
hide_title: true  
---  

<SectionTitle title="Hardware Files" backgroundImage="/img/inkplate_2/hardware.png" />

<QuickLink 
  title="Soldered Inkplate 2 hardware design" 
  description="Hardware design, BOM, Gerber files, and 3D files for Soldered Inkplate 2, designed by Soldered Electronics"
  url="https://github.com/SolderedElectronics/Soldered-Inkplate-2-hardware-design" 
/>

## Repository contents  

The Inkplate 2 hardware repository contains everything you need to understand, modify, or manufacture the board. Below is an overview of the available files.

### CAD files

We use [**KiCad**](https://www.kicad.org/), an open-source PCB design tool. You can open and edit the `.kicad_pro` project file, which includes both the schematic and PCB layout.

The `PANEL` files are used internally for production.

<CenteredImage src="/img/inkplate_2/kicad.png" alt="Inkplate 2 KiCad project" caption="Inkplate 2 KiCad project" />

---

### Schematic

The **OUTPUTS** folder contains the **schematic** in `.pdf` format, exported from KiCad. The schematic is divided into sections based on functionality, making it easy to navigate.

<CenteredImage src="/img/inkplate_2/schematic.png" alt="Inkplate 2 schematic" caption="Inkplate 2 schematic 2/6" />

---

### BOM (Bill of Materials)

The bill of materials (BOM) is provided in two formats:

- A **standard `.csv` table**, listing all components, part numbers, and values.
- An **interactive BOM (`.html`)** that visually highlights each component on the PCB, making it easy to locate and reference parts.

<CenteredImage src="/img/inkplate_2/ibom.png" alt="Inkplate 2 interactive BOM" caption="IBOM for Inkplate 2" />

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