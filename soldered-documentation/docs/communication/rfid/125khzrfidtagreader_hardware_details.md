---  
slug: /rfid/hardware  
title: Hardware details  
id: 125khzrfidtagreader-hardware  
hide_title: False  
---

## Pinout

<ErrorBox>The pinout image for this board hasn't been generated yet! We're working on it!</ErrorBox>

## Pin details

### Pin Details

| Pin Name | Description       | Notes                                                |
|:---------|:------------------|:------------------------------------------------------|
| GND      | Ground            | Common ground connection.                            |
| VCC      | Power Supply      | Connect to 5V power supply.                          |
| RXD      | UART Receive      | For UART communication (UART version only).          |
| TXD      | UART Transmit     | For UART communication (UART version only).          |
| INT      | Interrupt         | Signals when a tag is detected.   |
| UPDI     | Programming       | For firmware updates (do not use in normal operation). |
| 3V3      | 3.3V Output       | 3.3V output from onboard regulator.                  |
| SCL      | I2C Clock         | For I2C communication (Qwiic version only).            |
| SDA      | I2C Data          | For I2C communication (Qwiic version only).            |

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

## Address selection for Qwiic version

The board contains hardware address switches; see below for instructions on changing the breakout board's address.

<CenteredImage src="/img/rfid/RFID_switch.png" alt="ADDR" width="550px" />

### Address Table

| Address | SW3 | SW2 | SW1 |
|---------|----|----|----|
| 0x30    | 0  | 0  | 0  |
| 0x31    | 0  | 0  | 1  |
| 0x32    | 0  | 1  | 0  |
| 0x33    | 0  | 1  | 1  |
| 0x34    | 1  | 0  | 0  |
| 0x35    | 1  | 0  | 1  |
| 0x36    | 1  | 1  | 0  |
| 0x37    | 1  | 1  | 1  |

<InfoBox>Qwiic versions also contain UPDI headers for onboard ATTINY1604 programming; they will not be used in the following examples.</InfoBox>

---

## Dimensions

- **Board Dimensions:** 38 x 38 mm (1.5 x 1.5 inch) 
- **Header Pin Holes:** 1.5 mm  
- **Screw Holes:** Designed for M3 screws (3.2 mm diameter)  
- Soldered boards are LEGO compatible! 🧱 

---

## Jumper Details

This board contains hardware jumpers; see below for their locations and functions:

<FlickityCarousel
  images={[
    { src: '/img/rfid/rfid_1.png', alt: 'RFID jumper 1', caption: 'JP1' },
    { src: '/img/rfid/rfid_2.png', alt: 'RFID jumper 2', caption: 'JP2' },
    { src: '/img/rfid/rfid_3.png', alt: 'RFID jumper 3', caption: 'JP3' },
    { src: '/img/rfid/rfid_4.png', alt: 'RFID jumper 4', caption: 'JP4' },
    { src: '/img/rfid/rfid_5.png', alt: 'RFID jumper 5', caption: 'JP5' },
    { src: '/img/rfid/rfid_6.png', alt: 'RFID jumper 6', caption: 'JP6' },
  ]}
  jumpers={true}
/>

| Jumper  | Default State            | Function                                                                                                      |
| ------- | ------------------------ | ------------------------------------------------------------------------------------------------------------- |
| **JP1** | **NC** (Normally closed) | Connects **SDA/SCL pull-up resistors to 5V** for I2C communication.                                             |
| **JP2** | **NC**                   | Connects **SDA/SCL pull-up resistors to 3.3V** for I2C communication.                                             |
| **JP3** | **NC**                   | Used to connect or disconnect the **“DATA OUT” (INT)** signal line to its **LED (D4)**.                           |
| **JP4** | **NC**                   | Used to connect or disconnect the signal line to the **LED (D5)** via **“PWR” (3.3 V)**.                          |
| **JP5** | **NC**                   | When connected, the **voltage regulator is powered by 5V**, stepping it down to **3.3V for the IC**.              |
| **JP6** | **NO** (Normally open)   | When shorted, it **bypasses the voltage regulator**, allowing the board to be powered **directly from 3.3V** via headers. **Ensure JP5 is disconnected if JP6 is connected.** |

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