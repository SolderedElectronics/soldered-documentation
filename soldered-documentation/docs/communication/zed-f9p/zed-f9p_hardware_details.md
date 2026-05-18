---
slug: /zed-f9p/hardware 
title: ZED-F9P - Hardware details
sidebar_label: Hardware details
id: zed-f9p-hardware 
hide_title: False
---

## Pinout

<CenteredImage src="/img/zed-f9p/pinout.png" alt="ZED-F9P pinout" />

Click [**here**](/img/zed-f9p/pinout.png) for a high-resolution image of the pinout.

---

## Pin Details

| Pin Marking | Pin Name        | Description |
|---|---|---|
| GND        | GND             | Ground reference |
| 3V3        | VCC             | Main power supply (2.7–3.6 V input) |
| VCC        | VCC             | Main power supply input |
| FENCE      | GEOFENCE_STAT   | Geofence status output (user-defined) |
| RTK        | RTK_STAT        | RTK status indicator (fixed / corrections / no corrections) |
| TX         | TXD             | UART1 transmit (host output) |
| RX         | RXD             | UART1 receive (host input) |
| SDA        | SDA             | I2C data (or SPI CS when SPI enabled) |
| SCL        | SCL             | I2C clock (or SPI clock when SPI enabled) |
| RESET      | RESET_N         | Hardware reset (active low) |
| SAFEBOOT   | SAFEBOOT_N      | Safe boot mode (firmware recovery, leave open in normal use) |
| INT        | EXTINT          | External interrupt input |
| PPS        | TIMEPULSE       | Time pulse output (precise timing signal, e.g. 1 PPS) |
| TX2        | TXD2            | UART2 transmit (correction data output) |
| RX2        | RXD2            | UART2 receive (correction data input) |

<InfoBox>
**SDA/SCL** pins are multiplexed with **SPI** depending on configuration of D_SEL pin.
</InfoBox>

---

## Dimensions
- **Board Dimensions:** **55mm x 39mm** (2.2 x 1.55 inch)
- **Header Pin Holes:** 1.5 mm  
- **Screw Holes:** Designed for M3 screws (3.2 mm diameter)  
- Soldered boards are LEGO compatible! 🧱 


---

## Jumper Details

This board contains hardware jumpers. See below for their locations and functions:

<FlickityCarousel
  images={[
    { src: '/img/zed-f9p/jp1_highlighted.jpg', alt: 'jp1', caption: 'JP1' },
    { src: '/img/zed-f9p/jp2_highlighted.jpg', alt: 'jp2', caption: 'JP2' },
    { src: '/img/zed-f9p/jp3_highlighted.jpg', alt: 'jp3', caption: 'JP3' },
    { src: '/img/zed-f9p/jp4_highlighted.jpg', alt: 'jp4', caption: 'JP4' },
    { src: '/img/zed-f9p/jp5_highlighted.jpg', alt: 'jp5', caption: 'JP5' },
    { src: '/img/zed-f9p/jp6_highlighted.jpg', alt: 'jp6', caption: 'JP6' },
    { src: '/img/zed-f9p/jp7_highlighted.jpg', alt: 'jp7', caption: 'JP7' },
  ]}
  jumpers={true}
/>

| Jumper  | Default State | Function |
|--------|--------------|----------|
| **JP1** | **NC** (Normally connected) | Selects interface mode via **D_SEL** pin. When connected to **3V3**, enables **UART/I2C mode** (default). When pulled to GND, switches to **SPI mode**. |
| **JP2** | **NC** (Normally connected) | Enables the **antenna filter network**. When closed, activates filtering components between the RF input and antenna for improved signal integrity. |
| **JP3** | **NC** (Normally connected) | Enables **I2C pull-up resistors (10kΩ to 3.3V)** on SDA and SCL lines. Required when using I2C without external pull-ups. |
| **JP4** | **NC** (Normally connected) | Controls **PWR LED**. When closed, the **power LED is disconnected** (turns LED off to save power). |
| **JP5** | **NC** (Normally connected) | Controls **PPS LED**. When closed, the **time pulse (PPS) LED is disconnected**. |
| **JP6** | **NC** (Normally connected) | Controls **RTK LED**. When closed, the **RTK status LED is disconnected**. |
| **JP7** | **NC** (Normally connected) | Controls **Geofence LED**. When closed, the **GEOFENCE status LED is disconnected**. |

---

## Hardware repository

Schematics, KiCad files, Gerber files, and more can be found in the GitHub repository:

[link placeholder - hardware repository]

The hardware repository contains everything you need to understand, modify, or manufacture the board. The different output folders are versioned. You can check which board version you have by finding the version mark on the PCB.

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