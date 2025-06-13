---
slug: /stepper-motor-driver/hardware
title: Stepper Motor Driver - Hardware details
sidebar_label: Hardware details
id: stepper-motor-driver-hardware
hide_title: false
---

## Pinout

<CenteredImage src="/img/stepper-motor-driver/333134_pinout.jpg" alt="Pinout" />

Click [**here**](/img/stepper-motor-driver/333134_pinout.jpg) for a high reoslution image of the pinout.

### Pin details

| Pin Marking | Pin Name                        | Description                                                        |
| ----------- | ------------------------------- | ------------------------------------------------------------------ |
| **IN1**     | Stepper Coil A1                 | First terminal of Coil A in the stepper motor.                     |
| **IN2**     | Stepper Coil A2                 | Second terminal of Coil A in the stepper motor.                    |
| **IN3**     | Stepper Coil B1                 | First terminal of Coil B in the stepper motor.                     |
| **IN4**     | Stepper Coil B2                 | Second terminal of Coil B in the stepper motor.                    |
| **GND**     | Signal Ground (Microcontroller) | Ground reference for the control signals from the microcontroller. |
| **VCC**     | Motor Supply Voltage (+)        | Positive DC voltage input for the stepper motor power supply.      |
| **GND**     | Motor Ground (-)                | Ground connection for the stepper motor power supply.              |


<InfoBox>The IN pins can work at **3V3** or **5V** logic</InfoBox>
<WarningBox>**14V is the maximum** supported Motor supply voltage!</WarningBox>
<WarningBox>If you have the version of this product with the stepper motor, the **motor supply voltage needs to be exactly 5V**!</WarningBox>

As for the actual stepper motor connection, this is the pinout of the connector, in relation to the input pins:

<CenteredImage src="/img/stepper-motor-driver/stepper_pinout.jpg" alt="Basic stepper driver connected to Dasduino CORE" caption="Basic stepper driver connected to Dasduino CORE" width="600px" />

---

## Jumper Details

This board contains hardware jumpers, see below for their locations and functions:

<FlickityCarousel
  images={[
    { src: '/img/stepper-motor-driver/stepper_jp1.png', alt: 'Stepper driver jumper 1', caption: 'JP1' },
    { src: '/img/stepper-motor-driver/stepper_jp2.png', alt: 'Stepper driver jumper 2', caption: 'JP2' },
  ]}
  jumpers={true}
/>

| Jumper  | Default State            | Function                                                                                          |
| ------- | ------------------------ | ------------------------------------------------------------------------------------------------- |
| **JP1** | **NC** (Normally closed) | Enables the **power indicator LED**, which indicates when power is supplied to the stepper motor. |
| **JP2** | **NO** (Normally open)   | When shorted, it **enables the output LEDs** that pulse for each pin.                             |

---

## Dimensions

- **Board Dimensions:** 38 × 22 mm (1.5 × 0.9 inch)
- **Header Pin Holes:** 1.5 mm
- **Screw Holes:** Designed for M3 screws (3.2 mm diameter)
- Soldered boards are LEGO compatible! 🧱

---

## Motor

The version of the product with the stepper motor ships with the **28BYJ-48 5V DC** stepper motor. It's cable fits the connector on our basic stepper board and can just be plugged in. This motor has **2048 steps per one revolution**. See below for a pinout in relation to the internal coils:

<CenteredImage src="/img/stepper-motor-driver/motor.png" alt="28BYJ-48 5V DC stepper motor" caption="28BYJ-48 5V DC stepper motor" width="400px" />

---

## Hardware repository

Schematics, KiCad files, Gerber files and more can be found in the GitHub repository:

<QuickLink 
  title="Basic stepper driver Hardware design" 
  description="GitHub hardware repository for this product"
  url="https://github.com/SolderedElectronics/Basic-stepper-driver-hardware-design/tree/main" 
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
