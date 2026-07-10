---
slug: /nula_w55rp20/hardware
title: NULA Ether W55RP20 - Hardware details
sidebar_label: Hardware details
id: nula_w55rp20-hardware
hide_title: True
---

# Hardware details

## Pinout

<CenteredImage src="/img/nula_w55rp20/Pinout.png" alt="NULA Ether W55RP20 pinout" caption="NULA Ether W55RP20 Pinout Diagram"/>

Click [**here**](/img/nula_w55rp20/Pinout.png) for a high-resolution version of the pinout.

---

## Pin details

The board labels its GPIO pins **IO0-IO29** on the silkscreen (matching Soldered's other NULA boards), rather than the RP2040's raw "GPn" numbering. Several RP2040 GPIOs are consumed internally by the W55RP20 package and aren't exposed on the header at all, IO17 and IO20-IO25 don't appear anywhere on the board for this reason.

| Pin Marking | Peripheral options       | Description                                                    |
| ----------- | ------------------------ | ---------------------------------------------------------------|
| **IO0**     | UART0 TX, PWM0A           | Digital I/O.                                                    |
| **IO1**     | UART0 RX, PWM0B           | Digital I/O.                                                    |
| **IO2**     | I2C1 SDA, PWM1A           | Digital I/O.                                                    |
| **IO3**     | I2C1 SCL, PWM1B           | Digital I/O.                                                    |
| **IO4**     | SPI0 MISO, UART1 TX, PWM2A | Digital I/O.                                                    |
| **IO5**     | SPI0 CS, UART1 RX, PWM2B  | Digital I/O.                                                    |
| **IO6**     | SPI0 SCK, PWM3A           | Digital I/O.                                                    |
| **IO7**     | SPI0 MOSI, PWM3B          | Digital I/O.                                                    |
| **IO8**     | PWM4A                     | Digital I/O.                                                    |
| **IO9**     | SD Enable, PWM4B              | Digital I/O. Also reads the microSD card detect signal.         |
| **IO10**    | SPI1 SCK, PWM5A           | Digital I/O. Shared with the onboard microSD reader, see [jumper details](#jumper-details). |
| **IO11**    | SPI1 MOSI, PWM5B          | Digital I/O. Shared with the onboard microSD reader.             |
| **IO12**    | SPI1 MISO, PWM6A          | Digital I/O. Shared with the onboard microSD reader.             |
| **IO13**    | SPI1 CS, PWM6B            | Digital I/O. Shared with the onboard microSD reader.             |
| **IO14**    | PWM7A                     | Digital I/O.                                                    |
| **IO15**    | PWM7B                     | Digital I/O.                                                    |
| **IO16**    | PWM0A                     | Digital I/O.                                                    |
| **IO18**    | PWM1A                     | Digital I/O.                                                    |
| **IO19**    | PWM1B                     | Digital I/O.                                                    |
| **IO26**    | PWM5A                     | Analog input or digital I/O.                                     |
| **IO27**    | PWM5B                     | Analog input or digital I/O.                                     |
| **IO28**    | I2C0 SDA, PWM6A           | Analog input or digital I/O.                                     |
| **IO29**    | I2C0 SCL, PWM6B           | Analog input or digital I/O.                                     |
| **VREF**    | -                         | ADC reference voltage.                                          |
| **RESET**   | -                         | Active-low reset input.                                         |
| **3V3**     | -                         | 3.3 V regulated output.                                          |
| **GND**     | -                         | Ground.                                                          |
| **VCC**     | -                         | 5 V input from USB-C.                                            |
| **VBAT**    | -                         | Battery input, see [battery support](#battery-support).         |

<WarningBox>**IO17 and IO20-IO25** are consumed internally by the W55RP20 chip package, confirmed against WIZnet's own pinout diagram for the chip, and don't appear on this board's header at all. There's nothing to connect to on those numbers.</WarningBox>

<InfoBox>The board also has a dedicated 3-pin **SWD debug header** (SWD, GND, CLK) near the reset button, for programming or debugging directly over SWD instead of USB.</InfoBox>

---

## Qwiic connector

<CenteredImage src="/img/easyc_transparent.png" alt="Qwiic connector" width="550px" />

<InfoBox>The board includes a **Qwiic connector** for I2C peripherals - sensors, displays, and other Qwiic-compatible modules connect without soldering.</InfoBox>

<QuickLink
  title="Qwiic details and specifications"
  description="Learn more about Qwiic hardware compatibility and connector pinout."
  url="/qwiic"
/>

---

## Power supply

- **USB-C** powers the board (5 V input, exposed on the **VCC** pin).
- Onboard regulator provides **3.3 V** for logic and peripherals.
- GPIO pins are **3.3 V logic only - not 5 V tolerant**.
- The board can also run from a battery, see [battery support](#battery-support) below.

---

## MicroSD card reader

The board has an onboard microSD card slot, connected over SPI1 (**IO10-IO13**), with **IO9** reading the card-detect signal. JP5-JP7 and JP9 let you disconnect those four pins from the card reader if you need them as general-purpose header pins instead.

<CenteredImage src="/img/nula_w55rp20/Pinout.png" alt="NULA Ether W55RP20 microSD reader location" caption="The microSD card slot sits near the top of the board, next to the SWD debug header" width="700px" />

---

## Battery support

The board has a **JST battery connector** and a **VBAT** pin, alongside a charge status indicator, so it can run from a single-cell Li-Ion/Li-Po battery instead of USB-C power. JP12 controls how the battery connector is routed onto the board.

---

## Jumper details

This board contains hardware jumpers. See below for their locations and functions:

{/* Add jumper images to /img/nula_w55rp20/ and uncomment the carousel below.

<FlickityCarousel
  images={[
    { src: '/img/nula_w55rp20/jp1.png', alt: 'nula-w55rp20-jp1', caption: 'JP1' },
    { src: '/img/nula_w55rp20/jp2.png', alt: 'nula-w55rp20-jp2', caption: 'JP2' },
    { src: '/img/nula_w55rp20/jp3.png', alt: 'nula-w55rp20-jp3', caption: 'JP3' },
    { src: '/img/nula_w55rp20/jp4.png', alt: 'nula-w55rp20-jp4', caption: 'JP4' },
    { src: '/img/nula_w55rp20/jp5.png', alt: 'nula-w55rp20-jp5', caption: 'JP5' },
    { src: '/img/nula_w55rp20/jp6.png', alt: 'nula-w55rp20-jp6', caption: 'JP6' },
    { src: '/img/nula_w55rp20/jp7.png', alt: 'nula-w55rp20-jp7', caption: 'JP7' },
    { src: '/img/nula_w55rp20/jp8.png', alt: 'nula-w55rp20-jp8', caption: 'JP8' },
    { src: '/img/nula_w55rp20/jp9.png', alt: 'nula-w55rp20-jp9', caption: 'JP9' },
    { src: '/img/nula_w55rp20/jp10.png', alt: 'nula-w55rp20-jp10', caption: 'JP10' },
    { src: '/img/nula_w55rp20/jp11.png', alt: 'nula-w55rp20-jp11', caption: 'JP11' },
    { src: '/img/nula_w55rp20/jp12.png', alt: 'nula-w55rp20-jp12', caption: 'JP12' },
  ]}
  jumpers={true}
/>

*/}

| Jumper   | Default state         | Function                              |
| -------- | ---------------------- | -------------------------------------- |
| **JP1**  | NC (Normally closed)   | 5 V I2C pull-up resistors.             |
| **JP2**  | NC (Normally closed)   | 3.3 V I2C pull-up resistors.           |
| **JP3**  | NC (Normally closed)   | MicroSD card power control.            |
| **JP4**  | NO (Normally open)     | Voltage regulator bypass.              |
| **JP5**  | NC (Normally closed)   | IO12 header connection.                |
| **JP6**  | NC (Normally closed)   | IO13 header connection.                |
| **JP7**  | NC (Normally closed)   | IO11 header connection.                |
| **JP8**  | NC (Normally closed)   | IO5 header connection.                 |
| **JP9**  | NC (Normally closed)   | IO10 header connection.                |
| **JP10** | NC (Normally closed)   | IO4 header connection.                 |
| **JP11** | NC (Normally closed)   | Qwiic/I2C connector routing.           |
| **JP12** | NC (Normally closed)   | Battery connector routing.             |

<InfoBox>
JP1 and JP2 are mutually exclusive, they select whether the onboard I2C pull-ups reference 5 V or 3.3 V. Don't close both at once.
</InfoBox>

<InfoBox>
JP5-JP7 and JP9 each disconnect one of IO10-IO13 from the onboard microSD reader's SPI1 bus, freeing that pin for use on the header instead. Cutting all four fully frees up the microSD reader's SPI1 bus for other uses.
</InfoBox>

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
