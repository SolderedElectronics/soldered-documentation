---
slug: /inputronic-keyboard/hardware 
title: Inputronic Keyboard - Hardware details
sidebar_label: Hardware details
id: inputronic-keyboard-hardware 
hide_title: False
---

## Pinout 

<CenteredImage src="/img/inputronic-keyboard/pinout.png"/>

Click [**here**](/img/inputronic-keyboard/pinout.png) for a high-resolution image of the pinout.

## Pin details

| Pin Marking | Pin Name | Description |
| ----------- | -------- | ----------- |
| **VCC** | Power | Supply voltage (1.65V to 3.6V supported) |
| **GND** | Ground | Common ground for power and signals |
| **SDA** | Data | I²C data line for communication |
| **SCL** | Clock | I²C clock line for communication |
| **INT** | Interrupt | Active-low interrupt output (open-drain) |
| **RESET** | Reset | Active-low reset input |

<InfoBox>
This board operates at **1.65V to 3.6V logic levels** and is compatible with both 3.3V and 5V systems when used with appropriate level shifters or directly with 3.3V microcontrollers!
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

## I²C Address

The TCA8418 has a fixed 7-bit I²C address:

**0x34** (0b0110100)

<InfoBox>Unlike some I²C devices, the address on this board **cannot be changed** through hardware jumpers.</InfoBox>

---

## Dimensions 
- **Board Dimensions:** 136 x 60 mm
- **Header Pin Holes:** 1.5 mm
- **Screw Holes:** Designed for M3 screws (3.2 mm diameter)
- Soldered boards are LEGO compatible! 🧱

---

## Jumper Details

This board contains hardware jumpers. See below for their locations and functions:

<FlickityCarousel
    images={[
        { src: '/img/inputronic-keyboard/jp1.jpg', alt: 'Inputronic Keyboard jumper 1', caption: 'JP1'},
        { src: '/img/inputronic-keyboard/jp2.jpg', alt:'Inputronic Keyboard jumper 2', caption: 'JP2'}
    ]}
/>

| Jumper | Default State | Function |
|--------|---------------|----------|
| **JP1** | Normally open | Optional 3.3V power connection |
| **JP2** | Normally open | Reset button connection option |

<InfoBox>The keyboard matrix is pre-configured with 80 tactile switches arranged in an 8×10 matrix. All switches are connected to the TCA8418 chip's ROW and COL pins internally.</InfoBox>

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

