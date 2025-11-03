---
slug: /tmp117/how-it-works 
title: TMP117 Temperature Sensor – How It Works
id: tmp117-how-it-works
sidebar_label: How it works
hide_title: true
---  

# How it works

The **TMP117** is a high-accuracy, low-power digital temperature sensor with an **SMBus™- and I²C-compatible interface**, designed and manufactured by [**Texas Instruments**](https://www.ti.com/product/TMP117). It provides extremely precise temperature measurements across a wide range from –55 °C to +150 °C, making it ideal for applications where both precision and efficiency are required.  

<CenteredImage 
  src="/img/tmp117/tmp117_onboard.jpg" 
  alt="TMP117 sensor on board" 
  caption="TMP117 sensor on board" 
  width="500px" 
/>

## Datasheet

For an in-depth look at technical specifications, refer to the official TMP117 datasheet:  

<QuickLink  
  title="TMP117 Datasheet"  
  description="Detailed technical documentation for the TMP117 high-accuracy digital temperature sensor"  
  url="https://soldered.com/productdata/2025/10/tmp117_datasheet_soldered.pdf"  
/>  

## How the sensor works

The TMP117 combines a **temperature-sensing element**, **16-bit analog-to-digital converter (ADC)**, and **digital logic** into a single, factory-calibrated IC. This integration eliminates the need for analog front-end circuitry and external calibration, offering a simple digital interface for accurate temperature data acquisition.  

<CenteredImage 
  src="/img/tmp117/blockdiagram.png" 
  alt="TMP117 Functional Block Diagram" 
  caption="Functional block diagram of the TMP117 sensor showing the internal ADC, control logic, and I²C interface." 
  width="700px" 
/>

<br/><br/>

Each TMP117 device is calibrated against **NIST-traceable temperature standards**, achieving a typical accuracy of **±0.1 °C** between –20 °C and +50 °C. The sensor measures temperature using a precision bandgap reference, and the internal 16-bit ADC converts this analog signal into a digital output with a resolution of **0.0078 °C per least significant bit (LSB)**. Because of this high resolution and stability, the TMP117 performs comparably to platinum resistance thermometers (such as PT100 or PT1000) in precision applications.

The sensor supports multiple operating modes that allow users to optimize for power or performance. In **continuous conversion mode**, the TMP117 performs ongoing measurements for real-time monitoring. **Shutdown mode** minimizes current consumption to approximately **150 nA**, while **one-shot mode** enables single conversions on demand, providing flexibility for battery-powered and low-duty-cycle systems.

For temperature threshold monitoring, the device includes programmable **high and low limit registers** that trigger the **ALERT pin** when limits are exceeded. This output can be configured for different alert behaviors, such as comparator or therm mode, enabling both simple threshold warnings and window-based temperature detection.  

<CenteredImage 
  src="/img/tmp117/alertmodediagram.png" 
  alt="TMP117 Functional Block Diagram" 
  caption="Alert mode timing diagram." 
  width="700px" 
/>
<br/><br/>
The TMP117 also includes **48 bits of nonvolatile EEPROM memory**, which can store calibration constants, device IDs, or system configuration data. The sensor’s design ensures exceptional long-term stability and minimal drift over time, making it suitable for industrial, medical, and scientific instrumentation.

## I²C communication

Communication with the TMP117 occurs through a **two-wire I²C interface** consisting of the **SDA** (serial data) and **SCL** (serial clock) lines. Both lines require pull-up resistors, which are typically included on breakout boards. The sensor supports standard and fast-mode I²C operation, allowing easy integration with most microcontrollers.

The **I²C address** of the TMP117 is determined by the **ADD0 pin**, giving flexibility to connect up to **four sensors on the same bus**. Through this interface, the master device can read temperature data, configure conversion rates, set alert limits, and access the EEPROM memory.  

During operation, temperature measurements are stored in a dedicated **temperature register**, which can be read as a 16-bit digital value. Configuration and status registers allow control over averaging, conversion timing, and alert functionality.  

This combination of accuracy, simplicity, and low power makes the TMP117 an ideal choice for embedded systems, data logging, environmental monitoring, and medical-grade temperature measurement applications.
