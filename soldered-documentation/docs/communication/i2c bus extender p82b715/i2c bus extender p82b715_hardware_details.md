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

| **Pin** | **Description**                                                          |
|---------|---------------------------------------------------------------------------|
| SCL     | I²C clock line, local (Sx/Sy) side. Voltage set by **JP2** (5V or 3.3V). |
| SDA     | I²C data line, local (Sx/Sy) side. Voltage set by **JP1** (5V or 3.3V).  |
| VCC     | Fixed 5V, regardless of the JP1/JP2 SCL/SDA voltage setting.              |
| GND     | Ground.                                                                    |

<WarningBox>K3's VCC pin is always 5V, even if JP1/JP2 are set to 3.3V for SCL/SDA. If you're powering a 3.3V-only device from this header, don't use this pin, power it separately at 3.3V instead.</WarningBox>

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

<WarningBox>Jumper images for this board are not yet available. We're working on it!</WarningBox>

| **Jumper** | **Type**                 | **Function**                                                                                       |
|------------|--------------------------|----------------------------------------------------------------------------------------------------|
| **JP1**    | **NC** (3-pin selector)  | Selects the pull-up source for **SDA** on the local (Sx/Sy) side: 5V or 3.3V.                      |
| **JP2**    | **NC** (3-pin selector)  | Selects the pull-up source for **SCL** on the local (Sx/Sy) side: 5V or 3.3V.                      |
| **JP5**    | **NC** (Normally closed) | Enables the onboard power LED. Cut it to disconnect the LED circuit and turn off the power indicator. |

<InfoBox>

- JP1 and JP2 each connect the middle pin to one of the two outer pins, picking either the 5V or the 3.3V pull-up resistor for that line. Set both jumpers to the same voltage so SDA and SCL match.
- The extended side (screw terminal K4) has its own fixed 5V pull-ups and isn't affected by JP1/JP2.
- Remove the shunt on JP1/JP2 if your I²C bus already has external pull-up resistors, to avoid driving conflicts.
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
