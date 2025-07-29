---
slug: /simple-sensor/capacitive-soil-sensor/how-it-works
title: Capacitive Soil Sensor - How it works
sidebar_label: How it works
id: capacitive-soil-sensor-how-it-works
hide_title: false
---

The **Capacitive Soil Sensor** is a robust and corrosion-resistant device for measuring soil moisture. Unlike resistive sensors that rely on exposed metal probes, this sensor uses a capacitive sensing principle, resulting in longer lifespan and more reliable measurements in harsh environments.

<CenteredImage src="/img/capacitive-soil-sensor/333098.jpg" alt="Top view of the capacitive soil sensor" caption="Top view of the capacitive soil sensor" width="500px" />

---

## What’s on board?

This sensor is based on the **TLC555CD** IC – a CMOS version of the popular 555 timer from **Texas Instruments**. It’s used to generate a frequency that changes based on the capacitance of the soil. As soil moisture increases, the capacitance of the sensing area increases, altering the output frequency or voltage.

<QuickLink  
  title="TLC555CD Datasheet"  
  description="Official datasheet for the TLC555CD timer IC used in the capacitive soil sensor."  
  url="https://www.ti.com/lit/ds/symlink/tlc555.pdf"  
/>

<CenteredImage src="/img/capacitive-soil-sensor/333098_ic_highlighted.jpg" alt="TLC555CD IC location" caption="TLC555CD IC used on the sensor board" width="400px" />

---

## How it works

The capacitive soil moisture sensor detects changes in soil moisture using a **capacitive pad**. The pad forms one plate of a capacitor, while the surrounding soil acts as the dielectric. Moisture changes the dielectric constant, affecting the capacitance.

This capacitance is part of an RC (resistor-capacitor) circuit controlled by the TLC555CD timer. As the soil moisture changes, the capacitance shifts, causing the output pulse width or analog voltage to vary. This change can be measured by a microcontroller's **analog input** pin.

<InfoBox>This sensor provides an **analog voltage output** that correlates with the moisture level of the soil. Lower voltage generally indicates wetter soil.</InfoBox>

---

## Advantages over resistive sensors

- **Corrosion-resistant**: No exposed metal contacts
- **More reliable over time**: Ideal for long-term projects
- **Better performance in chemically active soils**

