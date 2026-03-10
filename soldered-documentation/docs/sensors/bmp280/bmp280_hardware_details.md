---
slug: /bmp280/hardware 
title: Hardware details
id: bmp280-hardware 
hide_title: False
---


## Pinout 

[IMAGE PLACEHOLDER - BMP280 pinout]

## Pin Details

| Pin Marking | Pin Name | Description                                     |
| ----------- | -------- | ----------------------------------------------- |
| **GND**     | Ground   | Common ground for power and signals.            |
| **VCC**     | Power    | Supply voltage (both 5V and 3V3 are supported). |
| **SDA**     | Data     | I2C data line for communication.                |
| **SCL**     | Clock    | I2C clock line for communication.               |

<InfoBox>This breakout board operates at **3.3V logic level**, but includes an onboard regulator for **5V compatibility** so it can be connected to both 3V3 and 5V logic boards!</InfoBox>

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

# Dimensions

- **Board Dimensions:** 22 × 38 mm (0.9 × 1.5 inch)  
- **Header Pin Holes:** 1.5 mm  
- **Screw Holes:** Designed for M3 screws (3.2 mm diameter)  
- Soldered boards are LEGO compatible! 🧱 

---

## Jumper Details

This board contains hardware jumpers; see below for their locations and functions:

[JUMPER DETAILS PLACEHOLDER]

| Jumper 	| Default State 	| Function 	|
|---	|---	|---	|
| **JP1** 	|  **NC** (Normally closed)	| Connects **SDA/SCL pull-up resistors to 5V** for I2C communication.  	|
| **JP2** 	| **NO** (Normally open) | When shorted, it changes the last address bit from 0 to 1 effectively changing devices I2C address from **0x76** to **0x77**.|
| **JP3** 	|  **NC** (Normally closed) 	| Connects **SDA/SCL pull-up resistors to 3.3V** for I2C communication. 	|
| **JP4** 	| **NC** (Normally closed)| When connected, the **voltage regulator is powered by 5V**, stepping it down to **3.3V for the I2C**.   	|
| **JP5** 	|**NO** (Normally open) |When shorted, it **bypassess the voltage regulator**, allowing the board to be powered **directly from 3.3V** via headers. **Ensure JP4 is disconnected if JP5 is connected.**  	|

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
- **Safety Instructions** – Safety guidelines and precautions in English and in German.
- **Info.txt** – Contains product details such as SKU, country of origin, HS tariff code, and barcode.