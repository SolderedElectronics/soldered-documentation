---
slug: /ads1219/how-it-works 
title: ADS1219 24-bit ADC - How it works
sidebar_label: How it works
id: ads1219-how-it-works 
hide_title: False
---

The ADS1219 is a precision **24-bit delta-sigma analog-to-digital converter (ADC)** manufactured by [**Texas Instruments**](https://www.ti.com/product/ADS1219). When using our board, you are communicating directly with the onboard ADS1219 via **I2C communication**.

<CenteredImage src="/img/ads1219/onboard.JPG" alt="ADS1219 on board" caption="ADS1219 on the board" width="400px" />

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
  <a title="Puffingbilly at English Wikipedia, CC BY-SA 3.0, via Wikimedia Commons" href="https://commons.wikimedia.org/wiki/File:Block_Diagram_Delta-Sigma_ADC.svg">
    <img width="800" alt="Block diagram of a first-order delta-sigma ADC" src="https://upload.wikimedia.org/wikipedia/commons/7/72/Block_Diagram_Delta-Sigma_ADC.svg"/>
  </a>
</div>

This is the core trick behind every delta-sigma ADC, including the ADS1219: instead of measuring the input voltage directly in one shot, an **integrator** continuously accumulates the difference between the input and a feedback signal, and a **1-bit comparator** (the "threshold") checks whether that running total is above or below zero many times per second. That single bit feeds straight back into the integrator, nudging it the other way - so the stream of 1s and 0s coming out ends up spending more time high when the input is large, and more time low when it's small. A **counter** then simply tallies how many of those bits were 1 over a fixed window, and that tally *is* the measurement - more 1s means a higher input voltage. Averaging many single-bit decisions this way is what "oversampling" means in practice, and it's how a comparator that only outputs 1 bit at a time ends up producing a 24-bit result.

The device accepts up to **four input channels (AIN0-AIN3)** that can be routed to the internal multiplexer in various **differential or single-ended configurations**. The selected input signal passes through a **programmable gain amplifier (PGA)**, which supports gains of **1 and 4**, effectively scaling the input range to make the best use of the ADC's full dynamic range.

After amplification, the signal enters the delta-sigma modulator described above, running at a high internal oversampling rate. A **digital decimation filter** processes that 1-bit stream and outputs a final 24-bit result at the selected data rate (**20, 90, 330, or 1000 SPS**). This oversampling and filtering is what gives the ADS1219 its low noise and high resolution.

The ADS1219 supports two operating modes:

- **Single-shot mode** - performs one conversion when triggered, then enters a low-power state. Ideal for battery-powered devices with infrequent measurements.
- **Continuous-conversion mode** - performs conversions back-to-back at the programmed data rate. The **DRDY** pin asserts low when each new result is ready, allowing the microcontroller to respond via interrupt instead of polling.

The device includes a built-in **2.048 V internal voltage reference**, which eliminates the need for external components in most applications. An **external reference** can also be applied via the REFP and REFN pins for use cases that require a custom reference voltage.

---

## I2C Communication

The ADS1219 communicates with the microcontroller over the **I2C bus**. Key aspects of the protocol implementation:

- **Addressing:** The device supports [**16 selectable I2C addresses**](/ads1219/hardware#address-selection) (0x40-0x4F), set via onboard jumpers, enabling multiple ADS1219 boards on a single bus.
- **Commands:** The host sends single-byte command words to start a conversion, reset the device, power it down, or read/write the internal registers.
- **Register access:** Configuration (gain, data rate, input channel, reference source, operating mode) is written to the **configuration register**. Conversion results are retrieved with a dedicated read command (RDATA), returned as a signed 24-bit value.
- **Data ready:** The **DRDY** pin provides a hardware interrupt signal that goes low when a fresh conversion result is available, avoiding the need to poll the bus.
- **Clock speed:** The device supports Standard-mode (100 kHz), Fast-mode (400 kHz), and Fast-mode Plus (1 Mbps) I2C clock speeds.






