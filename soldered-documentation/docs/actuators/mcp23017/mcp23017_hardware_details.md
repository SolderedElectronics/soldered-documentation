---
slug: /mcp23017/hardware 
title: Hardware Details
id: mcp23017-hardware 
hide_title: False
---

<CenteredImage src="/img/mcp23017/pinout.png" alt="Pinout" />

Click [**here**](/img/mcp23017/pinout.png) for a high-resolution image of the pinout.

| Pin Marking | Pin Name | Description                                     |
| ----------- | -------- | ----------------------------------------------- |
| **GND**     | Ground   | Common ground for power and signals.            |
| **VCC**     | Power    | Supply voltage (both 5V and 3V3 are supported). |
| **SDA**     | Data     | I2C data line for communication.                |
| **SCL**     | Clock    | I2C clock line for communication.               |
| **RST**     | Reset    | Reset pin.                                      |
| **A0-A7**   | I/O      | A channel digital I/O.                         |
| **B0-B7**   | I/O      | B channel digital I/O.                         |
| **INT A**   | Interrupt| A channel interrupt pin.                       |
| **INT B**   | Interrupt| B channel interrupt pin.                       |

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
    { src: '/img/mcp23017/jp1.webp', alt: 'IO expander jumper 1', caption: 'JP1' },
    { src: '/img/mcp23017/jp2.jpg', alt: 'IO expander jumper 2', caption: 'JP2' },
    { src: '/img/mcp23017/jp3.webp', alt: 'IO expander jumper 3', caption: 'JP3' },
    { src: '/img/mcp23017/jp4.webp', alt: 'IO expander jumper 4', caption: 'JP4' },
    { src: '/img/mcp23017/jp5.jpg', alt: 'IO expander jumper 5', caption: 'JP5' },
    { src: '/img/mcp23017/jp6.jpg', alt: 'IO expander jumper 6', caption: 'JP6' },
    { src: '/img/mcp23017/jp7.jpg', alt: 'IO expander jumper 7', caption: 'JP7' },

  ]}
  jumpers={true}
/>

| Jumper  | Default State            | Function                                                                                          |
| ------- | ------------------------ | ------------------------------------------------------------------------------------------------- |
| **JP1** | **NC** (Normally closed) | Connects **SDA/SCL pull-up resistors to 5V** for I2C communication.                              |
| **JP2** | **NC** (Normally closed) | Connects **SDA/SCL pull-up resistors to 3.3V** for I2C communication.                            |
| **JP3** | **NC** (Normally closed) | Disconnects the 3.3V voltage regulator.                                                          |
| **JP4** | **NO** (Normally open)   | When closed, bypasses 3.3V voltage regulator.                                                    |
| **JP5** | **NC** (Normally closed) | When connected to GND, sets the I2C address to 0xA0.                                             |
| **JP6** | **NC** (Normally closed) | When connected to GND, sets the I2C address to 0xA1.                                             |
| **JP7** | **NC** (Normally closed) | When connected to GND, sets the I2C address to 0xA2.                                             |

---

## Dimensions

- **Board Dimensions:** 38 x 22 mm (1.5 x 0.9 inches)
- **Header Pin Holes:** 1.5 mm
- **Screw Holes:** Designed for M3 screws (3.2 mm diameter)
- Soldered boards are LEGO compatible! 🧱

---

## Hardware Repository

Schematics, KiCad files, Gerber files, and more can be found in the GitHub repository:

<QuickLink 
  title="IO expander MCP23017 breakout Hardware Design" 
  description="GitHub hardware repository for this product"
  url="https://github.com/SolderedElectronics/IO-expander-MCP23017-breakout-hardware-design" 
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