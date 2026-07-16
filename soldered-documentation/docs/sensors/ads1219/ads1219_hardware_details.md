---
slug: /ads1219/hardware 
title: ADS1219 24-bit ADC - Hardware details
sidebar_label: Hardware details
id: ads1219-hardware 
hide_title: False
---

## Pinout

<CenteredImage src="/img/ads1219/Pinout.png" alt="ADS1219 pinout" caption="ADS1219 pinout diagram" />

Click [**here**](/img/ads1219/Pinout.svg) for a high-resolution image of the pinout.

---

## Pin Details

| Pin Marking  | Pin Name         | Description                                                              |
| ------------ | ---------------- | ------------------------------------------------------------------------ |
| **GND**      | Ground           | Common ground for power and signals.                                     |
| **VCC**      | Power            | Supply voltage, 2.3V to 5.5V (both 5V and 3V3 systems are supported directly).  |
| **AVDD**     | Power            | Analog supply for the ADS1219. Tied to VCC by default through jumper **JP2** - cut it to feed a separate, cleaner analog supply instead. |
| **SDA**      | Data             | I2C data line for communication.                                         |
| **SCL**      | Clock            | I2C clock line for communication.                                        |
| **AIN0**     | Analog Input 0   | Analog input channel 0.                                                  |
| **AIN1**     | Analog Input 1   | Analog input channel 1.                                                  |
| **AIN2**     | Analog Input 2   | Analog input channel 2.                                                  |
| **AIN3**     | Analog Input 3   | Analog input channel 3.                                                  |
| **DRDY**     | Data Ready       | Active-low, open-drain interrupt output; asserts when a conversion result is ready. Already pulled up to VCC on the board through a 10 kΩ resistor, so no external pull-up is needed. |
| **REFP**     | Reference +      | Positive terminal for external voltage reference input (optional).       |
| **REFN**     | Reference -      | Negative terminal for external voltage reference input (optional).       |
| **RESET**    | Reset            | Active-low reset input; pull low to reset the device. Already pulled up to VCC on the board through a 10 kΩ resistor, so it can be left unconnected. |

<InfoBox>The ADS1219 accepts a supply voltage anywhere from **2.3V to 5.5V** directly, no onboard regulator needed - so it works the same whether you power it at 3.3V or 5V.</InfoBox>

---

## Qwiic

<CenteredImage src="/img/easyc_transparent.png" alt="Qwiic cable" width="550px" />

<InfoBox>This board is fully **Qwiic-compatible**! Just plug it into your board using a **Qwiic cable** and start coding!</InfoBox>

<QuickLink 
  title="Qwiic details and specifications" 
  description="Learn about hardware specifications, compatibility, and usage of the Qwiic connector." 
  url="/qwiic" 
/>

---

## Timing Characteristics

The ADS1219 supports four programmable data rates, which directly determine conversion time:

| Data Rate | Conversion Time |
| --------- | --------------- |
| 20 SPS    | 50 ms           |
| 90 SPS    | ~11 ms          |
| 330 SPS   | ~3 ms           |
| 1000 SPS  | 1 ms            |

<InfoBox>Use the **DRDY** pin as a conversion-complete interrupt instead of polling over I2C to minimize bus traffic and get the lowest possible latency.</InfoBox>

---

## Dimensions

- **Board Dimensions:** 22 × 22 mm (0.9 × 0.9 inch)  
- **Header Pin Holes:** 1.5 mm  
- **Screw Holes:** Designed for M3 screws (3.2 mm diameter)  
- Soldered boards are LEGO compatible! 🧱

---

## Jumper Details

This board contains hardware jumpers; see below for their locations and functions:

<ErrorBox>Photos of the JP1 and JP2 jumpers are not available yet! We're working on it.</ErrorBox>

| Jumper  | Default State            | Function                                                                        |
| ------- | ------------------------ | ------------------------------------------------------------------------------- |
| **JP1** | **NC** (Normally closed) | Connects **SDA/SCL pull-up resistors to VCC** for I2C communication.           |
| **JP2** | **NC** (Normally closed) | Connects **AVDD to VCC**. Cut for a separate, low-noise analog supply. |

<InfoBox>The board also has eight additional jumper pads (JP3-JP10) dedicated to I2C address selection - see [**Address Selection**](#address-selection) below.</InfoBox>

---

## Address Selection

Depending on how you configure the A0 and A1 jumpers, you can define different I2C addresses for the ADS1219:

<ErrorBox>Photos of the A0/A1 address jumper configurations are not available yet! We're working on it.</ErrorBox>

| Address       | A1   | A0   |
| :-----------: | :--: | :--: |
| **0x40** (default) | DGND | DGND |
| 0x41          | DGND | VCC  |
| 0x42          | DGND | SDA  |
| 0x43          | DGND | SCL  |
| 0x44          | VCC  | DGND |
| 0x45          | VCC  | VCC  |
| 0x46          | VCC  | SDA  |
| 0x47          | VCC  | SCL  |
| 0x48          | SDA  | DGND |
| 0x49          | SDA  | VCC  |
| 0x4A          | SDA  | SDA  |
| 0x4B          | SDA  | SCL  |
| 0x4C          | SCL  | DGND |
| 0x4D          | SCL  | VCC  |
| 0x4E          | SCL  | SDA  |
| 0x4F          | SCL  | SCL  |

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
- **Safety Instructions** - Safety guidelines and precautions in English and in German.  
- **Info.txt** - Contains product details such as SKU, country of origin, HS tariff code, and barcode.










