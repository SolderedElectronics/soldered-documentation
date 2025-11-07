---
slug: /nula-deepsleep-esp32-s3/hardware-details
title: NULA Deepsleep ESP32-S3 - Hardware details
sidebar_label: Hardware details
id: deepsleep-esp32-s3_hardware_details
hide_title: True
---

# Hardware details

## Pinout

<CenteredImage src="/img/nula-deepsleep-esp32-s3/NULA-DEEPSLEEP-ESP32-S3-Pinout.webp" alt="NULA Deepsleep ESP32-S3 pinout" caption="NULA DeepSleep ESP32-S3 Pinout Diagram"/>

Click [**here**](/img/nula-deepsleep-esp32-s3/NULA-DEEPSLEEP-ESP32-S3-Pinout.webp) for a high-resolution image of the pinout.

## Pin Details

| Pin Marking | Pin Name | Description                                                               |
| ------------ | -------- | ------------------------------------------------------------------------- |
| **VBAT**     | Power    | Battery input for 3.7 V Li-Ion/Li-Poly battery through the JST connector. |
| **VCC**      | Power    | Main power input (5 V via USB-C or external 5 V supply).                  |
| **3V3**      | Power    | Regulated 3.3 V output from the onboard regulator.                        |
| **GND**      | Ground   | Common ground for power and signals.                                      |
| **RESET**    | Control  | Hardware reset pin.                                                       |
| **IO0–IO48** | GPIO     | General-purpose I/O pins, supporting PWM, I²C, SPI, UART, ADC, and touch. |
| **RX**       | RX  | UART0 receive pin for serial communication.                               |
| **TX**       | TX  | UART0 transmit pin for serial communication.                              |

<InfoBox>Some GPIOs have dual or special functions such as ADC, DAC, touch sensing, or RTC wake-up. Refer to the ESP32-S3 datasheet for a full pin capabilities list.</InfoBox>

---

## Qwiic / easyC Connector

<CenteredImage src="/img/easyc_transparent.png" alt="Qwiic/easyC connector" width="550px" />

<InfoBox>The **NULA DeepSleep ESP32-S3** includes a **Qwiic/easyC/STEMMA QT connector** for quick plug-and-play I²C connections with sensors and peripherals.</InfoBox>

<QuickLink
  title="Qwiic (formerly easyC) details and specifications"
  description="Learn more about Qwiic hardware compatibility and connector pinout."
  url="/qwiic"
/>

---

## Power Supply and Battery

- USB-C Port is used for both programming and powering the board  
- VBAT (JST connector) is used for connecting a 3.7 V Li-Ion or Li-Poly battery  
- The board includes an integrated Li-Ion charge management circuit  
- Operating voltage: 3.3 V (onboard regulator for 5 V input via USB-C)  

<InfoBox>The onboard power management system automatically handles charging and discharging when a battery is connected.  
For 5 V input, always power the board through the USB-C port.</InfoBox>

## Power Consumption

| Mode              | Typical Current |
| ----------------- | --------------- |
| Active (Wi-Fi TX) | around 240 mA   |
| Modem-sleep       | around 20 mA    |
| Light-sleep       | around 1.5 mA   |
| Deep-sleep        | around 7 µA     |

<InfoBox>These values are approximate and refer only to the ESP32-S3 chip’s consumption. Actual current may vary depending on peripherals, sensors, and LED status.</InfoBox>

---

## Achieving the lowest deep-sleep current

The **NULA DeepSleep ESP32-S3** has been engineered to minimize power consumption during sleep modes, making it ideal for long-term battery-powered applications such as remote sensors and data loggers.  

When properly configured, the board can achieve a **deep-sleep current as low as 7 µA**, consistent with the values specified in the **ESP32-S3 datasheet**.  
This level of performance assumes that all peripheral components are powered down and that the RGB status LED (WS2812B) is electrically isolated.

To achieve the lowest possible consumption:
- Ensure that no external devices are drawing power from the 3V3 or VCC rails during sleep.  
- Disconnect any I²C sensors or modules that lack dedicated power management.  
- **Open the JP1 solder jumper** to physically disconnect the onboard WS2812B RGB LED, which can otherwise introduce a small but measurable leakage current.  

---

## Dimensions

- **Board size**: 69 × 26 mm (2.72 × 1.02 inch)  
- **Mounting**: Breadboard compatible  
- **Header Pin Holes:** 1.5 mm  
- **Screw Holes:** Designed for M3 screws (3.2 mm diameter)  

Soldered boards are LEGO compatible! 🧱  

---

## Jumper Details

This board includes one hardware jumper that can be modified to optimize power usage.

<CenteredImage src="/img/nula-deepsleep-esp32-s3/jp1.png" alt="Qwiic/easyC connector" width="800px" />

| Jumper  | Default State            | Function                                                                         |
| -------- | ------------------------ | -------------------------------------------------------------------------------- |
| **JP1**  | **NC** (Normally closed) | Disconnects the WS2812B RGB LED to minimize standby current in deep-sleep mode. |

<InfoBox>For ultra-low-power battery projects, open **JP1** to completely disable the onboard WS2812B LED.</InfoBox>

---

## Hardware repository

Schematics, KiCad files, Gerber files and more can be found in the GitHub repository:

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