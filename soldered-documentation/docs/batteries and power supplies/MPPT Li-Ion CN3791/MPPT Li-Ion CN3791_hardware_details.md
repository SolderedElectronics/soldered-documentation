---
slug: /mppt-li-ion-cn3791/hardware
title: Hardware details
sidebar_label: Hardware details
id: mppt-li-ion-cn3791-hardware
hide_title: false
---

## Pinout

<CenteredImage src="/img/mppt_li-ion_cn3971/Pinout.png" alt="MPPT Li-Ion CN3791 charger board pinout" />

Click [**here**](/img/mppt_li-ion_cn3971/Pinout.png) for a high-resolution image of the pinout.

## Pin details

| Pin Marking       | Description                                                                                                                                |
| ----------------- | ------------------------------------------------------------------------------------------------------------------------------------------ |
| **IN+**           | Solar positive terminal.                                                                                                                   |
| **IN-**           | Solar negative terminal.                                                                                                                   |
| **OUT+**          | Battery positive terminal.                                                                                                                 |
| **OUT-**          | Battery negative terminal.                                                                                                                 |
| **SOLAR VOLTAGE** | Photovoltaic cell maximum power point tracking pin. **Short the connections on pin that corresponds to the voltage that your panel produces.** |

<InfoBox>In maximum power point tracking status, the MPPT pin's voltage is regulated to 1.205V.</InfoBox>

---

## Dimensions

- **Board Dimensions:** 54 × 38 mm (2.1 × 1.5 inch)  
- **Header Pin Holes:** 1.5 mm  
- **Screw Holes:** Designed for M3 screws (3.2 mm diameter)  
- Soldered boards are LEGO-compatible! 🧱

---

## LED indicators

The board has three onboard LEDs:

| LED | Color | Function |
|-----|-------|----------|
| D1 | Green | Power indicator |
| D2 | Red | Charging indicator |
| D5 | Purple | Charge complete indicator |

---

## Jumper details

<InfoBox>Image coming soon.</InfoBox>

| Jumper  | Default State            | Function         |
| ------- | ------------------------ | ---------------- |
| **JP1** | **NC** (Normally closed) | Connects PWR LED |

---

## Hardware repository

Schematics, KiCad files, Gerber files, and more can be found in the GitHub repository:

<QuickLink 
  title="MPPT Li-Ion CN3791 charger board Hardware Design" 
  description="GitHub hardware repository for this product"
  url="https://github.com/SolderedElectronics/MPPT-Li-Ion-CN3791-charger-board-hardware-design/tree/main" 
/> 

The output folders are versioned. You can find which board version you have by checking the version mark on the PCB.

#### CAD files

We use KiCad, an open-source PCB design tool. You can open and edit the `.kicad_pro` project file, which includes both the schematic and PCB layout.

The `PANEL` files are used internally for production.

#### Schematic

The **OUTPUTS** folder contains the schematic in `.pdf` format, exported from KiCad.

#### BOM (Bill of Materials)

The bill of materials (BOM) is provided in two formats:

- A **standard `.csv` table**, listing all components, part numbers, and values.
- An **interactive BOM (`.html`)** that visually highlights each component on the PCB, making it easy to locate and reference parts.

#### 3D files

A **3D model** of the PCB is available in `.step` format, allowing you to inspect the board design in CAD software.

#### Gerber files

Gerber files are essential for PCB manufacturing, as they contain precise instructions for each layer of the board. The repository includes standard Gerber outputs in a .zip file, such as:

- **Copper layers** (`.Cu.gbr`): Defines the traces and pads on the board.
- **Solder mask layers** (`.Mask.gbr`): Specifies the protective solder mask.
- **Silkscreen layers** (`.Silkscreen.gbr`): Contains text and component markings.
- **Paste layers** (`.Paste.gbr`): Used for stencil fabrication in SMD assembly.
- **Drill files** (`.drl`): Provides drilling coordinates for vias and holes.
- **Board outline** (`.Edge_Cuts.gbr`): Defines the shape of the PCB.
- **Gerber job file** (`.gbrjob`): Describes the set of Gerber files used for production.

#### Compliance

Regulatory and safety documents for this product:

- **CE**: Certification document confirming compliance with EU safety, health, and environmental requirements.
- **UKCA**: UKCA (UK Conformity Assessed) certification for the UK market.
- **Safety Instructions**: Safety guidelines and precautions provided in English and German.
- **Info.txt**: Contains product details such as SKU, country of origin, HS tariff code, and barcode.
