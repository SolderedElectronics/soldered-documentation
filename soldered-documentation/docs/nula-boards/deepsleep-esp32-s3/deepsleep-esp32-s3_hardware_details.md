---
slug: /nula-deepsleep-esp32-s3/hardware-details
title: NULA Deepsleep ESP32-S3 - Hardware details
sidebar_label: Hardware details
id: deepsleep-esp32-s3_hardware_details
hide_title: True
---

# Hardware details

## Pinout

<CenteredImage src="/img/nula-deepsleep-esp32-s3/NULA-DEEPSLEEP-ESP32-S3-Pinout.webp" alt="NULA Deepsleep ESP32-S3 pinout" caption="NULA Deepsleep ESP32-S3 Pinout Diagram"/>

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
| **RX**       | UART RX  | UART0 receive pin for serial communication.                               |
| **TX**       | UART TX  | UART0 transmit pin for serial communication.                              |

<InfoBox>Some GPIOs have dual or special functions such as ADC, DAC, touch sensing, or RTC wake-up. Refer to the ESP32-S3 datasheet for a full pin capabilities list.</InfoBox>

## Qwiic / easyC Connector

<CenteredImage src="/img/easyc_transparent.png" alt="Qwiic/easyC connector" width="550px" />

<InfoBox>The **NULA Deepsleep ESP32-S3** includes a **Qwiic/easyC/STEMMA QT connector** for quick plug-and-play I²C connections with sensors and peripherals.</InfoBox>

<QuickLink
  title="Qwiic (formerly easyC) details and specifications"
  description="Learn more about Qwiic hardware compatibility and connector pinout."
  url="/qwiic"
/>

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
| Deep-sleep        | around 6 µA     |

<InfoBox>These values are approximate and refer only to the ESP32-S3 chip’s consumption. Actual current may vary depending on peripherals, sensors, and LED status.</InfoBox>

## Dimensions

- Board size: 48 × 25.5 × 10.0 mm (1.89 × 1.00 × 0.39 inch)  
- Mounting: Breadboard compatible  
- **Header Pin Holes:** 1.5 mm  
- **Screw Holes:** Designed for M3 screws (3.2 mm diameter)  
- Soldered boards are LEGO compatible! 🧱  

## Jumper Details

This board includes one hardware jumper that can be modified to optimize power usage.

<FlickityCarousel
  images={[
    { src: '/img/nula-deepsleep-esp32-s3/jp1.png', alt: 'nula-deepsleep-jumper1', caption: 'JP1' }
  ]}
  jumpers={true}
/>

| Jumper  | Default State            | Function                                                                         |
| -------- | ------------------------ | -------------------------------------------------------------------------------- |
| **JP1**  | **NC** (Normally closed) | Disconnects the WS2812B RGB LED to minimize standby current in deep-sleep mode. |

<InfoBox>For ultra-low-power battery projects, open **JP1** to completely disable the onboard WS2812B LED.</InfoBox>

## Hardware repository

Schematics, KiCad files, Gerber files and more can be found in the GitHub repository:

<WarningBox>The hardware repository for this board is not available yet! We're working on it. In the meantime, please [**contact us**](https://soldered.com/contact/) to receive the hardware files.</WarningBox>

The hardware repository contains all resources for understanding, modifying, or manufacturing the board.  

#### Available files

- **Schematic (.pdf)** – Electrical connections and circuit design  
- **KiCad project (.kicad_pro)** – Editable schematic and PCB layout  
- **BOM (.csv, .html)** – Complete component list with references  
- **3D Model (.step)** – For visualization and enclosure design  
- **Gerber files (.zip)** – Ready for PCB fabrication  
- **Compliance documents** – CE, UKCA, safety, and product info

