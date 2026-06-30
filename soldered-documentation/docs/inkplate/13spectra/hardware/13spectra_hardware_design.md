---
slug: /inkplate/13spectra/hardware/design
title: Inkplate 13SPECTRA – Hardware design
sidebar_label: Hardware design
id: 13spectra-hardware-design
hide_title: true
---

<SectionTitle title="Hardware design" backgroundImage="/img/inkplate_6_motion/6_motion_hw.png" />

Inkplate 13SPECTRA is an **open-source** product, and we are happy to share an overview of its hardware design. On the following pages, you'll find schematics, KiCad design files, and other technical details related to the hardware. Whether you're looking to modify, troubleshoot, or simply understand the inner workings of Inkplate, this section has everything you need.

<InfoBox>All hardware designs and resources are provided under an [LINK PLACEHOLDER - inkplate 13 opensource license], meaning you're free to explore, modify, and improve upon them as needed.</InfoBox>

---

## Basic overview

The Inkplate 13SPECTRA features a 13.3" e-paper display, USB-C connectivity for both power and programming, abundant GPIO pins with I2C and Qwiic header, onboard ESP32-driven WiFi/Bluetooth, CH340 USB-to-UART bridging, microSD expansion, chac and TI-based power management (battery charing and temperature sensing), RTC and more.

---

## Components

Here is an overview of on-board components with their locations:
[IMAGE PLACEHOLDER - spectra front side with marked components]

<CenteredImage src="/img/13spectra/inkplate-13-spectra-technical-hw-overview.jpg" alt="Inkplate 13SPECTRA backside" caption="Inkplate 13SPECTRA backside" width="1200px" />

<InfoBox>The term "easyC" used here actually refers to **qwiic** connectors.</InfoBox>

---

## E-paper panel

The **[MODEL NAME PLACEHOLDER]** is a **13.3-inch** e-paper display panel from **E Ink Holdings Inc.** This model is **without a frontlight or touchscreen**, making it ideal for **low power, high-contrast applications** that **don't require ultra-fast refresh rates**, such as **displaying images**.

[TEXT PLACEHOLDER - display information]

[TABLE PLACEHOLDER - display specification table]

<InfoBox>**Note:** All specifications listed above are based on available datasheets and may contain minor inaccuracies. Always verify with the manufacturer for the latest details.</InfoBox>