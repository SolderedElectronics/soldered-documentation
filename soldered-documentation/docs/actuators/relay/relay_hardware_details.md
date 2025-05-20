---
slug: /relay/hardware
title: Relay - Hardware details
id: relay-hardware
hide_title: false
---

## Pinout

<CenteredImage src="/img/relay/333021_pinout.jpg" alt="Pinout" />
Click [**here**](/img/relay/333021_pinout.jpg) for a high resolution image of the pinout.
<CenteredImage src="/img/relay/333022_pinout.jpg" alt="Pinout" />
Click [**here**](/img/relay/333022_pinout.jpg) for a high resolution image of the pinout.
<CenteredImage src="/img/relay/333023_pinout.jpg" alt="Pinout" />
Click [**here**](/img/relay/333023_pinout.jpg) for a high resolution image of the pinout.
<CenteredImage src="/img/relay/333024_pinout.jpg" alt="Pinout" />
Click [**here**](/img/relay/333024_pinout.jpg) for a high resolution image of the pinout.

---

## Pin details for regular version

| Pin Marking | Pin Name | Description                                     |
| ----------- | -------- | ----------------------------------------------- |
| **VCC**     | Power    | Supply voltage (both 5V and 3V3 are supported). |
| **GND**     | Ground   | Common ground for power and signals.            |
| **IN**     | Data     | Data line for digital communication |

<InfoBox>The IN pins can work at **3V3** or **5V** logic</InfoBox>

---

## Qwiic (formerly easyC)  

<CenteredImage src="/img/easyc_transparent.png" alt="EasyC/qwiic cable" width="550px" />
 
<InfoBox> This board has **Qwiic-compatible** version! Just plug it into your board using a **Qwiic/easyC/STEMMA QT cable** and start coding! </InfoBox>

<QuickLink 
  title="Qwiic (formerly easyC) details and specifications" 
  description="Learn about hardware specifications, compatibility, and usage of the Qwiic connector." 
  url="/qwiic" 
/>

---

## Dimensions
**Regular**
    - **Number of relays:**
        - **1 relay**
        - **2 relays**
        - **4 relays**
    - **Dimensions:**
        - **54 x 22 mm** (2.1 x 0.9 inch)
        - **54 x 38 mm** (2.1 x 1.5 inch)
        - **54 x 70 mm** (2.1 x 2.8 inch)
- **Qwiic**
    - **Number of relays:**
        - **1 relay**
        - **2 relays**
    - **Dimensions:**
        - **70 x 22 mm** (2.8 x 0.9 inch)
        - **70 x 40 mm** (2.8 x 1.6 inch)
- **Header Pin Holes:** 1.5 mm  
- **Screw Holes:** Designed for M3 screws (3.2 mm diameter)  
- Soldered boards are LEGO compatible! 🧱 

---

## Address selection for Qwiic version

This board contains hardware address switches, see below how to change circuit board's address:

<CenteredImage src="/img/relay/relay_add.jpg" alt="Pinout" />

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

## Jumper Details

This board contains hardware jumpers, see below **example for 2 channel regular relay board** for their locations and functions:

<FlickityCarousel
  images={[
    { src: '/img/relay/333022_jp1.jpg', alt: 'Relay jumper 1', caption: 'JP1' },
    { src: '/img/relay/333022_jp2.jpg', alt: 'Relay jumper 2', caption: 'JP2' },
    { src: '/img/relay/333022_jp3.jpg', alt: 'Relay jumper 3', caption: 'JP3' },
  ]}
  jumpers={true}
/>

| Jumper  | Default State            | Function                                                                                          |
| ------- | ------------------------ | ------------------------------------------------------------------------------------------------- |
| **JP1** | **NO** (Normally open) | When shorted, it **enables the output LEDs** that pulse for each pin. |
| **JP2** | **NO** (Normally open)   | When shorted, it **enables the output LEDs** that pulse for each pin.                             |
| **JP3** | **NO** (Normally open)   | Enables the **power indicator LED**, which indicates when power is supplied to the circuit board.                           |

<InfoBox>First n (where n represents the number of channels) jumpers always represent output LEDs for every channel. Jumper with the biggest number always represents power indicator LED for the entire circuit board.</InfoBox>

<InfoBox>Jumpers on regular and Qwiic version work in the same way!</InfoBox>

---

## Hardware repository

Schematics, KiCad files, Gerber files and more can be found in the GitHub repository:

<QuickLink 
  title="2-cahnnel relay board qwiic Hardware Design" 
  description="Hardware design, BOM, gerbers and 3D files for 2-channel-relay-board-qwiic designed by Soldered Electronics."
  url="https://github.com/SolderedElectronics/2-channel-relay-board-qwiic-hardware-design" 
/> 

<QuickLink 
  title="2-channel-relay-board-hardware-design" 
  description="Hardware design, BOM, gerbers and 3D files for 2-channel-relay-board designed by Soldered Electronics."
  url="https://github.com/SolderedElectronics/2-channel-relay-board-hardware-design" 
/>

<QuickLink 
  title="1-channel-relay-board-hardware-design" 
  description="Hardware design, BOM, gerbers and 3D files for 1-channel-relay-board designed by Soldered Electronics."
  url="https://github.com/SolderedElectronics/1-channel-relay-board-hardware-design" 
/>

<QuickLink 
  title="4-channel-relay-board-hardware-design" 
  description="Hardware design, BOM, gerbers and 3D files for 4-channel-relay-board designed by Soldered Electronics."
  url="https://github.com/SolderedElectronics/4-channel-relay-board-hardware-design" 
/>

<QuickLink 
  title="1-channel-relay-board-qwiic-hardware-design" 
  description="Hardware design, BOM, gerbers and 3D files for 1-channel-relay-board-qwiic designed by Soldered Electronics."
  url="https://github.com/SolderedElectronics/1-channel-relay-board-qwiic-hardware-design" 
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



