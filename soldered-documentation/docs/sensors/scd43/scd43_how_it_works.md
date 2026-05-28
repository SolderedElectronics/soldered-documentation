---
slug: /scd43/how-it-works
title: SCD43 - How it works
sidebar_label: How it works
id: scd43-how-it-works
hide_title: false
---

The **SCD43** is a CO2, temperature, and humidity sensor by [**Sensirion**](https://sensirion.com/products/catalog/SCD43/). It communicates with a microcontroller via **I2C** at a fixed address of **0x62**.

{/* <CenteredImage src="/img/scd43/scd43_onboard.jpg" alt="SCD43 chip on board" caption="SCD43 on the breakout board" /> */}

---

## Datasheet

<QuickLink
  title="SCD4x Datasheet"
  description="Technical documentation for the Sensirion SCD4x CO2 sensor family (version 1.7, April 2025)"
  url="https://sensirion.com/media/documents/48C4B7FB/67FE0194/CD_DS_SCD4x_Datasheet_D1.pdf"
/>

---

## How the CO2 sensor works

The SCD43 measures CO2 using **photoacoustic NDIR** (Non-Dispersive Infrared) sensing. An infrared light source inside the sensor emits modulated IR light through the sample gas. CO2 molecules absorb IR light at ~4.26 µm, causing them to heat up and expand in sync with the modulation - creating tiny pressure waves that a microphone inside the sensor picks up. The amplitude of these pressure waves corresponds directly to the CO2 concentration.

---

## How the temperature and humidity sensor works

The SCD43 includes a **capacitive humidity sensor**: a polymer film between two electrodes absorbs or releases water molecules from the surrounding air, changing the capacitance between the plates. That change is converted into a relative humidity reading. Temperature is measured at the same time and used to compensate both the humidity and CO2 readings.

---

## Automatic Self-Calibration (ASC)

The SCD43 has an **Automatic Self-Calibration (ASC)** algorithm that corrects long-term CO2 drift. It assumes the sensor is exposed to fresh outdoor air (~420 ppm CO2) periodically and uses those readings to recalibrate over time. ASC is on by default and works well for most indoor installations. It can be turned off when the sensor is never exposed to fresh air - for example in sealed enclosures or industrial setups.

---

## I2C communication

The SCD43 communicates over I2C with a **fixed address of 0x62**.

Two operating modes are available:

- **Periodic measurement mode** - The sensor takes measurements every 5 seconds and stores the latest result. The microcontroller reads CO2, temperature, and humidity with a single command.
- **Single-shot mode** - The sensor takes one measurement on demand, then idles. Useful for low-power applications.

Each measurement returns three values: **CO2 (ppm)**, **temperature (°C)**, and **relative humidity (%)**, packed into a single I2C transaction with CRC checksums.
