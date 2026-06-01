---
slug: /breadboard-power-supply-board/hardware
title: Hardware details
id: breadboard-power-supply-board-hardware
hide_title: false
---

<CenteredImage src="/img/breadboard power supply board/Pinout.png" alt="Breadboard power supply board pinout" />

Click [**here**](/img/breadboard%20power%20supply%20board/Pinout.png) for a high-resolution image of the pinout.

| Pin Marking | Pin Name | Description                                     |
| ----------- | -------- | ----------------------------------------------- |
| **GND**     | Ground   | Common ground for power            |
| **VOUT1**   | Voltage output   | Output voltage (can be 12V or 3V3)    |
| **VOUT2**   | Voltage output   | Output voltage (can be 5V or 3V3)     |

---

## Jumper details

JP1 controls the onboard power LED:

<InfoBox>Image coming soon.</InfoBox>

| Jumper  | Default State            | Function                                                                                          |
| ------- | ------------------------ | ------------------------------------------------------------------------------------------------- |
| **JP1** | **NC** (Normally closed) | When shorted, it provides power to the onboard power LED                              |

---

## Switch details

S1, S2, and S3 control power and output voltage:

<InfoBox>Images coming soon.</InfoBox>

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

- **Copper layers** (`.Cu.gbr`): Defines the traces and pads on the board.  
- **Solder mask layers** (`.Mask.gbr`): Specifies the protective solder mask.  
- **Silkscreen layers** (`.Silkscreen.gbr`): Contains text and component markings.  
- **Paste layers** (`.Paste.gbr`): Used for stencil fabrication in SMD assembly.  
- **Drill files** (`.drl`): Provides drilling coordinates for vias and holes.  
- **Board outline** (`.Edge_Cuts.gbr`): Defines the shape of the PCB.  
- **Gerber job file** (`.gbrjob`): Describes the set of Gerber files used for production.  


#### Compliance  

Regulatory and safety documents for this product:

- **CE**: Certification document confirming compliance with EU safety, health, and environmental requirements.  
- **UKCA**: UKCA (UK Conformity Assessed) certification for the UK market.  
- **Safety Instructions**: Safety guidelines and precautions in English and in German.
- **Info.txt**: Contains product details such as SKU, country of origin, HS tariff code, and barcode.
