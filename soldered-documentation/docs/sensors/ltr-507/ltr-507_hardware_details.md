---
slug: /ltr-507/hardware
title: "LTR-507 Light and Proximity Sensor \u2013 Hardware details"
id: ltr-507-hardware
hide_title: false
---
## Pinout

<CenteredImage src="/img/ltr-507/pinout.jpg" alt="APDS-9960 pinout diagram" caption="LTR-507 pinout diagram"/>

Click [**here**](/img/ltr-507/pinout.jpg) for a high-resolution image of the pinout.

---

## Pin details

| Pin Marking | Pin Name | Description                                     |
| ----------- | -------- | ----------------------------------------------- |
| **VCC**     | Power    | Supply voltage (both 5V and 3V3 are supported). |
| **GND**     | Ground   | Common ground for power and signals.            |
| **SDA**     | Data     | I2C data line for communication.                |
| **SCL**     | Clock    | I2C clock line for communication.               |
| **VLED**    | Power    | Current supply for the proximity LED.           |
| **INT**     | Control  | Interrupt signal (from LTR-507).                |

<WarningBox>**IMPORTANT: An IR LED must be connected for the proximity sensor to function!**</WarningBox>

<InfoBox>This breakout board operates at **3.3V logic level**, but includes an onboard regulator for **5V compatibility** so it can be connected to both 3V3 and 5V logic boards!</InfoBox>

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

## Power Consumption

The LTR-507ALS-01 sensor is designed for low power consumption, making it suitable for battery-powered applications.

- **Low-power mode**: 0.2mA

<InfoBox>Low-power mode is not implemented in our library.</InfoBox>

- **Active mode**: 2.3 mA

<InfoBox>Power consumption can be minimized by utilizing **interrupt** and **sleep** modes!</InfoBox>

---

## Dimensions

- **Board Dimensions:** 38 × 22 mm (1.5 × 0.9 inch)  
- **Header Pin Holes:** 1.5 mm  
- **Screw Holes:** Designed for M3 screws (3.2 mm diameter)  
- Soldered boards are LEGO compatible! 🧱

---

## Jumper Details

This board contains hardware jumpers. See below for their locations and functions:

<FlickityCarousel
  images={[
    { src: '/img/ltr-507/jp1.png', alt: 'ltr507jumper1', caption: 'JP1' },
    { src: '/img/ltr-507/jp2.png', alt: 'ltr507jumper2', caption: 'JP2' },
    { src: '/img/ltr-507/jp3.png', alt: 'ltr507jumper3', caption: 'JP3' },
    { src: '/img/ltr-507/jp4.png', alt: 'ltr507jumper4', caption: 'JP4' },
    { src: '/img/ltr-507/jp5.png', alt: 'ltr507jumper5', caption: 'JP5' },
  ]}
  jumpers={true}
/>

| Jumper  | Default State            | Function                                                                                                                                                                       |
| ------- | ------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **JP1** | **NC** (Normally closed) | Connects the **SDA/SCL pull-up resistors to 5V** for I2C communication.                                                                                                        |
| **JP2** | **NC** (Normally closed) | Connects the **SDA/SCL pull-up resistors to 3.3V** for I2C communication.                                                                                                      |
| **JP3** | **NC** (Normally closed) | Address selection (default I2C address **0x3A**).                                                                                                                             |
| **JP4** | **NC** (Normally closed) | When connected, the **voltage regulator is powered by 5V**, which steps it down to **3.3V for the IC**.                                                                         |
| **JP5** | **NO** (Normally open)   | When shorted, it **bypasses the voltage regulator**, allowing the board to be powered **directly from 3.3V** via headers. **Ensure that JP4 is disconnected if JP5 is connected.** |

---

## Address Selection

The LTR-507 sensor has a configurable **7-bit I2C address**, determined by the state of the **SEL pin**. Depending on how the pin is connected, the sensor will respond to one of three possible addresses:

| **SEL Pin State** | **I2C Address** |
| ----------------- | --------------- |
| **GND (0)**       | `0x23`          |
| **VCC (1)**       | `0x26`          |
| **Floating**      | `0x3A`          |

If your **I2C scanner detects address `0x3A`**, this means the **SEL pin is floating** (not connected to either GND or VCC).

<InfoBox>To change the address, connect **SEL to GND or VCC** as needed via the **JP3**.</InfoBox>

---

## Hardware repository

Schematics, KiCad files, Gerber files, and more can be found in the GitHub repository:

<QuickLink 
  title="Digital light & proximity sensor LTR-507 breakout Hardware Design" 
  description="GitHub hardware repository for this product"
  url="https://github.com/SolderedElectronics/Digital-light---proximity-sensor-LTR-507ALS-breakout-hardware-design" 
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
- **Safety Instructions** – Safety guidelines and precautions in both English and German.
- **Info.txt** – Contains product details such as SKU, country of origin, HS tariff code, and barcode.