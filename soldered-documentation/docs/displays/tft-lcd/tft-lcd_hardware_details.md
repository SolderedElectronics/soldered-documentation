---
slug: /tft-lcd/hardware
title: 2.4" TFT LCD Breakout – Hardware Details
id: tft-lcd-hardware-details
sidebar_label: Hardware details
hide_title: false
---

## Pinout

<ErrorBox>The pinout image for this board hasn't been generated yet! We're working on it!</ErrorBox>

---

## Pin Details

| Pin Marking | Function             | Description                                                       |
|-------------|----------------------|-------------------------------------------------------------------|
| **VCC**     | Power                | Connect to 3.3V or 5V depending on board's onboard level shifting |
| **GND**     | Ground               | Common ground connection                                          |
| **CLK**     | SPI Clock (SCK)      | Clock signal for display and touchscreen                          |
| **DI**      | SPI Data (MOSI)      | Data output from MCU to display                                   |
| **D0**      | SPI Data (MISO)      | Data input from touchscreen (optional for touch)                  |
| **CSL**     | Display Chip Select  | Chip Select for TFT ILI9341 driver                                |
| **DC**      | Data/Command Select  | Control signal for distinguishing commands from data              |
| **RST**     | Reset                | Optional hardware reset                                           |
| **CST**     | Touch Chip Select    | Chip Select for touch controller (XPT2046)                        |
| **BL**      | Backlight            | Connect to VCC or PWM-capable GPIO for brightness control         |

---

## Dimensions

- **Board size:** 70 x 54 mm
- **Screen size:** 2.4"
- **Resolution:** 240 × 320 pixels
- **Touch Panel Type:** Resistive (XPT2046)
- **Backlight:** Edge-lit LED

---

## What is TFT?

TFT stands for **Thin-Film Transistor**, a display technology that provides active matrix control over each pixel using dedicated transistors. This ensures:
- Faster refresh rates
- Higher brightness and contrast
- Better responsiveness compared to passive matrix LCDs

---

## Components on Board

- **ILI9341**: Main TFT display controller (SPI)
- **XPT2046**: Resistive touchscreen controller (SPI)
- **microSD socket**: SPI interface for data logging, image display, etc.
- **Level-shifter circuitry**: Ensures compatibility with 3.3V and 5V logic

---

## Typical Wiring to Microcontroller

| MCU Pin        | Connects To | Notes                            |
|----------------|-------------|----------------------------------|
| SPI MOSI       | DI          | Data to display                  |
| SPI MISO       | D0          | Needed for reading touch data    |
| SPI SCK        | CLK         | Clock line                       |
| GPIO (Digital) | CSL         | Chip Select for TFT              |
| GPIO (Digital) | CST         | Chip Select for Touch            |
| GPIO (Digital) | DC          | Data/Command                     |
| GPIO (PWM)     | BL          | Optional for brightness control  |
| VCC            | VCC         | 3.3V or 5V depending on board    |
| GND            | GND         | Ground                           |

---

## Notes

<InfoBox>
Make sure your board supplies adequate current. Display with backlight may consume up to 100mA under full brightness and load.
</InfoBox>

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