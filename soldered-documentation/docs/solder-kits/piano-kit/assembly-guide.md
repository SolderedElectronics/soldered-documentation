---
slug: /piano-solder-kit/assembly-guide
title: Piano Solder Kit - Assembly Guide
sidebar_label: Assembly Guide
id: piano-solder-kit-assembly-guide 
hide_title: False
pagination_next: null
---

On this page, we'll guide you step-by-step on how to assemble your Piano Solder Kit. Let's go!

<WarningBox>
Please read the instructions carefully and take all the usual safety precautions when soldering. If you're a beginner, be cautious! You’re holding a 300 °C tool after all — but we know you can do it. 🙂
</WarningBox>

<InfoBox>
Before starting, make sure you have all the components at hand. You can find the complete components list in the [**Contents section on the Overview page**](/documentation/piano-solder-kit/overview/#contents-of-the-kit).
</InfoBox>

<CenteredImage src="/img/piano-solder-kit/tutorial/tutorial_00.jpg" alt="Piano Solder Kit Tutorial Components" width="450px" caption="Piano Solder Kit - ready to assemble"/>

---

## Step 1: Solder the IC sockets

We recommend starting by soldering the IC sockets. Be mindful of their orientation!

<WarningBox>
**Note:** Don’t insert the ICs (ATmega328P and LM386) into the sockets until the whole soldering process is complete to avoid damaging them with heat.
</WarningBox>

<CenteredImage src="/img/piano-solder-kit/tutorial/parts_00.jpg" alt="Step 1: Solder the IC sockets" caption="Step 1: Solder the IC sockets"/>

After turning the PCB face down, you can use the included speaker to balance it so it doesn’t rattle:

<CenteredImage src="/img/piano-solder-kit/tutorial/tutorial_01.jpg" alt="PCB turned over" width="450px"/>
<br></br>
<CenteredImage src="/img/piano-solder-kit/tutorial/tutorial_03.jpg" alt="Soldering IC socket" width="450px"/>

---

## Step 2: Solder the 1 MΩ resistors

Great! Now let’s solder the resistors for the capacitive touch pads.  
You can identify the 1 MΩ resistor by this color code:

<CenteredImage src="/img/piano-solder-kit/tutorial/1mohm.jpg" alt="1MΩ resistor" width="250px" caption="1 MΩ resistor color code"/>

These should come connected in a pack of 12:

<CenteredImage src="/img/piano-solder-kit/tutorial/tutorial_05.jpg" alt="1 MΩ resistors" width="450px"/>
<br></br>
<CenteredImage src="/img/piano-solder-kit/tutorial/parts_01.jpg" alt="1 MΩ resistors identification" caption="Step 2: Solder the 1 MΩ resistors"/>

**Placement table:**

| Resistor | Value | Position on PCB |
|-----------|--------|----------------|
| R6–R17    | 1 MΩ   | Touch pad resistors |

Push each resistor from the front face of the PCB through the two holes and then bend the leads slightly so it stays in place. After placing them all, solder away! You can then snip off the excess leads.

<InfoBox>
Resistors don’t have polarity — you can place them either way.
</InfoBox>

<InfoBox>
This same “bend–insert–bend–solder–cut” procedure applies to all other resistors and similar components, so we won’t describe it again each time.
</InfoBox>

<CenteredImage src="/img/piano-solder-kit/tutorial/tutorial_06.jpg" alt="1 MΩ resistors" width="450px"/>
<br></br>
<CenteredImage src="/img/piano-solder-kit/tutorial/tutorial_07.jpg" alt="1 MΩ resistors" width="450px"/>

---

## Step 3: Solder the 5.1 kΩ resistors

You can identify the 5.1 kΩ resistors by their **blue** (metal film) color — they’re the only blue resistors in the kit.

<CenteredImage src="/img/piano-solder-kit/tutorial/parts_02.jpg" alt="5.1 kΩ resistors identification" caption="Step 3: Solder the 5.1 kΩ resistors"/>

**Placement table:**

| Resistor | Value | Position on PCB |
|-----------|--------|----------------|
| R2, R3    | 5.1 kΩ | Input network resistors |

<CenteredImage src="/img/piano-solder-kit/tutorial/tutorial_08.jpg" alt="5.1 kΩ resistors" width="450px"/>

---

## Step 4: Solder the 10 kΩ resistors

You can identify the 10 kΩ resistor by this color code:

<CenteredImage src="/img/piano-solder-kit/tutorial/10kohm.jpg" alt="10 kΩ resistor" width="250px" caption="10 kΩ resistor color code"/>

<CenteredImage src="/img/piano-solder-kit/tutorial/parts_03.jpg" alt="10 kΩ resistor" caption="Step 4: Solder the 10 kΩ resistors"/>

**Placement table:**

| Resistor | Value | Position on PCB |
|-----------|--------|----------------|
| R1, R4, R5, R20 | 10 kΩ | Pull-ups and feedback resistors |

<CenteredImage src="/img/piano-solder-kit/tutorial/tutorial_09.jpg" alt="10 kΩ resistors" width="450px"/>

---

## Step 5: Solder the remaining resistors

Let’s solder the remaining three resistors:

| Resistor | Value | Reference Image |
|-----------|--------|----------------|
| R21 | 10 Ω | <CenteredImage src="/img/piano-solder-kit/tutorial/10ohm.jpg" alt="10 Ω resistor" width="250px" /> |
| R18 | 100 Ω | <CenteredImage src="/img/piano-solder-kit/tutorial/100ohm.jpg" alt="100 Ω resistor" width="250px" /> |
| R19 | 100 kΩ | <CenteredImage src="/img/piano-solder-kit/tutorial/100kohm.jpg" alt="100 kΩ resistor" width="250px" /> |

<CenteredImage src="/img/piano-solder-kit/tutorial/parts_04.jpg" alt="Remaining resistors" caption="Step 5: Solder the remaining resistors"/>

---

## Step 6: Solder the 100 nF capacitors

These capacitors come pre-bent and are easy to insert.  
They are **non-polarized**, so their orientation doesn’t matter.

**Placement table:**

| Capacitor | Value | Position on PCB |
|------------|--------|----------------|
| C13, C4, C5, C2, C8, C3, C9 | 100 nF | Decoupling capacitors |

<CenteredImage src="/img/piano-solder-kit/tutorial/parts_05.jpg" alt="100 nF capacitors" caption="Step 6: Solder the 100 nF capacitors"/>

---

## Step 7: Solder the electrolytic capacitors

These capacitors **are polarized**, so mind their orientation!  
You can identify their values by reading the labels on the side. The shorter leg is the **cathode** and is marked by the lighter color stripe on the casing. The 680 µF capacitor is also green-colored.

<WarningBox>
The cathode (shorter leg) must be inserted into the shaded pad, and the anode (longer leg) into the pad marked with a **+** sign.
</WarningBox>

**Placement table:**

| Capacitor | Value | Notes |
|------------|--------|-------|
| C1 | 100 µF | Power filtering |
| C11 | 100 µF | Audio path |
| C12 | 10 µF | Signal coupling |
| C14 | 680 µF | Output capacitor (green) |

<CenteredImage src="/img/piano-solder-kit/tutorial/parts_06.jpg" alt="Electrolytic capacitors" caption="Step 7: Solder the electrolytic capacitors"/>

---

## Step 8: Solder the diodes

The diodes in the package are identical and go into **D1** and **D2** — but **mind their orientation!**

<WarningBox>
To place the diode correctly, keep in mind the **white marked side** of the diode is the **cathode**.
<CenteredImage src="/img/piano-solder-kit/tutorial/diode_anode_cathode.png" alt="Diode anode and cathode orientation"/>
</WarningBox>

<CenteredImage src="/img/piano-solder-kit/tutorial/parts_07.jpg" alt="Diodes" caption="Step 8: Solder the diodes"/>

---

## Step 9: Solder the potentiometers and switches

Almost there! Let’s solder the mechanical parts.

**Potentiometers:**

| Label | Value | Function |
|--------|--------|----------|
| VR1 | 10 kΩ | Volume control |
| VR2 | 100 kΩ | Tone control |

The switches only fit one way in their respective slots (ON/OFF, octave selection, and arpeggio mode).

<CenteredImage src="/img/piano-solder-kit/tutorial/parts_08.jpg" alt="Potentiometers and switches" caption="Step 9: Solder the potentiometers and switches"/>

<CenteredImage src="/img/piano-solder-kit/tutorial/tutorial_16.jpg" alt="Soldering potentiometers" width="450px"/>
<br></br>
<CenteredImage src="/img/piano-solder-kit/tutorial/tutorial_17.jpg" alt="Almost there" width="450px"/>

---

## Step 10: Finish the build

Solder and attach the speaker wires to the speaker, then connect them to the speaker outputs on the board.  
The speaker includes a small piece of self-adhesive tape to attach it to the PCB.

Then, you can insert the ICs into their sockets — **mind their orientation!**

<CenteredImage src="/img/piano-solder-kit/tutorial/ic_dot_orientation.jpg" alt="IC orientation" width="450px" caption="Orientation of the reference dots on the ICs"/>

<CenteredImage src="/img/piano-solder-kit/tutorial/parts_09.jpg" alt="Finish the build" caption="Step 10: Finish the build"/>

---

## Ready to go!

Now, simply plug it into USB-C and play!

<CenteredImage src="/img/piano-solder-kit/Piano-Solder-Kit-Animated.webp" alt="Piano animated" caption="Playing the Piano Solder Kit"/>
