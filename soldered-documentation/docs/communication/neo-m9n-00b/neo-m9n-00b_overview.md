---
slug: /neo-m9n-00b/overview
title: NEO-M9N-00B - Overview
sidebar_label: Overview
id: neo-m9n-00b-overview 
hide_title: False
pagination_prev: null
---
## GPS Breakout NEO-M9N-00B

The **GPS Breakout NEO-M9N-00B** is a GNSS positioning module based on the **u-blox NEO-M9N** receiver. It concurrently receives **GPS, GLONASS, Galileo, and BeiDou** signals, reaching up to **2.0 m CEP** horizontal accuracy, and connects over **I2C, UART, or SPI** via two **Qwiic** connectors or a standard pin header.

Beyond position output, the module includes a configurable **1PPS timepulse**, a jumper-selectable **antenna bias voltage** for active antennas, and an onboard **CR1220 backup battery holder** for faster fixes after a power cycle. It can be configured and monitored with u-blox's free **u-center** desktop software.

<CenteredImage src="/img/neo-m9n-00b/izo.png" alt="GPS Breakout NEO-M9N-00B" caption="GPS Breakout NEO-M9N-00B" width="600px"/>

---

## Which product is this documentation for?

<QuickLink 
  title="GPS Breakout NEO-M9N-00B" 
  description="333378"
  url="https://soldered.com/products/gps-breakout-neo-m9n-00b-qwiic"
  image="/img/neo-m9n-00b/top.png" 
/>

---

## Key Features

- **GNSS constellations:** GPS, GLONASS, Galileo, BeiDou (concurrent reception)
- **Position accuracy:** 2.0 m CEP horizontal accuracy
- **Update rate:** Up to 25 Hz
- **Time to first fix:** ~24-29 s cold start, ~2 s hot/aided start
- **Data output:** NMEA 0183 and UBX binary protocols
- **Timepulse:** Configurable 1PPS output synchronized to GNSS time
- **Communication:** I2C and UART simultaneously by default (default I2C address: **0x42**), or SPI when switched over with the D_SEL jumper
- **Antenna power:** Jumper-selectable bias voltage for active (amplified) GPS antennas
- **Backup battery:** Onboard CR1220 coin-cell holder for faster hot/warm starts after a power cycle
- **Operating voltage:** 3.3V (onboard regulator for 5V compatibility)
- **Connector:** 2 × **Qwiic ports**
- **Mounting:** Two mounting holes
- **Dimensions:** **38 × 54 mm** (1.5 × 2.1 inch)

---

## You may also need

<QuickLink 
  title="Qwiic cable" 
  description="Qwiic compatible cables with connectors on both ends, available in various lengths."
  url="https://soldered.com/product/easyc-cable/"
  image="/img/333311.webp" 
/>
