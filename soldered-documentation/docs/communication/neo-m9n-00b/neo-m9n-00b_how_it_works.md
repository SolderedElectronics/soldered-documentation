---
slug: /neo-m9n-00b/how-it-works 
title: NEO-M9N-00B - How it works
sidebar_label: How it works
id: neo-m9n-00b-how-it-works 
hide_title: False
---  

The NEO-M9N-00B is a GNSS module from [**u-blox**](https://www.u-blox.com/en/product/neo-m9n-module) that simultaneously receives signals from GPS, GLONASS, Galileo, and BeiDou constellations.

<!--  
<CenteredImage src="/img/neo-m9n-00b/neo-m9n-00b_onboard.png" alt="NEO-M9N-00B module on board" caption="NEO-M9N-00B module on board" width="500px" />
-->
---

## Datasheet

<QuickLink
  title="NEO-M9N-00B Datasheet"
  description="Detailed technical documentation for the NEO-M9N-00B GNSS module"
  url="https://www.u-blox.com/sites/default/files/NEO-M9N-00B_DataSheet_UBX-19014285.pdf"
/>

---

## How the module works

The NEO-M9N-00B integrates a **GNSS receiver and signal processing unit** that tracks signals from multiple satellite constellations at the same time.

- **Multi-constellation reception** - The module simultaneously receives signals from **GPS, GLONASS, Galileo, and BeiDou**, which improves fix reliability and availability, especially in environments with obstructions.

- **Position fixing** - Using signals from multiple satellites, the module calculates **latitude, longitude, and altitude** through trilateration, achieving a horizontal accuracy of up to **2.0 meters CEP**.

- **Velocity and heading** - Beyond position, the module computes **speed and direction of movement**.

- **Timepulse output** - The module provides a configurable **1PPS signal** synchronized to GNSS time, useful for precise timing applications.

- **Protocol output** - Positioning results are delivered via **UART and I2C** using the standard **NMEA 0183** protocol or the proprietary **UBX binary protocol**.

---

## I2C & UART Communication

The NEO-M9N-00B supports both **I2C** and **UART** communication.

- **I2C** uses two lines: **SDA** for data and **SCL** for clock, with a default address of **0x42**. Multiple I2C devices can share the same bus.

- **UART** uses **TX** and **RX** lines for serial communication, useful when higher data throughput or simpler wiring is preferred.
