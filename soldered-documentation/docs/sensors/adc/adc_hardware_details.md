---  
slug: /adc/hardware  
title: Adc – Hardware details
id: adc-hardware  
hide_title: False  
---

---

## Pinout

<CenteredImage src="/img/adc/pinout.png" alt="adc pinout diagram" caption="ADC pinout diagram"/>

<InfoBox>Pinouts for the 12-bit and the 16-bit ADC are the same!</InfoBox>

---

## Pin Details

| Pin Marking | Pin Name | Description                                         |
| ----------- | -------- | --------------------------------------------------- |
| **VCC**     | Power    | Supply voltage (both 5V and 3V3 are supported).     |
| **GND**     | Ground   | Common ground for power and signals.                |
| **SDA**     | Data     | I2C data line for communication.                    |
| **SCL**     | Clock    | I2C clock line for communication.                   |
| **A0-A3**   | Input    | Analog input channels.                              |
| **ALERT**   | Output   | Alert pin for the programmable comparator function. |

<InfoBox>The ALERT pin functions as an interrupt output for the programmable comparator, triggering when an input voltage exceeds a set threshold. This allows the microcontroller to respond to changes without continuous polling.</InfoBox>

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

## Timing Characteristics

The timing characteristics of the **ADS1015** and **ADS1115** are crucial for understanding their performance during analog-to-digital conversion. Key parameters include:

- **Conversion Time**:
  - **ADS1015**: 160 µs (at 3.3 kSPS)
  - **ADS1115**: 4.92 ms (at 860 SPS)

- **Data Rate**: 
  - **ADS1015**: 128 SPS to 3.3 kSPS (programmable)
  - **ADS1115**: 128 SPS to 860 SPS (programmable)

- **Acquisition Time**:
  - **ADS1015**: 4.9 µs
  - **ADS1115**: 4.92 ms (due to higher resolution)

---

## Power Consumption

The **ADS1015** and **ADS1115** are both designed for low power consumption. The power usage varies depending on the operating mode and data rate:

- **ADS1015 (12-bit resolution)**:
  - **Continuous Conversion Mode**: ~150 µA (at a full data rate of 3.3 kSPS)
  - **Single-Shot Mode**: Current consumption is significantly reduced in single-shot mode due to automatic shutdown after a conversion.

- **ADS1115 (16-bit resolution)**:
  - **Continuous Conversion Mode**: ~230 µA (at a full data rate of 860 SPS)
  - **Single-Shot Mode**: Similar to the ADS1015, the current consumption drops significantly in shutdown mode after a conversion.

---

## Dimensions

- **Board Dimensions:** 22 × 22 mm (0.9 × 0.9 inch)  
- **Header Pin Holes:** 1.5 mm  
- **Screw Holes:** Designed for M3 screws (3.2 mm diameter)  
- Soldered boards are LEGO compatible! 🧱

---

## Jumper Details

<InfoBox>Jumper details are the same for 12-bit and 16-bit versions.</InfoBox>

This board contains hardware jumpers; see below for their locations and functions:

<FlickityCarousel
  images={[
    { src: '/img/adc/jp1.png', alt: 'adcjumper1', caption: 'JP1' },
    { src: '/img/adc/jp2.png', alt: 'adcjumper2', caption: 'JP2' },
    { src: '/img/adc/jp3.png', alt: 'adcjumper3', caption: 'JP3' },
    { src: '/img/adc/jp4.png', alt: 'adcjumper4', caption: 'JP4' },
    { src: '/img/adc/jp5.png', alt: 'adcjumper5', caption: 'JP5' },
  ]}
  jumpers={true}
/>

| Jumper  | Default State            | Function                        |
| ------- | ------------------------ | ------------------------------- |
| **JP1** | **NC** (Normally closed) | Connects PWR LED.               |
| **JP2** | **NC** (Normally closed) | I2C address 0x48 (**Default**). |
| **JP3** | **NO** (Normally open)   | I2C address 0x39 when closed.   |
| **JP4** | **NO** (Normally open)   | I2C address 0x4A when closed.   |
| **JP5** | **NO** (Normally open)   | I2C address 0x4B when closed.   |

<WarningBox>The ADC should have only one I2C address at a time. Having multiple address jumpers closed at the same time may cause malfunction or damage.</WarningBox>

---

## Hardware repository

Schematics, KiCad files, Gerber files, and more can be found in the GitHub repository:

<QuickLink 
  title="ADC 12-bit ADS1015 Hardware design" 
  description="GitHub hardware repository for this product"
  url="https://github.com/SolderedElectronics/ADC-12-bit-ADS1015-4-channel-with-PGA-breakout-hardware-design/tree/main" 
/> 

<QuickLink 
  title="ADC 16-bit ADS1115 Hardware design" 
  description="GitHub hardware repository for this product"
  url="https://github.com/SolderedElectronics/ADC-16-bit-ADS1115-4-channel-with-PGA-breakout-hardware-design/tree/main" 
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