---
slug: /SPK0641HT-microphone/getting-started
title: MEMS Microphone SPK0641HT4H Breakout - Getting started
sidebar_label: Getting started
id: spk0641ht-arduino-1
hide_title: true
---

# Getting started

This page provides the essential information for getting started with the **SPK0641HT4H-1 Digital MEMS Microphone breakout**, including wiring and basic usage with Arduino or ESP32 boards.

## Arduino library

The microphone outputs audio in **PDM format**, which can be captured and processed by microcontrollers that support a PDM interface (for example, ESP32, some Arduino boards, or through an audio codec).

<QuickLink  
  title="Arduino PDM library"  
  description="Official Arduino library for reading PDM microphone data"  
  url="https://www.arduino.cc/en/Reference/PDM"  
/>  

<InfoBox>

**First time Arduino user?** For a detailed tutorial on how to get started with Arduino, see this section of our docs:

<QuickLink  
  title="Getting started with Arduino"  
  description="A full, comprehensive tutorial on how to fully set up and upload code for the first time on an Arduino board, from scratch!"  
  url="/documentation/arduino/quick-start-guide"  
/>  

</InfoBox>

## Connections

To run the basic PDM examples, connect the breakout to your **Dasduino CONNECTPLUS** as follows:

| **Dasduino CONNECTPLUS**       | **SPK0641HT4H-1 Microphone Breakout**           |
| --------------- | ----------------------------------------------- |
| **3V3**         | **3V3**                                         |
| **GND**         | **GND**                                         |
| **IO4**         | **CLK**                                         |
| **IO27**        | **DATA**                                        |
| GPIO (optional) | **SEL** (set channel: High = Left, Low = Right) |

## PDM usage

The SPK0641HT4H-1 outputs audio as a **1-bit PDM signal**. Your microcontroller must:  

1. Provide the **clock signal** on the CLK pin.  
2. Read the **DATA stream** on the DATA pin.  
3. Optionally toggle **SEL** if using a stereo pair on the same data line.  
4. Use the **PDM library** (or an equivalent driver) to decimate and filter the PDM stream into PCM samples.  

Most modern MCUs (such as ESP32 and nRF52) have hardware support for PDM microphones, making setup straightforward once the wiring and library are in place.
