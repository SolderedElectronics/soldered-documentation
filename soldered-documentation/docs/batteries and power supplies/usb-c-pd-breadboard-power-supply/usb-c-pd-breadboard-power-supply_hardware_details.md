---
slug: /usb-c-pd-breadboard-power-supply/hardware 
title: Hardware details
id: usb-c-pd-breadboard-power-supply-hardware 
hide_title: False
---

## Pinout
<CenteredImage src="/img/usb-c-pd-breadboard-power-supply/pinout.png" alt="Pinout"/>

Click [**here**](/img/usb-c-pd-breadboard-power-supply/pinout.png) for a high-resolution image of the pinout.

## Pin Details

| Pin Marking | Pin Name | Description                                                                 |
| ----------- | -------- | --------------------------------------------------------------------------- |
| **VOUT** | Voltage Out| Negotiated output voltage supplied to the breadboard and terminal block.   |
| **GND** | Ground   | Common ground.                                                              |
| **SDA** | I2C Data | Optional I2C data line for dynamic configuration of the HUSB238 chip.      |
| **SCL** | I2C Clock| Optional I2C clock line for dynamic configuration of the HUSB238 chip.     |

---


## Jumper Details

This board contains a hardware jumper; see below for its location and function:

<ErrorBox>The jumper images for the USB-C PD Breadboard Power Supply haven't been generated yet! We're working on it!</ErrorBox>

| Jumper  | Default State            | Function                                                                                          |
| ------- | ------------------------ | ------------------------------------------------------------------------------------------------- |
| **JP1** | **NC** (Normally closed) | When shorted, it provides power to the onboard power LED                              |

---


## Switch Details

This board contains switches that control the voltage output, current limits, and power state.
<ErrorBox>The swtich images for the USB-C PD Breadboard Power Supply haven't been generated yet! We're working on it!</ErrorBox>

| Switch                 | Function                                                                                         |
| ---------------------- | ------------------------------------------------------------------------------------------------ |
| **ON/OFF Switch**      | Switches power to the board on or off.                                                           |
| **Voltage Selection**  | Hardware switches used to request standard USB-PD voltage levels (5V, 9V, 12V, 15V, 18V, 20V).   |
| **Current Selection**  | Hardware switches used to set the current limit (1.25A, 1.5A, 2A, 2.5A, 3A, 3.25A).              |

---

## Dimensions

- **Board Dimensions:** 54 x 30mm (2.1 x 1.2 inches)
- **Header Pin Holes:** 1.5 mm  
- **Screw Holes:** Designed for M3 screws (3.2 mm diameter)  
- Soldered boards are LEGO-compatible! 🧱

---

## HUSB238 USB-PD Controller

The board features the **HUSB238** integrated circuit as its core USB Power Delivery sink controller. It is designed to automatically negotiate standard PD voltage steps and predefined current limits from a USB-C source without the need for external software or microcontrollers.

---

## Hardware repository

Schematics, KiCad files, Gerber files, and more can be found in the GitHub repository:

<ErrorBox>The repository link for the USB-C PD Breadboard Power Supply haven't been generated yet! We're working on it!</ErrorBox>

The hardware repository contains everything you need to understand, modify, or manufacture the board. The various output folders are versioned. You can check which board version you have specifically by finding the version mark on the PCB. Below is an overview of the available files.

#### CAD files
We use KiCad, an open-source PCB design tool. You can open and edit the `.kicad_pcb` and `.kicad_sch` files to inspect the board design in CAD software.

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
- **Safety Instructions** – Safety guidelines and precautions provided in English and German.
- **Info.txt** – Contains product details such as SKU, country of origin, HS tariff code, and barcode.