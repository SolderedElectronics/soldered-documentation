---
slug: /inkplate/13spectra/hardware/design
title: Inkplate 13SPECTRA – Hardware design
sidebar_label: Hardware design
id: 13spectra-hardware-design
hide_title: true
---

<SectionTitle title="Hardware design" backgroundImage="/img/13spectra/inkplate-13-spectra-technical-hw-overview.jpg" />

Inkplate 13SPECTRA is an **open-source** product, and we are happy to share an overview of its hardware design. On the following pages, you'll find schematics, KiCad design files, and other technical details related to the hardware. Whether you're looking to modify, troubleshoot, or simply understand the inner workings of Inkplate, this section has everything you need.

<InfoBox>All hardware designs and resources will be released under an open-source license once the Inkplate 13SPECTRA hardware repository is published, meaning you'll be free to explore, modify, and improve upon them.</InfoBox>

---

## Basic overview

The Inkplate 13SPECTRA features a 13.3" e-paper display, USB-C connectivity for both power and programming, abundant GPIO pins with I2C and Qwiic header, onboard ESP32-driven WiFi/Bluetooth, CH340 USB-to-UART bridging, microSD expansion, such and TI-based power management (battery charging and temperature sensing), RTC and more.

---

## Components

Here is an overview of on-board components with their locations:

<CenteredImage src="/img/13spectra/inkplate-13-spectra-technical-hw-overview.jpg" alt="Inkplate 13SPECTRA backside" caption="Inkplate 13SPECTRA backside" width="1200px" />

---

## E-paper panel

The **E Ink EL133UF1** is a **13.3-inch** e-paper display panel from **E Ink Holdings Inc.** This model is **without a frontlight or touchscreen**, making it ideal for **low power, high-contrast applications** that **don't require ultra-fast refresh rates**, such as **displaying images**.

The EL133UF1 uses **E Ink Spectra™ 6** technology, a six-color active-matrix panel built on a glass backplane. Unlike grayscale Inkplate panels, it renders **black, white, yellow, red, green, and blue** directly, without dithering, giving flat, vivid color fills at the cost of only supporting **full-screen refreshes** (no partial updates or grayscale). It communicates over an **SPI interface** through a 60-pin FPC connector, and its glass construction makes it more rigid, but also more fragile, than the flexible panels used on some other Inkplate models.

| Parameter | Specification |
|---|---|
| **Model** | E Ink EL133UF1 |
| **Technology** | E Ink Spectra™ 6 (six-color ePaper) |
| **Screen size** | 13.3" |
| **Resolution** | 1600 × 1200 px |
| **Active area** | 270.4 × 202.8 mm |
| **Pixel density** | 150 ppi |
| **Pixel pitch** | 0.169 × 0.169 mm |
| **Colors** | Black, White, Yellow, Red, Green, Blue |
| **Interface** | SPI |
| **Connector** | 60-pin FPC, 0.5 mm pitch |
| **Backplane** | Glass |
| **Panel outline** | 284.7 × 208.8 × 0.85 mm |
| **Weight** | 50 ± 10 g |
| **Operating temperature** | 0 °C to 50 °C |
| **Partial update support** | Not supported (full refresh only) |