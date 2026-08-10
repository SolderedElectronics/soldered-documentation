---
slug: /pcal6416a/hardware 
title: PCAL6416A - Hardware details
sidebar_label: Hardware details
id: pcal6416a-hardware 
hide_title: false
---

## Pinout

<CenteredImage src="/img/pcal6416a/Pinout.png" alt="PCAL6416A pinout diagram" caption="PCAL6416A pinout diagram"/>

Click [**here**](/img/pcal6416a/Pinout.png) for a high resolution image of the pinout.

---

## Pin Details

| **Pin Marking** | **Pin Name**         | **Description**                                                                 |
|-----------------|----------------------|---------------------------------------------------------------------------------|
| **INT**         | Interrupt Output     | Active-low, open-drain interrupt output. Needs a pull-up to function - either the host's own internal pull-up on the pin it's wired to, or an external resistor. |
| **RES**         | Reset                | Hardware reset pin for the PCAL6416A. Pull low to reset the device. Already pulled up to 3.3V on the board through a 10 kΩ resistor, so it can be left unconnected. |
| **B0 - B7**          | GPIO Port B          | General-purpose input/output pins from Port B.                                 |
| **A0 - A7**          | GPIO Port A          | General-purpose input/output pins from Port A.                                 |
| **SCL**         | I2C Clock            | Clock line for I2C communication.                                              |
| **SDA**         | I2C Data             | Data line for I2C communication.                                               |
| **VCC**         | Supply Voltage       | Main power input for the board, nominally 5V. An onboard regulator steps this down to 3.3V for the PCAL6416A by default; closing jumper **JP5** bypasses the regulator and runs the chip directly at the supplied voltage instead. |
| **GND**         | Ground               | Common ground reference for the board and connected devices.                   |

<InfoBox>
- **GPIO Channels**: 16 total GPIO pins (Port A and Port B)
- **Communication Interface**: I2C
- **Operating Voltage**: Regulated to 3.3V on the board by default; 5V is possible by bypassing the regulator with jumper JP5
- **Interrupt Support**: Active-low interrupt output available on INT pin
- **Internal Pull-Up/Pull-Down**: 100 kΩ, enabled individually per pin
</InfoBox>

<WarningBox>Make sure the supply voltage and I2C logic levels are compatible with your microcontroller before connecting the board. Always connect GND between devices to establish a common signal reference.</WarningBox>

---

## Qwiic

<CenteredImage src="/img/easyc_transparent.png" alt="Qwiic cable" width="550px" />

<InfoBox>This board is fully **Qwiic-compatible**! Just plug it into your board using a **Qwiic (formerly easyC) cable** and start coding!</InfoBox>

<QuickLink 
  title="Qwiic details and specifications" 
  description="Learn about hardware specifications, compatibility, and usage of the Qwiic connector." 
  url="/qwiic" 
/>

---

## Jumper Details

This board contains hardware jumpers; see below for their locations and functions:

<FlickityCarousel
  images={[
    { src: '/img/pcal6416a/jp1.jpg', alt: 'pcal6416ajumper1', caption: 'JP1' },
    { src: '/img/pcal6416a/jp2.jpg', alt: 'pcal6416ajumper2', caption: 'JP2' },
    { src: '/img/pcal6416a/jp3.jpg', alt: 'pcal6416ajumper3', caption: 'JP3' },
    { src: '/img/pcal6416a/jp4.jpg', alt: 'pcal6416ajumper4', caption: 'JP4' },
    { src: '/img/pcal6416a/jp5.jpg', alt: 'pcal6416ajumper5', caption: 'JP5' },
  ]}
  jumpers={true}
/>

| **Jumper** | **Default State** | **Function** |
|------------|-------------------|--------------|
| **JP1** | NC | Enables the 5V I2C pull-up resistors for the SDA5 and SCL5 signal lines. |
| **JP2** | NC | Enables the 3.3V I2C pull-up resistors for the SDA_PULL3.3 and SCL_PULL3.3 signal lines. |
| **JP3** | Selectable | Connects the ADDR pin to GND, setting the I2C address to **0x20**. Cut this jumper and bridge it to VDD to change the address to **0x21**. |
| **JP4** | NC | Connects the output of the onboard voltage regulator to the 3.3V power rail. |
| **JP5** | NO | Bypasses the onboard voltage regulator by directly connecting the 5V rail to the 3.3V rail. |


<InfoBox>

- **NO (Normally Open)** means the jumper pads are disconnected by default.
- **NC (Normally Closed)** means the jumper pads are connected by default.
- Changing jumper states allows configuration of the board power routing and I2C pull-up behavior.

</InfoBox>

---

## Dimensions

- **Board Dimensions:** 22 × 38 mm (0.9 × 1.5 inch)  
- **Header Pin Holes:** 1.5 mm  
- **Screw Holes:** Designed for M3 screws (3.2 mm diameter)  
- Soldered boards are LEGO compatible! 🧱

---

## Hardware repository

Schematics, KiCad files, Gerber files, and more can be found in the GitHub repository:

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
- **Safety Instructions** - Safety guidelines and precautions in English and German.
- **Info.txt** - Contains product details such as SKU, country of origin, HS tariff code, and barcode.