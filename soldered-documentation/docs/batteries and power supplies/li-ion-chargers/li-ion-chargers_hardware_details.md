---
slug: /li-ion-chargers/hardware-details 
title: Li-ion Charger - Hardware details
sidebar_label: Hardware details
id: li-ion-chargers-hardware
hide_title: false
---

## Pinout

<CenteredImage src="/img/chargers/pinout1.png" alt="Li-ion charger pinout" caption="Li-ion Battery Charger pinout diagram"/>

<CenteredImage src="/img/chargers/pinout2.png" alt="Li-ion charger pinout" caption="Li-ion Battery Charger with protection pinout diagram"/>

## Pin Details

| Pin Marking | Pin Name  | Description                                                     |
| ----------- | --------- | --------------------------------------------------------------- |
| **VCC**     | Power In  | Connect to 5V USB-C power input.                                |
| **GND**     | Ground    | Common ground.                                                  |
| **BAT+**    | Battery + | Connect to the positive terminal of a single-cell Li-ion cell.  |
| **BAT-**    | Battery - | Connect to the negative terminal of the battery.              |

<InfoBox>In addition, the Li-ion Battery Charger with protection board has these pins.</InfoBox>

| Pin Marking | Pin Name  | Description                                                     |
| ----------- | --------- | --------------------------------------------------------------- |
| **OUT+**    | Output +  | Regulated output voltage (same as battery voltage).             |
| **OUT-**    | Output -  | Output ground.                                                  |

<InfoBox>These boards are designed for 3.7V Li-ion or Li-Po single-cell batteries.</InfoBox>

---

## Dimensions

- **Board Dimensions:** 25 × 19 mm (0.98 × 0.75 inch)
- **USB Connector:** USB-C female
- **Mounting holes:** None (breadboard-compatible)

---

## LEDs

| LED Name | Color | Meaning                  |
| -------- | ----- | ------------------------ |
| **CHRG** | Red   | Charging in progress     |
| **FULL** | Blue  | Battery fully charged    |

---

## Hardware repository

The hardware design files for these modules are available on GitHub:

<QuickLink 
  title="Li-ion Charger Hardware Repository" 
  description="Schematics and PCB layout for the charger module"
  url="https://github.com/SolderedElectronics/Li-ion-charger-hardware-design" 
/>

<QuickLink 
  title="Li-ion Charger with Protection Hardware Repository" 
  description="Schematics and PCB layout for the charger module"
  url="https://github.com/SolderedElectronics/Li-ion-charger-with-protection-hardware-design" 
/>

The hardware repository contains everything you need to understand, modify, or manufacture the board. The various output folders are versioned. You can check which board version you have specifically by finding the version mark on the PCB.

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
- **Safety Instructions** – Safety guidelines and precautions are provided in English and German.
- **Info.txt** – Contains product details such as SKU, country of origin, HS tariff code, and barcode.