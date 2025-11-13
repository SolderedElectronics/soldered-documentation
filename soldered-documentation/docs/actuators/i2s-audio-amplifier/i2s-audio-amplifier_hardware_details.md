---
slug: /i2s-audio-amplifier/hardware 
title: I2S Audio Amplifier - Hardware details
sidebar_label: Hardware details
id: i2s-audio-amplifier-hardware 
hide_title: False
---

## Pinout

<CenteredImage src="/img/i2s-audio-amp/stereo-i2s-amp-pinout.png" alt="Pinout image" />
Click [**here**](/img/i2s-audio-amp/stereo-i2s-amp-pinout.png) for a high reoslution image of the pinout.

### Pin details

| Pin Marking | Pin Name | Description |
|---|---|---|
| **VCC** | Power | Supply voltage (supports 3.3V and 5V) |
| **BCLK** | Bit Clock | Bit clock signaling when to read each bit of audio data | 
| **DIN** | Data In | Digital input signal (audio data) |
| **LRCLK** | Left-Right Clock | Left/Right clock for selecting **left** or **right** audio channel |
| **GND** | Ground | Ground |
| **LEFT OUTPUT** | Output | Left channel speaker output |
| **RIGHT OUTPUT** | Output | Right channel speaker output |

## Dimensions

- **Dimensions:** 
- **Header Pin Holes:** 
- **Screw Holes:** 
- Soldered boards are LEGO compatible! 🧱

---

## Gain selection jumpers

This board contains hardware gain selection jumpers for optimizing output levels for different speakers and applications:

<CenteredImage src="/img/i2s-audio-amp/i2s-audio-amp-gain-selection.png" alt="Gain selection jumpers" />

---

## Hardware repository

Schematics, KiCad files, Gerber files and more can be found in the GitHub repository:

<QuickLink 
  title="Stereo I2S Audio Amplifier Hardware Design" 
  description="Hardware design, BOM, gerbers and 3D files for Stereo I2S Audio Amplifier Board designed by Soldered Electronics."
  url="https://github.com/SolderedElectronics/NAZIV-PROIZVODA" 
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
