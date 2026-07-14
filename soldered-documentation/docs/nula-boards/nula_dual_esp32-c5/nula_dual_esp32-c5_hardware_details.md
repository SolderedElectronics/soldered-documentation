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
| **VBAT**    | Power     | Same net as the JST battery connector - an alternate connection point for a 3.7 V Li-Ion/Li-Poly battery. |
| **VCC**     | Power     | Output of the onboard power-source selection circuit. Follows USB 5 V when USB-C is connected, or the battery voltage otherwise - not a fixed, stable voltage. |
| **3V3**     | Power     | Regulated 3.3 V output from the onboard regulator.                 |
| **GND**     | Ground    | Common ground reference.                                           |
| **RESET**   | Control   | Active-low reset input, also wired to the onboard reset button.    |
| **RXD**     | UART      | UART receive pin.                                                  |
| **TXD**     | UART      | UART transmit pin.                                                 |
| **IO0**     | GPIO/ADC  | General-purpose I/O, ADC capable (A0).                             |
| **IO1**     | GPIO/ADC  | General-purpose I/O, ADC capable (A1).                             |
| **IO2**     | GPIO/ADC/SPI | ADC capable (A2). Default SPI **MISO**. Also the LP core's dedicated I2C data pin (LP_SDA). |
| **IO3**     | GPIO/ADC  | ADC capable (A3). Also the LP core's dedicated I2C clock pin (LP_SCL). |
| **IO4**     | GPIO/ADC/I2C | ADC capable (A4). Default I2C **SDA** pin (used by `Wire.begin()` with no arguments) - also feeds the Qwiic connector. Also the LP core's dedicated UART RX pin (LP_RX). |
| **IO5**     | GPIO/ADC/I2C | ADC capable (A5). Default I2C **SCL** pin - also feeds the Qwiic connector. Also the LP core's dedicated UART TX pin (LP_TX). |
| **IO6**     | GPIO/ADC/SPI | ADC capable (A6). Default SPI **SCK**.                          |
| **IO7**     | GPIO/ADC/SPI | ADC capable (A7). Default SPI **MOSI**.                         |
| **IO8**     | GPIO/ADC  | ADC capable (A8). Also drives the onboard WS2812B status LED, so anything you connect here interacts with that LED too. |
| **IO9**     | GPIO/ADC  | General-purpose I/O, ADC capable (A9).                             |
| **IO10**    | GPIO/ADC/SPI | ADC capable (A10). Default SPI **CS**.                          |
| **IO13**    | GPIO/ADC  | General-purpose I/O, ADC capable (A13).                            |
| **IO14**    | GPIO/ADC  | General-purpose I/O, ADC capable (A14).                            |
| **IO23**    | GPIO/ADC  | General-purpose I/O, ADC capable (A23).                            |
| **IO24**    | GPIO/ADC  | General-purpose I/O, ADC capable (A24).                            |
| **IO25**    | GPIO/ADC  | General-purpose I/O, ADC capable (A25).                            |
| **IO28**    | GPIO/ADC  | ADC capable (A28). Also wired to the onboard USER/boot-select button. |

<InfoBox>All GPIO pins operate at **3.3 V logic** - **do not connect 5 V signals directly to GPIO pins**. Always verify signal levels before connecting external peripherals.</InfoBox>

<InfoBox>**What are the LP pins?** The ESP32-C5 module on this board has two cores: the main high-performance (HP) core, which runs your Arduino sketch, and a separate low-power (LP) core that can keep running simple tasks (like watching a sensor over I2C) while the HP core sleeps to save power. The LP core has its own fixed I2C and UART peripherals, but they're not extra pins - they share the same physical pins as the HP core's default I2C and UART: **LP_SDA/LP_SCL** on IO2/IO3, and **LP_RX/LP_TX** on IO4/IO5. You only need to think about these if you're programming the LP core directly (e.g. via ESP-IDF's ULP/LP-core APIs); for normal Arduino sketches running on the HP core, these pins just behave as regular GPIO/I2C/UART pins.</InfoBox>

---

## Qwiic (formerly easyC) Connector

<CenteredImage src="/img/easyc_transparent.png" alt="Qwiic connector" width="550px" />

<InfoBox>The **NULA Dual ESP32-C5** includes a **Qwiic (formerly easyC) connector** for plug-and-play I²C peripherals. This allows fast prototyping with sensors, displays, and other modules without soldering.</InfoBox>

<QuickLink
  title="Qwiic (formerly easyC) details and specifications"
  description="Learn more about Qwiic hardware compatibility and connector pinout."
  url="/qwiic"
/>

---

## JST Battery Connector

The **NULA Dual ESP32-C5** includes a **JST connector** for connecting a **3.7 V Li-Ion or Li-Poly battery**, enabling fully wireless, battery-powered operation.

<InfoBox>Connect a **3.7 V Li-Ion or Li-Poly battery** via the onboard JST connector. The board includes an integrated battery charging circuit - when powered via USB-C, the battery will charge automatically.</InfoBox>

<QuickLink
  title="Li-Ion Battery 3.7 V"
  description="Rechargeable 3.7 V Li-Ion battery compatible with the NULA Dual ESP32-C5's JST connector."
  url="https://soldered.com/categories/power-sources-batteries/batteries/lithium-batteries/"
  image="/img/li-ion-battery/333284.jpg"
/>

---

## Power Supply

- **USB-C port** used for programming and power input (5 V).
- **JST battery connector** (also mirrored on the **VBAT** header pin) for a 3.7 V Li-Ion/Li-Poly battery, with an onboard charging circuit that charges the battery whenever USB-C is connected.
- An automatic power-source-selection circuit picks USB 5 V over the battery whenever both are present, exposed on the **VCC** header pin.
- An onboard regulator steps that supply down to a stable **3.3 V** rail for the module and all peripherals.
- Logic level is **3.3 V** - **do not connect 5 V signals directly to GPIO pins**.

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
| **JP2** | NC (Normally Closed) | Enables the power LED.                                |

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

- **Copper layers** (`.Cu.gbr`) - Defines the traces and pads on the board.
- **Solder mask layers** (`.Mask.gbr`) - Specifies the protective solder mask.
- **Silkscreen layers** (`.Silkscreen.gbr`) - Contains text and component markings.
- **Paste layers** (`.Paste.gbr`) - Used for stencil fabrication in SMD assembly.
- **Drill files** (`.drl`) - Provides drilling coordinates for vias and holes.
- **Board outline** (`.Edge_Cuts.gbr`) - Defines the shape of the PCB.
- **Gerber job file** (`.gbrjob`) - Describes the set of Gerber files used for production.

These files are ready for fabrication and can be used in PCB manufacturing.

#### Compliance

The **Compliance** section includes important regulatory and safety documentation for this product. These files ensure compliance with relevant industry standards and legal requirements.

- **CE** - Certification document confirming compliance with EU safety, health, and environmental requirements.
- **UKCA** - UKCA (UK Conformity Assessed) certification for the UK market.
- **Safety Instructions** - Safety guidelines and precautions in English and in German.
- **Info.txt** - Contains product details such as SKU, country of origin, HS tariff code, and barcode.

