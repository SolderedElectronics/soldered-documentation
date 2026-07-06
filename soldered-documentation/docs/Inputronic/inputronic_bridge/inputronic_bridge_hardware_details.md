---
slug: /inputronic_bridge/hardware 
title: Inputronic BRIDGE - Hardware details
sidebar_label: Hardware details
id: inputronic_bridge-hardware 
hide_title: False
---

## Pinout 

<CenteredImage src="/img/inputronic_bridge/Pinout.png"/>

Click [**here**](/img/inputronic_bridge/Pinout.png) for a high-resolution image of the pinout.

## Pin details

| Pin Marking | Pin Name | Description |
| ----------- | -------- | ----------- |
| **FAULT** | USB fault (output only) | Goes active when the USB-A port's overcurrent protection trips |
| **MISO** | SPI data out | SPI mode only, active when JP4 is bridged |
| **SCK** | SPI clock | SPI mode only, active when JP4 is bridged |
| **MOSI** | SPI data in | SPI mode only, active when JP4 is bridged |
| **CS** | SPI chip select | SPI mode only, active when JP4 is bridged |
| **INT** | Interrupt | Tells the host MCU that a new HID event is ready to read |
| **SCL** | I²C clock | Default protocol, also present on both Qwiic connectors |
| **SDA** | I²C data | Default protocol, also present on both Qwiic connectors |
| **IO0** | Boot mode select | Hold low at power-up to flash new firmware; wired to the IO0 button |
| **RESET** | Reset | Active-low reset input; wired to the RESET button |
| **RX** | UART receive | UART mode only, active when JP3 is bridged |
| **TX** | UART transmit | UART mode only, active when JP3 is bridged |
| **3V3** | Power | 3.3V supply pin |
| **GND** | Ground | Common ground for power and signals |

<InfoBox>
The board runs its logic at **3.3V**, the native level of the ESP32-S3. The header pins are not 5V tolerant, so route them through a level shifter before wiring them to a 5V microcontroller.
</InfoBox>

---

## Qwiic
<CenteredImage src="/img/easyc_transparent.png" alt="EasyC/qwiic cable" width="550px" />
 
<InfoBox>This board is fully **Qwiic-compatible**! Just plug it into your board using a **Qwiic/easyC/STEMMA QT cable** and start coding!</InfoBox>

<QuickLink 
  title="Qwiic (formerly easyC) details and specifications" 
  description="Learn about hardware specifications, compatibility, and usage of the Qwiic connector." 
  url="/qwiic" 
/>

---

## I²C Address

The BRIDGE ships with a default 7-bit I²C address of **0x50**. Unlike sensors whose address is set by a hardwired pin, this one lives in the ESP32-S3's non-volatile storage, so it can be changed at any time to anywhere in the **0x08–0x77** range using the Arduino library's `changeI2CAddress()` function, without needing to touch a jumper or resolder anything.

---

## Dimensions 
- **Board Dimensions:** [BOARD_DIMENSIONS]
- **Header Pin Holes:** 1.5 mm
- **Screw Holes:** Designed for M3 screws (3.2 mm diameter)
- Soldered boards are LEGO compatible! 🧱

---

## Jumper Details

This board contains four hardware jumpers. See below for their locations and functions:

<ErrorBox>The jumper images for Inputronic BRIDGE haven't been generated yet! We're working on it!</ErrorBox>

| Jumper | Default State | Function |
|--------|---------------|----------|
| **JP1** | Closed | Power LED enable. Cut it to disconnect the purple PWR LED |
| **JP2** | Closed | 3.3V I²C pull-up enable. Cut it to remove the onboard 10 kΩ pull-ups on SDA/SCL |
| **JP3** | Open | Protocol select. Bridge it to switch the output protocol from I²C to UART |
| **JP4** | Open | Protocol select. Bridge it to switch the output protocol from I²C to SPI |

<InfoBox>
Leave both JP3 and JP4 open for the default I²C mode. Bridge only one of the two at a time, either JP3 for UART or JP4 for SPI, to match the protocol you pass to the library's `begin()` function.
</InfoBox>

---

## ESP32-S3FH4R2

The **ESP32-S3FH4R2** is the microcontroller running the show on this board. It handles the USB host stack that talks to the connected HID device, parses the incoming reports, and drives whichever output protocol you've selected. This particular variant packs a dual-core processor running at up to 240 MHz alongside 4 MB of flash and 2 MB of PSRAM, both integrated into the chip package.

<ErrorBox>The image of the ESP32-S3FH4R2 on the board hasn't been generated yet! We're working on it!</ErrorBox>

---

## Hardware repository

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
