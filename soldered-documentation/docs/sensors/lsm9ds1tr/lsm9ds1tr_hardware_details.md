---
slug: /lsm9ds1tr/hardware
title: LSM9DS1TR – Hardware details
sidebar_label: Hardware details
id: lsm9ds1tr-hardware
hide_title: False
---

## Pinout

<ErrorBox>The pinout image for this board hasn't been generated yet! We're working on it!</ErrorBox>

## Pin details

| Pin Marking  | Pin Name   | Description                                                                 |
|--------------|------------|-----------------------------------------------------------------------------|
| **VCC**      | Power      | Supply voltage (both 5V and 3V3 are supported).                             |
| **GND**      | Ground     | Common ground for power and signals.                                        |
| **SDA**      | Data       | I2C data line for communication.                                            |
| **SCL**      | Clock      | I2C clock line for communication.                                           |
| **INT1-A**   | Interrupt  | Accelerometer and gyroscope interrupt 1 signal.                             |
| **INT2-A**   | Interrupt  | Accelerometer and gyroscope interrupt 2 signal.                             |
| **INT-M**    | Interrupt  | Magnetic sensor interrupt signal.                                           |
| **DEN-A**    | Data Enable| Accelerometer and gyroscope data enable signal.                             |
| **RDY-M**    | Data Ready | Magnetic sensor data ready signal.                                          |
| **CS-M**     | Chip Select| SPI enable, I2C/SPI mode selection for the magnetometer.                     |
| **CS-A**     | Chip Select| SPI enable, I2C/SPI mode selection for the accelerometer and gyroscope.      |
| **SDO-M**    | Data Output| SPI serial data output (SDO) for the magnetometer, I2C address bit (SA0) for the magnetometer. |
| **SDO-A**    | Data Output| SPI serial data output (SDO) for the accelerometer and gyroscope, I2C address bit (SA0) for A/G. |

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

| Mode                    | Current Consumption |
|-------------------------|---------------------|
| Always-on eco power mode| down to 1.9 mA      |

| Mode           | Voltage Consumption |
|----------------|---------------------|
| Operating mode | ~3.3V               |

---

## Dimensions

- **Board Dimensions:** 3.5 mm × 3 mm x 1 mm (0.14 x 0.11 x 0.04 inch)
- **Header Pin Holes:** 1.5 mm  
- **Screw Holes:** Designed for M3 screws (3.2 mm diameter)  
- Soldered boards are LEGO compatible! 🧱 

---

## Jumper Details

This board contains hardware jumpers; see below for their locations and functions:

<FlickityCarousel
  images={[
    { src: '/img/lsm9ds1tr/lsm9ds1tr_1.png', alt: 'LSM9DS1 jumper 1', caption: 'JP1' },
    { src: '/img/lsm9ds1tr/lsm9ds1tr_2.png', alt: 'LSM9DS1 jumper 2', caption: 'JP2' },
    { src: '/img/lsm9ds1tr/lsm9ds1tr_3.png', alt: 'LSM9DS1 jumper 3', caption: 'JP3' },
    { src: '/img/lsm9ds1tr/lsm9ds1tr_4.png', alt: 'LSM9DS1 jumper 4', caption: 'JP4' },
    { src: '/img/lsm9ds1tr/lsm9ds1tr_5.png', alt: 'LSM9DS1 jumper 5', caption: 'JP5' },
    { src: '/img/lsm9ds1tr/lsm9ds1tr_6.png', alt: 'LSM9DS1 jumper 6', caption: 'JP6' },    
  ]}
  jumpers={true}
/>

| Jumper  | Default State            | Function                                                                                                                                    |
|---------|--------------------------|--------------------------------------------------------------------------------------------------------------------------------------------|
| **JP1** | **NC** (Normally closed) | Connects **SDA/SCL pull-up resistors to 5V** for I2C communication.                                                                          |
| **JP2** | **NC**                   | Connects **SDA/SCL pull-up resistors to 3.3V** for I2C communication.                                                                        |
| **JP3** | **NC**                   | **Address jumper** (more below) that allows swapping between 2 addresses.                                                                   |
| **JP4** | **NO** (Normally open)   | When shorted, it **bypasses the voltage regulator**, allowing the board to be powered **directly from 3.3V** via headers. **Ensure JP6 is disconnected if JP4 is connected.** |
| **JP5** | **NC**                   | Selects between **SPI** and **I2C** communication modes.                                                                                    |
| **JP6** | **NC**                   | When connected, the **voltage regulator is powered by 5V**, stepping it down to **3.3V**.                                                   |

---
## Address jumper

As mentioned before, the **JP3** is an **address jumper** for the **I2C address** that, when left **open**, has an address of **0x6A**, while when closed, its address changes to **0x6B**.

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