---  
slug: /hc-sr04/hardware  
title: Hc Sr04 – Hardware details
sidebar_label: Hardware details
id: hc-sr04-hardware  
hide_title: False  
---

## Pinout

<CenteredImage src="/img/hc-sr04/hc-sr04_pinout.png" alt="Pinout" />

Click [**here**](/img/hc-sr04/hc-sr04_pinout.png) for a high resolution image of the pinout.

---

## Pin details

| Pin Marking | Pin Name | Description                                     |
| ----------- | -------- | ----------------------------------------------- |
| **VCC**     | Power    | Supply voltage (5V)                             |
| **GND**     | Ground   | Common ground for power and signals.            |
| **ECHO**    | Echo     | Pin that receives the reflected wave            |
| **TRIG**    | Trigger  | Pin that emits the start pulse                  |
| **3V3**     | Power    | Supply voltage for the UPDI                     |
| **UPDI**    | UPDI     | Communication pin for UPDI                      |

<WarningBox>UPDI stands for Unified Program and Debug Interface. It is used to program and debug Atmel devices. The atmel chip on this board is used for the easyC I2C communication only. DO NOT try to use this for sensor communication!</WarningBox>

<InfoBox> This sensor is made to work specifically with the Qwiic connector; the echo and trigger pins are pre-connected. </InfoBox>

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

## Dimensions

- **Board Dimensions:** 45 x 22 mm (1.8 x 0.9 inch)

---

## Address selection (Qwiic version)
This board contains hardware address switches. See below for instructions on changing the breakout board's address:
<CenteredImage src="/img/hc-sr04/333001_address.jpg" alt="Pinout" width="500px" />
| Address |  SW3  |  SW2  |  SW1  |
| :-----: | :---: | :---: | :---: |
|  0x30   |   0   |   0   |   0   |
|  0x31   |   0   |   0   |   1   |
|  0x32   |   0   |   1   |   0   |
|  0x33   |   0   |   1   |   1   |
|  0x34   |   1   |   0   |   0   |
|  0x35   |   1   |   0   |   1   |
|  0x36   |   1   |   1   |   0   |
|  0x37   |   1   |   1   |   1   |

---

## Hardware repository

Schematics, KiCad files, Gerber files and more can be found in the GitHub repository:

<QuickLink 
  title="Ultrasonic sensor with easyC Hardware design" 
  description="GitHub hardware repository for this product"
  url="https://github.com/SolderedElectronics/Ultrasonic-sensor-with-easyC-hardware-design" 
/> 

The hardware repository contains everything you need to understand, modify, or manufacture the board. The different output folders are versioned. You can determine your board version by checking the version mark on the PCB.

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