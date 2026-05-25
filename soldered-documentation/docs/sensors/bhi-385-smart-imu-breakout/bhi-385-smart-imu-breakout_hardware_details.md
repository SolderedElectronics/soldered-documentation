---
slug: /bhi-385-smart-imu-breakout/hardware
title: BHI385 Smart IMU - Hardware details
sidebar_label: Hardware details
id: bhi-385-smart-imu-breakout-hardware
hide_title: false
---

## Pinout

<CenteredImage src="/img/bhi-385-smart-imu-breakout/BHI385 Smart IMU Breakout Pinout.png" alt="BHI385 Smart IMU Breakout Pinout"/>

## Pin details

| Pin Marking | Pin Name  | Description                                                        |
| ----------- | --------- | ------------------------------------------------------------------ |
| **INT**     | Interrupt | Active interrupt output from the BHI385 HIRQ pin (3.3V logic)     |
| **GND**     | Ground    | Common ground for power and signals                                |
| **3V3**     | Power     | 3.3V supply input                                                  |
| **SCL**     | Clock     | I2C clock line (3.3V level, level-shifted to 1.8V on board)       |
| **SDA**     | Data      | I2C data line (3.3V level, level-shifted to 1.8V on board)        |

<InfoBox>This board operates from a **3.3V supply**. An onboard SE5218DLG-LF LDO regulator generates the **1.8V** rail required by the BHI385, and a dual NMOS level-shifter translates I2C signals between the 1.8V sensor domain and the 3.3V host interface. The board is **not** directly 5V-tolerant on the I2C lines without an external level-shifter.</InfoBox>

---

## Qwiic (formerly easyC)

<CenteredImage src="/img/easyc_transparent.png" alt="EasyC/qwiic cable" width="550px" />

<InfoBox>This board is fully **Qwiic-compatible**! Just plug it into your board using a **Qwiic/easyC/STEMMA QT cable** and start coding!</InfoBox>

<QuickLink 
  title="Qwiic (formerly easyC) details and specifications" 
  description="Learn about hardware specifications, compatibility, and usage of the Qwiic connector." 
  url="/qwiic" 
/>

---

## Jumper Details

This board contains hardware jumpers; see below for their locations and functions:

<ErrorBox>The jumper images for BHI385 Smart IMU Breakout haven't been generated yet! We're working on it!</ErrorBox>

| Jumper  | Default State            | Function                                                                                                                                             |
| ------- | ------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| **JP1** | **NC** (Normally closed) | Connects the **3.3V-side pull-up resistors** (both SDA and SCL) on the I2C level-shifter to the 3V3 rail.                                            |
| **JP2** | **NC** (Normally closed) | Connects the **1.8V-side pull-up resistors** (both SDA and SCL) on the I2C level-shifter to the 1.8V rail.                                           |
| **JP3** | **NO** (Normally open)   | Connects the **3.3V rail to the input of the onboard LDO regulator**. Bridge to power the LDO from 3V3; leave open to isolate the regulator input.   |
| **JP4** | **NC** (Normally closed) | Connects the **EN pin** of the onboard SE5218DLG-LF LDO to the 3.3V rail, enabling the regulator.                                                    |
| **JP5** | **0x29**                 | Selects the **I2C address**: bridge towards **0x29** (HSDO = VDDIO, default) or **0x28** (HSDO = GND).                                               |

---

## Dimensions

- **Board Dimensions:** 22 × 22 mm
- **Header Pin Holes:** 1.5 mm
- **Screw Holes:** Designed for M3 screws (3.2 mm diameter)
- Soldered boards are LEGO compatible! 🧱

---

## BHI385 Smart IMU

The BHI385 is a programmable Smart IMU from Bosch Sensortec that combines a high-dynamic 6-DoF inertial measurement unit with an internal 32-bit Fuser2 microcontroller core (based on the Synopsys ARC EM4 architecture). On this breakout, it is powered from the onboard 1.8V LDO regulator and communicates with the host over a level-shifted I2C bus. Because the BHI385 features a volatile, RAM-based memory architecture with no persistent internal flash storage, the host microcontroller must upload the firmware binary to the chip's program RAM on every power-on before any virtual sensors or edge AI features can be activated.

---

## Datasheet

Refer to the official BHI385 datasheet for full electrical specifications, register maps, and firmware interface details.

<QuickLink  
  title="BHI385 Datasheet"  
  description="Complete technical reference for the Bosch BHI385 Smart IMU, including register maps, electrical characteristics, and firmware protocol."  
  url="https://www.bosch-sensortec.com/media/boschsensortec/downloads/datasheets/bst-bhi385-ds000.pdf"  
/>

---

## Hardware repository

<WarningBox>The hardware repository for this board is not available yet! We're working on it.
In the meantime, please [**contact us**](https://soldered.com/contact/) to receive the hardware files.</WarningBox>

The hardware repository contains everything you need to understand, modify, or manufacture the board.
The different output folders are versioned. You can check which board version you have specifically by
finding the version mark on the PCB.

Below is an overview of the available files.

#### CAD files

We use KiCad, an open-source PCB design tool. You can open and edit the `.kicad_pro` project file,
which includes both the schematic and PCB layout.

The `PANEL` files are used internally for production.

#### Schematic

The **OUTPUTS** folder contains the **schematic** in `.pdf` format, exported from KiCad.

#### BOM (Bill of Materials)

The bill of materials (BOM) is provided in two formats:

- A **standard `.csv` table**, listing all components, part numbers, and values.
- An **interactive BOM (`.html`)** that visually highlights each component on the PCB, making it
  easy to locate and reference parts.

#### 3D files

A **3D model** of the PCB is available in `.step` format, allowing you to inspect the board design
in CAD software.

#### Gerber files

Gerber files are essential for PCB manufacturing. The repository includes copper layers, solder mask,
silkscreen, paste layers, drill files, board outline, and the Gerber job file.

#### Compliance

The **Compliance** section includes CE, UKCA, Safety Instructions, and an Info.txt file.
