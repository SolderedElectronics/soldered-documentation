---
slug: /button,led&buzzerboar/how-it-works 
title: Button, LED & Buzzer Board - How it works
sidebar_label: How it works
id: button,led&buzzerboar-how-it-works 
hide_title: false
---

The **Button, LED & Buzzer Board with Qwiic** is produced by **Soldered Electronics** and combines three fundamental I/O components — a **tactile push button**, an **LED**, and a **buzzer** — on a single breakout board. The board uses a preprogrammed **ATTiny404 IC** by [**Microchip**](https://www.microchip.com/en-us/product/attiny404) to read and control these components, communicating with the host via **I2C (Qwiic)** connectivity with a default I2C address of **0x30**.

{/* PLACEHOLDER: Add a board image with components highlighted once available.
<CenteredImage src="/img/button,led&buzzerboar/333182_highlighted.jpg" alt="Button, LED & Buzzer Board components" caption="Button, LED & Buzzer Board components" width="400px" />
*/}

---

## Datasheet

For an in-depth look at technical specifications of the onboard microcontroller, refer to the official ATTiny404 Datasheet:

<QuickLink  
  title="ATTiny404 Datasheet"  
  description="Detailed technical documentation for the ATTiny202/204/402/404/406 microcontroller family by Microchip"  
  url="https://ww1.microchip.com/downloads/aemDocuments/documents/MCU08/ProductDocuments/DataSheets/ATtiny202-204-402-404-406-DataSheet-DS40002318A.pdf"  
/>

---

## How each component works

### Button

The **tactile push button** is a momentary switch — it is open (not pressed) in its default state and closes the circuit when pressed. The onboard microcontroller reads the button state digitally and reports it over I2C. This makes it easy to detect button presses without any debouncing logic needed on the host side.

### LED

The **LED (Light Emitting Diode)** is controlled as a simple digital output. When the onboard microcontroller receives an I2C command to turn the LED on or off, it drives the LED pin accordingly. A current-limiting resistor on the board protects the LED from overcurrent.

### Buzzer

The **buzzer** is a passive component that produces sound when driven with a PWM signal. The onboard microcontroller generates the appropriate signal to produce a tone when commanded over I2C. The frequency and duration of the tone can be controlled through the library.

---

## I2C Communication

The board uses **I2C** (Inter-Integrated Circuit) communication to exchange data with a microcontroller. I2C uses two lines: **SDA** for **data transfer** and **SCL** for **clock synchronization**.

As a follower device, the onboard **ATTiny404** has a unique address that allows the host microcontroller to send commands and receive data, enabling control of the **LED**, **buzzer**, and reading of the **button** state. The default I2C address is **0x30**.
