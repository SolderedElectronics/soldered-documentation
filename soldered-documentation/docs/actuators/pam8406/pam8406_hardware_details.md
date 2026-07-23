---
slug: /pam8406/hardware 
title: 5W Stereo Audio Amplifier PAM8406 - Hardware details
sidebar_label: Hardware details
id: pam8406-hardware 
hide_title: False
---

## Pin details

### K1 - Audio input jack (3.5mm)

| Pin Marking | Pin Name | Description |
| ----------- | -------- | ----------- |
| **TIP** | Left channel in | Left channel audio input |
| **RING** | Right channel in | Right channel audio input |
| **SLEEVE** | GND | Analog ground |

### K2 - Audio input header

An alternate way to feed the same stereo signal, useful when you'd rather wire audio in directly than use the jack:

| Pin Marking | Pin Name | Description |
| ----------- | -------- | ----------- |
| **1** | Right channel in | Right channel audio input |
| **2** | GND | Analog ground |
| **3** | Left channel in | Left channel audio input |

### K3 - Power and control header

| Pin Marking | Pin Name | Description |
| ----------- | -------- | ----------- |
| **1** | MODE | Class-D / Class-AB select. High = Class-D (default), low = Class-AB |
| **2** | SHND | Shutdown, active low. Must be driven high for the amplifier to run |
| **3** | MUTE | Mute, active low. Must be driven high for audio output to pass through |
| **4** | GND | Ground |
| **5** | VCC | Supply voltage, 2.5V to 6V |

### K4 / K5 - Speaker outputs

| Pin Marking | Pin Name | Description |
| ----------- | -------- | ----------- |
| **K4** | Right channel out | Right channel speaker output (screw terminal) |
| **K5** | Left channel out | Left channel speaker output (screw terminal) |

<InfoBox>
This board has no onboard voltage regulator. VCC is fed straight to the PAM8406, so the board runs at whatever voltage you supply it, anywhere from **2.5V to 6V**.
</InfoBox>

<InfoBox>
**SHND** and **MUTE** don't have onboard pull-ups, so they float if left unconnected. Tie both to VCC (or drive them high from a microcontroller) to bring the amplifier out of shutdown and hear audio. **MODE** does have an onboard pull-up, so it defaults to Class-D if you don't connect anything to it.
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

## PAM8406DR

The board is built around the **PAM8406**, a Diodes Incorporated Class-D/AB switchable stereo amplifier in an SOP-16 package. It's the only active IC on the board: all output filtering, muting, and mode switching happens around it, and the control header exposes its MODE, SHND, and MUTE pins directly.

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

Gerber files are essential for PCB manufacturing. The repository includes copper layers, solder mask, silkscreen, paste layers, drill files, board outline, and the Gerber job file.

#### Compliance

The **Compliance** section includes CE, UKCA, Safety Instructions, and an Info.txt file.
