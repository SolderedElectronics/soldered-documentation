---
slug: /rs-485/hardware
title: Rs 485 - Hardware details
sidebar_label: Hardware details
id: rs-485-hardware
hide_title: false
---

## Pinout

<CenteredImage src="/img/rs-485/RS-485-breakout.png" alt="RS-485 transceiver pinout diagram" caption="RS-485 transceiver pinout diagram"/>

Click [**here**](/img/rs-485/RS-485-breakout.png) for a high-resolution image of the pinout.

---

## Pin Details

| **Pin Marking** | **Pin Name**       | **Description**                                                                 |
|------------------|--------------------|---------------------------------------------------------------------------------|
| **D**           | Driver Input       | Accepts TTL logic data to be transmitted on the RS-485 bus.                    |
| **DE**          | Driver Enable      | Enables or disables the driver (active high).                                  |
| **NRE**         | Receiver Enable    | Enables or disables the receiver (active low).                                 |
| **R**           | Receiver Output    | Outputs TTL logic data received from the RS-485 bus.                           |
| **5V**          | Supply Voltage     | Power input for the board (5V).                                                |
| **GND**         | Ground             | Common ground for both RS-485 and TTL sides.                                   |
| **A**           | Data Line A        | Non-inverting differential data line for RS-485 communication.                 |
| **B**           | Data Line B        | Inverting differential data line for RS-485 communication.                     |


<WarningBox>**Ensure that GND is connected between all devices on the RS-485 bus to establish a common reference for signals.**</WarningBox>

---

## Jumper Details

This board contains a hardware jumper; see below for its location and function:


<FlickityCarousel
  images={[
    { src: '/img/rs-485/485_jp1.png', alt: 'RS-485 jumper 1', caption: 'JP1' },
    { src: '/img/rs-485/485_jp2.png', alt: 'RS-485 jumper 2', caption: 'JP2' },
  ]}
  jumpers={true}
/>

| Jumper  | Default State            | Function                                                                                                      |
| ------- | ------------------------ | ------------------------------------------------------------------------------------------------------------- |
| **JP1** | **NC** (Normally closed) | Controls the power LED by **connecting** or **disconnecting** it from the **5V** power supply.                                     |
| **JP2** | **NC** (Normally closed) | Enables or disables the **120Ω termination resistor** on the **RS-485 bus**, ensuring proper signal termination at the ends of the communication line. |

---

## Dimensions

- **Board Dimensions:** 38 × 22 mm (1.5 × 0.9 inch)  
- **Header Pin Holes:** 1.5 mm  
- **Screw Holes:** Designed for M3 screws (3.2 mm diameter)  
- Soldered boards are LEGO-compatible! 🧱 

---

## Hardware repository

Schematics, KiCad files, Gerber files, and more can be found in the GitHub repository:

<QuickLink 
  title="RS-485 transceiver board Hardware design" 
  description="GitHub hardware repository for this product"
  url="https://github.com/SolderedElectronics/RS-485-Transceiver-breakout-hardware-design" 
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
- **Safety Instructions** – Safety guidelines and precautions in English and German.
- **Info.txt** – Contains product details such as SKU, country of origin, HS tariff code, and barcode.