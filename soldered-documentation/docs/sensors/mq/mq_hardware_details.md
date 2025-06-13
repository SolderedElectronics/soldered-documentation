---
slug: /mq/hardware 
title: MQ Gas Sensors – Hardware details
sidebar_label: Hardware details
id: mq-hardware 
hide_title: False
---

## Pinout

### Native version

<CenteredImage src="/img/mq/pinout_native.webp" alt="MQ Native pinout" />

Click [**here**](/img/mq/pinout_native.webp) for a high-resolution image of the pinout.

<InfoBox>While the pinout shown is for the MQ135, it is exactly the same for any Native MQ sensor</InfoBox>

| Pin Marking | Pin Name | Description                                     |
| ----------- | -------- | ----------------------------------------------- |
| **5V**      | Power    | Supply voltage for the sensor                   |
| **DO**    | Digital Output    | Set to HIGH when sensor reads gas concentration over the trigger level set by the onboard potentiometer                    |
| **AO**      | Analog Output    | Voltage output proportional to gas measurement                  |
| **GND**     | Ground   | Common ground for power and signals.            |


### Qwiic version

<CenteredImage src="/img/mq/pinout_qwiic.png" alt="MQ Qwiic pinout" />

Click [**here**](/img/mq/pinout_qwiic.png) for a high-resolution image of the pinout.

<InfoBox>While the pinout shown is for the MQ8, it is exactly the same for any Qwiic MQ sensor</InfoBox>

| Pin Marking | Pin Name | Description                                     |
| ----------- | -------- | ----------------------------------------------- |
| **3V3**     | Power    | Supply voltage for the UPDI                     |
| **UPDI**    | UPDI     | Communication pin for UPDI                      |
| **GND**     | Ground   | Common ground for power and signals.            |

<WarningBox>UPDI stands for Unified Program and Debug Interface. It is used to program and debug Atmel devices. The atmel chip on this board is used for the easyC I2C communication only. DO NOT try to use this for sensor communication!</WarningBox>


<CenteredImage src="/img/easyc_transparent.png" alt="EasyC/qwiic cable" width="550px" />
 
<InfoBox> This board is fully **Qwiic-compatible**! Just plug it into your board using a **Qwiic/easyC/STEMMA QT cable** and start coding! </InfoBox>

<QuickLink 
  title="Qwiic (formerly easyC) details and specifications" 
  description="Learn about hardware specifications, compatibility, and usage of the Qwiic connector." 
  url="/qwiic" 
/>


---

## Dimensions 

### Native

- **Board Dimensions:** 22 x 38 mm (0.9 x 1.5 inches)
- **Header Pin Holes:** 1.5 mm  
- **Screw Holes:** Designed for M3 screws (3.2 mm diameter)  
- Soldered boards are LEGO-compatible! 🧱 

### Qwiic

- **Board Dimensions:** 54 x 22 mm (2.1 x 0.9 inches)  
- **Header Pin Holes:** 1.5 mm  
- **Screw Holes:** Designed for M3 screws (3.2 mm diameter)  
- Soldered boards are LEGO-compatible! 🧱

---

## Jumper Details (Qwiic version)

This board contains hardware jumpers. See below for their locations and functions:

<FlickityCarousel
  images={[
    { src: '/img/mq/jp1.jpg', alt: 'jumper 1', caption: 'JP1' },
    { src: '/img/mq/jp2.jpg', alt: 'jumper 2', caption: 'JP2' },
  ]}
  jumpers={true}
/>

| Jumper  | Default State            | Function                                                                                                      |
| ------- | ------------------------ | ------------------------------------------------------------------------------------------------------------- |
| **JP1** | **NC** (Normally closed) |  Connects **SDA/SCL pull-up resistors to 5V** for I2C communication.                                             |
| **JP2** | **NC** (Normally closed) | Connects **SDA/SCL pull-up resistors to 3.3V** for I2C communication.                                      |

---

## Address selection (Qwiic version)

This board contains hardware address switches. See below for instructions on changing the breakout board's address:

<CenteredImage src="/img/mq/address.jpg" alt="MQ adresses" />

| Address |  SW3  |  SW2  |  SW1  |
| :-----: | :---: | :---: | :---: |
|  0x30   |   0   |   0   |   0   |
|  0x31   |   0   |   0   |   1   |
|  0x32   |   0   |   1   |   0   |
|  0x33   |   0   |   1   |   1   |
|  0x34   |   1   |   0   |   0   |
|  0x35   |   1   |   0   |   1   |
|  0x36   |   1   |   1   |   0   |
|  0x37   |   1   |   1   |   1   |

---

## Hardware repository

In the link below, you can find repositories of hardware designs for all MQ sensor types, which include Schematics, KiCad files, Gerber files and more:

<QuickLink 
  title="MQ Sensors Hardware Design" 
  description="GitHub hardware repositories for all MQ sensors"
  url="https://github.com/orgs/SolderedElectronics/repositories?language=&q=mq+sensor+hardware&sort=&type=all" 
/> 

The hardware repository contains everything you need to understand, modify, or manufacture the board. The different output folders are versioned. You can determine your board version by checking the version mark on the PCB.

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