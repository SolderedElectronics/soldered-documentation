---
slug: /tca9548a/hardware
title: "TCA9548A I2C multiplexer \u2013 Hardware details"
id: tca9548a-hardware
hide_title: false
---
<CenteredImage src="/img/tca9548a/pinout.png" alt="Pinout" />

Click [**here**](/img/tca9548a/pinout.png) for a high-resolution image of the pinout.

| Pin Marking   | Pin Name       | Description                                     |
| ------------- | -------------- | ----------------------------------------------- |
| **GND**       | Ground         | Common ground for power and signals.            |
| **VCC**       | Power Supply   | Supply voltage (1.65V - 5.5V).                  |
| **SDA0-SDA7** | Data Lines     | Individual I2C data lines for each channel.     |
| **SCL0-SCL7** | Clock Lines    | Individual I2C clock lines for each channel.    |
| **SDA/SCL**   | Main Bus       | Main I2C bus data and clock lines.              |
| **A0-A2**     | Address Select | Adjustable pins to set the multiplexer address. |

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

## Jumper Details

This board contains hardware jumpers, see below for their locations and functions:

<FlickityCarousel
images={[
{ src: '/img/tca9548a/a0.png', alt: 'Multiplexer jumper A0', caption: 'A0' },
{ src: '/img/tca9548a/a1.png', alt: 'Multiplexer jumper A1', caption: 'A1' },
{ src: '/img/tca9548a/a2.png', alt: 'Multiplexer jumper A2', caption: 'A2' },
]}
jumpers={true}
/>


| Jumper | Default State          | Function                                 |
| ------ | ---------------------- | ---------------------------------------- |
| **A0** | **NO** (Normally open) | Sets address bit A0 to HIGH when closed. |
| **A1** | **NO** (Normally open) | Sets address bit A1 to HIGH when closed. |
| **A2** | **NO** (Normally open) | Sets address bit A2 to HIGH when closed. |

---

## Adress selection

| **A0** | **A1** | **A2** | **I2C Address** |
| ------ | ------ | ------ | --------------- |
| Open   | Open   | Open   | 0x70            |
| Closed | Open   | Open   | 0x71            |
| Open   | Closed | Open   | 0x72            |
| Closed | Closed | Open   | 0x73            |
| Open   | Open   | Closed | 0x74            |
| Closed | Open   | Closed | 0x75            |
| Open   | Closed | Closed | 0x76            |
| Closed | Closed | Closed | 0x77            |


---

## Dimensions

- **Board Dimensions:** 54 x 38 mm (2.1 x 1.5 inch)
- **Header Pin Holes:** 1.5 mm
- **Screw Holes:** Designed for M3 screws (3.2 mm diameter)
- Soldered boards are LEGO compatible! 🧱

---

## Hardware Repository

Schematics, KiCad files, Gerber files, and more can be found in the GitHub repository:

<QuickLink title="I2C multiplexer TCA9548A breakout Hardware Design" 
description="GitHub hardware repository for this product" 
url="https://github.com/SolderedElectronics/I2C-multiplexer-TCA9548A-breakout-hardware-design" />

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