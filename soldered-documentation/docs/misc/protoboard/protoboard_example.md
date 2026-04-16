---
slug: /protoboard/example
title: Protoboard - How to use
sidebar_label: How to use
id: protoboard-example
hide_title: False
pagination_prev: null
---

This guide will familiarize you with the concept and working with a protoboard by making a simple circuit in which an NULA MINI controlls an LED. 

## Required components
- Protoboard (make sure it can fit a Soldered NULA MINI)
- Soldered NULA MINI
- LED (any color)
- Ressitor (220-330 ohm recommended)
- Hook-up wires
- Soldering iron & solder

---

## Understanding the circuit
Before we start soldering, we should understand the circuit and its connections.

The circuit is very straightforward:
- A **GPIO pin** from the NULA MINI is connected to a **resistor**
- The resistor is connected to the **anode (long leg)** of the LED
- The **cathode (short leg)** of the LED is connected to the **GND pin** of the NULA MINI

[image placeholder - connection diagram]

When the GPIO pin outputs HIGH (3.3V), current flows through the resistor and LED

---

## Soldering the components to protoboard

Start by placing the NULA MINI on protoboard:

[image placeholder - NULA MINI on protoboard]

<InfoBox>
Instead of soldering the NULA MINI directly, you can solder female header pins to the protoboard and connect the NULA MINI on them. This makes it easy to swap the board if something happends to it.
</InfoBox>

Solder the header pins to the protoboard:

[image placeholder - header pins soldered to protoboard]

Take a piece of wire with both ends stripped, solder one side to the VCC pin on NULA MINI and other one to a free hole on the protoboard, away from the components that were placed up until this point.

[Image placeholder - vcc wire]

Take a 330 ohm resistor, bend its contact ends and place it on the protoboard so that one contact end is near the wire that was soldered in previous step.

[image placeholder - resistor]

Take the LED and and place it on the protoboard. **Make sure that the LED's anode connector is facing the resistor**. Solder the anode to the other end of the resistor.

[image placeholder - led-resistor]

Take another piece of wire and connect LED's cathode with NULA MINI's GND pin.

[image placeholder - led-NULA MINI].

---

## Testing the circuit

If everything was connected correctly, LED should power on after powering the NULA MINI.

[image placeholder - LED glowing]