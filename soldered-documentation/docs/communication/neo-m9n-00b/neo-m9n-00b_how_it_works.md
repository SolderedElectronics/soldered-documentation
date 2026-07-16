---
slug: /neo-m9n-00b/how-it-works 
title: NEO-M9N-00B - How it works
sidebar_label: How it works
id: neo-m9n-00b-how-it-works 
hide_title: False
---  

The NEO-M9N-00B is a GNSS module from [**u-blox**](https://www.u-blox.com/en/product/neo-m9n-module) that simultaneously receives signals from GPS, GLONASS, Galileo, and BeiDou constellations.

<CenteredImage src="/img/neo-m9n-00b/chip.png" alt="u-blox NEO-M9N chip on the board" caption="u-blox NEO-M9N" width="500px" />

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

- **Protocol output** - Positioning results are delivered via **UART, I2C, or SPI** using the standard **NMEA 0183** protocol or the proprietary **UBX binary protocol**.

- **Update rate** - The module can output a new position up to **25 times per second**, far more often than most GNSS receivers need, useful for tracking fast-moving objects.

- **Time to first fix** - A cold start (first power-up, or after a long time unpowered) takes around **24-29 seconds** depending on which constellations are enabled. A hot or aided start, with recent almanac data still available (for example from the CR1220 backup battery), takes around **2 seconds**.

Each of the four constellations the module can track sits in its own set of medium-Earth orbits, all far higher up than something like the International Space Station:

<div align="center">
  <a title="Cmglee, CC BY-SA 3.0, via Wikimedia Commons" href="https://commons.wikimedia.org/wiki/File:Comparison_satellite_navigation_orbits.svg">
    <img width="600" alt="Comparison of GPS, GLONASS, Galileo, and BeiDou (COMPASS) orbits" src="https://upload.wikimedia.org/wikipedia/commons/b/b4/Comparison_satellite_navigation_orbits.svg"/>
  </a>
</div>

Tracking more than one of these constellations at once means more visible satellites overall, which is what actually improves the fix, not any single constellation being "better" than another.

Once the module has locked onto enough satellites, it works out its position by **trilateration**: each satellite broadcasts its own orbital position along with a precise timestamp, and the receiver measures how long the signal took to arrive to work out its distance to that satellite. Doing this for several satellites at once narrows the possible location down to a single point on Earth, the intersection of all those distance measurements.

<div align="center">
  <a title="Javiersanp, CC BY-SA 4.0, via Wikimedia Commons" href="https://commons.wikimedia.org/wiki/File:Trilateration-with-3-satellites.svg">
    <img width="450" alt="Trilateration using distance measurements from three satellites" src="https://upload.wikimedia.org/wikipedia/commons/8/86/Trilateration-with-3-satellites.svg"/>
  </a>
</div>

In practice the module needs at least **4 satellites** for a full 3D fix (latitude, longitude, altitude), since it also has to solve for its own clock error alongside the three position coordinates. This is also why more satellites in view, thanks to tracking several constellations at once, means a faster and more reliable fix.

---

## I2C & UART Communication

The NEO-M9N-00B supports both **I2C** and **UART** communication at the same time, which is the module's default configuration.

- **I2C** uses two lines: **SDA** for data and **SCL** for clock, with a default address of **0x42**. Multiple I2C devices can share the same bus. The module only supports **I2C Fast-mode (400 kbit/s)**, it doesn't fall back to Standard-mode (100 kbit/s), and it can use clock stretching (holding SCL low for up to 20 ms) to pause a transaction when it needs more time.

- **UART** uses **TX** and **RX** lines for serial communication, useful when higher data throughput or simpler wiring is preferred.

---

## SPI communication

The same four pins used for I2C and UART (**SDA, SCL, TX, RX**) double as an **SPI** interface: **SPI_CS_N, SPI_SCK, SPI_MISO, and SPI_MOSI** respectively. Which function they serve depends on the **D_SEL** pin, broken out on this board as the **JP4** selectable jumper:

- **JP4 default position** - **D_SEL** is pulled high, so the module runs in **I2C + UART** mode and the SPI functions are inactive.
- **JP4 re-bridged to the other position** - **D_SEL** is pulled to ground, so the module switches to **SPI-only** mode. I2C is disabled entirely while SPI is active.

The module only exposes one interface pair at a time on these shared pins, so you need to decide upfront which one you'll use and set the jumper accordingly. SPI runs in **mode 1** (CPHA = 0) at up to **5.5 MHz**, with a maximum transfer rate of **125 kB/s**, which is slower than what the interface itself can theoretically reach but still fast enough for GNSS data.

<InfoBox>Switching JP4 to SPI mode is not enough by itself. You must also open the module in **u-center** and set the SPI port's input/output protocol to **UBX only**, otherwise it will not respond to commands over SPI. See [Configuring the module with u-center](/neo-m9n-00b/arduino/geting-started#configuring-the-module-with-u-center) for the exact steps.</InfoBox>

---

## Additional capabilities

Beyond basic positioning, the NEO-M9N supports a couple of features worth knowing about:

- **SBAS augmentation** - The module can use satellite-based augmentation systems (SBAS) like WAAS or EGNOS, regional networks of ground stations and geostationary satellites that broadcast correction data, to improve position accuracy further.

- **Jamming and interference monitoring** - The receiver can detect RF jamming or interference on the GNSS frequency bands and report it, which is useful for diagnosing why a fix is suddenly unreliable in an otherwise clear-sky environment.

Both are configured through UBX messages rather than dedicated pins, so they don't require any extra wiring, only the corresponding library or u-center commands to enable.
