---
slug: /drv8825/hardware 
title: DRV8825 – Hardware details
id: drv8825-hardware 
hide_title: False
---

## Pinout

<CenteredImage src="/img/drv8825/333000_pinout.jpg" alt="Pinout" />
Click [**here**](/img/drv8825/333000_pinout.jpg) for a high reoslution image of the pinout.

### Pin details

| Pin Marking 	| Pin Name 	| Description 	|
|---	|---	|---	|
| **VIN** 	| Motor Supply Voltage (+) 	| Positive DC voltage input for the stepper. 	|
| **GND** 	| Motor Ground (-) 	| Ground connection for the stepper motor power supply. 	|
| **B2** 	| Stepper Coil B2 	| Second terminal of Coil B in the stepper motor. 	|
| **B1** 	| Stepper Coil B1 	| First terminal of Coil B in the stepper motor. 	|
| **A1** 	| Stepper Coil A1 	| First terminal of Coil A in the stepper motor. 	|
| **A2** 	| Stepper Coil A2 	| Second terminal of Coil A in the stepper motor. 	|
| **Fault** 	| Fault pin 	| Logic low when in fault condition (overtemp, overcurrent) 	|
| **GND** 	| Signal Ground (Microcontroller) 	| Ground reference for the control signals from the microcontroller 	|
| **EN** 	| Enable input 	| Logic high to disable outputs, logic low to enable. 	|
| **M0** 	| Microstep mode 0 	| Set the step mode 	|
| **M1** 	| Microstep mode 1 	| Set the step mode 	|
| **M2** 	| Microstep mode 2 	| Set the step mode 	|
| **RST** 	| Reset input 	| Initialises the indexer logic and disables the H-bridge outputs. 	|
| **SLP** 	| Sleep mode input 	| Logic high to disable device outputs, logic low to enter low-power sleep mode. 	|
| **STEP** 	| Step input 	| Rising edge causes the indexer to move one step. 	|
| **DIR** 	| Direction input 	| Sets the direction of stepping. 	|

<WarningBox>**45V is the maximum** supported Motor supply voltage!</WarningBox>

---

## Dimensions

- **Dimensions:** 38 x 22 mm (1.5 x 0.9 inch)
- **Header Pin Holes:** 1.5 mm
- **Screw Holes:** Designed for M3 screws (3.2 mm diameter)
- Soldered boards are LEGO compatible! 🧱

---

## Jumper Details

This board contains hardware jumpers, se below for  their locations and functions:
<FlickityCarousel
  images={[
    { src: '/img/drv8825/333000_jp1_highlighted.jpg', alt: 'Stepper driver jumper 1', caption: 'JP1' },
  ]}
  jumpers={true}
/>

| Jumper 	| Default State 	| Function 	|
|---	|---	|---	|
| **JP1** 	| **NC** (Normally closed) 	| Enables the **power indicator LED**, which indicates when power is supplied to the board. 	|

---

## Hardware repository

Schematics, KiCad files, Gerber files and more can be found in the GitHub repository:

<QuickLink 
  title="Stepper-motor-driver-DRV8825-board-hardware-design" 
  description="Hardware design, BOM, gerbers and 3D files for Stepper-motor-driver-DRV8825-board designed by Soldered Electronics."
  url="https://github.com/SolderedElectronics/Stepper-motor-driver-DRV8825-board-hardware-design" 
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
