---
slug: /gnss-gps/how-it-works 
title: Gnss Gps – How it works
sidebar_label: How it works
id: gnss-gps-how-it-works 
hide_title: false
---  

The **L86-M33** from Quectel is a compact GNSS module supporting **GPS, GLONASS, Galileo, and QZSS**. It includes **EASY™** (autonomous ephemeris prediction for faster fixes), **AlwaysLocate™** (adaptive power management), and an integrated **LOCUS™** data logger.

<CenteredImage src="/img/gnss-gps/onboard.png" alt="GNSS GPS L86-M33 Standard Board" caption="GNSS GPS L86-M33" width="500px" />

---

## Datasheet

For detailed technical specifications, please refer to the official L86 Datasheet:  

<QuickLink  
  title="L86-M33 Datasheet"  
  description="Complete technical documentation for the GNSS-GPS L86-M33 board"  
  url="https://docs.rs-online.com/1fe5/0900766b8147dbfb.pdf"  
/>  

---

## How the L86-M33 Works

The L86-M33 module receives signals from multiple **GNSS satellite constellations** simultaneously, combining data from GPS, GLONASS, Galileo, and QZSS to compute a position fix.

- **Multi-GNSS Support** - The module processes signals from **GPS, GLONASS, Galileo, and QZSS**, reducing positioning time and improving fix availability compared to single-constellation receivers.

<CenteredImage src="/img/gnss-gps/constellation.png" alt="GNSS satellite constellations" caption="GNSS constellations" width="800px" />

- **Embedded Assist System (EASY™)** - This feature allows the module to predict satellite orbits and accelerate positioning using up to **3 days of ephemeris data**, even when satellite signals are weak.

- **AlwaysLocate™ Power Optimization** - Adjusts the module's duty cycle dynamically based on motion and environmental conditions. Current drops to ~3.5 mA in this mode, compared to 26 mA during continuous tracking.

<CenteredImage src="/img/gnss-gps/alwayslocate.png" alt="alwayslocate" caption="AlwaysLocate™ Mode" width="500px" />

- **Internal LOCUS™ Data Logger** - The built-in flash memory can store **location history for over 16 hours**, eliminating the need for an external microcontroller for basic tracking applications.

- **Integrated and External Antenna Support** - The **18.4mm × 18.4mm** onboard ceramic patch antenna ensures reliable operation, while an **IPX connector** allows for an external active antenna if needed.

---

## High-Precision Positioning

The L86-M33 provides the following positioning performance:

- **−167 dBm tracking sensitivity**
- **Position accuracy: < 2.5 m CEP**
- **Balloon Mode** supports positioning at altitudes up to **80 km**
- **Multi-tone Active Interference Canceller (MAIC)** filters RF interference to improve signal quality in noisy environments

---

## Communication Interface

The **L86-M33** communicates via a **UART interface** at 9600 baud by default. The relevant pins are:

- **TX (Transmit)**: Outputs GNSS data to a connected microcontroller or device.
- **RX (Receive)**: Receives commands from the microcontroller to configure the module.
- **PPS (Pulse Per Second)**: Provides a **1 Hz timing pulse** synchronized with GNSS signals, useful for high-precision timing applications.
- **F_ON (Force On)**: Used to wake the module from low-power mode when needed.

The module outputs standard **NMEA** sentences, which the library parses automatically.

