---  
slug: /apds-9960/hardware  
title: Apds-9960 – Hardware details
sidebar_label: Hardware details
id: apds-9960-hardware  
hide_title: False  
---

## Pinout

<CenteredImage src="/img/apds-9960/apds9960_pinout.png" alt="APDS-9960 pinout diagram" caption="APDS-9960 pinout diagram"/>

Click [**here**](/img/apds-9960/apds9960_pinout.png) for a high resolution image of the pinout.

---

## Pin Details

| Pin Marking | Pin Name | Description                                     |
| ----------- | -------- | ----------------------------------------------- |
| **VCC**     | Power    | Supply voltage (both 5V and 3V3 are supported). |
| **GND**     | Ground   | Common ground for power and signals.            |
| **SDA**     | Data     | I2C data line for communication.                |
| **SCL**     | Clock    | I2C clock line for communication.               |
| **VLED**    | Power    | Supply current for IR LED.                      |
| **INT**     | Control  | Interrupt signal (from APDS-9960).              |

<InfoBox>This breakout board operates at **3.3V logic level**, but includes an onboard regulator for **5V compatibility**, so it can be connected to both 3V3 and 5V logic boards!</InfoBox>

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

- **Sleep mode:** Uses just 1.0 µA, making it ideal for **low-power applications**.
- **Active mode:** Depends on the functions in use. Uses up to 100mA.

<InfoBox>For best results, consider utilizing sleep mode during inactivity and fine-tuning the IR LED timing for your specific needs.</InfoBox>

---

## Window Air Gap

<InfoBox>Skip this section if using the sensor in open air.</InfoBox>

**Crosstalk** is the output caused by unwanted reflection of LED IR rays, even in the absence of any object. To control this interference when the sensor is used in gesture mode, we recommend fitting a rubber isolating barrier over the sensor.

<CenteredImage src="/img/apds-9960/apds9960_window_gap.png" alt="APDS-9960 Barrier design" caption="APDS-9960 Barrier design" width="600px"/>

The rubber consists of two cylindrical openings, one for the **LED** and the other for the **Photodetector**. When assembled, the rubber barrier should form a good optical seal to the bottom of the window.

| Air Gap | PD Opening Diameter | LED Opening Diameter |
| ------- | ------------------- | -------------------- |
| 1mm     | 2mm                 | 1.5mm                |

---

## Dimensions

- **Board Dimensions:** 38 × 22 mm (1.5 × 0.9 inch)  
- **Header Pin Holes:** 1.5 mm  
- **Screw Holes:** Designed for M3 screws (3.2 mm diameter)  
- Soldered boards are LEGO compatible! 🧱 

---

## Jumper Details

This board contains hardware jumpers; see below for their locations and functions:

<FlickityCarousel
  images={[
    { src: '/img/apds-9960/jp1.jpg', alt: 'apds-9960jumper1', caption: 'JP1' },
    { src: '/img/apds-9960/jp2.jpg', alt: 'apds-9960jumper2', caption: 'JP2' },
    { src: '/img/apds-9960/jp3.jpg', alt: 'apds-9960jumper3', caption: 'JP3' },
    { src: '/img/apds-9960/jp4.jpg', alt: 'apds-9960jumper4', caption: 'JP4' },
    { src: '/img/apds-9960/jp5.jpeg', alt: 'apds-9960jumper5', caption: 'JP5' },
  ]}
  jumpers={true}
/>

| Jumper  | Default State            | Function                                                                                                                                                                      |
| ------- | ------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **JP1** | **NC** (Normally closed) | Connects **SDA/SCL pull-up resistors to 5V** for I2C communication.                                                                                                           |
| **JP2** | **NC** (Normally closed) | Connects **SDA/SCL pull-up resistors to 3.3V** for I2C communication.                                                                                                         |
| **JP3** | **NC** (Normally closed) | Disconnect to remove VLED power supply.                                                                                                                                          |
| **JP4** | **NC** (Normally closed) | When connected, the **voltage regulator is powered by 5V**, stepping it down to **3.3V for the IC**.                                                                          |
| **JP5** | **NO** (Normally open)   | When shorted, it **bypasses the voltage regulator**, allowing the board to be powered **directly from 3.3V** via headers. **Ensure JP4 is disconnected if JP5 is connected**. |

---

## Hardware repository

Schematics, KiCad files, Gerber files and more can be found in the GitHub repository:

<QuickLink 
  title="APDS-9960 Hardware design" 
  description="GitHub hardware repository for this product"
  url="https://github.com/SolderedElectronics/Color---gesture-sensor-APDS-9960-breakout-hardware-design" 
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