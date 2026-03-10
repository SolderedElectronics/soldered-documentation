---
slug: /lofi-noise-machine/assembly-guide
title: Lo-Fi Noise Machine - Assembly Guide
id: lofi-noise-machine-assembly-guide
hide_title: False
pagination_next: null
sidebar_label: Assembly guide
---

On this page, we will guide you step by step on how to assemble this kit.

<WarningBox> Please read the instructions carefully and take all the usual safety precautions when soldering. If you're a beginner, be cautious! You’re holding a 300 °C tool after all — but we know you can do it. 🙂 </WarningBox>

<InfoBox> Before starting, make sure you have all the components at hand. You can find the complete components list in the [**Contents section on the Overview page**](/documentation/macro-pad/overview/#contents-of-the-kit). </InfoBox>

## Step 1: Solder the IC sockets

We'll start of by soldering the IC sockets for out NE556 timer and power regulator. **Be mindful of their orientation, align the notch from the socket with the notch on the breadboard.**

<WarningBox> **NOTE:** Don't yet insert the ICs in their sockets to avoid damaging them with heat. This will be done at the end. </WarningBox>

<CenteredImage src="/img/lofi-noise-kit/ic_sockets_solder_position.png" alt="IC sockets soldering" caption="Soldering IC sockets" /> 

## Step 2: Solder the inductor

Because of its placement, we recommend soldering the inductor now as it will be easier while the board is still empty. This component is labeled **L1** on the PCB.

<CenteredImage src="/img/lofi-noise-kit/inductor_placement.png" alt="IC sockets soldering" caption="Inductor placement on the PCB" width="700px" /> 

## Step 3: Solder the resistors

Next, we'll solder all the resistors to the PCB. We have a total of 14 resistors. Resistors use color codes printed on their bodies to represent their resistance and tolerance value. Take a look at the table below:

<InfoBox> **NOTE:** Resistors don't have polarity so you can place them either way! </InfoBox>

| Resistor    | Value       | Reference image (Color codes) |
|-------------|-------------|-------------------------------|
| R2, R9, R18 | 1 kΩ | <CenteredImage src="/img/lofi-noise-kit/1kohm.png" alt="1k ohm resistor" caption="" width="250px" /> |  
|   R1, R11   | 2.2 kΩ | <CenteredImage src="/img/lofi-noise-kit/2k2ohm.png" alt="2.2k ohm resistor" caption="" width="250px" /> |
| R7          | 10 kΩ | <CenteredImage src="/img/lofi-noise-kit/10kohm.jpg" alt="10k ohm resistor" caption="" width="250px" /> |
| R8          | 4.7 kΩ | <CenteredImage src="/img/lofi-noise-kit/4k7ohm.png" alt="4.7k ohm resistor" caption="" width="250px" /> |
| R10         | 150R 1W | <CenteredImage src="/img/lofi-noise-kit/150r1w.png" alt="150r1w resistor" caption="" width="250px" /> |
| R12         | 470R | <CenteredImage src="/img/lofi-noise-kit/470ohm.png" alt="470 ohm resistor" caption="" width="250px" /> |
| R13         | 22 kΩ | <CenteredImage src="/img/lofi-noise-kit/22kohm.png" alt="22k ohm resistor" caption="" width="250px" /> |
| R14         | 33 kΩ | <CenteredImage src="/img/lofi-noise-kit/33kohm.png" alt="33k ohm resistor" caption="" width="250px" /> |
| R15         | 0.3R 2W | <CenteredImage src="/img/lofi-noise-kit/0.3-2w-resistor.png" alt="0.3R resistor" caption="" width="250px" />|
| R16         | 180R | <CenteredImage src="/img/lofi-noise-kit/180rohm.png" alt="180r ohm resistor" caption="" width="250px" /> |
| R19         | 6.2 kΩ | <CenteredImage src="/img/lofi-noise-kit/6k2ohm.png" alt="6k2 ohm resistor" caption="" width="250px" /> |

<CenteredImage src="/img/lofi-noise-kit/resistors_placement.png" alt="IC sockets soldering" caption="All resistors locations on the PCB" width="700px"/> 

## Step 4: Solder the capacitors

Now, let's solder the capacitors. There are a total of 11 capacitors to be soldered, out of which 8 are ceramic capacitors and 3 electrolytic capacitors.

<InfoBox> **NOTE:** Ceramic capacitors are **not polarized**, so their orientation doesn't matter! Electrolytic capacitors have a **positive** and a **negative** side!</InfoBox>

<CenteredImage src="/img/lofi-noise-kit/capacitors_highlighted.png" alt="Capacitors" caption="" width="700px" />

### Soldering ceramic capacitors

As mentioned above, these types of capacitors are **not polarized**, meaning you can rotate them how ever you want. Below is a reference table showing where to solder each ceramic capacitor:

| Capacitor   | Value       |
|-------------|-------------|
| C1, C2, C8  |  10nF       |
| C3          |  10uF       |
| C7          | 100nF       |
| C9          | 1nF         |
| C10         | 1uF         |
| C12         | 220pF       |


<CenteredImage src="/img/lofi-noise-kit/ceramic_capacitors_values_new.png" alt="Ceramic capacitors" caption="Ceramic capacitors placement on the PCB" width="700px"/>

### Soldering electrolytic capacitors

Before soldering these capacitors, make sure you check their polarity. The **longer leg is positive (+)**, and **shorter leg is negative (-)**. Additionaly, the **negative side** is marked with a stripe on the capacitor body, printed with **'(-)'** symbols. Below is a reference table showing where to solder each electrolytic capacitor:

| Capacitor   | Value       |
|-------------|-------------|
| C4, C11     |  100µF      |
| C5          |  560µF      |

<CenteredImage src="/img/lofi-noise-kit/electrolytic_capacitors.png" alt="Electrolytic capacitors" caption="Electrolytic capacitors placement on the PCB" width="700px"/>

## Step 5: Solder the diode

The diode is located at the right side of the PCB, **labeled D3**. Be mindful of its orientation, take a look at the image below:

<CenteredImage src="/img/lofi-noise-kit/diode_anode_cathode.png" alt="Diode polarity" caption="Diode polarity" width="500px" />

<CenteredImage src="/img/lofi-noise-kit/diode.png" alt="Diode placement" caption="Diode placement on the PCB" width="700px" />

## Step 6: Solder the LEDs

When soldering the LEDs, pay attention to which side is positive, and which is negative. The labels for LEDs on the PCB have a **positive (left) side** marked with a '+' sign.

<CenteredImage src="/img/stop-me-game/led.jpg" alt="Marked pins on LED" caption="Marked pins on LED" width="500px"/>

<CenteredImage src="/img/lofi-noise-kit/leds_placement.png" alt="LEDs placement" caption="LEDs placement on the PCB" width="700px" />


## Step 7: Solder the potentiometers and pushbutton

Now, let's solder the mechanical parts.

**Potentiometers:**

| Label    | Value       | Function |
|-------------|-------------|-------------------------------|
| VR1       | 500 kΩ        | Pitch |
| VR2       | 500 kΩ        | Pulse width |

<CenteredImage src="/img/lofi-noise-kit/pushbutton_potentiometers.png" alt="Mechanical parts" caption="2 x potentiometers and pushbutton placement on PCB" width="700px" />

## Step 8: Solder audio outputs

And for the final soldering step, attach the 3.5mm audio jack, the buzzer and the speaker wires. Make sure the buzzer and speaker polarity is soldered correctly.

<InfoBox> **NOTE:** The buzzer has a **(+)** symbol printed on top of its body indicating the positive pin side. </InfoBox>

<CenteredImage src="/img/lofi-noise-kit/audio_inputs.png" alt="Audio componetns" caption="Audio components placement on PCB" with="700px" />

## Step 9: Insert the ICs

To finish the build of, insert the two ICs in their sockets which we soldered in the first step. **Be careful about their orientation!**

<CenteredImage src="/img/lofi-noise-kit/ic_sockets_marked.png" alt="IC sockets orientation" caption="IC sockets reference dots for orientation" width="600px" />

## All done!

Ready to plug and play!