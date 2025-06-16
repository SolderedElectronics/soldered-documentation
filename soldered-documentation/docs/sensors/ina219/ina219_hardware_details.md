---
slug: /ina219/hardware 
title: INA219 - Hardware details
sidebar_label: Hardware details
id: ina219-hardware 
hide_title: False
---

## Pinout

<CenteredImage src="/img/ina219/pinout.webp" alt="ina219 pinout" />

Click [**here**](/img/ina219/pinout.webp) for a high-resolution image of the pinout.

## Pin details

| Pin Marking | Pin Name | Description                                     |
| ----------- | -------- | ----------------------------------------------- |
| **GND**     | Ground   | Common ground for power and signals.            |
| **VCC**     | Power    | Supply voltage (both 5V and 3V3 are supported). |
| **SDA**     | Data     | I2C data line for communication.                |
| **SCL**     | Clock    | I2C clock line for communication.               |
| **IN+**     | Input    | Positive shunt voltage connector.               |
| **IN-**     | Input    | Negative shunt voltage connector.               |

<InfoBox>This breakout board operates at **3.3V logic level**, but includes an onboard regulator for **5V compatibility** so it can be connected to both 3V3 and 5V logic boards!</InfoBox>

---

## Qwiic (formerly easyC)  

<CenteredImage src="/img/easyc_transparent.png" alt="EasyC/qwiic cable" width="550px" />
 
<InfoBox>This board is fully **Qwiic-compatible**! Just plug it into your board using a **Qwiic/easyC/STEMMA QT cable** and start coding!</InfoBox>

<QuickLink 
  title="Qwiic (formerly easyC) details and specifications" 
  description="Learn about hardware specifications, compatibility, and usage of the Qwiic connector." 
  url="/qwiic" 
/>

---

## Dimensions

- **Board Dimensions:** 38 × 22 mm (1.5 × 0.9 inch)  
- **Header Pin Holes:** 1.5 mm  
- **Screw Holes:** Designed for M3 screws (3.2 mm diameter)  
- Soldered boards are LEGO compatible! 🧱

---

## Jumper Details

This board contains hardware jumpers; see below for their locations and functions:

<FlickityCarousel
  images={[
    { src: '/img/ina219/jp1.webp', alt: 'ina219 jumper 1', caption: 'JP1' },
    { src: '/img/ina219/jp2.webp', alt: 'ina219 jumper 2', caption: 'A0' },
    { src: '/img/ina219/jp3.webp', alt: 'ina219 jumper 3', caption: 'A1' },
  ]}
  jumpers={true}
/>

| Jumper  | Default State            | Function                                                                                                      |
| ------- | ------------------------ | ------------------------------------------------------------------------------------------------------------- |
| **JP1** | **NC** (Normally closed) | Connects **SDA/SCL pull-up resistors to VCC** for I2C communication.                                            |
| **A0**  | **NO** (Normally open)   | When shorted, it connects the A0 pin to VCC.                                                                   |
| **A1**  | **NO** (Normally open)   | When shorted, it connects the A1 pin to VCC.                                                                   |

---

## Address selection

Depending on how you configure the A0 and A1 jumpers, you can define different I2C addresses for the INA219:

| Address |        A1       |        A0       |
| :-----: | :-------------: | :-------------: |
|  0x40   |  Not shorted    |  Not shorted    |
|  0x41   |  Not shorted    |    Shorted      |
|  0x44   |    Shorted      |  Not shorted    |
|  0x45   |    Shorted      |    Shorted      |

---

## Hardware repository

Schematics, KiCad files, Gerber files, and more can be found in the GitHub repository:

<QuickLink 
  title="Voltage & current sensor INA219 breakout Hardware Design" 
  description="GitHub hardware repository for this product"
  url="https://github.com/SolderedElectronics/Voltage---current-sensor-INA219-breakout-hardware-design/tree/main" 
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
- **Safety Instructions** – Safety guidelines and precautions in English and German.
- **Info.txt** – Contains product details such as SKU, country of origin, HS tariff code, and barcode.