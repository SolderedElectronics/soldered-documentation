---
slug: /as5600/hardware
title: "AS5600 - Hardware details"
sidebar_label: "Hardware details"
id: as5600_hardware_details
hide_title: false
---

## Pinout

<CenteredImage src="/img/as5600/AS5600_pinout.png" alt="AS5600 pinout diagram" caption="AS5600 pinout diagram"/>


Click [**here**](/img/as5600/AS5600_pinout.png) for a high resolution image of the pinout.

---

## Pin Details

| Pin Marking | Pin Name | Description                                     |
| ----------- | -------- | ----------------------------------------------- |
| **VCC**     | Power    | Supply voltage (both 5V and 3V3 are supported). |
| **GND**     | Ground   | Common ground for power and signals.            |
| **SDA**     | Data     | I2C data line for communication.                |
| **SCL**     | Clock    | I2C clock line for communication.               |
| **OUT**     | Other    | Angle output signal                             |

<InfoBox>This breakout board operates at **3.3V logic level**, but includes an onboard regulator for **5V compatibility**, so it can be connected to both 3V3 and 5V logic boards!</InfoBox>

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

## Power Consumption

- **Typical operating current:** Approximately 6.5 mA during normal operation.
- **Maximum operating current:** Up to 8 mA depending on usage conditions.
- **Low-power operation:** Suitable for low-power embedded and battery-powered applications.

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
    { src: '/img/as5600/jp1.jpg', alt: 'as5600jumper1', caption: 'JP1' },
    { src: '/img/as5600/jp2.jpg', alt: 'as5600jumper2', caption: 'JP2' },
    { src: '/img/as5600/jp3.jpg', alt: 'as5600jumper3', caption: 'JP3' },
    { src: '/img/as5600/jp4.jpg', alt: 'as5600jumper4', caption: 'JP4' },
    { src: '/img/as5600/jp5.jpg', alt: 'as5600jumper5', caption: 'JP5' },
    { src: '/img/as5600/jp6.jpg', alt: 'as5600jumper6', caption: 'JP6' },
  ]}
  jumpers={true}
/>

| Jumper  | Default State            | Function |
| ------- | ------------------------ | -------- |
| **JP1** | **NO** (Normally open) | Sets the rotation direction polarity. GND = clockwise increase, VDD = counterclockwise increase. |
| **JP2** | **NO** (Normally open) | Connects the PGO pin to GND. |
| **JP3** | **NO** (Normally open) | Bypasses the onboard voltage regulator for direct 3.3V operation. |
| **JP4** | **NC** (Normally closed) | Disconnects the 5V input from the voltage regulator circuit. |
| **JP5** | **NC** (Normally closed) | Connects SDA/SCL pull-up resistors to **5V** for I2C communication. |
| **JP6** | **NC** (Normally closed) | Connects SDA/SCL pull-up resistors to **3.3V** for I2C communication. |

---

## Hardware repository

Schematics, KiCad files, Gerber files and more can be found in the GitHub repository:

[link placeholder]
{/*github link za hardware*/}

{/*
<QuickLink 
  title="AS5600 Hardware design" 
  description="GitHub hardware repository for this product"
  url="https://github.com/SolderedElectronics/Color---gesture-sensor-APDS-9960-breakout-hardware-design" 
/> 
*/}
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