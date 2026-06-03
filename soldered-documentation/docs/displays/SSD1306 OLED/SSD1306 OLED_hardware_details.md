---
slug: /ssd1306-new/hardware
title: SSD1306 - Hardware details
sidebar_label: Hardware details
id: ssd1306-new-hardware
hide_title: false
---

<CenteredImage src="/img/ssd1306/333100_pinout.jpg" alt="Pinout" />

Click [**here**](/img/ssd1306/333100_pinout.jpg) for a high resolution image of the pinout.

| Pin Marking | Pin Name | Description                                     |
| ----------- | -------- | ----------------------------------------------- |
| **GND**     | Ground   | Common ground for power and signals.            |
| **VCC**     | Power    | Supply voltage (both 5V and 3V3 are supported). |
| **SDA**     | Data     | I2C data line for communication.                |
| **SCL**     | Clock    | I2C clock line for communication.               |

<InfoBox>This breakout board operates at **5V logic level** but includes an onboard regulator for **3.3V compatibility**, so it can be connected to both 3.3V and 5V logic boards!</InfoBox>

---

## Qwiic (formerly easyC)

<CenteredImage src="/img/easyc_transparent.png" alt="Qwiic (formerly easyC) cable" width="550px" />

<InfoBox>This display is fully **Qwiic (formerly easyC)-compatible**! Just plug it into your board using a **Qwiic (formerly easyC)/STEMMA QT cable** and start coding!</InfoBox>

<QuickLink 
  title="Qwiic (formerly easyC) details and specifications" 
  description="Learn about hardware specifications, compatibility, and usage of the Qwiic connector." 
  url="/qwiic" 
/>

---

## Jumper details

JP1–JP6 control pull-up voltage, LED power, regulator bypass, and I2C address:

<FlickityCarousel
  images={[
    { src: '/img/ssd1306/333100_jp1.jpg', alt: 'display jumper 1', caption: 'JP1' },
    { src: '/img/ssd1306/333100_jp2.jpg', alt: 'display jumper 2', caption: 'JP2' },
    { src: '/img/ssd1306/333100_jp3.jpg', alt: 'display jumper 3', caption: 'JP3' },
    { src: '/img/ssd1306/333100_jp4.jpg', alt: 'display jumper 4', caption: 'JP4' },
    { src: '/img/ssd1306/333100_jp5.jpg', alt: 'display jumper 5', caption: 'JP5' },
    { src: '/img/ssd1306/333100_jp6.jpg', alt: 'display jumper 6', caption: 'JP6' },
  ]}
  jumpers={true}
/>

| Jumper  | Default State            | Function                                                                                                                                                                 |
| ------- | ------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **JP1** | **NC** (Normally closed) | Connects **SDA/SCL pull-up resistors to 5V** for I2C communication.                                                                                                      |
| **JP2** | **NC** (Normally closed) | Supplies power to the purple LED that indicates the display is turned on.                                                                                                |
| **JP3** | **NC** (Normally closed) | Connects **SDA/SCL pull-up resistors to 3.3V** for I2C communication.                                                                                                    |
| **JP4** | **NC** (Normally closed) | Connects the VCC pin to a 5V to 3V3 voltage regulator IC.                                                                                                                |
| **JP5** | **NO** (Normally open)   | When connected, bypasses the voltage regulator on VCC pin, allowing 3V3 to be connected instead of 5V on VCC pin. **Make sure JP4 is disconnected if JP5 is connected.** |
| **JP6** | **NO** (Normally open)   | I2C address jumper. When shorted, the address is 0x3D; if not, it is 0x3C.                                                                                               |

---

## Dimensions

- **Board Dimensions:** 30 x 30 mm / 1.2 x 1.2 inch
- **Header Pin Holes:** 1.5 mm
- **Screw Holes:** Designed for M3 screws (3.2 mm diameter)
- Soldered boards are LEGO compatible! 🧱

---

## Hardware repository

Schematics, KiCad files, Gerber files, and more can be found in the GitHub repository:

<QuickLink 
  title="Display OLED I2C White 0.96' SSD1306 Hardware design" 
  description="GitHub hardware repository for this product"
  url="https://github.com/SolderedElectronics/Display-OLED-I2C-White-0.96-hardware-design/tree/main" 
/> 

<QuickLink 
  title="Display OLED I2C Blue 0.96' SSD1306 Hardware design" 
  description="GitHub hardware repository for this product"
  url="https://github.com/SolderedElectronics/Display-OLED-I2C-Blue-0.96-hardware-design" 
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

The repository includes standard Gerber outputs in a .zip file:

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
- **Safety Instructions**: Safety guidelines and precautions in English and German.
- **Info.txt**: Contains product details such as SKU, country of origin, HS tariff code, and barcode.
