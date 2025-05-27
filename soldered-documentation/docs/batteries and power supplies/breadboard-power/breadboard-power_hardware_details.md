---
slug: /breadboard-power/hardware
title: "Breadboard Power \u2013 Hardware details"
id: breadboard-power-hardware
hide_title: false
---
<CenteredImage src="/img/breadboard-power/pinout.png" alt="Pinout" />

Click [**here**](/img/breadboard-power/pinout.png) for a high-resolution image of the pinout.

| Pin Marking | Pin Name | Description                                     |
| ----------- | -------- | ----------------------------------------------- |
| **GND**     | Ground   | Common ground for power            |
| **VOUT1**   | Voltage output   | Output voltage (can be 12V or 3V3)    |
| **VOUT2**   | Voltage output   | Output voltage (can be 5V or 3V3)     |

---

## Jumper Details

This board contains a hardware jumper; see below for its location and function:

<CenteredImage src="/img/breadboard-power/jp1.webp" alt="Breadboard power jumper location" width="550px" />

| Jumper  | Default State            | Function                                                                                          |
| ------- | ------------------------ | ------------------------------------------------------------------------------------------------- |
| **JP1** | **NC** (Normally closed) | When shorted, it provides power to the onboard power LED                              |

---

## Switch Details

This board contains switches that control the voltage output; see below for their locations and functions:

<FlickityCarousel
  images={[
    { src: '/img/breadboard-power/S1.webp', alt: 'Breadboard power supply switch 1', caption: 'S1' },
    { src: '/img/breadboard-power/S2.webp', alt: 'Breadboard power supply switch 2', caption: 'S2' },
    { src: '/img/breadboard-power/S3.webp', alt: 'Breadboard power supply switch 3', caption: 'S3' },
  ]}
  jumpers={true}
/>

| Switch  | Function                                    |
| ------- | ------------------------------------------- |
| **S1**  | Switches power to the board on or off          |
| **S2**  | Switches between a 12V or 3V3 output on VOUT1 pin |
| **S3**  | Switches between a 5V or 3V3 output on VOUT2 pin |

---

## Dimensions

- **Board Dimensions:** 54 x 30mm (2.1 x 1.2 inches)
- **Header Pin Holes:** 1.5 mm
- **Screw Holes:** Designed for M3 screws (3.2 mm diameter)
- Soldered boards are LEGO compatible! 🧱

---

## Hardware repository

Schematics, KiCad files, Gerber files, and more can be found in the GitHub repository:

<QuickLink 
  title="Breadboard power supply board Hardware Design" 
  description="GitHub hardware repository for this product"
  url="https://github.com/SolderedElectronics/Breadboard-power-supply-board-hardware-design" 
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