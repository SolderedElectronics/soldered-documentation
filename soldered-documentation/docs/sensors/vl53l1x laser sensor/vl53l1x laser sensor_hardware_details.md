---
slug: /vl53l1x laser sensor/hardware 
title: Hardware details
id: vl53l1x laser sensor-hardware 
hide_title: False
---

## Pinout

<ErrorBox>The pinout image for this board hasn't been generated yet! We're working on it!</ErrorBox>

## Pin details

| Pin Marking  | Pin Name   | Description                                                                 |
|--------------|------------|-----------------------------------------------------------------------------|
| **VCC**      | Power      | Supply voltage (both 5V and 3V3 are supported).                             |
| **GND**      | Ground     | Common ground for power and signals.                                        |
| **SCL**      | Clock      | I²C clock line for communication.                                           |
| **SDA**      | Data       | I²C data line for communication.                                            |
| **SHTD**     | Shutdown   | Manually power down or reset the sensor.                                    |
| **GPIO1**    | Interrupt  | Interrupt line from sensor to microcontroller.                              |


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

- **Board Dimensions:** 22 × 22 mm (0.9 × 0.9 inch)  
- **Header Pin Holes:** 1.5 mm  
- **Screw Holes:** Designed for M3 screws (3.2 mm diameter)  
- Soldered boards are LEGO compatible! 🧱 

---

## Jumper Details

This board contains hardware jumpers; see below for their locations and functions:

<FlickityCarousel
  images={[
    { src: '/img/under_construction.png', alt: 'VL53L1X jumper 1', caption: 'JP1' },
    { src: '/img/under_construction.png', alt: 'VL53L1X jumper 2', caption: 'JP2' },
    { src: '/img/under_construction.png', alt: 'VL53L1X jumper 3', caption: 'JP3' },
    { src: '/img/under_construction.png', alt: 'VL53L1X jumper 4', caption: 'JP4' },
    { src: '/img/under_construction.png', alt: 'VL53L1X jumper 5', caption: 'JP5' },   
  ]}
  jumpers={true}
/>

| Jumper  | Default State            | Function                                                                                                                                    |
|---------|--------------------------|--------------------------------------------------------------------------------------------------------------------------------------------|

---

## Address jumper


---

## Hardware repository

Schematics, KiCad files, Gerber files and more can be found in the GitHub repository:

<QuickLink 
  title="VL53L1X sensor with easyC Hardware design" 
  description="GitHub hardware repository for this product"
  url="https://github.com/SolderedElectronics/NAZIVPROIZVODA" 
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