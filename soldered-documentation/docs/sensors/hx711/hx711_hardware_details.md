---
slug: /hx711/hardware 
title: Hardware details
id: hx711-hardware 
hide_title: False
---

## HX711 Regular Pinout

<CenteredImage src="/img/hx711/hx711_standard_pinout.png" alt="hx711_standard_pinout" caption="HX711 regular pinout diagram"/>

Click [**here**](/img/hx711/hx711_standard_pinout.png) for a high resolution image of the pinout.

---

## HX711 Qwiic Pinout

<CenteredImage src="/img/hx711/hx711_easyc_pinout.png" alt="hx711_easyc_pinout" caption="HX711 qwiic (easyC) pinout diagram"/>

Click [**here**](/img/hx711/hx711_easyC_pinout.png) for a high resolution image of the pinout.

---

## Pin Details Regular Version

| Pin Marking | Pin Name                 | Description                                                                                                             |
| ----------- | ------------------------ | ----------------------------------------------------------------------------------------------------------------------- |
| **E+**      | Excitation Positive      | Provides positive excitation voltage to the load cell. Typically connected to the red wire of the load cell.            |
| **E-**      | Excitation Negative      | Provides negative excitation voltage (ground) to the load cell. Typically connected to the black wire of the load cell. |
| **A+**      | Channel A Positive Input | Positive differential input for Channel A. Typically connected to the white wire of the load cell.                      |
| **A-**      | Channel A Negative Input | Negative differential input for Channel A. Typically connected to the green wire of the load cell.                      |
| **B+**      | Channel B Positive Input | Positive differential input for Channel B. This is a secondary input channel.                                           |
| **B-**      | Channel B Negative Input | Negative differential input for Channel B. This is a secondary input channel.                                           |
| **GND**     | Ground                   | Common ground for power and signals.                                                                                    |
| **VCC**     | Power                    | Supply voltage for the HX711 module. Accepts 2.7V to 5.5V.                                                              |
| **DAT**     | Data                     | Serial data output for communication with a microcontroller.                                                            |
| **SCK**     | Clock                    | Serial clock input for communication with a microcontroller.                                                            |

---

## Pin Details Qwiic Version

| Pin Marking | Pin Name                 | Description                                                                                                             |
| ----------- | ------------------------ | ----------------------------------------------------------------------------------------------------------------------- |
| **E+**      | Excitation Positive      | Provides positive excitation voltage to the load cell. Typically connected to the red wire of the load cell.            |
| **E-**      | Excitation Negative      | Provides negative excitation voltage (ground) to the load cell. Typically connected to the black wire of the load cell. |
| **A+**      | Channel A Positive Input | Positive differential input for Channel A. Typically connected to the white wire of the load cell.                      |
| **A-**      | Channel A Negative Input | Negative differential input for Channel A. Typically connected to the green wire of the load cell.                      |
| **B+**      | Channel B Positive Input | Positive differential input for Channel B. This is a secondary input channel.                                           |
| **B-**      | Channel B Negative Input | Negative differential input for Channel B. This is a secondary input channel.                                           |
| **GND**     | Debug Ground             | Ground pin for debugging purposes.                                                                                      |
| **UPDI**    | Debug Interface          | Used for debugging and programming the onboard ATTiny404 microcontroller.                                               |
| **3V3**     | Debug Power              | 3.3V power supply for debugging purposes.                                                                               |

<WarningBox>The **GND, UPDI, and 3V3 pins** are **for debugging and programming the onboard ATTINY**. They are **not required** for normal operation and should only be used by advanced users.</WarningBox>

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

## Electrical Characteristics  

- **Power Requirements**  
   - **Operating Voltage:** 2.6V – 5.5V  
   - **Current Consumption:** < 1.5mA (typical during operation)  
   - **Sleep Mode Current:** < 1µA (low-power standby mode)  
- **Operating Conditions**  
   - **Operating Temperature Range:** **-40°C to 85°C**  
   - **Recommended Load Cell Type:** **Wheatstone Bridge-based strain gauges**  

---

## Dimensions

- **Board Dimensions Regular:** 22 × 22 mm (0.9 × 0.9 inch)  
- **Board Dimensions Qwiic (easyC):** 38 × 22 mm (1.5 × 0.9 inch)  
- **Header Pin Holes:** 1.5 mm  
- **Screw Holes:** Designed for M3 screws (3.2 mm diameter)  
- Soldered boards are LEGO compatible! 🧱 

---

## Address selection (Qwiic version)

This board contains hardware address switches. See below for instructions on how to change the breakout board's address:

<CenteredImage src="/img/hx711/address_selection.png" alt="Pinout" width="500px" />

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

Schematics, KiCad files, Gerber files and more can be found in the GitHub repository:

<QuickLink 
  title="HX711 Regular Hardware design" 
  description="GitHub hardware repository for this product"
  url="https://github.com/SolderedElectronics/Load-cell-ampfilier-HX711-board-hardware-design" 
/> 

<QuickLink 
  title="HX711 Qwiic (easyC) Hardware design" 
  description="GitHub hardware repository for this product"
  url="https://github.com/SolderedElectronics/Load-cell-ampfilier-HX711-board-with-easy-C-hardware-design" 
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