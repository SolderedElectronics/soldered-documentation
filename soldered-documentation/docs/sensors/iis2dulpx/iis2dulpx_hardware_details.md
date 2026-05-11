---
slug: /iis2dulpx/hardware 
title: Hardware details
id: iis2dulpx-hardware 
hide_title: False
---

## Pinout

<CenteredImage src="/img/iis2dulpx/iis2dulpx-pinout.png" alt="IIS2DULPX Accelerometer breakout pinout" caption="IIS2DULPX Accelerometer breakout pinout" />

Click [**here**](/img/iis2dulpx/iis2dulpx-pinout.png) for a high-resolution image of the pinout.

## Pin details

| Pin Marking | Pin Name  | Description                                      |
| ----------- | --------- | ------------------------------------------------ |
| **VCC**     | Power     | Supply voltage (both 5V and 3.3V are supported). |
| **GND**     | Ground    | Common ground for power and signals.             |
| **SDA**     | Data      | I2C data line for communication.                 |
| **SCL**     | Clock     | I2C clock line for communication.                |
| **INT1**    | Interrupt | Programmable interrupt output 1.                 |
| **INT2**    | Interrupt | Programmable interrupt output 2.                 |

<InfoBox>This breakout board operates on supply voltages of 3.3V and 5V thanks to the onboard voltage regulator.</InfoBox>

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

## Power consumption

The IIS2DULPX is designed for ultra-low-power operation, making it ideal for wearables, industrial IoT, and battery-powered applications.

| Mode                             | Current Consumption |
| -------------------------------- | ------------------- |
| High Performance (all ODRs)      | 9.3 µA              |
| Low Power (50 Hz)                | 6.5 µA              |
| Ultra Low Power (1.6 Hz)         | 3 µA                |
| Deep power-down                  | 12 nA               |

---

## Dimensions

- **Board Dimensions:** 22 × 22 mm / 0.9 × 0.9 inch
- **Screw Holes:** Designed for M3 screws (3.2 mm diameter)
- Soldered boards are LEGO-compatible!

---

## Jumper Details

<FlickityCarousel
  images={[
    { src: '/img/iis2dulpx/jp1.png', alt: 'JP1', caption: 'JP1' },
    { src: '/img/iis2dulpx/jp2.png', alt: 'JP2', caption: 'JP2' },
    { src: '/img/iis2dulpx/jp3.png', alt: 'JP3', caption: 'JP3' },
    { src: '/img/iis2dulpx/jp4.png', alt: 'JP4', caption: 'JP4' },
  ]}
  jumpers={true}
/>

| Jumper  | Default State            | Function                                                                                                       |
| ------- | ------------------------ | -------------------------------------------------------------------------------------------------------------- |
| **JP1** | **NC** (Normally closed) | Connects **SDA/SCL pull-up resistors to 5V** for I2C communication.                                           |
| **JP2** | **NC** (Normally closed) | Connects **SDA/SCL pull-up resistors to 3.3V** for I2C communication.                                         |
| **JP3** | **NC** (Normally closed) | When closed, the onboard **3.3V voltage regulator is active**. Cut to disconnect the LDO from the 3.3V rail.  |
| **JP4** | **NO** (Normally open)   | When shorted, **bypasses the voltage regulator**, allowing the board to be powered **directly from 3.3V** via headers. Ensure JP3 is cut if JP4 is shorted. |

---

## Hardware repository

<QuickLink
  title="IIS2DULPX Accelerometer breakout hardware repository"
  description="Schematics, PCB layout, BOM, 3D files, and Gerber files for the IIS2DULPX Accelerometer breakout board."
  url="https://github.com/SolderedElectronics/IIS2DULPXTR-Accelerometer-brakeout-hardware-design"
/>

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
