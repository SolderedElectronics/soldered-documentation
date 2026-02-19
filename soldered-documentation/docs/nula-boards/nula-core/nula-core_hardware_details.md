---
slug: /nula-core/hardware
title: NULA Core - Hardware details
sidebar_label: Hardware details
id: core_hardware_details
hide_title: True
---

# Hardware details

## Pinout

<CenteredImage src="/img/nula-core/Dasduino-CORE-ATmega328-Pinout.webp" alt="NULA Core pinout" caption="NULA Core Pinout Diagram"/>

Click [**here**](/img/nula-core/Dasduino-CORE-ATmega328-Pinout.webp) for a high-resolution image of the pinout.

## Pin Details

| Pin Marking | Pin Name | Description                                                               |
| ----------- | -------- | ------------------------------------------------------------------------- |
| **VBAT**    | Power    | Battery input for 3.7 V Li-Ion/Li-Poly battery through the JST connector. |
| **VCC**     | Power    | Main power input (5 V via USB-C or external 5 V supply).                  |
| **3V3**     | Power    | Regulated 3.3 V output from the onboard regulator.                        |
| **GND**     | Ground   | Common ground for power and signals.                                      |
| **RESET**   | Control  | Hardware reset pin.                                                       |
| **D0-D13/A0-A7** | GPIO | General-purpose I/O pins, supporting PWM, I²C, SPI, UART, ADC.           |

<InfoBox> **A0-A5** can be used as Digital IO pins, but **A6/A7** are analog-only inputs. </InfoBox>

---

## Qwiic / easyC Connector

<CenteredImage src="/img/easyc_transparent.png" alt="Qwiic/easyC connector" width="550px" />

<InfoBox>The **NULA Core** includes a **Qwiic/easyC/STEMMA QT connector** for quick plug-and-play connections with I²C devices such as sensors and peripherals.</InfoBox>

<QuickLink
  title="Qwiic (formerly easyC) details and specifications"
  description="Learn more about Qwiic hardware compatibility and connector pinout."
  url="/qwiic"
/>

---

## Power Supply and Battery

- **USB-C Port** is used for both programming and powering the board  
- VBAT (JST connector) is used for connecting a 3.7 V Li-Ion or Li-Poly battery  
- The board includes an integrated **Li-Ion charge management** circuit  
- Operating voltage: 3.3 V (onboard regulator for 5 V input)

<InfoBox>When powered using a battery, the onboard charger automatically handles charging and discharging.  
For 5 V input, always power the board through the USB-C port.</InfoBox>

---

## Dimensions

- **Board size**: 63 x 22 mm / 2.5 x 0.9 inch
- **Mounting**: Breadboard compatible  
- **Header Pin Holes:** 1.5 mm  
- **Screw Holes:** Designed for M3 screws (3.2 mm diameter)  

Soldered boards are LEGO compatible! 🧱 

---

## Jumper Details

<FlickityCarousel
  images={[
    { src: '/img/under_construction.png', alt: 'nula-core-jumper1', caption: 'JP1' },
    { src: '/img/under_construction.png', alt: 'nula-core-jumper2', caption: 'JP2' },
    { src: '/img/under_construction.png', alt: 'nula-core-jumper3', caption: 'JP3' }
  ]}
  jumpers={true}
/>

| Jumper  | Default State            | Function                                                                                                      |
| ------- | ------------------------ | ------------------------------------------------------------------------------------------------------------- |
| **JP1** | **NC** (Normally closed) | Disconnects the Power LED to reduce standby current draw when running from battery power.                     |
| **JP2** | **NC** (Normally closed) | Connects the **5 V I²C pull-up resistors** for SDA and SCL lines when required by connected I²C devices.      |
| **JP3** | **NC** (Normally closed) | Connects the **3.3 V I²C pull-up resistors** for SDA and SCL lines when required by connected I²C devices.    |

---

## Hardware repository

Schematics, KiCad files, Gerber files and more can be found in the GitHub repository:

<QuickLink
title="NULA-Core-hardware-design"
description="GitHub hardware repository for this product"
url="https://github.com/SolderedElectronics/Dasduino-CORE-hardware-design"
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