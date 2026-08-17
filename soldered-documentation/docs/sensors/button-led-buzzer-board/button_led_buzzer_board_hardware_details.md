---
slug: /button-led-buzzer-board/hardware
title: Button, LED & Buzzer Board - Hardware details
sidebar_label: Hardware details
id: button_led_buzzer_board-hardware
hide_title: false
---

## Pinout

<CenteredImage src="/img/button_led_buzzer_board/pinout.png" alt="Pinout" />
Click [**here**](/img/button_led_buzzer_board/pinout.png) for a high resolution image of the pinout.

---

## Pin details

The five through-holes are split across two separate headers, one on each side of the board.

**UPDI header** (left side):

| Pin Marking | Pin Name | Description |
|---|---|---|
| **VCC** | Power | 3.3 V supply, the same rail the Qwiic connectors carry |
| **UPDI** | Programming | UPDI programming interface for the onboard microcontroller |
| **GND** | Ground | Common ground for power and signals |

**I2C header** (right side):

| Pin Marking | Pin Name | Description |
|---|---|---|
| **SCL** | I2C Clock | I2C clock line, the same net as both Qwiic connectors |
| **SDA** | I2C Data | I2C data line, the same net as both Qwiic connectors |

<InfoBox>The board has two identical **Qwiic connectors** wired in parallel, so you can daisy-chain other Qwiic devices from it.</InfoBox>

<InfoBox>The I2C header carries only **SCL** and **SDA** - it has no power pins. If you wire the board up by hand instead of using a Qwiic cable, take **VCC** and **GND** from the UPDI header on the other side.</InfoBox>

---

## Onboard components

- **3 tactile push buttons**, numbered 1-3 on the silkscreen. Each is read as one bit over I2C.
- **3 addressable RGB LEDs (WS2812B)**, one next to each button, individually controllable.
- **1 passive piezo buzzer**, driven with a PWM signal to produce a tone.
- **1 three-position DIP switch**, used to set the I2C address (see below).

---

## I2C address

The board answers on **0x30** out of the box. The three-position DIP switch on the top of the board is wired to the address inputs of the onboard ATtiny404, so you can give each board a different address and run several of them on the same bus.

The library's constructor takes the address, so pass it in if you have changed the switch:

```cpp
ButtonLedBuzzerBoard_Soldered board(0x31);
```

<InfoBox>All switches off is the default **0x30**. If you are unsure which address a board is set to, run an I2C scanner sketch and see which address responds.</InfoBox>

---

## Dimensions

- **Board Dimensions:** 38 × 22 mm (1.5 × 0.9 inch)
- **Board thickness:** 1.6 mm, 2-layer PCB
- **Header Pin Holes:** 1.0 mm, on the standard 2.54 mm pitch
- **Screw Holes:** Two 3.2 mm holes, designed for M3 screws
- Soldered boards are LEGO compatible! 🧱

---

## Hardware repository

Schematics, KiCad files, Gerber files and more can be found in the GitHub repository:

<WarningBox>The hardware repository for this board is not available yet! We're working on it. In the meantime, please [**contact us**](https://soldered.com/contact/) to receive the hardware files.</WarningBox>

These pages describe hardware revision **v1.1**.

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

- **Copper layers** (`.Cu.gbr`) - Defines the traces and pads on the board.
- **Solder mask layers** (`.Mask.gbr`) - Specifies the protective solder mask.
- **Silkscreen layers** (`.Silkscreen.gbr`) - Contains text and component markings.
- **Paste layers** (`.Paste.gbr`) - Used for stencil fabrication in SMD assembly.
- **Drill files** (`.drl`) - Provides drilling coordinates for vias and holes.
- **Board outline** (`.Edge_Cuts.gbr`) - Defines the shape of the PCB.
- **Gerber job file** (`.gbrjob`) - Describes the set of Gerber files used for production.

These files are ready for fabrication and can be used in PCB manufacturing.

#### Compliance

The **Compliance** section includes important regulatory and safety documentation for this product. These files ensure compliance with relevant industry standards and legal requirements.

- **CE** - Certification document confirming compliance with EU safety, health, and environmental requirements.
- **UKCA** - UKCA (UK Conformity Assessed) certification for the UK market.
- **Safety Instructions** - Safety guidelines and precautions in English and in German.
- **Info.txt** - Contains product details such as SKU, country of origin, HS tariff code, and barcode.


