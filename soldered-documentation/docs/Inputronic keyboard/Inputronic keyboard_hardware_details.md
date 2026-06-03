---
slug: /inputronic-keyboard-new/hardware
title: Inputronic Keyboard - Hardware details
sidebar_label: Hardware details
id: inputronic-keyboard-new-hardware
hide_title: false
---

## Pinout

<CenteredImage src="/img/inputronic_keyboard/pinout.png"/>

Click [**here**](/img/inputronic_keyboard/pinout.png) for a high-resolution image of the pinout.

## Pin details

| Pin Marking | Pin Name | Description |
| ----------- | -------- | ----------- |
| **VCC** | Power | Supply voltage (1.65V to 3.6V supported) |
| **GND** | Ground | Common ground for power and signals |
| **SDA** | Data | I²C data line for communication |
| **SCL** | Clock | I²C clock line for communication |
| **INT** | Interrupt | Active-low interrupt output (open-drain) |
| **RESET** | Reset | Active-low reset input |

<InfoBox>
This board operates at **1.65V to 3.6V**. Use it directly with 3.3V microcontrollers, or with a level shifter for 5V systems.
</InfoBox>

---

## Qwiic (formerly easyC)

<CenteredImage src="/img/easyc_transparent.png" alt="Qwiic (formerly easyC) cable" width="550px" />

<InfoBox>This board works with any **Qwiic (formerly easyC)** or **STEMMA QT** cable.</InfoBox>

<QuickLink 
  title="Qwiic (formerly easyC) details and specifications" 
  description="Learn about hardware specifications, compatibility, and usage of the Qwiic connector." 
  url="/qwiic" 
/>

---

## I²C address

The TCA8418 has a fixed 7-bit I²C address:

**0x34** (0b0110100)

<InfoBox>Unlike some I²C devices, the address on this board **cannot be changed** through hardware jumpers.</InfoBox>

---

## Dimensions

- **Board Dimensions:** 136 x 60 mm
- **Header Pin Holes:** 1.5 mm
- **Screw Holes:** Designed for M3 screws (3.2 mm diameter)
- Soldered boards are LEGO compatible! 🧱

---

## Jumper details

<InfoBox>Images coming soon.</InfoBox>

| Jumper | Default State | Function |
|--------|---------------|----------|
| **JP1** | Normally open | Optional 3.3V power connection |
| **JP2** | Normally open | Reset button connection option |

<InfoBox>The keyboard matrix is pre-configured with 80 tactile switches arranged in an 8×10 matrix. All switches are connected to the TCA8418 chip's ROW and COL pins internally.</InfoBox>

---

## Hardware repository

<WarningBox>The hardware repository for this board is not available yet! We're working on it. In the meantime, please [**contact us**](https://soldered.com/contact/) to receive the hardware files.</WarningBox>

The output folders are versioned. You can find which board version you have by checking the version mark on the PCB.

#### CAD files

We use KiCad, an open-source PCB design tool. You can open and edit the `.kicad_pro` project file, which includes both the schematic and PCB layout.

The `PANEL` files are used internally for production.

#### Schematic

The **OUTPUTS** folder contains the schematic in `.pdf` format, exported from KiCad.

#### BOM (Bill of Materials)

The bill of materials (BOM) is provided in two formats:

- A **standard `.csv` table**, listing all components, part numbers, and values.
- An **interactive BOM (`.html`)** that visually highlights each component on the PCB, making it easy to locate and reference parts.

#### 3D files

A **3D model** of the PCB is available in `.step` format, allowing you to inspect the board design in CAD software.

#### Gerber files

The repository includes standard Gerber outputs in a .zip file:

- **Copper layers** (`.Cu.gbr`): Defines the traces and pads on the board.
- **Solder mask layers** (`.Mask.gbr`): Specifies the protective solder mask.
- **Silkscreen layers** (`.Silkscreen.gbr`): Contains text and component markings.
- **Paste layers** (`.Paste.gbr`): Used for stencil fabrication in SMD assembly.
- **Drill files** (`.drl`): Provides drilling coordinates for vias and holes.
- **Board outline** (`.Edge_Cuts.gbr`): Defines the shape of the PCB.
- **Gerber job file** (`.gbrjob`): Describes the set of Gerber files used for production.

#### Compliance

Regulatory and safety documents for this product:

- **CE**: Certification document confirming compliance with EU safety, health, and environmental requirements.
- **UKCA**: UKCA (UK Conformity Assessed) certification for the UK market.
- **Safety Instructions**: Safety guidelines and precautions in English and in German.
- **Info.txt**: Contains product details such as SKU, country of origin, HS tariff code, and barcode.
