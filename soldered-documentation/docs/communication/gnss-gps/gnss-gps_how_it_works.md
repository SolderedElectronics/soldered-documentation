---
slug: /gnss-gps/how-it-works 
title: Gnss Gps – How it works
sidebar_label: How it works
id: gnss-gps-how-it-works 
hide_title: False
---  

The **L86-M33** is a highly compact and energy-efficient **GNSS module** that supports **GPS, GLONASS, and Galileo** satellite systems. Designed for applications requiring precise positioning, the L86-M33 includes advanced features such as **EASY™ (Embedded Assist System)**, **AlwaysLocate™**, and an integrated **LOCUS™ data logger**.

<CenteredImage src="/img/gnss-gps/onboard.png" alt="HX711 Standard Board" caption="GNSS GPS L86-M33" width="500px" />

<CenteredImage src="/img/gnss-gps/onboardeasyC.jpg" alt="HX711 Standard Board" caption="GNSS GPS L86-M33 Qwiic (easyC) Board" width="500px" />
---

## Datasheet

For detailed technical specifications, please refer to the official L86 Datasheet:  

<QuickLink  
  title="L86-M33 Datasheet"  
  description="Complete technical documentation for the GNSS-GPS L86-M33 board"  
  url="https://soldered.com/productdata/2023/01/Soldered_L86-M33_datasheet.pdf"  
/>  

---

## How the L86-M33 Works

The L86-M33 module receives signals from multiple **GNSS satellite constellations**, allowing for **high-accuracy positioning** even in challenging environments. Its small form factor and built-in antenna make it ideal for **IoT, asset tracking, and wearable devices**.

- **Multi-GNSS Support** - The module processes signals from **GPS, GLONASS, and Galileo**, improving accuracy and reducing positioning time compared to single-system receivers.

<CenteredImage src="/img/gnss-gps/constellation.png" alt="attiny404 on the HX711 easyC Board" caption="GNSS constellations" width="800px" />

- **Embedded Assist System (EASY™)** - This feature allows the module to predict satellite orbits and accelerate positioning using up to **3 days of ephemeris data**, even when satellite signals are weak.

- **AlwaysLocate™ Power Optimization** - Adjusts the module's activity dynamically based on motion and environmental conditions, ensuring energy-efficient operation without compromising accuracy.

<CenteredImage src="/img/gnss-gps/alwayslocate.png" alt="alwayslocate" caption="AlwaysLocate™ Mode" width="500px" />

- **Internal LOCUS™ Data Logger** - The built-in flash memory can store **location history for over 16 hours**, eliminating the need for an external microcontroller for basic tracking applications.

- **Integrated and External Antenna Support** - The **18.4mm × 18.4mm** onboard ceramic patch antenna ensures reliable operation, while an **IPX connector** allows for an external active antenna if needed.

---

## High-Precision Positioning

The L86-M33 provides **high-sensitivity tracking**, ensuring accuracy in urban areas and weak-signal environments:

- **-167 dBm tracking sensitivity** allows reliable operation indoors and in obstructed environments.
- **Position accuracy of ±2.5 meters** in ideal conditions.
- **Balloon Mode** supports positioning at altitudes up to **80 km**, making it suitable for high-altitude projects.
- **Multi-tone Active Interference Canceller (MTK chipset)** filters out unwanted signals, improving accuracy in noisy environments.

---

## Communication Interface

The **L86-M33** communicates with microcontrollers and other devices through a **UART interface**, making integration straightforward. The key communication pins include:

- **TX (Transmit)**: Outputs GNSS data to a connected microcontroller or device.
- **RX (Receive)**: Receives commands from the microcontroller to configure the module.
- **PPS (Pulse Per Second)**: Provides a **1 Hz timing pulse** synchronized with GNSS signals, useful for high-precision timing applications.
- **F_ON (Force On)**: Used to wake the module from low-power mode when needed.

The module supports standard **NMEA** sentences for easy parsing of positioning data.

---

## I2C communication - Qwiic

Qwiic versions of the product use the onboard ATTINY404 MCU to implement I2C communication. The breakout board operates with a default I2C address of **0x30**, but it can be changed using [**onboard switches**](/gnss-gps/hardware#address-selection-qwiic-version). Once detected, the ATTINY404 receives data from the sensor and passes it to the main MCU using the I2C data line. To check in detail how the ATTINY404 is programmed, please refer to the [**firmware GitHub page**](https://github.com/SolderedElectronics/Soldered-HX711-ADC-For-Weight-Scales-Arduino-Library/tree/dev/extras/attiny_firmware).

<CenteredImage src="/img/gnss-gps/tiny404onboard.png" alt="attiny404 on the HX711 easyC Board" caption="attiny404 on the L86-M33 easyC Board" width="500px" />