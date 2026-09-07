---
slug: /refill-2-0-kit/components
title: Soldered Refill 2.0 Kit - Components
id: refill-2-0-kit-components
hide_title: False
pagination_next: null
sidebar_label: Components
---

This page goes through every part in the kit: what it is, the numbers that matter when you wire it, and the mistake that most often kills it.

<ErrorBox>The component photos for the Soldered Refill 2.0 Kit haven't been generated yet! We're working on it!</ErrorBox>

---

## Resistors

The kit holds **50 × 330 Ω** and **50 × 10 kΩ**, both through-hole with 5% tolerance. Those two values cover the two jobs a beginner circuit almost always needs.

**330 Ω** is the LED series resistor. At 3.3 V it lets roughly 4 mA through a red LED, at 5 V roughly 9 mA. Both are bright enough to read across a room and both stay well inside what a GPIO pin can source.

**10 kΩ** is the pull-up and pull-down value. Put one between a button pin and 3.3 V and the pin reads HIGH until the button pulls it to ground. It is also the value to reach for in a voltage divider with a photoresistor, since the two are then in the same order of magnitude.

Read the value off the colour bands: orange-orange-brown-gold is 330 Ω, brown-black-orange-gold is 10 kΩ.

<InfoBox>Resistors have no polarity. Either leg can go either way round.</InfoBox>

---

## Capacitors

**10 × 100 nF 50 V ceramic.** These are the decoupling capacitors. One across the supply pins of an IC, as close to the chip as the breadboard allows, smooths out the current spikes the chip draws when it switches. The NE556 in particular behaves much better with one fitted. They also set the timing on the control pin of a 555 or 556 circuit.

**5 × 10 µF 25 V electrolytic.** These are the bulk capacitors, roughly a hundred times larger than the ceramics. They hold up the supply rail when something with a real appetite for current switches on, such as a motor through a MOSFET. In an RC timing circuit a 10 µF capacitor is what stretches a delay out to seconds instead of milliseconds.

<WarningBox>**The electrolytic capacitors are polarised.** The shorter leg and the stripe printed down the side of the can both mark the negative terminal, and that leg goes to ground. Wire one backwards and it will heat up, vent and can burst. The 100 nF ceramics have no polarity and can go in either way.</WarningBox>

---

## 1N4148 signal diode

Ten of them, in a small glass body with a black band at one end. The band marks the cathode, the leg current flows out of.

The 1N4148 blocks up to 100 V in reverse and passes a couple of hundred milliamps forward, and it switches fast enough for logic-speed signals. In this kit it has two jobs. As a flyback diode it sits across a relay coil or a motor, band toward the positive supply, and absorbs the voltage spike the coil throws out when the current stops. As a steering diode it lets you OR two signals together or protect an input against reverse polarity.

<WarningBox>Switching any coil, whether a relay, a solenoid or a DC motor, without a flyback diode across it will destroy the transistor or MOSFET driving it. The spike from a collapsing coil field easily reaches hundreds of volts.</WarningBox>

---

## NPN transistor, TO-92

Ten general-purpose NPN transistors in the flat black TO-92 package. A small current into the base lets a much larger current flow from collector to emitter, so a GPIO pin that can only manage a few milliamps can switch a load drawing a hundred or so.

Use one to drive a relay coil, a small buzzer, or a string of LEDs that would otherwise overload a pin. Always put a base resistor between the GPIO pin and the base; 10 kΩ from this kit is a sensible starting point.

The three legs are emitter, base and collector, and the order depends on the exact part. Read the marking on the flat face and check the pinout before you wire it.

<InfoBox>For anything above roughly 200 mA, skip the TO-92 transistor and use one of the IRLZ44N MOSFETs instead. It handles far more current and needs no base resistor.</InfoBox>

---

## IRLZ44N logic-level N-channel MOSFET

Three of them, in the large TO-220 package with a metal tab and a mounting hole. Rated **55 V** drain-to-source and **47 A** continuous drain current, with an on-resistance of about 0.022 Ω specified at a gate drive of 5 V.

The word that matters is **logic-level**. An ordinary MOSFET needs around 10 V on its gate before it turns fully on, which a microcontroller pin cannot supply. The IRLZ44N is designed to turn on from logic voltages, so a 5 V pin drives it directly.

This is the part that lets the kit switch things the beginner kits cannot: 12 V LED strips, DC motors, pumps, heaters, solenoids. The load goes between the positive supply and the drain, the source goes to ground, and the gate goes to the GPIO pin through a small series resistor. Add a 10 kΩ pull-down from gate to ground so the MOSFET stays off while the board is booting.

<WarningBox>**The tab is electrically connected to the drain**, not to ground. If you bolt the MOSFET to a metal chassis or let the tab touch another component's tab, you are shorting the load supply through whatever it touches. Use an insulating washer, or leave the tab free.</WarningBox>

<InfoBox>The on-resistance figure is specified with 5 V on the gate. Driven from a 3.3 V pin the MOSFET still turns on, but with a higher on-resistance, so it runs hotter at the same current. For heavy loads on a 3.3 V board, keep the current modest or drive the gate from 5 V through a level shifter.</InfoBox>

---

## Photoresistor, 10 kΩ

Five light-dependent resistors with the familiar zigzag track on the face. Bright light drops the resistance to a few kilohms; darkness pushes it up into the hundreds of kilohms.

On its own a photoresistor tells a microcontroller nothing, because an analog pin measures voltage, not resistance. Wire it in a voltage divider with one of the 10 kΩ resistors and the junction between them becomes a voltage that tracks the light level, which `analogRead()` can then measure.

The [**2.3 Photoresistor Analog Read**](/soldered-nula-beginner-kit-arduino/photoresistor-analog-read) example walks through that divider step by step.

<InfoBox>Photoresistors have no polarity, and they are slow: expect tens of milliseconds for the resistance to settle after a sudden change in light. That is fine for ambient light sensing and far too slow for detecting anything that flickers.</InfoBox>

---

## Small THT pushbutton

Five 4-legged tactile buttons that straddle the centre channel of a breadboard.

The catch with these is that only two of the four legs are useful. The two legs on the same side of the button are joined together inside it, permanently. Pressing the button connects one side to the other. So the two wires must come from **opposite** sides, diagonally across the centre channel. Take both from the same side and the circuit behaves as if the button is held down forever.

A pressed button also does not settle cleanly. The contacts bounce for a few milliseconds and a fast microcontroller reads that as several presses. [**2.2 Button Debounce**](/soldered-nula-beginner-kit-arduino/button-debounce) shows how to filter it in software.

---

## SPST panel switch, 17 × 13 mm

Three square panel-mount switches, single pole single throw: one circuit, on or off, and it stays where you put it. Unlike the pushbuttons, these latch, so they suit a main power switch or a mode selector on a finished project.

They mount through a rectangular cutout in an enclosure panel and terminate in solder lugs rather than breadboard-friendly pins, so solder a short wire to each lug before trying to use one on a breadboard.

<WarningBox>Never put a latching switch directly in series with a battery pack and a load without knowing the current the load draws. A panel switch of this size is meant for signal-level and low-power switching, not for breaking a high-current motor supply.</WarningBox>

---

## Potentiometers, 10 kΩ and 100 kΩ

Three of each, both through-hole with three legs. Turning the shaft moves a wiper along a resistive track, so the resistance between the wiper and each end pin changes while the total between the two end pins stays fixed.

Wire the two outer legs to 3.3 V and ground and the middle leg becomes an adjustable voltage that `analogRead()` reads as a value from 0 to the top of the ADC range. That is the standard way to add a volume knob, a brightness dial or a threshold adjustment to a project.

**Which value to use.** The 10 kΩ is the one for voltage dividers feeding an analog pin: low enough that the ADC input impedance does not skew the reading, high enough that it does not waste current. The 100 kΩ is for RC timing, where a larger resistance stretches the same capacitor over a much longer period. Pair a 100 kΩ potentiometer with a 10 µF capacitor on an NE556 and you get an adjustable delay running into seconds.

---

## 5 mm LED pack

One pack of 13 LEDs in assorted colours.

The **longer leg is the anode** and goes toward the positive side; the shorter leg is the cathode and goes to ground. There is also a flat spot on the rim of the case next to the cathode, which is easier to find once the legs have been trimmed.

<WarningBox>**An LED always needs a series resistor.** Connected straight across a supply it draws whatever current the supply can deliver and burns out in an instant, often taking the GPIO pin with it. Use one of the 330 Ω resistors.</WarningBox>

<InfoBox>An LED backwards will not break, it just will not light. If a circuit looks right and nothing happens, turning the LED round is the first thing to try.</InfoBox>

---

## Passive buzzer QMB-09B-03

One passive buzzer. Passive means it has no oscillator inside: it makes a sound only when you feed it a changing signal, and the pitch is whatever frequency you send. That is what makes it able to play melodies rather than just beep.

On a microcontroller, `tone()` generates the square wave and `noTone()` stops it. The buzzer goes straight between a GPIO pin and ground with no resistor, since the pin only ever swings between 0 V and the supply voltage. Look for the **+** marked on the top of the case; that leg is the positive one.

The NE556 in this kit can drive it too, with no code involved at all: wired as an astable oscillator with a 100 nF capacitor, its output lands in the audible range and drives the buzzer directly.

<InfoBox>Both legs must land in different breadboard rows. Push them into the same row and the buzzer is shorted out and stays silent no matter what the code does. [**2.4 Buzzer Beep**](/soldered-nula-beginner-kit-arduino/buzzer-beep) covers the wiring and the code.</InfoBox>

---

## NE556 dual timer IC

One NE556 in a 14-pin DIP package. It holds **two complete and independent 555 timers**, sharing only the supply pins. Each half triggers at about one third of the supply voltage and its threshold sits at about two thirds, and each output can sink or source up to 200 mA, which is enough to drive an LED or the buzzer directly.

Two resistors and a capacitor around one half give you an astable oscillator: a square wave whose frequency is set entirely by those component values. Swap the capacitor for a larger one and the same circuit becomes a slow blinker; make it small and the output moves into the audio range. Wired as a monostable instead, one half produces a single pulse of a fixed length each time it is triggered.

With two timers in one chip you can chain them, using one to gate or trigger the other, which is how a single NE556 produces a warbling siren or a blinking tone.

<WarningBox>**The NE556 needs at least 4.5 V.** A 3.3 V rail will not run it reliably, so power it from 5 V or a higher supply up to 16 V. Also check the orientation before applying power: the notch at one end of the package marks the pin 1 end, and putting a DIP in backwards puts the supply across the wrong pins and destroys it.</WarningBox>

<InfoBox>Fit one of the 100 nF ceramic capacitors between the supply pins and ground, as close to the chip as the breadboard allows. A 556 switching 200 mA drags its own supply rail around, and without decoupling the timing wanders.</InfoBox>

<QuickLink
  title="NE556 datasheet"
  description="Texas Instruments, dual precision timer"
  url="https://www.ti.com/lit/ds/symlink/ne556.pdf"
/>

---

## Large breadboard and jumper wire set

One large breadboard and one set of jumper wires, so the kit works standing on its own without borrowing parts from another project.

The breadboard inner rows are connected in groups of five across the centre channel, and the two long rails down each edge carry power and ground. If that layout is new to you, [**0.1 Breadboard Fundamentals**](/soldered-nula-beginner-kit-arduino/breadboard-fundementals) explains it before you build anything.

<InfoBox>The rail beside the red line and the rail beside the blue line are separate strips and are not connected to each other, nor are the rails on opposite edges of the board. Every rail you intend to use needs its own wire back to the supply.</InfoBox>
