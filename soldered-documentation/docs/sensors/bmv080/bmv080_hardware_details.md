---
slug: /bmv080/hardware 
title: BMV080 Particulate Matter Sensor - Hardware details
sidebar_label: Hardware details
id: bmv080-hardware 
hide_title: False
---

# BMV080 - Hardware details

## Pinout

<CenteredImage src="/img/bmv080/bmv080-pinout.png" alt="BMV080 pinout" />

Click [**here**](/img/bmv080/bmv080-pinout.png) for a high resolution image of the pinout.

## Pin details

| Pin Marking |  Pin Name | Description                                                                 |
| ----------- | --------- | --------------------------------------------------------------------------- |
| **VCC**     | Power     | Power supply input.                                                         |
| **GND**     | GND       | Ground reference for power and signals.                                     |
| **IRQ**     | Interrupt | Interrupt line, digital out, active **low.**                                         |
| **AB1**     | Address bit 1 | This pin functions as **I²C Address Bit 1**, or as not Slave Select (nSS) in **SPI mode**. |
| **AB0**     | Address bit 0 | This pin functions as **I²C Address Bit 0**, or as Master In Slave Out (MISO) in **SPI mode**. |
| **SDA**     | Serial Data line | Pin acts as Serial data line in I²C mode, or as Master Out Slave In (MOSI) in **SPI mode**. |
| **SCL**     | Serial Clock line | Pin acts as serial input for **both serial interface protocols** (SPI and I²C). |

<InfoBox> 

Address pins 1 and 0 (AB1 and AB0) allow the BMV080 to have four possible I²C addresses (0x54–0x57) by adjusting the **address bits 0 and 1** of the slave. **Both are active low.** Below is a table for address selection (per datasheet):

| AB1   | AB0   | Address  |
| :---: | :---: | :-----:  |
| 0     | 0     | 0x54     |
| 0     | 1     | 0x55     |
| 1     | 0     | 0x56     |
| 1     | 1     | 0x57     |

</InfoBox>


## Dimensions

- **Board Dimensions:**  38 x 22mm (1.5 x 0.9 inches)
- **Header Pin Holes:** 1.5 mm
- **Screw Holes:** Designed for M3 screws (3.2 mm diameter)
- Soldered boards are LEGO compatible! 🧱

## Jumper Details

This board contains hardware jumpers; see below for their locations and functions:


<FlickityCarousel
  images={[
    { src: '/img/under_construction.png', alt: 'bmv080-jumper-1', caption: 'JP1' },
    { src: '/img/under_construction.png', alt: 'bmv080-jumper-2', caption: 'JP2' },
    { src: '/img/under_construction.png', alt: 'bmv080-jumper-3', caption: 'JP3' },
    { src: '/img/under_construction.png', alt: 'bmv080-jumper-4', caption: 'JP4' }
  ]}
  jumpers={true}
/>

## Jumpers

| Jumper    |  Default State | Function |   
| :-------: | :------------: | --------- |
| **JP1** 	|  Pulled up | Connect low for selecting SPI mode.  | 
| **JP2** 	|  Pulled up | Connect low for setting the address bit 0 state to HIGH. |
| **JP3** 	|  Pulled up | Connect low for setting the address bit 1 state to HIGH. |
| **JP4** 	|  Normally connected (NC) | Connects **SDA/SCL pull-up ressitors to 3.3V** for I2C communication. |                                                 


## Hardware repository

Schematics, KiCad files, Gerber files, and more can be found in the GitHub repository:

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
