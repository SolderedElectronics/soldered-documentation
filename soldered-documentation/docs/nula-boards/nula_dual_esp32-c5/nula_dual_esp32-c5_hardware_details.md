---
slug: /nula_dual_esp32-c5/hardware
title: NULA Dual ESP32-C5 - Hardware details
sidebar_label: Hardware details
id: nula_dual_esp32-c5-hardware
hide_title: True
---

# Hardware details

## Pinout

<CenteredImage src="/img/nula_dual_esp32-c5/Pinout.png" alt="NULA Dual ESP32-C5 pinout" caption="NULA Dual ESP32-C5 Pinout Diagram"/>

Click [**here**](/img/nula_dual_esp32-c5/Pinout.png) for a high-resolution version of the pinout.

---

## Pin Details

| Pin Marking | Type      | Description                                                        |
| ----------- | --------- | ------------------------------------------------------------------ |
| **VBAT**    | Power     | Battery voltage input.                                             |
| **VCC**     | Power     | 5 V power input.                                                   |
| **3V3**     | Power     | Regulated 3.3 V output from onboard regulator.                     |
| **GND**     | Ground    | Common ground reference.                                           |
| **RESET**   | Control   | Active-low reset input.                                            |
| **RXD**     | UART      | UART receive pin.                                                  |
| **TXD**     | UART      | UART transmit pin.                                                 |
| **IO0**     | GPIO      | General-purpose I/O, boot mode select.                             |
| **IO1**     | GPIO/ADC  | General-purpose I/O, ADC capable.                                  |
| **IO2**     | GPIO/ADC  | General-purpose I/O, ADC capable.                                  |
| **IO3**     | GPIO/ADC  | General-purpose I/O, ADC capable.                                  |
| **IO4**     | GPIO/ADC  | General-purpose I/O, ADC capable.                                  |
| **IO5**     | GPIO/ADC  | General-purpose I/O, ADC capable.                                  |
| **IO6**     | GPIO      | General-purpose I/O, SPI/I²C/UART capable.                        |
| **IO7**     | GPIO      | General-purpose I/O, SPI/I²C/UART capable.                        |
| **IO28**    | GPIO      | General-purpose I/O.                                               |

<InfoBox>All GPIO pins operate at **3.3 V logic** — pins are **not 5 V tolerant**. Always verify signal levels before connecting external peripherals.</InfoBox>

---

## Qwiic / easyC Connector

<CenteredImage src="/img/easyc_transparent.png" alt="Qwiic/easyC connector" width="550px" />

<InfoBox>The **NULA Dual ESP32-C5** includes a **Qwiic/easyC connector** for plug-and-play I²C peripherals. This allows fast prototyping with sensors, displays, and other modules without soldering.</InfoBox>

<QuickLink
  title="Qwiic (formerly easyC) details and specifications"
  description="Learn more about Qwiic hardware compatibility and connector pinout."
  url="/qwiic"
/>

---

## Power Supply

- **USB-C port** used for programming and power input (5 V).
- **VBUS** exposes the raw 5 V USB supply on the pin header.
- Onboard regulator provides a stable **3.3 V** rail for both modules and all peripherals.
- Logic level is **3.3 V** — GPIO pins are **not 5 V tolerant**.

---

## Jumper Details

This board contains hardware jumpers. See below for their locations and functions:

{/* Add jumper images to /img/nula_dual_esp32-c5/ and uncomment the carousel below.

<FlickityCarousel
  images={[
    { src: '/img/nula_dual_esp32-c5/jp1.png', alt: 'nula-dual-esp32-c5-jp1', caption: 'JP1' },
    { src: '/img/nula_dual_esp32-c5/jp2.png', alt: 'nula-dual-esp32-c5-jp2', caption: 'JP2' },
  ]}
  jumpers={true}
/>

*/}

| Jumper  | Default State        | Function                                              |
| ------- | -------------------- | ----------------------------------------------------- |
| **JP1** | NC (Normally Closed) | Enables onboard 3.3 V I²C pull-up resistors.          |
| **JP2** | NO (Normally Open)   | When closed, enables the power LED.                   |

---

## Dimensions

- **Board dimensions:** 26 × 63 mm (1.02 × 2.48 inch)
- **Header Pin Holes:** 1.5 mm
- **Screw Holes:** Designed for M3 screws (3.2 mm diameter)

Soldered boards are LEGO compatible! 🧱

---

## Hardware repository

Schematics, KiCad files, Gerber files and more can be found in the GitHub repository:

<WarningBox>The hardware repository for this board is not available yet! We're working on it. In the meantime, please [**contact us**](https://soldered.com/contact/) to receive the hardware files.</WarningBox>

{/* Once the repo is live, replace the WarningBox above with:

<QuickLink
  title="NULA Dual ESP32-C5 Hardware Design"
  description="GitHub hardware repository for this product"
  url="https://github.com/SolderedElectronics/..."
/>

*/}

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
