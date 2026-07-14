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

The board labels its GPIO pins **IO0-IO29** on the silkscreen, the same convention used on Soldered's other NULA boards, instead of the RP2040's raw "GPn" numbering. Several RP2040 GPIOs are consumed internally by the W55RP20 package and aren't exposed on the header at all, IO17 and IO20-IO25 don't appear anywhere on the board for this reason.

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
| **IO9**     | SD Enable, PWM4B              | Digital I/O. Controls power to the onboard microSD card through a switch, see [jumper details](#jumper-details). |
| **IO10**    | SPI1 SCK, PWM5A           | Digital I/O. Hardwired to the onboard microSD reader.             |
| **IO11**    | SPI1 MOSI, PWM5B          | Digital I/O. Hardwired to the onboard microSD reader.             |
| **IO12**    | SPI1 MISO, PWM6A          | Digital I/O. Hardwired to the onboard microSD reader.             |
| **IO13**    | SPI1 CS, PWM6B            | Digital I/O. Connects to the onboard microSD reader's CS line only if JP1 is bridged, see [jumper details](#jumper-details). |
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

The board has an onboard microSD card slot, connected over SPI1 (**IO10-IO13**). **IO9** controls power to the card through an onboard switch (see **JP3** and **JP4** in [jumper details](#jumper-details)), and **IO13** only reaches the card's CS line if **JP1** is bridged.

<CenteredImage src="/img/nula_w55rp20/Pinout.png" alt="NULA Ether W55RP20 microSD reader location" caption="The microSD card slot sits near the top of the board, next to the SWD debug header" width="700px" />

---

## Battery support

The board has a **JST battery connector** and a **VBAT** pin, alongside a charge status indicator, so it can run from a single-cell Li-Ion/Li-Po battery instead of USB-C power.

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
| **JP1**  | NO (Normally open)     | Connects **IO13** to the onboard microSD reader's CS line. |
| **JP2**  | NC (Normally closed)   | 3.3 V I2C pull-up resistors for the Qwiic connector's SDA/SCL lines. |
| **JP3**  | NC (Normally closed)   | Connects **IO9** to the microSD power switch's control gate. |
| **JP4**  | NO (Normally open)     | Bypasses the microSD power switch, tying the card's power rail directly to 3.3 V. |
| **JP5**  | NC (Normally closed)   | Power LED (purple).                    |
| **JP6**  | NC (Normally closed)   | Ethernet duplex status LED (yellow).   |
| **JP7**  | NC (Normally closed)   | Ethernet speed status LED (green).     |
| **JP8**  | NC (Normally closed)   | Ethernet link status LED (blue).       |
| **JP9**  | NC (Normally closed)   | Ethernet activity status LED (red).    |
| **JP10** | Selectable              | Selects the W5500's **PMODE0** pin: pull-up (3.3 V, default) or pull-down (GND). |
| **JP11** | Selectable              | Selects the W5500's **PMODE1** pin: pull-up (3.3 V, default) or pull-down (GND). |
| **JP12** | Selectable              | Selects the W5500's **PMODE2** pin: pull-up (3.3 V, default) or pull-down (GND). |

Together, JP10-JP12 set the W5500's PHY operation mode at power-up. Each jumper is independently selectable, so all eight combinations below are possible:

| JP10 (PMODE0) | JP11 (PMODE1) | JP12 (PMODE2) | Resulting mode |
| ------------- | ------------- | ------------- | --------------- |
| Pull-down     | Pull-down     | Pull-down     | 10BT half-duplex, auto-negotiation disabled |
| Pull-up       | Pull-down     | Pull-down     | 10BT full-duplex, auto-negotiation disabled |
| Pull-down     | Pull-up       | Pull-down     | 100BT half-duplex, auto-negotiation disabled |
| Pull-up       | Pull-up       | Pull-down     | 100BT full-duplex, auto-negotiation disabled |
| Pull-down     | Pull-down     | Pull-up       | 100BT half-duplex, auto-negotiation enabled |
| Pull-up       | Pull-down     | Pull-up       | Not used |
| Pull-down     | Pull-up       | Pull-up       | Not used |
| **Pull-up (default)** | **Pull-up (default)** | **Pull-up (default)** | **All modes capable, auto-negotiation enabled** |

<InfoBox>The factory default (all three jumpers pulled up) lets the W5500 auto-negotiate speed and duplex with whatever it's plugged into - the right choice for almost everyone. The other combinations force a fixed speed/duplex, useful mainly for troubleshooting a link that won't auto-negotiate correctly with older or unusual network hardware.</InfoBox>

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
