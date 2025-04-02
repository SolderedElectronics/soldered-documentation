---
slug: /simple-sensor/simple-rain-sensor/simple-rain-sensor-hardware
title: Hardware details
id: simple-rain-sensor-hardware
hide_title: False
---

## Pinout

<CenteredImage src="/img/simple-sensor/simple-rain-sensor/333043_pinout.jpg" alt="Pinout" />
Click [**here**](/img/simple-sensor/simple-rain-sensor/333043_pinout.jpg) for a high resolution image of the pinout.

<ErrorBox>The pinout image for the regular board hasn't been generated yet! We're working on it!</ErrorBox>
---

# Pin details for regular version

| Pin Marking | Pin Name | Description                                     |
| ----------- | -------- | ----------------------------------------------- |
| **GND**     | Ground   | Common ground for power and signals.            |
| **A0**      | Data     | Analog output pin.                              |
| **D0**      | Data     | Digital output pin.                             |
| **VCC**     | Power    | Supply voltage                                  |


### Dimensions for regular version

- **Rain sensor Dimensions:** 55 x 38 mm (2.2 x 1.5 inch)
- **Simple sensor Dimensions:** 22 × 22 mm (0.9 × 0.9 inch)  
- **Header Pin Holes:** 1.5 mm  
- **Screw Holes:** Designed for M3 screws (3.2 mm diameter)  
- Soldered boards are LEGO compatible! 🧱 

---

## Pin details for Qwiic version
For the Qwiic version, connection is achieved using a Qwiic connector.

<InfoBox> Qwiic versions also contain UPDI headers for preprogramming the onboard ATTINY404 MCU, they are used only for debugging purposes. </InfoBox>

### Dimensions for Qwiic version

- **Rain sensor Dimensions:** 55 x 38 mm (2.2 x 1.5 inch)
- **Simple sensor Dimensions:** 38 × 22 mm (1.5 × 0.9 inch)  
- **Header Pin Holes:** 1.5 mm  
- **Screw Holes:** Designed for M3 screws (3.2 mm diameter)  
- Soldered boards are LEGO compatible! 🧱 

### Address selection for Qwiic version
This board contains hardware address switches. See below for instructions on how to change the breakout board's address.

<CenteredImage src="/img/simple-sensor/simple-rain-sensor/333043_add_highlighted.jpg" alt="Address Switches" />

| Address | SW3 | SW2 | SW1 |
|:---:|:---:|:---:|:---:|
| 0x30 | 0 | 0 | 0 |
| 0x31 | 0 | 0 | 1 |
| 0x32 | 0 | 1 | 0 |
| 0x33 | 0 | 1 | 1 |
| 0x34 | 1 | 0 | 0 |
| 0x35 | 1 | 0 | 1 |
| 0x36 | 1 | 1 | 0 |
| 0x37 | 1 | 1 | 1 |      

---

## Hardware repository

Schematics, KiCad files, Gerber files and more can be found in the GitHub repository:

<ErrorBox>The Hardware repository for this board hasn't been generated yet! We're working on it!</ErrorBox>

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