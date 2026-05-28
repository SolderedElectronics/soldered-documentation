---
slug: /ads1219/hardware 
title: ADS1219 24-bit ADC - Hardware details
sidebar_label: Hardware details
id: ads1219-hardware 
hide_title: False
---

## Pinout

<CenteredImage src="/img/ads1219/pinout.png" alt="ADS1219 pinout" caption="ADS1219 pinout diagram" />

Click [**here**](/img/ads1219/pinout.png) for a high-resolution image of the pinout.

---

## Pin Details

| Pin Marking  | Pin Name         | Description                                                              |
| ------------ | ---------------- | ------------------------------------------------------------------------ |
| **GND**      | Ground           | Common ground for power and signals.                                     |
| **VCC**      | Power            | Supply voltage (both 5V and 3V3 are supported).                          |
| **SDA**      | Data             | I2C data line for communication.                                         |
| **SCL**      | Clock            | I2C clock line for communication.                                        |
| **AIN0**     | Analog Input 0   | Analog input channel 0.                                                  |
| **AIN1**     | Analog Input 1   | Analog input channel 1.                                                  |
| **AIN2**     | Analog Input 2   | Analog input channel 2.                                                  |
| **AIN3**     | Analog Input 3   | Analog input channel 3.                                                  |
| **DRDY**     | Data Ready       | Active-low interrupt output; asserts when a conversion result is ready.  |
| **REFP**     | Reference +      | Positive terminal for external voltage reference input (optional).       |
| **REFN**     | Reference -      | Negative terminal for external voltage reference input (optional).       |
| **RESET**    | Reset            | Active-low reset input; pull low to reset the device.                    |

<InfoBox>This breakout board operates at **3.3V logic level**, but includes an onboard regulator for **5V compatibility** so it can be connected to both 3V3 and 5V logic boards!</InfoBox>

---

## Qwiic (formerly easyC)

<CenteredImage src="/img/easyc_transparent.png" alt="Qwiic (formerly easyC) cable" width="550px" />

<InfoBox>This board is fully **Qwiic-compatible**! Just plug it into your board using a **Qwiic (formerly easyC) cable** and start coding!</InfoBox>

<QuickLink 
  title="Qwiic (formerly easyC) details and specifications" 
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

<FlickityCarousel
  images={[
    { src: '/img/ads1219/jp1.JPG', alt: 'ads1219 jumper 1', caption: 'JP1' },
  ]}
  jumpers={true}
/>

| Jumper  | Default State            | Function                                                                        |
| ------- | ------------------------ | ------------------------------------------------------------------------------- |
| **JP1** | **NC** (Normally closed) | Connects **SDA/SCL pull-up resistors to VCC** for I2C communication.           |

---

## Address Selection

Depending on how you configure the A0 and A1 jumpers, you can define different I2C addresses for the ADS1219:

<FlickityCarousel
  images={[
    { src: '/img/ads1219/A0G.JPG', alt: 'A0 connected to DGND', caption: 'A0 → DGND' },
    { src: '/img/ads1219/A0V.JPG', alt: 'A0 connected to VCC', caption: 'A0 → VCC' },
    { src: '/img/ads1219/A0D.JPG', alt: 'A0 connected to SDA', caption: 'A0 → SDA' },
    { src: '/img/ads1219/A0C.JPG', alt: 'A0 connected to SCL', caption: 'A0 → SCL' },
    { src: '/img/ads1219/A1G.JPG', alt: 'A1 connected to DGND', caption: 'A1 → DGND' },
    { src: '/img/ads1219/A1V.JPG', alt: 'A1 connected to VCC', caption: 'A1 → VCC' },
    { src: '/img/ads1219/A1D.JPG', alt: 'A1 connected to SDA', caption: 'A1 → SDA' },
    { src: '/img/ads1219/A1C.JPG', alt: 'A1 connected to SCL', caption: 'A1 → SCL' },
  ]}
  jumpers={true}
/>

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

## Hardware Repository

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










