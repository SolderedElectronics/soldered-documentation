---
slug: /battery-protection/hardware 
title: Hardware details
id: battery-protection-hardware 
hide_title: False
---

## Pinout

<CenteredImage src="/img/battery-protection/pinout.png" alt="bp pinout diagram" caption="1S Li-Ion Battery Protection pinout diagram"/>

## Pin Details

| Pin Marking | Pin Name  | Description                                              |
| ----------- | --------- | -------------------------------------------------------- |
| **GND**     | Ground    | Common ground for the battery circuit.                   |
| **VBAT**    | Battery   | Main voltage input from the battery (positive terminal). |
| **BAT-**    | Negative  | Battery negative terminal (connected to the negative pole). |
| **BAT+**    | Positive  | Battery positive terminal (connected to the positive pole). |

<WarningBox>Ensure that **GND** is connected to both the high and low voltage grounds to establish a common reference for signals.</WarningBox>

<WarningBox>Do not short the **BAT+** and **BAT-** pins. Short-circuiting these pins can cause overheating, damage to the protection circuit, or battery failure.</WarningBox>

---

## FS8205A MOSFET

The **FS8205A** is a dual N-channel MOSFET commonly used in battery protection circuits for efficient switching and low power loss.

<CenteredImage src="/img/battery-protection/mosfet.png" alt="bp pinout diagram" caption="FS8205A MOSFET on the Battery Protection Board" width="600px"/>

The FS8205A has a **low on-resistance** of 25mΩ (max) at V_GS = 4.5V, which ensures minimal power dissipation during operation. It also has a **drain-source voltage (V_DSS)** rating of 20V, making it suitable for typical lithium battery voltage levels. With a **continuous drain current (I_D)** of 6A, it provides sufficient current handling for most battery protection applications. The MOSFET is packaged in an **SOT-23-6**, a compact, space-efficient surface-mount package.

In battery protection systems, the FS8205A is used in the charge and discharge paths. It ensures safe operation by preventing overcurrent and short-circuit conditions, helping to protect the battery and associated circuits.

The FS8205A operates with a **junction temperature range** of -55°C to 150°C, making it suitable for a wide range of operating conditions. Its **gate threshold voltage (V_GS(th))** is around 1V, which allows for efficient switching with low gate drive voltages, contributing to the overall energy efficiency of the system.

---

## Dimensions

- **Board Dimensions:** 22 × 22 mm (0.9 × 0.9 inch)  
- **Header Pin Holes:** 1.5 mm  
- **Screw Holes:** Designed for M3 screws (3.2 mm diameter)  
- Soldered boards are LEGO compatible! 🧱 

---

## Jumper Details

This board contains hardware jumpers, see below for their locations and functions:

<CenteredImage src="/img/battery-protection/jp1.png" alt="jp1" caption="JP1" width="600px"/>

| Jumper  | Default State            | Function                      |
| ------- | ------------------------ | ----------------------------- |
| **JP1** | **NC** (Normally closed) | Connects PWR LED.             |

---

## Hardware repository

Schematics, KiCad files, Gerber files and more can be found in the GitHub repository:

<QuickLink 
  title="1S Li-Ion Battery Protection Hardware Design" 
  description="GitHub hardware repository for this product"
  url="https://github.com/SolderedElectronics/1S-Li-Ion-battery-protection-hardware-design/tree/main" 
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
