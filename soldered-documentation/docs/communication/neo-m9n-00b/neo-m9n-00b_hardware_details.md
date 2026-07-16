---
slug: /neo-m9n-00b/hardware 
title: NEO-M9N-00B - Hardware details
sidebar_label: Hardware details
id: neo-m9n-00b-hardware 
hide_title: False
---

## Pinout

<CenteredImage src="/img/neo-m9n-00b/Pinout.png" alt="NEO-M9N-00B pinout diagram" caption="NEO-M9N-00B pinout diagram"/>

Click [**here**](/img/neo-m9n-00b/Pinout.svg) for a high resolution image of the pinout.

---

## Pin Details

| Pin Marking | Pin Name | Description |
| ----------- | -------- | ----------- |
| **GND** | Ground | Common ground reference for the module. |
| **VCC** | Power | Main power input for the board. |
| **3V3** | Power | 3.3V regulated power output/input. |
| **SDA** | Data / SPI CS | I2C serial data line, or SPI chip select when the module is switched to SPI mode (see **JP4** below). |
| **SCL** | Clock / SPI SCK | I2C serial clock line, or SPI clock when the module is switched to SPI mode. |
| **TX** | UART TX / SPI MISO | UART transmit pin, or SPI MISO when the module is switched to SPI mode. |
| **RX** | UART RX / SPI MOSI | UART receive pin, or SPI MOSI when the module is switched to SPI mode. |
| **RESET** | Control | Resets the GNSS module. |
| **INT** | Interrupt | Interrupt output pin for event notifications. |
| **PPS** | Timing | Pulse-per-second timing output for precise synchronization applications. |
| **SAFEBOOT** | Control | Forces the module into safe boot mode for firmware recovery or updates. Leave open for normal operation. |

<InfoBox>This breakout board operates at **3.3V logic level** and includes onboard power regulation for compatibility with both **3.3V and 5V systems**.</InfoBox>

<InfoBox>The **SDA/SCL/TX/RX** pins are shared between I2C, UART, and SPI. Which function is active depends on the **JP4** jumper, see the [Jumper Details](#jumper-details) section below.</InfoBox>

---

## Antenna connector

The board also features a connector for an external GNSS antenna.

<CenteredImage src="/img/neo-m9n-00b/antenna.png" alt="Antenna connector on board" caption="Antenna connector on board" width="600px" />

<InfoBox>**JP5** is closed by default, supplying bias voltage to the antenna's center pin for an active (amplified) antenna. If you're using a passive antenna, open **JP5** instead, see [Jumper Details](#jumper-details) below.</InfoBox>

---

## Qwiic

<CenteredImage src="/img/easyc_transparent.png" alt="Qwiic cable" width="550px" />

<InfoBox>This board is fully **Qwiic-compatible**! Just plug it into your board using a **Qwiic cable** and start coding!</InfoBox>

<QuickLink 
  title="Qwiic details and specifications" 
  description="Learn about hardware specifications, compatibility, and usage of the Qwiic connector." 
  url="/qwiic" 
/>

---

## Power Consumption

Current draw depends on how many constellations are enabled at once and whether power save mode is active:

| Mode | GPS+GLONASS+Galileo+BeiDou | GPS+GLONASS | GPS only |
| ---- | -------------------------- | ----------- | -------- |
| Peak (acquisition) | 100 mA | 100 mA | 100 mA |
| Acquisition | 50 mA | 43 mA | 36 mA |
| Tracking (continuous mode) | 36 mA | 32 mA | 28 mA |
| Tracking (power save mode) | 21 mA | 20 mA | 19 mA |

<InfoBox>For lower power consumption, reduce the navigation update rate and disable unused GNSS constellations when possible.</InfoBox>

---

## Backup battery

The board has an onboard holder for a **CR1220 coin-cell battery**, which keeps the module's real-time clock and almanac data alive whenever main power is removed. With a backup battery installed, the module can perform a much faster **hot** or **warm start** the next time it's powered up, instead of a full cold start that has to re-download almanac data from scratch.

<InfoBox>The backup battery is optional. Without one, the module still works normally, it just takes longer to get its first fix after a power cycle.</InfoBox>

---


## Dimensions

- **Board Dimensions:** 38 × 54 mm (1.5 × 2.1 inch)
- **Header Pin Holes:** 1.5 mm
- **Screw Holes:** Designed for M3 screws (3.2 mm diameter)
- Soldered boards are LEGO compatible! 🧱

---

## Jumper Details

This board contains hardware jumpers; see below for their locations and functions:

<FlickityCarousel
  images={[
    { src: '/img/neo-m9n-00b/JP1.png', alt: 'neo-m9n-00b-jp1', caption: 'JP1' },
    { src: '/img/neo-m9n-00b/JP2.png', alt: 'neo-m9n-00b-jp2', caption: 'JP2' },
    { src: '/img/neo-m9n-00b/JP3.png', alt: 'neo-m9n-00b-jp3', caption: 'JP3' },
    { src: '/img/neo-m9n-00b/JP4.png', alt: 'neo-m9n-00b-jp4', caption: 'JP4' },
    { src: '/img/neo-m9n-00b/JP5.png', alt: 'neo-m9n-00b-jp5', caption: 'JP5' },
  ]}
  jumpers={true}
/>

| Jumper | Default State | Function |
| ------- | ------------------------ | -------- |
| **JP1** | **NC** (Normally closed) | Enables the power LED. |
| **JP2** | **NC** (Normally closed) | Connects SDA/SCL pull-ups to 3.3V. |
| **JP3** | **NC** (Normally closed) | Enables the PPS LED. |
| **JP4** | **Selectable** | Selects **D_SEL**: default = I2C + UART, re-bridged = SPI only. |
| **JP5** | **NC** (Normally closed) | Supplies antenna bias voltage for an active antenna. |

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

- **Copper layers** (`.Cu.gbr`) - Defines the traces and pads on the board.  
- **Solder mask layers** (`.Mask.gbr`) - Specifies the protective solder mask.  
- **Silkscreen layers** (`.Silkscreen.gbr`) - Contains text and component markings.  
- **Paste layers** (`.Paste.gbr`) - Used for stencil fabrication in SMD assembly.  
- **Drill files** (`.drl`) - Provides drilling coordinates for vias and holes.  
- **Board outline** (`.Edge_Cuts.gbr`) - Defines the shape of the PCB.  
- **Gerber job file** (`.gbrjob`) - Describes the set of Gerber files used for production.  

These files are ready for fabrication and can be used in PCB manufacturing.

#### Compliance  

The **Compliance** section includes important regulatory and safety documentation for this product. These files ensure compliance with relevant industry standards and legal requirements.  

- **CE** - Certification document confirming compliance with EU safety, health, and environmental requirements.  
- **UKCA** - UKCA (UK Conformity Assessed) certification for the UK market.  
- **Safety Instructions** - Safety guidelines and precautions in English and in German.
- **Info.txt** - Contains product details such as SKU, country of origin, HS tariff code, and barcode.