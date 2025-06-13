---
slug: /pcf85063a/hardware
title: PCF85063A - Hardware details
id: pcf85063a-hardware
hide_title: false
---

## Pinout

<CenteredImage src="/img/pcf85063a/pinout.jpg" alt="Pinout" />

Click [**here**](/img/pcf85063a/pinout.jpg) for a high resolution image of the pinout.

---

## Pin details

| Pin Marking | Pin Name | Description                                                                  |
| ----------- | -------- | ---------------------------------------------------------------------------- |
| **VCC**     | Power    | Supply voltage (both 5V and 3V3 are supported).                              |
| **GND**     | Ground   | Common ground for power and signals.                                         |
| **SDA**     | Data     | I2C data line for communication.                                             |
| **SCL**     | Clock    | I2C clock line for communication.                                            |
| **CLK-OE**  | Clock output enable  | Enables the clock output pin when the pin is set to HIGH.          |
| **CLK-OUT** | Clock output         | Sends square wave signals at a speed defined by the user.          |
| **INT**     | Interrupt            | Sends a hardware interrupt.                                        |

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

## Jumper details

This board contains hardware jumpers; see below for their locations and functions:

<FlickityCarousel
  images={[
    { src: '/img/pcf85063a/jp1.webp', alt: 'RTC jumper 1', caption: 'JP1' },
    { src: '/img/pcf85063a/jp2.webp', alt: 'RTC jumper 2', caption: 'JP2' },
    { src: '/img/pcf85063a/jp3.webp', alt: 'RTC jumper 3', caption: 'JP3' },
    { src: '/img/pcf85063a/jp4.webp', alt: 'RTC jumper 4', caption: 'JP4' },
  ]}
  jumpers={true}
/>

| Jumper  | Default State            | Function                                                                                                                                                                      |
| ------- | ------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **JP1** | **NC** (Normally closed) | Connects **SDA/SCL pull-up resistors to 5V** for I2C communication.                                                                                                           |
| **JP2** | **NC** (Normally closed) | Connects **SDA/SCL pull-up resistors to 3.3V** for I2C communication.                                                                                                         |
| **JP3** | **NC** (Normally closed) | Connects the VCC pin to a 5V-to-3V3 voltage regulator IC.                                                                                                                     |
| **JP4** | **NO** (Normally open)   | When connected, bypasses the voltage regulator on the VCC pin, allowing 3V3 to be connected instead of 5V. **Make sure JP3 is disconnected if JP4 is connected.** |

---

## Dimensions

- **Board Dimensions:** 38 x 22 mm (1.5 x 0.9 inches)
- **Header Pin Holes:** 1.5 mm
- **Screw Holes:** Designed for M3 screws (3.2 mm diameter)
- Soldered boards are LEGO compatible! 🧱

---

## Hardware repository

Schematics, KiCad files, Gerber files, and more can be found in the GitHub repository:

<QuickLink 
  title="Real time clock RTC PCF85063A breakout Hardware Design" 
  description="GitHub hardware repository for this product"
  url="https://github.com/SolderedElectronics/Real-time-clock-RTC-PCF85063A-breakout-hardware-design/tree/main" 
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