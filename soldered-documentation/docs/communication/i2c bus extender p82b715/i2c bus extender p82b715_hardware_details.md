---
slug: /i2c-bus-extender-p82b715/hardware
title: P82B715 I2C Bus Extender - Hardware details
sidebar_label: Hardware details
id: i2c bus extender p82b715-hardware
hide_title: false
---

## Pinout

<CenteredImage src="/img/i2c bus extender p82b715/Pinout.png" alt="P82B715 pinout diagram" caption="P82B715 pinout diagram"/>

Click [**here**](/img/i2c%20bus%20extender%20p82b715/Pinout.png) for a high resolution image of the pinout.

---

## Pin details

### Qwiic connectors (K1, K2): local 3.3V I2C side

| **Pin** | **Description**                          |
|---------|------------------------------------------|
| GND     | Ground.                                  |
| 3V3     | 3.3V power input from the Qwiic cable.  |
| SDA     | I²C data line, local (3.3V) side.      |
| SCL     | I²C clock line, local (3.3V) side.     |

### Pin header (K3): local side breakout

| **Pin** | **Description**                                                     |
|---------|----------------------------------------------------------------------|
| GND     | Ground.                                                              |
| VCC     | 5V from the onboard boost converter.                                 |
| SDA     | I²C data line on the P82B715's Sx/Sy side. Always 5V logic.        |
| SCL     | I²C clock line on the P82B715's Sx/Sy side. Always 5V logic.       |

<WarningBox>K3 is a 5V header. Its SDA and SCL sit at 5V logic and VCC is 5V, whatever you do with JP1 and JP2, which only switch the pull-ups. Don't power a 3.3V-only device from this header, and don't wire its SDA/SCL straight to a 3.3V-only part. Use a Qwiic port instead, that side is level shifted to 3.3V.</WarningBox>

### Screw terminal (K4): extended bus side

| **Pin** | **Description**                                                         |
|---------|-------------------------------------------------------------------------|
| SCL     | Buffered I²C clock line, connects to the long cable / remote device.  |
| SDA     | Buffered I²C data line, connects to the long cable / remote device.   |
| GND     | Ground.                                                                 |

<InfoBox>
Connect your microcontroller to the **Qwiic ports (K1 or K2)** on the local side. Connect your long cable or remote I²C device to the **screw terminal (K4)** on the extended side. The onboard boost converter and level shifter operate automatically, so there's no configuration needed for basic use.
</InfoBox>

---

## Qwiic

<CenteredImage src="/img/easyc_transparent.png" alt="Qwiic cable" width="550px" />

<InfoBox>This board is fully **Qwiic-compatible**! Just plug it into your microcontroller using a **Qwiic/STEMMA QT cable** and start coding!</InfoBox>

<QuickLink 
  title="Qwiic details and specifications" 
  description="Learn about hardware specifications, compatibility, and usage of the Qwiic connector." 
  url="/qwiic" 
/>

---

## Jumper details

This board contains hardware jumpers; see below for their locations and functions:

{/* TODO: add the JP1, JP2 and JP5 jumper photos here once available */}

| **Jumper** | **Type**                 | **Function**                                                                                       |
|------------|--------------------------|----------------------------------------------------------------------------------------------------|
| **JP1**    | **NC** (3-pad SMD jumper) | Connects the **5V** rail to the SDA and SCL pull-ups on the 5V nets (K3 and the P82B715's Sx/Sy). One trace per line, so you can cut either or both. |
| **JP2**    | **NC** (3-pad SMD jumper) | Connects the **3V3** rail to the SDA and SCL pull-ups on the Qwiic side of the level shifter. One trace per line.                                    |
| **JP5**    | **NC** (Normally closed) | Enables the onboard power LED. Cut it to disconnect the LED circuit and turn off the power indicator. |

<InfoBox>

- JP1 and JP2 each have a centre pad on a supply rail and a trace running out to the SDA and the SCL pull-up. They pick which side of the level shifter gets pulled up, not which voltage a line runs at.
- The local pull-ups are 10 kΩ. The extended side (screw terminal K4) has its own fixed 470 Ω pull-ups to 5V and isn't affected by JP1 or JP2.
- Cut a JP1 or JP2 trace if your I²C bus already has external pull-up resistors, to avoid running them in parallel.
- JP5 is closed by default, so the power LED is on out of the box. Cut it if you want to disable the LED.

</InfoBox>

---

## Power consumption

- **Power input:** 3.3V via Qwiic
- **Onboard boost converter:** Generates 5V internally for the P82B715 buffer chip
- **Power LED:** Purple indicator LED, on by default. Cut JP5 to disable it

---

## Dimensions

- **Board Dimensions:** 22 × 38 mm (0.9 × 1.5 inch)
- **Header Pin Holes:** 1.0 mm
- **Screw Holes:** Designed for M3 screws (3.2 mm diameter)
- Soldered boards are LEGO compatible! 🧱

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

- **Copper layers** (`.Cu.gbr`): the traces and pads on the board.
- **Solder mask layers** (`.Mask.gbr`): the protective solder mask.
- **Silkscreen layers** (`.Silkscreen.gbr`): text and component markings.
- **Paste layers** (`.Paste.gbr`): used for stencil fabrication in SMD assembly.
- **Drill files** (`.drl`): drilling coordinates for vias and holes.
- **Board outline** (`.Edge_Cuts.gbr`): the shape of the PCB.
- **Gerber job file** (`.gbrjob`): describes the set of Gerber files used for production.

These files are ready for fabrication and can be used in PCB manufacturing.

#### Compliance

The **Compliance** section includes important regulatory and safety documentation for this product. These files ensure compliance with relevant industry standards and legal requirements.

- **CE**: certification document confirming compliance with EU safety, health, and environmental requirements.
- **UKCA**: UKCA (UK Conformity Assessed) certification for the UK market.
- **Safety Instructions**: safety guidelines and precautions in English and German.
- **Info.txt**: product details such as SKU, country of origin, HS tariff code, and barcode.
