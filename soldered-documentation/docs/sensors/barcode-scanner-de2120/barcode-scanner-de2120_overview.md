---
slug: /barcode-scanner-de2120/overview
title: Barcode Scanner DE2120 - Overview
sidebar_label: Overview
id: barcode-scanner-de2120-overview
hide_title: true
pagination_prev: null
---

# Overview

## DE2120 2D Barcode Scanner

The **DE2120** is a compact, high-performance **CMOS 2D barcode scanner module** capable of reading **20+ barcode symbologies** — including all major 1D formats (UPC, EAN, Code 128, Code 39) and 2D formats (QR Code, Data Matrix, PDF417, Aztec). It communicates with a microcontroller over **UART (TTL serial)** and is controlled through a simple command protocol.

The Soldered breakout board exposes the scanner's UART interface along with power, trigger, and status pins, making it straightforward to integrate into Arduino-based projects using the provided library.

{/*
TODO: Add product image once available
<CenteredImage src="/img/barcode-scanner-de2120/barcode-scanner-de2120.webp" alt="Barcode Scanner DE2120" caption="DE2120 2D Barcode Scanner Breakout Board" width="500px"/>
*/}

## Which products is this documentation for?

<QuickLink
  title="Barcode Scanner DE2120"
  description="333384"
  url="https://soldered.com/product/barcode-scanner-de2120/"
  image="/img/barcode-scanner-de2120/barcode-scanner-de2120.webp"
/>

## Key Features

* **Supported 1D Symbologies:** UPC-A, UPC-E, EAN-8, EAN-13, Code 128, GS1-128, Code 39, Code 93, Code 11, Interleaved 2 of 5, Codabar (NW-7), MSI Plessey, GS1 Databar, and more
* **Supported 2D Symbologies:** QR Code, Data Matrix, PDF417, Micro PDF417, Aztec
* **Interface:** UART (TTL), 9600 bps (auto-negotiated from 115200)
* **Operating Voltage:** 3.3 V
* **Current Consumption:** < 190 mA (operating)
* **Scan Distance:** 25 mm – 400 mm
* **Image Sensor:** CMOS, 640 × 480 px
* **Light Source:** 5600 K white LEDs (illumination) + 625 nm red LED (aiming reticle)
* **Scan Angles:** Pitch ±45°, Skew ±40°, Roll ±360°
* **Operating Temperature:** –20 °C to 50 °C
* **Scanning Modes:** Manual (trigger), Continuous, Motion Sense
{/* TODO: Add breakout board dimensions once the hardware design is finalized — uncomment and fill in: * **Dimensions:** XX x XX mm */}
