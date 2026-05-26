---
slug: /neo-m9n-00b/how-it-works 
title: NEO-M9N-00B - How it works
sidebar_label: How it works
id: neo-m9n-00b-how-it-works 
hide_title: False
---  

NEO-M9N-00B is a high-performance GNSS module that provides precise positioning data using GPS, GLONASS, Galileo, and BeiDou satellite systems in a compact package, manufactured by [**u-blox**](https://www.u-blox.com/en/product/neo-m9n-module).

<!--  
<CenteredImage src="/img/neo-m9n-00b/neo-m9n-00b_onboard.png" alt="NEO-M9N-00B module on board" caption="NEO-M9N-00B module on board" width="500px" />
-->
---

## Datasheet

For an in-depth look at technical specifications, refer to the official NEO-M9N-00B Datasheet:

<QuickLink
  title="NEO-M9N-00B Datasheet"
  description="Detailed technical documentation for the NEO-M9N-00B GNSS module"
  url="https://www.u-blox.com/sites/default/files/NEO-M9N-00B_DataSheet_UBX-19014285.pdf"
/>

---

## How the module works

The NEO-M9N-00B is a versatile GNSS module that provides **precise positioning, velocity, and time data**. It integrates a **GNSS receiver, signal processing unit, and serial communication interface** into a compact module, offering reliable positioning across a wide range of applications.

The NEO-M9N-00B operates with **low power consumption** and **high accuracy**, making it ideal for **navigation systems**, **asset tracking**, and **timing applications**.

- **Multi-Band GNSS Reception** - The module simultaneously receives signals from **GPS, GLONASS, Galileo, and BeiDou** satellite constellations, maximizing positioning accuracy and availability even in challenging environments.

- **Position Fixing** - Using signals from multiple satellites, the module calculates the precise **latitude, longitude, and altitude** of the device through trilateration, achieving a horizontal accuracy of up to **2.5 meters CEP**.

- **Velocity and Heading** - Beyond position, the module also computes **speed and direction of movement**, making it suitable for vehicle tracking and navigation applications.

- **Timepulse Output** - The module provides a configurable **timepulse signal (1PPS)** synchronized to GNSS time, enabling precise timing and synchronization in time-critical applications.

- **Signal Processing and Output** - The module processes satellite data internally and delivers positioning results via **UART and I2C** interfaces using the standard **NMEA 0183** protocol or the proprietary **UBX binary protocol** for easy integration with microcontrollers.

---

## I2C & UART Communication

The NEO-M9N-00B module supports both **I2C** (Inter-Integrated Circuit) and **UART** (Universal Asynchronous Receiver-Transmitter) communication to exchange data with a microcontroller.

- **I2C** uses two lines: **SDA** for **data transfer** and **SCL** for **clock synchronization**, allowing the module to coexist with other I2C devices on the same bus using its default address of **0x42**.

- **UART** uses **TX** and **RX** lines for serial communication, commonly used when higher data throughput or simpler wiring is preferred.

As a follower device, the NEO-M9N-00B responds only when addressed by a master device, delivering positioning data such as **latitude, longitude, altitude, speed**, and **satellite count** on demand.