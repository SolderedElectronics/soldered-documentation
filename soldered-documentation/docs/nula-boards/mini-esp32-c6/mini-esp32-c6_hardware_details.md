---
slug: /nula-mini-esp32-c6/hardware
title: NULA Mini ESP32-C6 - Hardware details
sidebar_label: Hardware details
id: mini-esp32-c6-hardware
hide_title: True
---

# Hardware details

## Pinout

<CenteredImage src="/img/nula-mini-esp32-c6/NULA-MINI-ESP32-C6-Pinout.webp" alt="NULA Mini ESP32-C6 pinout" caption="NULA Mini ESP32-C6 Pinout Diagram"/>

Click [**here**](/img/nula-mini-esp32-c6/NULA-MINI-ESP32-C6-Pinout.webp) for a high-resolution image of the pinout.

## Pin Details

| Pin Marking | Pin Name | Description                                                               |
| ----------- | -------- | ------------------------------------------------------------------------- |
| **VBAT**    | Power    | Battery input for 3.7 V Li-Ion/Li-Poly battery through the JST connector. |
| **VCC**     | Power    | Main power input (5 V via USB-C or external 5 V supply).                  |
| **3V3**     | Power    | Regulated 3.3 V output from the onboard regulator.                        |
| **GND**     | Ground   | Common ground for power and signals.                                      |
| **IO2**     | GPIO     | General-purpose I/O pin, supports PWM.                                    |
| **IO3**     | GPIO     | General-purpose I/O pin, SPI MOSI function available.                     |
| **IO4**     | GPIO     | General-purpose I/O pin, SPI MISO function available.                     |
| **IO5**     | GPIO     | General-purpose I/O pin, SPI SCK function available.                      |
| **IO18**    | GPIO     | General-purpose I/O pin, supports PWM.                                    |
| **IO19**    | GPIO     | General-purpose I/O pin, supports PWM.                                    |
| **TX**      | TX       | UART0 transmit pin used for serial communication.                         |
| **RX**      | RX       | UART0 receive pin used for serial communication.                          |

## Breadboard mounting recommendation

When using the **NULA Mini ESP32-C6** on a breadboard, we recommend soldering **male header pins** so that the **ESP32-C6 module (chip)** faces **downwards** toward the breadboard.  

This orientation keeps the board level and stable because the **JST battery connector** on the opposite side is taller and can prevent a flat fit on the breadboard.

<InfoBox>Solder the **male headers on the same side as the Qwiic connector**, with the chip facing down when plugged into the breadboard.  
This provides better mechanical stability and makes the USB-C port easier to access.</InfoBox>

<CenteredImage  
  src="/img/nula-mini-esp32-c6/nula-mini-breadboard-orientation.png"  
  alt="Recommended breadboard orientation for NULA Mini ESP32-C6"  
  caption="Recommended orientation when mounting the NULA Mini ESP32-C6 on a breadboard"  
  width="800px"  
/>

<br></br>
## Qwiic / easyC Connector

<CenteredImage src="/img/easyc_transparent.png" alt="Qwiic/easyC connector" width="550px" />

<InfoBox>The **NULA Mini ESP32-C6** includes a **Qwiic/easyC/STEMMA QT connector** for quick plug-and-play connections with I²C devices such as sensors and peripherals.</InfoBox>

<QuickLink
  title="Qwiic (formerly easyC) details and specifications"
  description="Learn more about Qwiic hardware compatibility and connector pinout."
  url="/qwiic"
/>

## Power Supply and Battery

- USB-C Port is used for both programming and powering the board  
- VBAT (JST connector) is used for connecting a 3.7 V Li-Ion or Li-Poly battery  
- The board includes an integrated Li-Ion charge management circuit  
- Operating voltage: 3.3 V (onboard regulator for 5 V input)

<InfoBox>When powered using a battery, the onboard charger automatically handles charging and discharging.  
For 5 V input, always power the board through the USB-C port.</InfoBox>

## Power Consumption

| Mode              | Typical Current |
| ----------------- | --------------- |
| Active (Wi-Fi TX) | around 120 mA   |
| Modem-sleep       | around 25 mA    |
| Light-sleep       | around 1 mA     |
| Deep-sleep        | around 7 µA     |

<InfoBox>These values are approximate and refer only to the power consumption of the ESP32-C6 chip.</InfoBox>

## Dimensions

- **Board size**: 25.33 × 25.33 x 10.0 mm (1.00 x 1.00 x 0.39 inch)
- **Mounting**: Breadboard compatible  
- **Header Pin Holes:** 1.5 mm  
- **Screw Holes:** Designed for M3 screws (3.2 mm diameter)  
- Soldered boards are LEGO compatible! 🧱 

## Jumper Details

This board includes two hardware jumpers that can be modified to adjust behavior or reduce power consumption.

<FlickityCarousel
  images={[
    { src: '/img/nula-mini-esp32-c6/jp1.png', alt: 'nula-mini-jumper1', caption: 'JP1' },
    { src: '/img/nula-mini-esp32-c6/jp2.png', alt: 'nula-mini-jumper2', caption: 'JP2' },
  ]}
  jumpers={true}
/>

| Jumper  | Default State            | Function                                                                                               |
| ------- | ------------------------ | ------------------------------------------------------------------------------------------------------ |
| **JP1** | **NC** (Normally closed) | Disconnects the Power LED to reduce standby current draw when running from battery power.              |
| **JP2** | **NC** (Normally closed) | Connects the 3.3 V I²C pull-up resistors for SDA and SCL lines when required by connected I²C devices. |

<InfoBox>For ultra-low-power battery projects, it is recommended to open **JP1** to disable the power LED.  
Use **JP2** when connecting I²C sensors or peripherals that do not include onboard pull-up resistors.</InfoBox>

## Hardware repository

Schematics, KiCad files, Gerber files and more can be found in the GitHub repository:

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