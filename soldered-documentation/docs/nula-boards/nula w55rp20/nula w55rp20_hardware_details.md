---
slug: /nula_w55rp20/hardware
title: NULA Ether W55RP20 - Hardware details
sidebar_label: Hardware details
id: nula_w55rp20-hardware
hide_title: True
---

# Hardware details

## Pinout

<CenteredImage src="/img/nula w55rp20/Pinout.png" alt="NULA Ether W55RP20 pinout" caption="NULA Ether W55RP20 Pinout Diagram"/>

Click [**here**](/img/nula w55rp20/Pinout.png) for a high-resolution version of the pinout.

---

## Pin details

| Pin Marking  | Type     | Description                                                               |
| ------------ | -------- | ------------------------------------------------------------------------- |
| **3V3**      | Power    | 3.3 V regulated output.                                                   |
| **VBUS**     | Power    | 5 V from the USB-C connector.                                             |
| **GND**      | Ground   | Ground.                                                                   |
| **RUN**      | Control  | Active-low reset.                                                         |
| **GP0–GP15** | GPIO     | General-purpose I/O with peripheral support (UART, SPI, I²C, PWM).       |
| **GP16**     | SPI/MISO | Internally connected to W5500 — do not use as general GPIO.               |
| **GP17**     | SPI/CS   | Internally connected to W5500 — do not use as general GPIO.               |
| **GP18**     | SPI/CLK  | Internally connected to W5500 — do not use as general GPIO.               |
| **GP19**     | SPI/MOSI | Internally connected to W5500 — do not use as general GPIO.               |
| **GP20**     | Control  | Internally connected to W5500 RST — do not use as general GPIO.           |
| **GP21**     | Control  | Internally connected to W5500 INT — do not use as general GPIO.           |
| **GP22**     | GPIO     | General-purpose I/O with peripheral support.                              |
| **GP26**     | ADC/GPIO | ADC channel 0.                                                            |
| **GP27**     | ADC/GPIO | ADC channel 1.                                                            |
| **GP28**     | ADC/GPIO | ADC channel 2.                                                            |

<WarningBox>**GP16–GP21** are internally routed to the W5500 Ethernet controller. Using them for other purposes will break Ethernet communication.</WarningBox>

<InfoBox>The board uses a **dual-row pin header layout**: the **inner rows** have **female (socket) pins** and the **outer rows** have **male (pin) headers**. This allows the board to be used standalone with jumper wires, or stacked via the inner female pins.</InfoBox>

---

## Qwiic connector

<CenteredImage src="/img/easyc_transparent.png" alt="Qwiic connector" width="550px" />

<InfoBox>The board includes a **Qwiic connector** for I²C peripherals — sensors, displays, and other Qwiic-compatible modules connect without soldering.</InfoBox>

<QuickLink
  title="Qwiic details and specifications"
  description="Learn more about Qwiic hardware compatibility and connector pinout."
  url="/qwiic"
/>

---

## Power supply

- **USB-C** powers the board (5 V input).
- **VBUS** exposes the raw 5 V USB supply on the pin header.
- Onboard regulator provides **3.3 V** for logic and peripherals.
- GPIO pins are **3.3 V logic only — not 5 V tolerant**.

---

## Jumper details

This board contains hardware jumpers. See below for their locations and functions:

{/* Add jumper images to /img/nula w55rp20/ and uncomment the carousel below.

<FlickityCarousel
  images={[
    { src: '/img/nula w55rp20/jp1.png', alt: 'nula-w55rp20-jp1', caption: 'JP1' },
    { src: '/img/nula w55rp20/jp2.png', alt: 'nula-w55rp20-jp2', caption: 'JP2' },
    { src: '/img/nula w55rp20/jp3.png', alt: 'nula-w55rp20-jp3', caption: 'JP3' },
    { src: '/img/nula w55rp20/jp4.png', alt: 'nula-w55rp20-jp4', caption: 'JP4' },
    { src: '/img/nula w55rp20/jp5.png', alt: 'nula-w55rp20-jp5', caption: 'JP5' },
    { src: '/img/nula w55rp20/jp6.png', alt: 'nula-w55rp20-jp6', caption: 'JP6' },
    { src: '/img/nula w55rp20/jp7.png', alt: 'nula-w55rp20-jp7', caption: 'JP7' },
    { src: '/img/nula w55rp20/jp8.png', alt: 'nula-w55rp20-jp8', caption: 'JP8' },
    { src: '/img/nula w55rp20/jp9.png', alt: 'nula-w55rp20-jp9', caption: 'JP9' },
    { src: '/img/nula w55rp20/jp10.png', alt: 'nula-w55rp20-jp10', caption: 'JP10' },
    { src: '/img/nula w55rp20/jp11.png', alt: 'nula-w55rp20-jp11', caption: 'JP11' },
    { src: '/img/nula w55rp20/jp12.png', alt: 'nula-w55rp20-jp12', caption: 'JP12' },
  ]}
  jumpers={true}
/>

*/}

| Jumper   | Default state        | Function                                                                   |
| -------- | -------------------- | -------------------------------------------------------------------------- |
| **JP1**  | NC (Normally closed) | Connects GPIO13 to the microSD card CS line. Open to disable SD SPI.      |
| **JP2**  | NC (Normally closed) | Enables onboard 10 kΩ I²C pull-up resistors on the Qwiic SCL/SDA lines.  |
| **JP3**  | NC (Normally closed) | Connects GPIO09 to the PMOS gate for software-controlled microSD power.   |
| **JP4**  | NO (Normally open)   | When closed, keeps 3V3_MICROSD always powered, bypassing GPIO09 control.  |
| **JP5**  | NC (Normally closed) | Enables the purple power LED (D4). Open to disable it.                    |
| **JP6**  | NC (Normally closed) | Enables the yellow duplex status LED (D5).                                |
| **JP7**  | NC (Normally closed) | Enables the green speed status LED (D6).                                  |
| **JP8**  | NC (Normally closed) | Enables the blue link status LED (D7).                                    |
| **JP9**  | NC (Normally closed) | Enables the red activity LED (D8).                                        |
| **JP10** | NO (Normally open)   | PHY mode bit 0 (PMODE0). Pull-down to GND via 10 kΩ. Close to set HIGH.  |
| **JP11** | NO (Normally open)   | PHY mode bit 1 (PMODE1). Pull-down to GND via 10 kΩ. Close to set HIGH.  |
| **JP12** | NO (Normally open)   | PHY mode bit 2 (PMODE2). Pull-down to GND via 10 kΩ. Close to set HIGH.  |

**JP10–JP12** set the Ethernet PHY operating mode of the W5500. All open = all bits LOW (mode `000`):

| JP12 (PMODE2) | JP11 (PMODE1) | JP10 (PMODE0) | Mode                                       |
| ------------- | ------------- | ------------- | ------------------------------------------ |
| 0             | 0             | 0             | 10BT Half-Duplex, auto-negotiation off     |
| 0             | 0             | 1             | 10BT Full-Duplex, auto-negotiation off     |
| 0             | 1             | 0             | 100BT Half-Duplex, auto-negotiation off    |
| 0             | 1             | 1             | 100BT Full-Duplex, auto-negotiation off    |
| 1             | 0             | 0             | 100BT Half-Duplex, auto-negotiation on     |
| 1             | 0             | 1             | Not used                                   |
| 1             | 1             | 0             | Not used                                   |
| 1             | 1             | 1             | All capable, auto-negotiation on           |

---

## Dimensions

- **Board dimensions:** 68.6 × 58.4 mm (2.70 × 2.30 inch)
- **Header pin holes:** 1.5 mm
- **Screw holes:** Designed for M3 screws (3.2 mm diameter)

Soldered boards are LEGO compatible! 🧱

---

## Hardware repository

Schematics, KiCad files, Gerber files and more can be found in the GitHub repository:

<WarningBox>The hardware repository for this board is not available yet! We're working on it. In the meantime, please [**contact us**](https://soldered.com/contact/) to receive the hardware files.</WarningBox>

{/* Once the repo is live, replace the WarningBox above with:

<QuickLink
  title="NULA Ether W55RP20 Hardware Design"
  description="GitHub hardware repository for this product"
  url="https://github.com/SolderedElectronics/..."
/>

*/}

The hardware repository contains everything you need to understand, modify, or manufacture the board. The different output folders are versioned. You can check which board version you have by finding the version mark on the PCB.

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

- **Copper layers** (`.Cu.gbr`) — Defines the traces and pads on the board.
- **Solder mask layers** (`.Mask.gbr`) — Specifies the protective solder mask.
- **Silkscreen layers** (`.Silkscreen.gbr`) — Contains text and component markings.
- **Paste layers** (`.Paste.gbr`) — Used for stencil fabrication in SMD assembly.
- **Drill files** (`.drl`) — Provides drilling coordinates for vias and holes.
- **Board outline** (`.Edge_Cuts.gbr`) — Defines the shape of the PCB.
- **Gerber job file** (`.gbrjob`) — Describes the set of Gerber files used for production.

These files are ready for fabrication and can be used in PCB manufacturing.

#### Compliance

The **Compliance** section includes important regulatory and safety documentation for this product. These files ensure compliance with relevant industry standards and legal requirements.

- **CE** — Certification document confirming compliance with EU safety, health, and environmental requirements.
- **UKCA** — UKCA (UK Conformity Assessed) certification for the UK market.
- **Safety Instructions** — Safety guidelines and precautions in English and in German.
- **Info.txt** — Contains product details such as SKU, country of origin, HS tariff code, and barcode.
