---
slug: /pam8406/hardware 
title: 5W Stereo Audio Amplifier PAM8406 - Hardware details
sidebar_label: Hardware details
id: pam8406-hardware 
hide_title: False
---

## Pinout

<CenteredImage src="/img/pam8406/Pinout.png" alt="5W Stereo Audio Amplifier PAM8406 pinout" caption="5W Stereo Audio Amplifier PAM8406 pinout" />

Click [**here**](/img/pam8406/Pinout.png) for a high-resolution image of the pinout.

## Pin details

### K1 - Audio input jack (3.5mm)

| Pin Marking | Pin Name | Description |
| ----------- | -------- | ----------- |
| **TIP** | INL | Left channel audio input |
| **RING** | INR | Right channel audio input |
| **SLEEVE** | AGND | Audio ground |

### K2 - Audio input header

An alternate way to feed the same stereo signal, useful when you'd rather wire audio in directly than use the jack:

| Pin Marking | Pin Name | Description |
| ----------- | -------- | ----------- |
| **INR** | Right channel in | Right channel audio input |
| **AGND** | Audio ground | Audio ground |
| **INL** | Left channel in | Left channel audio input |

### K3 - Power and control header

| Pin Marking | Pin Name | Description |
| ----------- | -------- | ----------- |
| **VCC** | Supply voltage | 2.5V to 5.5V |
| **GND** | Ground | Ground |
| **MUTE** | Mute | Active low. Internal pull-up keeps this high by default; pull low to mute |
| **SHDN** | Shutdown | Active low. Internal pull-up keeps this high by default; pull low to shut down |
| **MODE** | Mode select | Class-D / Class-AB select. High = Class-D (default), low = Class-AB |

### K4 / K5 - Speaker outputs

| Pin Marking | Pin Name | Description |
| ----------- | -------- | ----------- |
| **R+ / R-** | Right channel out | Right channel speaker output (screw terminal, K4) |
| **L+ / L-** | Left channel out | Left channel speaker output (screw terminal, K5) |

<InfoBox>
This board has no onboard voltage regulator. VCC is fed straight to the PAM8406, so the board runs at whatever voltage you supply it, anywhere from **2.5V to 5.5V**.
</InfoBox>

<WarningBox>
Do not exceed **6V** on VCC. This is the PAM8406's absolute maximum supply voltage, and going above it can permanently damage the chip.
</WarningBox>

<InfoBox>
**SHDN** and **MUTE** have internal pull-ups inside the PAM8406 itself, so both default high (amplifier active, unmuted) if left unconnected. This board's footprints for external pull-ups on these pins (R5/R6) aren't populated since they'd be redundant. **MODE** is different: the PAM8406 doesn't allow MODE to float, so this board adds its own external pull-up (R7) to hold it high, defaulting to Class-D.
</InfoBox>

---

## Jumper Details

This board contains two hardware jumpers; see below for their locations and functions:

| Jumper | Default State | Function |
| ------ | ------------- | -------- |
| **JP1** | NC (Normally closed) | Powers the onboard status LED. Cut to disconnect the LED from VCC |
| **JP2** | NC (Normally closed) | Ties analog and digital ground together. Cut to separate them for noise-sensitive setups |

---

## Dimensions

- **Board Dimensions:** 38 × 38 mm (1.50 × 1.50 in)
- **Header Pin Holes:** 1.5 mm
- **Screw Holes:** Designed for M3 screws (3.2 mm diameter)
- Soldered boards are LEGO compatible! 🧱

---

## Hardware repository

<WarningBox>The hardware repository for this board is not available yet! We're working on it.
In the meantime, please [**contact us**](https://soldered.com/contact/) to receive the hardware files.</WarningBox>

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
