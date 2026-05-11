---
slug: /pomodoro-solder-kit/assembly-guide
title: Pomodoro Solder Kit - Assembly Guide
sidebar_label: Assembly Guide
id: pomodoro-solder-kit-assembly-guide 
hide_title: False
---

On this page, we'll guide you step-by-step on how to assemble your Pomodoro Solder Kit. Let's go!

<WarningBox>Please read the instructions carefully and take all the usual safety precautions when soldering. If you're a beginner, be cautious! You’re holding a 300 °C tool after all — but we know you can do it. 🙂</WarningBox>

<InfoBox>Before starting, make sure you have all the components at hand. You can find the complete components list in the [**Contents section on the Overview page**](/documentation/piano-solder-kit/overview/#contents-of-the-kit).</InfoBox>

## 10k Ohm Resistors

Let's start by soldering the 4 10k ohm resistors which are used as **pull-ups** for the user buttons. They are easy to spot in your package because they will come in a pack of 4, this is the color code of a 10k ohm resistor:

<CenteredImage src="/img/pomodoro-solder-kit/tutorial/10kohm.png" alt="10k Ohm Resistor" width="400px" caption="10k Ohm Resistor"/>

Here's where they need to be Soldered, R1, R2, R3 and R4:

<CenteredImage src="/img/pomodoro-solder-kit/tutorial/pomodoro_01.jpeg" alt="Pomodoro Solder Kit Tutorial Components" width="700px" caption="10k Ohm resistor soldering locations"/>

First, bend the resistor leads in a 'U' shape so that it fits into the through-holes and place it in one of the four resistor locations.

<InfoBox>Resistors aren't polarized so their orientation doesn't matter!</InfoBox>

<CenteredImage src="/img/pomodoro-solder-kit/tutorial/pomodoro_01.webp" alt="Bending the resistor leads in an 'U' shape" width="700px" caption="Bending the resistor leads in an 'U' shape"/>

<CenteredImage src="/img/pomodoro-solder-kit/tutorial/pomodoro_02.webp" alt="Placing a resistor" width="700px" caption="Placing the resistor in the through-hole to be soldered"/>

Now, bend the leads on the other side so that the component stays in place!

<CenteredImage src="/img/pomodoro-solder-kit/tutorial/pomodoro_03.webp" alt="Pomodoro Solder Kit Tutorial Components" width="700px" caption="Bending the leads of the resistor  on the other side of the PCB"/>

Now, solder away!

<CenteredImage src="/img/pomodoro-solder-kit/tutorial/pomodoro_04.webp" alt="Pomodoro Solder Kit Tutorial Components" width="700px" caption="Soldering the 10k ohm resistors"/>

Now, we can remove the extra lead on the other side with some wire cutters, ensuring a clean finish.

<CenteredImage src="/img/pomodoro-solder-kit/tutorial/pomodoro_06.webp" alt="Pomodoro Solder Kit Tutorial Components" width="700px" caption="Cutting the extra leads"/>

## 220 Ohm Resistors

The 220 ohm resistors are connected in series to anodes on the 7 segment display, as a resistor always needs to be connected to a diode in series to limit current. 

8 of these resistors are included in the kit:

<CenteredImage src="/img/pomodoro-solder-kit/tutorial/220ohm.png" alt="Pomodoro Solder Kit Tutorial Components" width="400px" caption="220 ohm resistor color code"/>

Here's where they need to go: R9, R10, R11, R12, R13, R14, R15, R16:

<CenteredImage src="/img/pomodoro-solder-kit/tutorial/pomodoro_02.jpeg" alt="Pomodoro Solder Kit Tutorial Components" width="700px" caption="220 ohm resistor locations"/>

We will use the same soldering technique as with the 10k ohm resistors: bend, insert, bend, solder, cut:

<CenteredImage src="/img/pomodoro-solder-kit/tutorial/pomodoro_05.webp" alt="Pomodoro Solder Kit Tutorial Components" width="700px" caption="Soldering the 220 ohm resistors"/>

## Pushbuttons

<CenteredImage src="/img/pushbutton.webp" alt="Pushbutton" width="300px" caption="Pushbutton"/>

The buttons are here to provide user interaction, here's where they are located on the PCB:

<CenteredImage src="/img/pomodoro-solder-kit/tutorial/pomodoro_03.jpeg" alt="Pomodoro Solder Kit Tutorial Components" width="700px" caption="Buttons location on the PCB"/>

Insert the buttons in the through-holes, making sure the button pins don't bend:

<CenteredImage src="/img/pomodoro-solder-kit/tutorial/pomodoro_07.webp" alt="Pomodoro Solder Kit Tutorial Components" width="700px" caption="Inserting the buttons"/>

Now you can solder them:

<CenteredImage src="/img/pomodoro-solder-kit/tutorial/pomodoro_08.webp" alt="Pomodoro Solder Kit Tutorial Components" width="700px" caption="Soldering the buttons"/>

## Buzzer

The buzzer is here to beep when it's time to rest or work! You'll easily spot it in the kit:

<CenteredImage src="/img/buzzer.webp" alt="Buzzer" width="300px" caption="Buzzer"/>

Insert the buzzer here, making sure to match the + sign with the + side marked on the PCB:

<CenteredImage src="/img/pomodoro-solder-kit/tutorial/pomodoro_04.jpeg" alt="Pomodoro Solder Kit Tutorial Components" width="700px" caption="Buzzer location"/>

<CenteredImage src="/img/pomodoro-solder-kit/tutorial/pomodoro_09.webp" alt="Pomodoro Solder Kit Tutorial Components" width="700px" caption="Inserting the buzzer"/>

<CenteredImage src="/img/pomodoro-solder-kit/tutorial/pomodoro_10.webp" alt="Pomodoro Solder Kit Tutorial Components" width="700px" caption="Soldering the buzzer"/>

## WS2812B RGB LED

To insert the RGB LED correctly, pay attention to the symbol on the front and the lenghts of the leads of the LED, they should match up like this:

<CenteredImage src="/img/pomodoro-solder-kit/tutorial/tht_diode_alignment.png" alt="Pomodoro Solder Kit Tutorial Components" width="150px" caption="WS2812B LED Orientation"/>

<WarningBox>This component is a bit more difficult to solder due to the smaller size pads. Use **very little** solder and make sure there's **no short between the LED leads**.</WarningBox>

<CenteredImage src="/img/pomodoro-solder-kit/tutorial/pomodoro_05.jpeg" alt="Pomodoro Solder Kit Tutorial Components" width="700px" caption="WS2812B RGB LED location"/>

<CenteredImage src="/img/pomodoro-solder-kit/tutorial/pomodoro_11.webp" alt="Pomodoro Solder Kit Tutorial Components" width="700px" caption="Inserting the LED"/>

## 7 Segment Display

Finally, the star of the show, the red 4 digit 7 segment display. Take off the protective cover and insert the 7 segment display, for orientation, pay attention the the decimal dots on the display, they should face down. 

<CenteredImage src="/img/pomodoro-solder-kit/tutorial/pomodoro_06.jpeg" alt="Pomodoro Solder Kit Tutorial Components" width="700px" caption="7 segment display location"/>

<CenteredImage src="/img/pomodoro-solder-kit/tutorial/pomodoro_12.webp" alt="Pomodoro Solder Kit Tutorial Components" width="700px" caption="Removing the protective cover from the 7 segment display"/>

<CenteredImage src="/img/pomodoro-solder-kit/tutorial/pomodoro_13.webp" alt="Pomodoro Solder Kit Tutorial Components" width="700px" caption="Inserting the 7 segment display"/>

Now solder away! 

<CenteredImage src="/img/pomodoro-solder-kit/tutorial/pomodoro_14.webp" alt="Pomodoro Solder Kit Tutorial Components" width="700px" caption="Soldering the 7 segment display"/>

<InfoBox>You can also trim the ends like the resistor leads</InfoBox>

## All done!

Now, simply plug in via USB-C and give your new Pomodoro Timer a try! It should welcome you with a
- Purple LED
- A Beep
- Settings menu where you can set the time interval

<CenteredImage src="/img/pomodoro-solder-kit/tutorial/pomodoro_15.webp" alt="Pomodoro Solder Kit Tutorial Components" width="700px" caption="The build is done!"/>

<br></br>

Check out the next page for details on how to use the pomodoro timer! 