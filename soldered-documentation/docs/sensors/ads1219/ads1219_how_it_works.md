---
slug: /ads1219/how-it-works 
title: ADS1219 24-bit ADC - How it works
sidebar_label: How it works
id: ads1219-how-it-works 
hide_title: False
---

The ADS1219 is a precision **24-bit delta-sigma analog-to-digital converter (ADC)** manufactured by [**Texas Instruments**](https://www.ti.com/product/ADS1219). When using our board, you are communicating directly with the onboard ADS1219 via **I2C communication**.

<ErrorBox>A photo of the ADS1219 chip on the board is not available yet! We're working on it.</ErrorBox>

---

## Datasheet

For an in-depth look at technical specifications, see the official ADS1219 Datasheet:

<QuickLink  
  title="ADS1219 Datasheet"  
  description="Detailed technical documentation for the ADS1219 24-bit ADC"  
  url="https://www.ti.com/lit/ds/symlink/ads1219.pdf"  
/>

---

## How it works

The **ADS1219** is a **delta-sigma (ΔΣ) analog-to-digital converter** that achieves high resolution and low noise by oversampling and filtering the input signal. It works well for slow-changing signals like those from **load cells, bridge sensors, and thermocouples**, where accuracy matters more than sampling speed.

<div align="center">
  <a title="Kaldosh at English Wikipedia, Public domain, via Wikimedia Commons" href="https://commons.wikimedia.org/wiki/File:Pulse-density_modulation_1_period.gif">
    <img width="500" alt="A sine wave encoded as a stream of dense and sparse pulses, denser where the wave is higher" src="https://upload.wikimedia.org/wikipedia/commons/2/20/Pulse-density_modulation_1_period.gif"/>
  </a>
</div>

Instead of measuring the input voltage directly in one shot, the ADS1219 samples it extremely fast and turns it into a stream of 1s and 0s like the one above: **more 1s when the signal is high, more 0s when it's low**. Averaging thousands of these single-bit samples together is what "oversampling" means in practice, and it's how a signal that's only ever 1 or 0 at any instant ends up producing a precise 24-bit result.

The output is always 24 bits, but the noise floor is what actually limits how much of that is useful. At the lowest data rate (20 SPS, gain 1), the effective resolution is about **19.6 bits**, close to the datasheet's headline "up to 20 bits effective resolution". Push the data rate up to 1000 SPS and that drops to around **16.8 bits**, since there's less time to average out noise between readings, faster conversions trade resolution for speed.

The device accepts up to **four input channels (AIN0-AIN3)**, routed through an internal multiplexer in **differential or single-ended** configurations, then through a **programmable gain amplifier (PGA)** (gain of **1 or 4**) before conversion. A **digital decimation filter** turns the oversampled bitstream into a final 24-bit result at whichever **data rate** you've selected (**20, 90, 330, or 1000 SPS**), trading speed for noise performance.

The ADS1219 supports two operating modes:

- **Single-shot mode** - performs one conversion when triggered, then enters a low-power state. Ideal for battery-powered devices with infrequent measurements.
- **Continuous-conversion mode** - performs conversions back-to-back at the programmed data rate. The **DRDY** pin asserts low when each new result is ready, allowing the microcontroller to respond via interrupt instead of polling.

The device includes a built-in **2.048 V internal voltage reference**, which eliminates the need for external components in most applications. An **external reference** can also be applied via the REFP and REFN pins for use cases that require a custom reference voltage.

---

## I2C Communication

The ADS1219 talks over I2C at Standard-mode (100 kHz), Fast-mode (400 kHz), or Fast-mode Plus (1 Mbps), and never stretches the clock.

Its address comes from how the **A0** and **A1** pins are wired, each tied to GND, VCC, SDA, or SCL gives one of 16 addresses (0x40-0x4F), letting multiple boards share a bus. See [Address Selection](/ads1219/hardware#address-selection) for the full table.

Six commands control the device: reset, start/restart a conversion, power down, read the latest result, or read/write the configuration register, which holds gain, data rate, input channel, reference source, and operating mode all in one place.

The **DRDY** pin goes low when a result is ready, so you can use an interrupt instead of polling. A built-in ~55 ms timeout also resets the interface automatically if a transaction stalls.

The Arduino library builds these commands and register writes for you, converts the raw 24-bit two's complement result to millivolts, and tracks the current gain setting internally so that conversion stays correct after you change it. You just call functions like `setMux()` or `getConversionMillivolts()`.






