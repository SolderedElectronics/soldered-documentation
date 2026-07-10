---
slug: /button_led_buzzer_board/how-it-works 
title: Button, LED & Buzzer Board - How it works
sidebar_label: How it works
id: button_led_buzzer_board-how-it-works 
hide_title: false
---

The **Button, LED & Buzzer Board with Qwiic** is produced by **Soldered Electronics** and combines three fundamental I/O components - **three tactile push buttons**, **three addressable RGB LEDs**, and a **buzzer** - on a single breakout board. The board uses a preprogrammed **ATTiny404 IC** by [**Microchip**](https://www.microchip.com/en-us/product/attiny404) to read and control these components, communicating with the host via **I2C (Qwiic)** connectivity with a default I2C address of **0x30**.

{/* PLACEHOLDER: Add a board image with components highlighted once available.
<CenteredImage src="/img/button_led_buzzer_board/333182_highlighted.jpg" alt="Button, LED & Buzzer Board components" caption="Button, LED & Buzzer Board components" width="400px" />
*/}

---

## Datasheet

For an in-depth look at technical specifications of the onboard microcontroller, see the official ATTiny404 Datasheet:

<QuickLink  
  title="ATTiny404 Datasheet"  
  description="Detailed technical documentation for the ATTiny202/204/402/404/406 microcontroller family by Microchip"  
  url="https://ww1.microchip.com/downloads/aemDocuments/documents/MCU08/ProductDocuments/DataSheets/ATtiny202-204-402-404-406-DataSheet-DS40002318A.pdf"  
/>

---

## How each component works

### Buttons

The board has **three tactile push buttons** (BTN1, BTN2, BTN3), each a momentary switch that's open (not pressed) in its default state and closes the circuit when pressed. Inside the button, a small flexible metal dome sits over two separate contact pads. Pressing the button collapses the dome, and it bridges the two pads, closing the circuit. Releasing the button lets the dome spring back to its resting shape, opening the circuit again. This is also what gives tactile buttons their distinct "click" feel.

<CenteredImage src="/img/button_led_buzzer_board/pushbutton_mechanism.png" alt="How a tactile pushbutton switch works" caption="Inside the button: the dome lifts the contacts apart when released, and flattens to bridge them when pressed" width="600px" />

The onboard microcontroller reads all three button states digitally and reports them over I2C as a single bitmask, one bit per button. This makes it easy to detect presses without any debouncing logic needed on the host side.

### LEDs

An **LED (Light Emitting Diode)** is a semiconductor component with a p-n junction: two layers of semiconductor material with different electrical properties. When current flows through the junction in the right direction, electrons and "holes" (missing electrons) recombine at the junction and release their extra energy as light instead of heat.

<div align="center">
  <a title="Inductiveload, Public domain, via Wikimedia Commons" href="https://commons.wikimedia.org/wiki/File:LED,_5mm,_green_(en).svg">
    <img width="300" alt="Labelled cross-section of a 5mm LED" src="https://upload.wikimedia.org/wikipedia/commons/f/f9/LED%2C_5mm%2C_green_%28en%29.svg"/>
  </a>
</div>

The board has **three addressable RGB LEDs (WS2812B)**, one next to each button. A regular LED can only be turned on or off (or dimmed) by the voltage applied to it directly. A WS2812B is different: it packs a tiny driver chip in the same package as the red, green, and blue LED dies, and that chip listens for color data sent over a single data wire. Each LED reads the first 24 bits of color data meant for it, then passes the rest down the line to the next LED, which is what lets many of them be chained together and controlled individually from a single pin. On this board, the onboard ATtiny404 handles that single-wire protocol itself, so from the host's side, setting an LED's color is just a normal I2C command.

### Buzzer

The **buzzer** on this board is a **piezoelectric buzzer**: it produces sound using a piezo element, a thin disc made of a material that changes shape slightly when a voltage is applied across it. Driving the disc with a repeating voltage signal makes it flex back and forth rapidly, and that vibration pushes air to create a sound wave. The rate of vibration determines the pitch you hear.

<div align="center">
  <a title="Sonitron Support, CC BY-SA 3.0, via Wikimedia Commons" href="https://commons.wikimedia.org/wiki/File:PiezoBendingPrinciple.gif">
    <img width="350" alt="Piezo element bending when voltage is applied" src="https://upload.wikimedia.org/wikipedia/commons/3/3a/PiezoBendingPrinciple.gif"/>
  </a>
</div>

The onboard microcontroller generates a PWM signal at the requested frequency and applies it to the piezo element, which is what produces the tone when commanded over I2C. Since it's a **passive** buzzer (unlike an active buzzer, which has its own built-in oscillator and can only beep at one fixed pitch), it needs this externally-driven signal to make any sound at all, but in exchange it can produce any frequency the microcontroller sends it, not just one fixed tone.

---

## I2C Communication

The board uses **I2C** (Inter-Integrated Circuit) communication to exchange data with a microcontroller. I2C uses two lines: **SDA** for **data transfer** and **SCL** for **clock synchronization**.

As a follower device, the onboard **ATTiny404** has a unique address that allows the host microcontroller to send commands and receive data, enabling control of the **LEDs**, **buzzer**, and reading of the **button** states. The default I2C address is **0x30**.

Every I2C transaction follows the same pattern shown below: the host pulls SDA low while SCL is high to signal a **start condition (S)**, then SCL toggles once per bit as data (a color to set, a frequency to play, or the button states coming back) shifts out one bit at a time over SDA, and the transaction ends with a **stop condition (P)**, SDA going high while SCL is high. The Arduino library handles all of this internally, so calling `board.setLED()`, `board.setBuzzer()`, or `board.readButtons()` runs this exact exchange for you.

<CenteredImage src="/img/button_led_buzzer_board/i2c_data_transfer.svg" alt="I2C SDA and SCL signal timing during a data transfer" caption="SDA and SCL signal timing during an I2C data transfer, the same protocol this board uses" width="600px" />

