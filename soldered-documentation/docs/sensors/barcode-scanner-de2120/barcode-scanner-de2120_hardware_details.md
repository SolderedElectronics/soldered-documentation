---
slug: /barcode-scanner-de2120/hardware
title: DE2120 Barcode Scanner Hardware Details
sidebar_label: Hardware details
id: barcode-scanner-de2120-hardware
hide_title: true
---

# Hardware details

## Pinout

{/*
TODO: Add pinout image once available
<CenteredImage src="/img/barcode-scanner-de2120/pinout.png" alt="DE2120 Barcode Scanner Pinout" />

Click here for a high resolution image of the pinout.
*/}

## Pin details

| Pin Marking | Pin Name | Description |
|-------------|----------|-------------|
| **STAT** | Status Output | Active-low decode status output from the scanner. Pulled low on each successful barcode decode. Also drives the onboard blue status LED. Connect to any MCU GPIO to detect scans in hardware. |
| **TRIG** | Trigger Input | Active-low hardware scan trigger. Pull low to start a scan in manual mode. Also connected to the onboard trigger button (SW1). |
| **3V3** | Power | 3.3 V power rail. Outputs regulated 3.3 V when the board is powered from USB-C. Supply 3.3 V here when powering externally without USB-C. |
| **RX** | UART RX | Serial data input from microcontroller to scanner. Connect to MCU **TX** pin. |
| **TX** | UART TX | Serial data output from scanner to microcontroller. Connect to MCU **RX** pin. |
| **GND** | GND | Ground reference for power and signals. |

## Dimensions

- **Board Dimensions:** 55 × 23 mm (2.16 × 0.9 inches)
- **Header Pin Holes:** 1.5 mm
- **Screw Holes:** Designed for M3 screws (3.2 mm diameter)
- Soldered boards are LEGO compatible! 🧱

The DE2120 scan engine module itself measures **16.0 × 21.2 × 12.0 mm** and weighs less than 4 g.

## Jumper Details

{/*
TODO: Add jumper photos to /img/barcode-scanner-de2120/ and uncomment the carousel below.

<FlickityCarousel
  images={[
    { src: '/img/barcode-scanner-de2120/barcode-scanner-de2120_jp1.jpg', alt: 'barcode-scanner-jp1', caption: 'JP1' },
    { src: '/img/barcode-scanner-de2120/barcode-scanner-de2120_jp2.jpg', alt: 'barcode-scanner-jp2', caption: 'JP2' },
    { src: '/img/barcode-scanner-de2120/barcode-scanner-de2120_jp3.jpg', alt: 'barcode-scanner-jp3', caption: 'JP3' },
  ]}
  jumpers={true}
/>
*/}

| Jumper | Default State | Function |
|--------|--------------|----------|
| **JP1** | **NC** (Normally Closed) | Enables the **blue STAT LED** (D3). When closed (default), the LED lights on each successful barcode decode. Cut to disable the status LED. |
| **JP2** | **NC** (Normally Closed) | Enables the **onboard buzzer** (U2). When closed (default), the buzzer sounds on each successful decode. Cut to silence the buzzer. |
| **JP3** | **NC** (Normally Closed) | Enables the **purple power LED** (D2). When closed (default), the LED is lit whenever the board has power. Cut to disable the power indicator. |

## Hardware repository

{/*
TODO: Add hardware repository link once available
<QuickLink
  title="Barcode Scanner DE2120 Hardware Design"
  description="GitHub hardware repository for this product"
  url="https://github.com/SolderedElectronics/Barcode-Scanner-DE2120-hardware-design"
  image="/img/barcode-scanner-de2120/hw.png"
/>
*/}

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
