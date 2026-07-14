---
slug: /neo-m9n-00b/overview
title: NEO-M9N-00B - Overview
sidebar_label: Overview
id: neo-m9n-00b-overview 
hide_title: False
pagination_prev: null
---
## GPS Breakout NEO-M9N-00B

The **GPS Breakout NEO-M9N-00B** is a GNSS positioning module based on the **u-blox NEO-M9N** receiver. It concurrently receives signals from **GPS, GLONASS, Galileo, and BeiDou** satellite constellations at the same time, achieving up to **2.0 m CEP** horizontal accuracy - considerably better than older single-constellation GPS-only modules, since more visible satellites mean a faster, more reliable fix, especially around buildings or trees.

The board talks to your microcontroller over **I2C, UART, or SPI**. I2C and UART are both available at the same time by default, over two **Qwiic (formerly easyC)** connectors or a standard pin header. Switching to SPI instead (via the **D_SEL** jumper) repurposes those same pins as SPI signals and disables I2C, since the module only exposes one interface pair at a time on those shared pins.

Beyond basic position output, the module provides a configurable **1PPS timepulse** output for precise timing applications, an **antenna bias-voltage jumper** for powering an active (amplified) GPS antenna, and an onboard **CR1220 backup battery holder** that keeps the module's clock and almanac data alive when main power is removed - so it can get a much faster fix the next time it's powered up, instead of doing a full cold start. Positioning data is available as standard **NMEA 0183** sentences or the more compact, binary **UBX protocol**, and the module can be configured and monitored with u-blox's free **u-center** desktop software.

---

## Which product is this documentation for?

<WarningBox>

This product is not yet available in our store. Please check back soon!

</WarningBox>

---

## Key Features

- **GNSS constellations:** GPS, GLONASS, Galileo, BeiDou (concurrent reception)
- **Position accuracy:** 2.0 m CEP horizontal accuracy
- **Data output:** NMEA 0183 and UBX binary protocols
- **Timepulse:** Configurable 1PPS output synchronized to GNSS time
- **Communication:** I2C and UART simultaneously by default (default I2C address: **0x42**), or SPI when switched over with the D_SEL jumper
- **Antenna power:** Jumper-selectable bias voltage for active (amplified) GPS antennas
- **Backup battery:** Onboard CR1220 coin-cell holder for faster hot/warm starts after a power cycle
- **Operating voltage:** 3.3V (onboard regulator for 5V compatibility)
- **Connector:** 2 × **Qwiic (formerly easyC) ports**
- **Mounting:** Two mounting holes
- **Dimensions:** **38 × 54 mm** (1.5 × 2.1 inch)

---

## You may also need

<QuickLink 
  title="Qwiic cable" 
  description="Qwiic (formerly easyC) compatible cables with connectors on both ends, available in various lengths."
  url="https://soldered.com/product/easyc-cable/"
  image="/img/333311.webp" 
/>
