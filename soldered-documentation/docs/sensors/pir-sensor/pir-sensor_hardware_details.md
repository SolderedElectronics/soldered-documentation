---
slug: /pir-sensor/hardware
title: "PIR Movement sensor \u2013 Hardware details"
id: pir-sensor-hardware
hide_title: false
---
## Pinout

### Standard version

<ErrorBox>The pinout image for this board hasn't been generated yet! We're working on it!</ErrorBox>

| Pin Marking | Pin Name | Description                                     |
| ----------- | -------- | ----------------------------------------------- |
| **VCC**     | Power    | Supply voltage                                  |
| **DOUT**     | Delayed output | Gets delayed output depending on MCU     |
| **SOUT**     | Sensor output    | Gets instant sensor output             |
| **GND**     | Ground   | Common ground for power and signals.            |

### Qwiic version

<ErrorBox>The pinout image for this board hasn't been generated yet! We're working on it!</ErrorBox>

| Pin Marking | Pin Name | Description                                     |
| ----------- | -------- | ----------------------------------------------- |
| **3V3**     | Power    | Supply voltage for the UPDI                     |
| **UPDI**    | UPDI     | Communication pin for UPDI                      |
| **GND**     | Ground   | Common ground for power and signals.            |

<WarningBox>UPDI stands for Unified Program and Debug Interface. It is used to program and debug Atmel devices. The atmel chip on this board is used for the easyC I2C communication only. DO NOT try to use this for sensor communication!</WarningBox>


<CenteredImage src="/img/easyc_transparent.png" alt="EasyC/qwiic cable" width="550px" />
 
<InfoBox> This board is fully **Qwiic-compatible**! Just plug it into your board using a **Qwiic/easyC/STEMMA QT cable** and start coding! </InfoBox>

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

## Jumper Details (Standard version)

This board contains hardware jumpers, see below for their locations and functions:

<FlickityCarousel
  images={[
    { src: '/img/pir-sensor/jp1.webp', alt: 'PIR sensor jumper 1', caption: 'JP1' },
    { src: '/img/pir-sensor/jp2.webp', alt: 'PIR sensor jumper 2', caption: 'JP2' },
  ]}
  jumpers={true}
/>

| Jumper  | Default State            | Function                                                                                                      |
| ------- | ------------------------ | ------------------------------------------------------------------------------------------------------------- |
| **JP1** | **NC** (Normally closed) |  When shorted, Connects the **voltage regulator to 5V**                                           |
| **JP2** | **NO** (Normally closed) | When shorted, **bypasses the voltage regulator**                                        |

---

## Address selection (Qwiic version)
This board contains hardware address switches, see below how to change breakout board's address:
<CenteredImage src="/img/pir-sensor/addresses.webp" alt="Pinout" width="500px" />
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
  title="PIR Movement sensor board Hardware Design" 
  description="GitHub hardware repository for this product"
  url="https://github.com/SolderedElectronics/PIR-Movement-sensor-board-hardware-design/tree/main" 
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