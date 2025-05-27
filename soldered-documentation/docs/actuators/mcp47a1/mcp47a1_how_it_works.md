---
slug: /mcp47a1/how-it-works
title: "MCP47A1 DAC \u2013 How it works"
id: mcp47a1-how-it-works
hide_title: false
---
The MCP47A1 is an integrated circuit by [**Microchip Technology**]. When using our board, you are essentially communicating with the onboard MCP47A1 directly via **I2C communication**.

<CenteredImage src="/img/mcp47a1/onboard.webp" alt="MCP47A1 sensor on board" caption="MCP47A1 sensor on the board" width="400px" />

---

## Datasheet

For an in-depth look at technical specifications, refer to the official MCP47A1 Datasheet:  

<QuickLink  
  title="MCP47A1 Datasheet"  
  description="Detailed technical documentation for the MCP47A1 DAC"  
  url="https://soldered.com/productdata/2022/03/Soldered-MCP47A1-datasheet.pdf"  
/>  

---

## How it works

**Digital to Analog Conversion (DAC)** is the process of transforming digital signals, which consist of discrete binary values (0s and 1s), into continuous analog signals. This is necessary because most real-world applications, such as sound reproduction, video display, and industrial control systems, require smooth, continuous signals rather than discrete digital values.

The conversion process begins with a digital input, typically represented as a series of binary numbers. Each binary value corresponds to a specific voltage or current level. The DAC interprets these binary numbers and generates a corresponding analog voltage or current. However, since digital signals change in **discrete steps**, the initial analog output appears as a staircase-like waveform rather than a smooth signal. To make it truly continuous, the output is often passed through a **low-pass filter**, which removes high-frequency noise and smooths the transitions between steps.

<CenteredImage src="/img/mcp47a1/sample.png" alt="Sampling discrete steps" caption="Sampling discrete steps" width="600px" />

---

## I2C communication  

The MCP47A1 uses the I2C protocol to communicate with a microcontroller. It operates with a fixed I2C address of **0x2E**. Over I2C, we can give the MCP47A1 commands to change the converted output voltage, as well as have it output a waveform.