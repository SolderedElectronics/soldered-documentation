---
slug: /zed-f9p/how-it-works 
title: ZED-F9P - How it works
sidebar_label: How it works
id: zed-f9p-how-it-works 
hide_title: False
---  

## How It Works

The **GPS-GNSS BREAKOUT ZED-F9P** determines its position by receiving signals from multiple **Global Navigation Satellite Systems (GNSS)** such as GPS, GLONASS, Galileo, and BeiDou. By calculating the time it takes for signals to travel from satellites to the receiver, the module computes its precise location using trilateration.

[Image placeholder - zed-f9p highlighted]

### Multi-band GNSS Reception
Unlike standard GPS modules, the ZED-F9P uses **multi-band reception**, meaning it listens to multiple frequency bands from each satellite. This improves accuracy and reliability, especially in challenging environments like urban areas or near obstacles.

### High-Precision Positioning (RTK & PPP-RTK)
For centimeter-level accuracy, the module supports:
- **RTK (Real-Time Kinematic)**: Uses correction data from a nearby base station to eliminate positioning errors.
- **PPP-RTK**: Uses satellite-delivered correction data for high accuracy without a local base station.

These corrections significantly reduce errors caused by atmospheric conditions, satellite clock drift, and signal reflections.

### Base and Rover Operation
The module can operate in two roles:
- **Rover**: Receives satellite signals and correction data to compute its precise position.
- **Base station**: Calculates correction data and transmits it to rover units.

It also supports **moving base mode**, where both base and rover are in motion, enabling applications like drone following or heading/attitude estimation.

### Communication Interfaces
The computed position and status data are sent to a host system (e.g., microcontroller or computer) via:
- **UART (default)**
- **I2C (Qwiic compatible)**
- **SPI**
- **USB**

The module outputs standard formats such as **NMEA** or binary **UBX** messages.

### Timing and Status Outputs
- **PPS (Timepulse)**: Outputs a precise timing signal (typically 1 pulse per second) for synchronization.
- **RTK LED / Status pin**: Indicates positioning quality (fixed, float, or no correction).
- **Geofence output**: Signals whether the device is inside a predefined area.

### Power and Operation
The module runs on **3.3V** and continuously processes satellite signals. Power usage depends on the number of satellites tracked and enabled features, with higher consumption during acquisition and high-precision modes.

<InfoBox>The ZED-F9P achieves centimeter-level accuracy by combining multi-band GNSS with real-time correction data, making it suitable for robotics, surveying, and precision navigation applications.</InfoBox>

---

## Datasheet

For detailed technical specifications, please refer to the official ZED-F9P-05B Datasheet:

<QuickLink  
  title="ZED-F9P-05B Datasheet"  
  description="Complete technical documentation for the GNSS-GPS ZED-F9P-05B board"  
  url="https://content.u-blox.com/sites/default/files/documents/ZED-F9P-05B_DataSheet_UBXDOC-963802114-12824.pdf"  
/>  

---

## Communication Interface

The ZED-F9P supports multiple communication interfaces, allowing flexible integration with microcontrollers and embedded systems:

- **UART (TX/RX)**: Primary interface for GNSS data output and configuration commands.
- **UART2 (TX2/RX2)**: Dedicated interface for correction data (RTCM) in RTK applications.
- **I2C (SDA/SCL)**: Qwiic-compatible interface for easy connection to development boards.
- **SPI**: Available as an alternative interface when selected via hardware configuration.
- **USB**: Direct connection to a computer for configuration and data streaming.

Additional useful signals include:
- **PPS (Timepulse)**: Outputs a precise **1 Hz timing signal** synchronized with GNSS time.
- **RTK status pin**: Indicates fix quality (fixed, float, or no correction).
- **Geofence output**: Signals when the device enters or exits a predefined area.

The module supports standard **NMEA**, **UBX (binary)**, and **RTCM** protocols.

---

## I2C Communication - Qwiic

The breakout board provides a **Qwiic-compatible I2C interface** for easy plug-and-play connectivity.

- The module uses a fixed I2C address of **0x42**.
- Communication is handled **directly by the ZED-F9P module**, without any intermediary microcontroller.
- Supports **I2C Fast-mode (up to 400 kHz)**.
- Optional **onboard pull-up resistors** can be enabled via jumper **JP3** if required.

Since there is **no onboard I2C bridge (such as an ATTINY404)**:
- All GNSS data (NMEA, UBX, RTCM) is transmitted **directly over I2C**.
- The host microcontroller must handle parsing and configuration.

<InfoBox>Because the I2C address is fixed, only one ZED-F9P module can be used per I2C bus unless an I2C multiplexer is added.</InfoBox>

