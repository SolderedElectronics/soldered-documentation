---
slug: /w5500/hardware 
title: Hardware details
id: w5500-hardware 
hide_title: False
---

## Pinout

<ErrorBox>The pinout image for this board has not been generated yet. We are working on it!</ErrorBox>

---

## Pin Details

| Pin Marking 	| Pin Name           	| Description                                         	|
|--------------	|--------------------	|-----------------------------------------------------	|
| **GND**    	| Ground             	| Common ground.                                      	|
| **VCC**    	| Power              	| Power supply.                                       	|
| **INTN**   	| Interrupt output   	| Active low interrupt pin.                           	|
| **RSTN**   	| Reset              	| Active low reset pin.                               	|
| **MISO**   	| SPI communication  	| SPI master input, slave (W5500) output.             	|
| **MOSI**   	| SPI communication  	| SPI master output, slave (W5500) input.             	|
| **SCLK**   	| Clock              	| SPI clock input.                                    	|
| **SCSN**   	| Chip select        	| Chip select for the SPI bus.                        	|

---

## Dimensions

- **Board Dimensions:** **54mm x 38mm** (2.1 x 1.5 inch)
- **Header Pin Holes:** 1.5 mm  
- **Screw Holes:** Designed for M3 screws (3.2 mm diameter)  
- Soldered boards are LEGO compatible! 🧱 

---

## Jumper Details

This board contains hardware jumpers. See below for their locations and functions:

<FlickityCarousel
  images={[
    { src: '/img/w5500/jp1.png', alt: 'w5500-jp1', caption: 'JP1' },
    { src: '/img/w5500/jp2.png', alt: 'w5500-jp2', caption: 'JP2' },
    { src: '/img/w5500/jp3.png', alt: 'w5500-jp3', caption: 'JP3' },
    { src: '/img/w5500/jp4.png', alt: 'w5500-jp4', caption: 'JP4' },
  ]}
  jumpers={true}
/>

| Jumper 	| Default State                  	| Function                                                         	|
|--------	|--------------------------------	|-------------------------------------------------------------------	|
| **JP1** 	| **NC** (Normally closed)       	| When closed, it enables the PWR LED.                               	|
| **JP2** 	| **NO** (Normally open)          	| PHY Operation mode select pin PMODE0.                              	|
| **JP3** 	| **NO** (Normally open)          	| PHY Operation mode select pin PMODE1.                              	|
| **JP4** 	| **NO** (Normally open)          	| PHY Operation mode select pin PMODE2.                              	|

PHY operation mode pins determine the network mode. Refer to the table below for details:

| PMODE2 	| PMODE1 	| PMODE0 	| Description                                             	|
|--------	|--------	|--------	|---------------------------------------------------------	|
| 0      	| 0      	| 0      	| 10BT Half-Duplex, Auto-negotiation disabled.             	|
| 0      	| 0      	| 1      	| 10BT Full-Duplex, Auto-negotiation disabled.             	|
| 0      	| 1      	| 0      	| 100BT Half-Duplex, Auto-negotiation disabled.            	|
| 0      	| 1      	| 1      	| 100BT Full-Duplex, Auto-negotiation disabled.            	|
| 1      	| 0      	| 0      	| 100BT Half-Duplex, Auto-negotiation enabled.             	|
| 1      	| 0      	| 1      	| Not used.                                              	|
| 1      	| 1      	| 0      	| Not used.                                              	|
| 1      	| 1      	| 1      	| All capable, Auto-negotiation enabled.                 	|

---

## Hardware repository

Schematics, KiCad files, Gerber files, and more can be found in the GitHub repository:

<QuickLink 
  title="Ethernet controller W5500 board Hardware Design" 
  description="GitHub hardware repository for this product"
  url="https://github.com/SolderedElectronics/Ethernet-controller-W5500-board-hardware-design" 
/> 

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