---
slug: /capacitive-soil-sensor/hardware 
title: Capacitive Soil Sensor - Hardware details
sidebar_label: Hardware details
id: capacitive-soil-sensor-hardware 
hide_title: False
---


## Pinout


<CenteredImage src="/img/capacitive-soil-sensor/capacitive-soil-sensor-pinout.png" alt="Capacitvie soil sensor pinout image" />

Click [**here**](/img/capacitive-soil-sensor/capacitive-soil-sensor-pinout.png) for a high resolution image of the pinout.

## Pin Details

| Pin Marking | Pin Name | Description                                     |
| ----------- | -------- | ----------------------------------------------- |
| **GND**     | Ground   | Common ground for power and signals.            |
| **AOUT**    | Analog Output | Analog voltage level corresponding to soil moisture. |
| **VCC**     | Power    | Supply voltage (3.3V to 5V).                    |

---

## Dimensions

- **PCB Dimensions:** 109 × 22 mm (4.3 × 0.9 inch)
- **Sensing Area:** ~60 mm length
- **Header Pin Holes:** 1.5 mm diameter  
- **Mounting Hole:** 3.2 mm diameter (M3 screw compatible)  
- **Board Thickness:** ~1.6 mm
- Soldered boards are LEGO compatible! 🧱

---

## Hardware repository

Schematics, KiCad files, Gerber files, and more can be found in the GitHub repository:

<QuickLink 
  title="Capacitive Soil Sensor Hardware Repository" 
  description="Open-source files for PCB design, schematics, and manufacturing." 
  url="https://github.com/SolderedElectronics/Capacitive-soil-sensor-hardware-design" 
/>

The hardware repository contains everything you need to understand, modify, or manufacture the board.

#### CAD files

The `.kicad_pro` project contains both schematic and PCB layout. It can be edited using KiCad.

#### Schematic

Located in the **outputs** folder in `.pdf` format for easy reference.

#### BOM (Bill of Materials)

Includes a `.csv` file listing all components, values, and part numbers. An **interactive HTML BOM** is also included for visual identification of components on the board.

#### 3D files

A `.step` file of the PCB is available for 3D inspection in CAD software.

#### Gerber files

Standard Gerber files and drill files are provided in a `.zip`, ready for fabrication.

- Copper layers (`.Cu.gbr`)
- Solder mask (`.Mask.gbr`)
- Silkscreen (`.Silkscreen.gbr`)
- Drill files (`.drl`)
- Edge cuts (`.Edge_Cuts.gbr`)
- Gerber job file (`.gbrjob`)

#### Compliance

Files for regulatory compliance may be added in future revisions.

