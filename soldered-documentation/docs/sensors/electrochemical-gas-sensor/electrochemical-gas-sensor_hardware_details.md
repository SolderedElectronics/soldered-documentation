---
slug: /electrochemical-gas-sensor/hardware 
title: Hardware details
id: electrochemical-gas-sensor-hardware 
hide_title: False
---
## Pinout

<ErrorBox>The pinout image for this board hasn't been generated yet! We're working on it!</ErrorBox>

---

## Pin details

| Pin Marking | Pin Name        | Description                                     |
| ----------- | --------------- | ----------------------------------------------- |
| **GND**     | Ground          | Common ground for power and signals.            |
| **VCC**     | Power           | Supply voltage (both 5V and 3V3 are supported). |
| **SDA**     | Data            | I2C data line for communication.                |
| **SCL**     | Clock           | I2C clock line for communication.               |
| **AIN1**    | Analog input    | Analog input 1                                  |
| **AIN2**    | Analog input    | Analog input 2                                  |
| **AIN3**    | Analog input    | Analog input 3                                  |
| **VOUT**    | Analog output   | Analog output from LMP                          |
| **ALERT**   | Digital output   | when the conversion data exceeds the Hi_thresh register or falls below the Lo_thresh register value.                         |
| **LMPEN**    | LMP enable    | Module Enable, Active-Low                                  |

---

## Qwiic (formerly easyC)  

<CenteredImage src="/img/easyc_transparent.png" alt="EasyC/qwiic cable" width="550px" />
 
<InfoBox> This board is fully **Qwiic-compatible**! Just plug it into your board using a **Qwiic/easyC/STEMMA QT cable** and start coding! </InfoBox>

<QuickLink 
  title="Qwiic (formerly easyC) details and specifications" 
  description="Learn about hardware specifications, compatibility, and usage of the Qwiic connector." 
  url="/qwiic" 
/>

---

## Dimensions

- **Board Dimensions:** 38 × 38 mm (1.5 × 1.5 inch)  
- **Header Pin Holes:** 1.5 mm  
- **Screw Holes:** Designed for M3 screws (3.2 mm diameter)  
- Soldered boards are LEGO compatible! 🧱 

---

## LMPEN pin functionality

The LMP91000 comes with a unique and fixed I2C address of **0x48**. It is still possible to connect more than one LMP91000 to an I2C bus and select each device using the LMPEN pin. The LMPEN simply enables/disables the
I2C communication of the LMP91000. When the LMPEN is at logic level low all the I2C communication is enabled,
it is disabled when LMPEN is at high logic level. In a system based on a μcontroller and more than one LMP91000 connected to the I2C bus, the I2C lines (SDAand SCL) are shared, while the LMPEN of each LMP91000 is connected to a dedicate GPIO port of the μcontroller. The μcontroller starts communication asserting one out of N LMPEN signals where N is the total number of LMP91000s connected to the I2C bus. Only the enabled device will acknowledge the I2C commands. After
finishing communicating with this particular LMP91000, the microcontroller de-asserts the corresponding LMPEN and repeats the procedure for other LMP91000s

<CenteredImage src="/img/electrochemical-gas-sensor/LMPEN.png" alt="LMPEN pin functionality" width="550px" />

## Sensor datasheets

| SKU     | Sensor name              | Datasheet                       |
| ------- | ------------------------ | ------------------------------- |
| [333325](https://soldered.com/product/high-precision-electrochemical-so2-gas-sensor-breakout/) | SGX-4SO2 - Sulphur Dioxide sensor | [Datasheet](https://sgx.cdistore.com/datasheets/sgx/ds-0314-sgx-4so2-datasheet.pdf) |
| [333326](https://soldered.com/product/high-precision-electrochemical-no2-gas-sensor-breakout/) | SGX-4NO2 - Nitrogen Dioxide sensor | [Datasheet](https://sgxsensortech.com/uploads/f_note/DS-0228-SGX-4NO2-datasheet-v3.pdf) |
| [333327](https://soldered.com/product/high-precision-electrochemical-no-gas-sensor-breakout/) | SGX-4NO-250 - Nitric Oxide sensor | [Datasheet](https://docs.rs-online.com/bc43/A700000009288858.pdf) |
| [333328](https://soldered.com/product/high-precision-electrochemical-co-gas-sensor-breakout/) | SGX-4CO - Carbon Monoxide sensor | [Datasheet](https://sgx.cdistore.com/datasheets/sgx/ds-0138%20(sgx-4co)%20v2.pdf) |
| [333329](https://soldered.com/product/high-precision-electrochemical-o3-gas-sensor-breakout/) | SGX-403-20 - Ozone sensor | [Datasheet](https://sgxsensortech.com/uploads/f_note/DS-0461-SGX-4O3-20.pdf) |
| [333330](https://soldered.com/product/high-precision-electrochemical-nh3-gas-sensor-breakout/) | SGX-4NH3-300 - Ammonia sensor | [Datasheet](https://sgx.cdistore.com/datasheets/sgx/ds-0306-sgx-4nh3-300-datasheet-v2.pdf) |
| [333331](https://soldered.com/product/high-precision-electrochemical-h2s-gas-sensor-breakout/) | SGX-4H2S-100 - Hydrogen Sulphide sensor | [Datasheet](https://www.sgxsensortech.com/content/uploads/2020/04/DS-0323-SGX-4H2S-100-datasheet.pdf) |
| [333332](https://soldered.com/product/high-precision-electrochemical-cl2-gas-sensor-breakout/) | SGX-4CL2 - Chlorine sensor | [Datasheet](https://sgx.cdistore.com/datasheets/sgx/ds-0310-sgx-4cl2-datasheet.pdf) |

## Jumper Details

This board contains hardware jumpers, see below for their locations and functions:

<FlickityCarousel
  images={[
    { src: '/img/electrochemical-gas-sensor/JP1.webp', alt: 'jumper 1', caption: 'JP1' },
    { src: '/img/electrochemical-gas-sensor/JP2.webp', alt: 'jumper 2', caption: 'JP2' },
    { src: '/img/electrochemical-gas-sensor/JP3.webp', alt: 'jumper 3', caption: 'JP3' },
    { src: '/img/electrochemical-gas-sensor/JP4.webp', alt: 'jumper 4', caption: 'JP4' },
    { src: '/img/electrochemical-gas-sensor/JP5.webp', alt: 'jumper 5', caption: 'JP5' },
    { src: '/img/electrochemical-gas-sensor/JP6.webp', alt: 'jumper 6', caption: 'JP6' },
    { src: '/img/electrochemical-gas-sensor/JP7.webp', alt: 'jumper 7', caption: 'JP7' },
  ]}
  jumpers={true}
/>

| Jumper  | Default State            | Function                                                                                                      |
| ------- | ------------------------ | ------------------------------------------------------------------------------------------------------------- |
| **JP1** | **NC** (Normally closed) | Connects **SDA/SCL pull-up resistors to 5V** for I2C communication.                                           |
| **JP2** | **NC** (Normally closed) | Connects **SDA/SCL pull-up resistors to 3.3V** for I2C communication.                                         |
| **JP3** | **NC** (Normally closed) | When connected, the **voltage regulator is powered by 5V**, stepping it down to **3.3V for the IC**.          |
| **JP4** | **NO** (Normally open)   | When shorted, it **bypasses the voltage regulator**, allowing the board to be powered **directly from 3.3V** via headers. **Ensure JP3 is disconnected if JP4 is connected.** |
| **JP5** | **NC** (Normally closed) | When shorted, sets the I2C address to **0x49**                                          |
| **JP6** | **NO** (Normally open) | When shorted, sets the I2C address to **0x4A**                                          |
| **JP7** | **NO** (Normally open) | When shorted, sets the I2C address to **0x4B**                                          |

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