---
slug: /nula-max-rp2350/hardware
title: NULA Max RP2350 - Hardware details
sidebar_label: Hardware details
id: max-rp2350_hardware_details
hide_title: True
---

# Hardware details

## Pinout

<CenteredImage src="/img/nula-max-rp2350/Nula Max RP2350 Pinout.png" alt="NULA Max RP2350 pinout" caption="NULA Max RP2350 Pinout Diagram"/>

Click [**here**](/img/nula-max-rp2350/Nula-Max-RP2350-Pinout.png) for a high-resolution version of the pinout.

---

## Pin Details

| Pin Marking    | Type   | Description                                                                   |
| -------------- | ------ | ----------------------------------------------------------------------------- |
| **3V3**        | Power  | Regulated 3.3 V output from onboard regulator.                                |
| **VCC**        | Power  | Main power input (5 V via USB-C or external 5 V supply).                      |
| **VBAT**       | Power  | JST battery connector input for 3.7 V Li-Ion/Li-Poly cells.                   |
| **GND**        | Ground | Common ground reference.                                                      |
| **IO0 - IO47** | GPIO   | General-purpose I/O pins with peripheral support (PWM, SPI, I²C, UART, etc.). |

<InfoBox>The **front side** of the board, which features the female connectors on solder pads, exposes all GPIO pins, power rails, and control interfaces. This view is typically used when soldering or connecting to the top of the board.<br></br><br></br>The **back side** markings describe the header pin holes. Only a few pins differ between the two sides, and these are clearly marked in the pinout diagram.</InfoBox>

---

## Qwiic / easyC Connector

<CenteredImage src="/img/easyc_transparent.png" alt="Qwiic/easyC connector" width="550px" />

<InfoBox>The **NULA Max RP2350** includes a **Qwiic/easyC connector** for plug-and-play I²C peripherals.  
This allows fast prototyping with sensors, displays, and other modules without soldering.</InfoBox>

<QuickLink
  title="Qwiic (formerly easyC) details and specifications"
  description="Learn more about Qwiic hardware compatibility and connector pinout."
  url="/qwiic"
/>

---

## Power Supply and Battery

- **USB-C port** used for programming and power input (5 V).  
- **VBAT (JST connector)** supports 3.7 V Li-Ion or Li-Poly batteries.  
- Integrated **Li-Ion charging circuit** with automatic charge/discharge management.  
- **VSYS** internally regulated to **3.3 V** for logic and peripherals.  

<InfoBox>When using a battery, the onboard charging circuit handles charging automatically via USB.  
For 5 V supply, always power the board through the **USB-C port**.</InfoBox>

---

## Jumper Details

This board includes **five hardware jumpers** for power management and peripheral configuration.


<FlickityCarousel
  images={[
    { src: '/img/nula-max-rp2350/jp1.png', alt: 'nula-max-jumper1', caption: 'JP1' },
    { src: '/img/nula-max-rp2350/jp2.png', alt: 'nula-max-jumper2', caption: 'JP2' },
    { src: '/img/nula-max-rp2350/jp3.png', alt: 'nula-max-jumper3', caption: 'JP3' },
    { src: '/img/nula-max-rp2350/jp4.png', alt: 'nula-max-jumper4', caption: 'JP4' },
    { src: '/img/nula-max-rp2350/jp5.png', alt: 'nula-max-jumper5', caption: 'JP5' },
  ]}
  jumpers={true}
/>


| Jumper  | Default State        | Function                                                 |
| ------- | -------------------- | -------------------------------------------------------- |
| **JP1** | NC (Normally Closed) | Disconnects Power LED to reduce standby current.         |
| **JP2** | NC (Normally Closed) | Enables MicroSD chip select line.                        |
| **JP3** | NC (Normally Closed) | Connects GPIO4 to the MicroSD card power enable line.    |
| **JP4** | NO (Normally Open)   | Keeps the microSD card powered at all times when closed. |
| **JP5** | NC (Normally Closed) | Enables Qwiic I²C interface.                             |

---

### Dimensions

- **Board size:** 69 × 58.5 mm (2.72 × 2.30 inch)  
- **Mounting**: Breadboard compatible  
- **Header Pin Holes:** 1.5 mm  
- **Screw Holes:** Designed for M3 screws (3.2 mm diameter)  

Soldered boards are LEGO compatible! 🧱 

---

## Hardware repository

Schematics, KiCad files, Gerber files and more can be found in the GitHub repository:

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