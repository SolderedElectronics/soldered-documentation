---
slug: /slider-potentiometer/hardware 
title: Hardware details
id: slider-potentiometer-hardware 
hide_title: False
---

## Pinout

<ErrorBox>The pinout image for this board hasn't been generated yet! We're working on it!</ErrorBox>

## Pin details

| Pin Name | Description       | Notes                           |
|----------|-------------------|---------------------------------|
| OUTA     | Analog Output A   | Outputs analog signal (side A). |
| VCCA     | Power Supply A    | Connect to 5V for side A.       |
| GND      | Ground            | Common ground for both sides.   |
| OUTB     | Analog Output B   | Outputs analog signal (side B). |
| VCCB     | Power Supply B    | Connect to 5V for side B.       |


---

## Qwiic (formerly easyC)  

<CenteredImage src="/img/easyc_transparent.png" alt="EasyC/qwiic cable" width="550px" />
 
<InfoBox> This board is fully **Qwiic-compatible**! Just plug it into your board using a **Qwiic/easyC/STEMMA QT cable** and start coding! </InfoBox>

<QuickLink 
  title="Qwiic (formerly easyC) details and specifications" 
  description="Learn about hardware specifications, compatibility, and usage of the Qwiic connector." 
  url="/qwiic" 
/>

---

## Pin details for Qwiic version

For the Qwiic version, connection is achieved with the Qwiic connector.

<InfoBox>Qwiic versions also contain UPDI headers for onboard ATTINY404 programming. They will not be used in the following examples.</InfoBox>

<a id="addressSelection"></a>
## Address selection for Qwiic version 

The board contains hardware address switches. See below for instructions on how to change the breakout board's address.

<CenteredImage src="/img/slider-potentiometer/333131addr.jpg" alt="ADDR" width="550px" />

### Address Table

| Address | SW3 | SW2 | SW1 |
|---------|-----|-----|-----|
| 0x30    | 0   | 0   | 0   |
| 0x31    | 0   | 0   | 1   |
| 0x32    | 0   | 1   | 0   |
| 0x33    | 0   | 1   | 1   |
| 0x34    | 1   | 0   | 0   |
| 0x35    | 1   | 0   | 1   |
| 0x36    | 1   | 1   | 0   |
| 0x37    | 1   | 1   | 1   |

---

## Dimensions

- **Board Dimensions:** 86 × 22 mm (3.39 × 0.9 inch)  
- **Header Pin Holes:** 1.5 mm  
- **Screw Holes:** Designed for M3 screws (3.2 mm diameter)  
- Soldered boards are LEGO-compatible! 🧱 

---

## Hardware repository

<WarningBox>The hardware repository for this board is not available yet! We're working on it. In the meantime, please [**contact us**](https://soldered.com/contact/) to receive the hardware files.</WarningBox>

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
- **Safety Instructions** – Safety guidelines and precautions in English and German.  
- **Info.txt** – Contains product details such as SKU, country of origin, HS tariff code, and barcode.