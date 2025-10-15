---
slug: /bme688/hardware 
title: BME688 - Hardware details
sidebar_label: Hardware details
id: bme688-hardware 
hide_title: False
---

## Pinout 
<CenteredImage src="/img/under_construction.png"/>

## Pin details

| Pin Marking | Pin Name | Description                                     |
| ----------- | -------- | ----------------------------------------------- |
| **VCC**     | Power    | Supply voltage (both 5V and 3V3 are supported).  |
| **GND**     | Ground   | Common ground for power and signals.            |
| **SDA**     | Data     | I2C data line for communication.                |
| **SCL**     | Clock    | I2C clock line for communication.               |


<InfoBox>
This breakout board operates at **3.3V logic level**, but includes an onboard regulator for **5V compatibility** so it can be connected to both 3V3 and 5V logic boards!
</InfoBox>
---

## Qwiic
<CenteredImage src="/img/easyc_transparent.png" alt="EasyC/qwiic cable" width="550px" />
 
<InfoBox>This board is fully **Qwiic-compatible**! Just plug it into your board using a **Qwiic/easyC/STEMMA QT cable** and start coding!</InfoBox>

<QuickLink 
  title="Qwiic (formerly easyC) details and specifications" 
  description="Learn about hardware specifications, compatibility, and usage of the Qwiic connector." 
  url="/qwiic" 
/>

---

## Dimensions 
- **Board Dimensions:** 38 x 22mm(1.5 x 0.9 inch)
- **Header Pin Holes:** 1.5 mm
- **Screw Holes:** Designed for M3 screws (3.2 mm diameter)
- Soldered boards are LEGO compatible! 🧱

---

## Jumper Details
This board contains hardware jumpers. See below for their locations and functions:

<FlickityCarousel
    images={[
        { src: '/img/bme688/jp1.jpg', alt: 'BME688 jumper 1', caption: 'JP1'},
        { src: '/img/bme688/jp2.jpg', alt:'BME688 jumper 2', caption: 'JP2'},
        { src: '/img/bme688/jp3.jpg', alt:'BME688 jumper 3', caption: 'JP3'},
        { src: '/img/bme688/jp4.jpg', alt:'BME688 jumper 4', caption: 'JP4'},
        { src:'/img/bme688/jp5.jpg', alt:'BME688 jumper 5', caption: 'JP5'}
    ]}
/>

| Jumper 	| Default State 	| Function 	|
|---	|---	|---	|
| **JP1** 	| Normally open 	| Used to change the device address. When shorted to GND, the address is **0x76**, **0x77** when connected to VCC. 	|
| **JP2** 	| Normally open 	| When connected, the **voltage regulator is powered by 5V** 	|
| **JP3** 	| Normally closed 	| Enables the Voltage regulator 	|
| **JP4** 	| Normally closed 	| Connects **SDA/SCL pull-up resistors to 5V** for I2C communication. 	|
| **JP5** 	| Normally closed 	| Connects **SDA/SCL pull-up ressitors to 3.3V** for I2C communication. 	|

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