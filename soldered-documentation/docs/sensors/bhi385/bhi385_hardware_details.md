---
slug: /bhi385/hardware
title: BHI385 – Hardware details
sidebar_label: Hardware details
id: bhi385-hardware
hide_title: False
---

## Pinout

{/* TODO: add pinout image once available
<CenteredImage src="/img/bhi385/bhi385_pinout.png" alt="BHI385 Smart IMU Breakout pinout" caption="BHI385 Smart IMU Breakout pinout" />
*/}

<ErrorBox>The pinout image for this board hasn't been generated yet! We're working on it!</ErrorBox>

---

## Pin details

| Pin Marking | Pin Name  | Description                                                              |
| ----------- | --------- | ------------------------------------------------------------------------ |
| **GND**     | Ground    | Common ground for power and signals (connected to K3 2-pin header).      |
| **INT**     | Interrupt | Active-high interrupt output from BHI385. Asserted when FIFO has data.  |
| **SCL**     | Clock     | I2C clock line (3.3V logic level, level-shifted onboard to 1.8V).        |
| **SDA**     | Data      | I2C data line (3.3V logic level, level-shifted onboard to 1.8V).         |
| **3V3**     | Power     | 3.3V supply input. Powers the onboard LDO and I2C level shifter.         |
| **GND**     | Ground    | Common ground for power and signals (connected to K4 4-pin header).      |

<InfoBox>

The board operates from a **3.3V supply**. An onboard **SE5218DLG LDO regulator** generates the **1.8V** required by the BHI385 chip. An integrated **NMOS dual level shifter** translates I2C signals between the 1.8V chip domain and the 3.3V host interface — no external components are needed.

</InfoBox>

---

## Qwiic (formerly easyC)

<CenteredImage src="/img/easyc_transparent.png" alt="EasyC/qwiic cable" width="550px" />

<InfoBox>This board is fully **Qwiic-compatible**! Just plug it into your board using a **Qwiic/easyC/STEMMA QT cable** and start coding! The board has **two Qwiic connectors** so you can daisy-chain other Qwiic devices on the same bus.</InfoBox>

<QuickLink
  title="Qwiic (formerly easyC) details and specifications"
  description="Learn about hardware specifications, compatibility, and usage of the Qwiic connector."
  url="/qwiic"
/>

---

## Power consumption

The values below are chip-level measurements from the Bosch BHI385 datasheet. Actual board-level consumption may be slightly higher due to the onboard LDO regulator and I2C level shifter.

| Mode                               | Current Consumption |
| ---------------------------------- | ------------------- |
| Sleep mode                         | ~5 µA               |
| Accelerometer only (low-power)     | ~200 µA             |
| Accelerometer + Gyroscope (normal) | ~1.4 mA             |

---

## Dimensions

{/* TODO: measure board and fill in dimensions */}

- **Board Dimensions:** (to be measured)
- **Header Pin Holes:** 1.5 mm
- **Screw Holes:** Designed for M3 screws (3.2 mm diameter)
- Soldered boards are LEGO-compatible! 🧱

---

## Jumper Details

This board contains hardware jumpers; see below for their locations and functions:

{/* TODO: add jumper photos once available
<FlickityCarousel
  images={[
    { src: '/img/bhi385/bhi385_jp1.png', alt: 'BHI385 jumper JP1', caption: 'JP1' },
    { src: '/img/bhi385/bhi385_jp2.png', alt: 'BHI385 jumper JP2', caption: 'JP2' },
    { src: '/img/bhi385/bhi385_jp3.png', alt: 'BHI385 jumper JP3', caption: 'JP3' },
    { src: '/img/bhi385/bhi385_jp4.png', alt: 'BHI385 jumper JP4', caption: 'JP4' },
    { src: '/img/bhi385/bhi385_jp5.png', alt: 'BHI385 jumper JP5', caption: 'JP5' },
  ]}
  jumpers={true}
/>
*/}

| Jumper  | Default State            | Function                                                                                                          |
| ------- | ------------------------ | ----------------------------------------------------------------------------------------------------------------- |
| **JP1** | **NC** (Normally closed, pins 1–2) | Connects **SDA pull-up resistor to 3.3V**. Bridge pins 2–3 instead to use **1.8V pull-up** (for 1.8V hosts). |
| **JP2** | **NC** (Normally closed, pins 1–2) | Connects **SCL pull-up resistor to 3.3V**. Bridge pins 2–3 instead to use **1.8V pull-up** (for 1.8V hosts). |
| **JP3** | **NC** (Normally closed) | Connects 3.3V supply to the onboard **1.8V LDO regulator** (SE5218DLG). Keep closed for normal operation.       |
| **JP4** | **NC** (Normally closed) | LDO ground path. Part of the voltage regulation circuit. Keep closed for normal operation.                        |
| **JP5** | **NO** (Normally open)   | **I2C address jumper**. Open = address **0x29** (default). Bridge to connect HSDO to GND = address **0x28**.     |

---

## Address jumper

The **JP5** jumper controls the BHI385 I2C address by connecting the **HSDO** (host SDO) pin either to the onboard 1.8V pull-up resistor or to GND:

- **JP5 open** (default): HSDO is pulled to 1.8V → I2C address **0x29** (`BHI385_I2C_ADDR_HIGH`)
- **JP5 bridged**: HSDO is connected to GND → I2C address **0x28** (`BHI385_I2C_ADDR_LOW`)

<InfoBox>

The default address is **0x29**. When using the Soldered Arduino library, always call `imu.begin(BHI385_I2C_ADDR_HIGH)` unless you have bridged JP5.

</InfoBox>

---

## Hardware repository

<WarningBox>The hardware repository for this board is not available yet! We're working on it. In the meantime, please <a href="https://soldered.com/contact/"><b>contact us</b></a> to receive the hardware files.</WarningBox>

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
