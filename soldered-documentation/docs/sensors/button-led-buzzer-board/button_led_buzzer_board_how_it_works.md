---
slug: /button-led-buzzer-board/how-it-works
title: Button, LED & Buzzer Board - How it works
sidebar_label: How it works
id: button_led_buzzer_board-how-it-works
hide_title: false
---

The **Button, LED & Buzzer Board with Qwiic** is made by **Soldered Electronics**. It carries **three tactile push buttons**, **three addressable RGB LEDs** and a **buzzer**, and a preprogrammed **ATtiny404** by [**Microchip**](https://www.microchip.com/en-us/product/attiny404) does the work of reading the buttons and driving the LEDs and buzzer. The host only ever speaks **I2C** to it, at address **0x30** by default.

{/* PLACEHOLDER: Add a board image with components highlighted once available.
<CenteredImage src="/img/button_led_buzzer_board/333182_highlighted.jpg" alt="Button, LED & Buzzer Board components" caption="Button, LED & Buzzer Board components" width="400px" />
*/}

---

## Datasheet

For an in-depth look at technical specifications of the onboard microcontroller, see the official ATtiny404 Datasheet:

<QuickLink  
  title="ATtiny404 Datasheet"  
  description="Detailed technical documentation for the ATTiny202/204/402/404/406 microcontroller family by Microchip"  
  url="https://ww1.microchip.com/downloads/aemDocuments/documents/MCU08/ProductDocuments/DataSheets/ATtiny202-204-402-404-406-DataSheet-DS40002318A.pdf"  
/>

---

## How each component works

### Buttons

The board has **three tactile push buttons** (BTN1, BTN2, BTN3), each a momentary switch that's open (not pressed) in its default state and closes the circuit when pressed. Inside the button, a small flexible metal dome sits over two separate contact pads. Pressing the button collapses the dome, and it bridges the two pads, closing the circuit. Releasing the button lets the dome spring back to its resting shape, opening the circuit again. This is also what gives tactile buttons their distinct "click" feel.

<CenteredImage src="/img/button_led_buzzer_board/pushbutton_mechanism.png" alt="How a tactile pushbutton switch works" caption="Inside the button: the dome lifts the contacts apart when released, and flattens to bridge them when pressed" width="600px" />

The onboard microcontroller reads all three buttons and reports them over I2C as a single bitmask, one bit per button. It deals with the contact bounce as well, so your sketch does not need any debouncing code of its own.

### LEDs

An **LED (Light Emitting Diode)** is a semiconductor component with a p-n junction: two layers of semiconductor material with different electrical properties. When current flows through the junction in the right direction, electrons and "holes" (missing electrons) recombine at the junction and release their extra energy as light instead of heat.

<div align="center">
  <a title="Inductiveload, Public domain, via Wikimedia Commons" href="https://commons.wikimedia.org/wiki/File:LED,_5mm,_green_(en).svg">
    <img width="300" alt="Labelled cross-section of a 5mm LED" src="https://upload.wikimedia.org/wikipedia/commons/f/f9/LED%2C_5mm%2C_green_%28en%29.svg"/>
  </a>
</div>

The board has **three addressable RGB LEDs (WS2812B)**, one next to each button. A plain LED lights up when current flows through it, and that is the whole extent of the control you get: on, off, or dimmed by limiting the current. A WS2812B is different. It packs a tiny driver chip in the same package as the red, green and blue LED dies, and that chip listens for color data sent over a single data wire. Each LED reads the first 24 bits of color data meant for it, then passes the rest down the line to the next LED, which is what lets many of them be chained together and controlled individually from a single pin. On this board, the onboard ATtiny404 handles that single-wire protocol itself, so from the host's side, setting an LED's color is just a normal I2C command.

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

The onboard **ATtiny404** is a follower device with its own address on the bus. The host uses that address to send it commands and to read data back from it. The default address is **0x30**, and the DIP switch on the board changes it when you need more than one of these boards on the same bus.

Every transaction follows the same pattern, shown below. The host pulls SDA low while SCL is high to signal a **start condition (S)**. SCL then toggles once per bit, and the data shifts out over SDA one bit at a time, whether that data is a color you are setting, a frequency to play, or the button states coming back. A **stop condition (P)** ends the transaction, with SDA going high while SCL is high. The Arduino library does all of this for you, so `board.setLED()` and `board.readButtons()` each amount to one of these exchanges.

<CenteredImage src="/img/button_led_buzzer_board/i2c_data_transfer.svg" alt="I2C SDA and SCL signal timing during a data transfer" caption="SDA and SCL signal timing during an I2C data transfer, the same protocol this board uses" width="600px" />

