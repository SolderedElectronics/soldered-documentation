---
slug: /scd43/how-it-works
title: SCD43 – How it works
sidebar_label: How it works
id: scd43-how-it-works
hide_title: false
---

The **SCD43** is an integrated CO2, temperature, and humidity sensor by [**Sensirion**](https://sensirion.com/). When using our board, you are communicating directly with the onboard SCD43 chip via **I2C communication**.

{/* TODO: Add onboard chip image once available: /img/scd43/scd43_onboard.jpg */}

---

## Datasheet

For an in-depth look at technical specifications, refer to the official SCD4x Datasheet:

<QuickLink
  title="SCD4x Datasheet"
  description="Detailed technical documentation for the Sensirion SCD4x CO2 sensor family (version 1.7, April 2025)"
  url="https://sensirion.com/media/documents/48C4B7FB/67FE0194/CD_DS_SCD4x_Datasheet_D1.pdf"
/>

---

## How the CO2 sensor works

The SCD43 measures CO2 concentration using **photoacoustic NDIR** (Non-Dispersive Infrared) sensing. An infrared light source inside the sensor emits modulated IR light through the sample gas. CO2 molecules absorb IR light at a specific wavelength (~4.26 µm), causing them to heat up and expand rhythmically in sync with the modulation. This creates **tiny pressure waves — essentially sound** — that are picked up by a sensitive microphone inside the sensor. The amplitude of these pressure waves is directly proportional to the **CO2 concentration** in the air.

This photoacoustic approach allows the SCD43 to achieve accurate CO2 readings in an ultra-compact package without needing a long optical path.

---

## How the temperature and humidity sensor works

Alongside CO2, the SCD43 includes an integrated **temperature and humidity sensor**. It works on a **capacitive principle**: a polymer film between two electrodes absorbs or releases water molecules from the surrounding air, changing the capacitance between the plates. This change is converted into a relative humidity reading. Temperature is measured simultaneously and used internally to compensate both the humidity and CO2 readings for improved accuracy.

---

## Automatic Self-Calibration (ASC)

The SCD43 features an **Automatic Self-Calibration (ASC)** algorithm that continuously corrects long-term CO2 drift. It works by assuming the sensor is periodically exposed to fresh outdoor air (~420 ppm CO2) and using those baseline readings to recalibrate over time. ASC is enabled by default and is suitable for most indoor air quality applications. It can be disabled for use cases where the sensor never sees fresh air (e.g., sealed environments or industrial monitoring).

---

## I2C communication

The SCD43 uses the **I2C protocol** to communicate with a microcontroller. It operates with a **fixed I2C address of 0x62**.

The sensor supports two main operating modes:

- **Periodic measurement mode** – The sensor continuously takes measurements at a fixed interval (default: every 5 seconds) and stores the latest result. The host microcontroller reads CO2, temperature, and humidity with a single read command.
- **Single-shot mode** – The sensor takes one measurement on demand and then idles, which is useful for low-power applications.

Each measurement response contains three values: **CO2 (ppm)**, **temperature (°C)**, and **relative humidity (%)**, all packed into a single I2C transaction with CRC checksums for data integrity.
