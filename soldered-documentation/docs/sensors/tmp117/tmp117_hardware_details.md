---
slug: /tmp117/hardware
title: TMP117 Temperature Sensor Hardware details
sidebar_label: Hardware details
id: tmp117-hardware
hide_title: True
---

# Hardware details

## Pinout

<CenteredImage src="/img/tmp117/pinout.png" alt="TMP117 Pinout" />

Click [**here**](/img/tmp117/pinout.png) for a high resolution image of the pinout.

## Pin details

| Pin Marking | Pin Name | Description                                                                 |
| ----------- | -------- | --------------------------------------------------------------------------- |
| **VCC**     | Power    | Power supply input (1.7 V – 5.5 V).                                         |
| **GND**     | GND      | Ground reference for power and signals.                                     |
| **SCL**     | Clock    | Serial clock input for I²C/SMBus communication.                             |
| **SDA**     | Data     | Serial data line (open-drain, requires pull-up resistor).                   |
| **ALERT**   | ALERT    | Configurable pin: over-temperature alert or data-ready signal (open-drain). |


## Dimensions

- **Board Dimensions:** 38 x 22 mm (1.5 x 0.9 inches)
- **Header Pin Holes:** 1.5 mm
- **Screw Holes:** Designed for M3 screws (3.2 mm diameter)
- Soldered boards are LEGO compatible! 🧱

## Jumper Details

This board contains hardware jumpers; see below for their locations and functions:


<FlickityCarousel
  images={[
    { src: '/img/tmp117/tmp117_jp1.jpg', alt: 'tmp117-jumper1', caption: 'JP1' },
    { src: '/img/tmp117/tmp117_jp2.jpg', alt: 'tmp117-jumper2', caption: 'JP2' },
    { src: '/img/tmp117/tmp117_jp3.jpg', alt: 'tmp117-jumper3', caption: 'JP3' },
    { src: '/img/tmp117/tmp117_jp4.jpg', alt: 'tmp117-jumper4', caption: 'JP4' },
    { src: '/img/tmp117/tmp117_jp5.jpg', alt: 'tmp117-jumper5', caption: 'JP5' },
    { src: '/img/tmp117/tmp117_jp6.jpg', alt: 'tmp117-jumper6', caption: 'JP6' },
    { src: '/img/tmp117/tmp117_jp7.jpg', alt: 'tmp117-jumper7', caption: 'JP7' },
    { src: '/img/tmp117/tmp117_jp8.jpg', alt: 'tmp117-jumper8', caption: 'JP8' },
  ]}
  jumpers={true}
/>

## Jumpers

| Jumper  | Default State            | Function                                                                                            |
| ------- | ------------------------ | --------------------------------------------------------------------------------------------------- |
| **JP1** | **NO** (Normally open)   | When shorted, **bypasses the voltage regulator**, allowing direct 3.3V supply via headers.          |
| **JP2** | **NC** (Normally closed) | Connects **ADD0 pin to 3.3V**, setting I²C address accordingly.                                     |
| **JP3** | **NC** (Normally closed) | Connects **I²C pull-up resistors to 5V** for SDA/SCL lines.                                         |
| **JP4** | **NC** (Normally closed) | Connects **I²C pull-up resistors to 3.3V** for SDA/SCL lines.                                       |
| **JP5** | **NO** (Normally open)   | Connects **ADD0 pin to SCL (3.3V)** for I²C address selection.                                      |
| **JP6** | **NO** (Normally open)   | Connects **ADD0 pin to SDA (3.3V)** for I²C address selection.                                      |
| **JP7** | **NO** (Normally open)   | Connects **ADD0 pin to GND** for I²C address selection.                                             |
| **JP8** | **NC** (Normally closed) | Enables **voltage regulator** to power the board from 5V input (steps down to 3.3V for the TMP117). |


## Hardware repository

Schematics, KiCad files, Gerber files, and more can be found in the GitHub repository:

<WarningBox>The hardware repository for this board is not available yet! We're working on it. In the meantime, please [**contact us**](https://soldered.com/contact/) to receive the hardware files.</WarningBox>

<!--
<QuickLink 
  title="TMP117 Temperature Sensor Hardware Design" 
  description="GitHub hardware repository for this product"
  url="https://github.com/TexasInstruments/TMP117-hardware"
  image="/img/tmp117/hw.png"
/>
-->

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
