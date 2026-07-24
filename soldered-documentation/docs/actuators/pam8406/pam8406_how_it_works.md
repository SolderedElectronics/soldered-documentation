---
slug: /pam8406/how-it-works 
title: 5W Stereo Audio Amplifier PAM8406 – How it works
sidebar_label: How it works
id: pam8406-how-it-works 
hide_title: False
pagination_next: null
---

The PAM8406 is a Class-D stereo audio amplifier made by [**Diodes Incorporated**](https://www.diodes.com/part/view/PAM8406). Instead of amplifying an analog waveform directly the way a Class-AB amplifier does, it converts the incoming audio signal into a high-frequency switching pattern and uses that to drive the speaker. This board wraps the PAM8406 with input coupling, an output filter, and a control header, so you can feed it line-level stereo audio and get amplified sound out the other side.

---

## Datasheet

For the full electrical characteristics, absolute maximum ratings, and recommended application circuits, see the manufacturer datasheet:

<QuickLink
  title="PAM8406 Datasheet"
  description="Diodes Incorporated datasheet covering electrical characteristics, pin functions, and application circuits for the PAM8406."
  url="https://www.diodes.com/assets/Datasheets/PAM8406.pdf"
/>

---

## How the amplifier works

The picture below shows the trick: the audio signal (green) is compared against a fast carrier wave (blue). Wherever the audio is above the carrier, the output pulses on; wherever it's below, the output pulses off. That's the pink PWM signal at the bottom, and its pulses get wider or narrower as the audio signal rises and falls.

<div align="center">
  <a title="Cyril BUTTAY, CC BY-SA 3.0, via Wikimedia Commons" href="https://commons.wikimedia.org/wiki/File:Pwm.png">
    <img width="500" alt="An audio signal compared against a carrier wave to produce a PWM signal: wider pulses when the audio is high, narrower pulses when it's low" src="https://upload.wikimedia.org/wikipedia/commons/a/af/Pwm.png"/>
  </a>
</div>

The PAM8406 drives the speaker with that pulse train directly, switching fully on or fully off rather than sweeping through a continuous voltage range. Since the transistors spend almost no time in between, very little energy turns into heat, which is why Class-D amplifiers like this one are so efficient. A low-pass filter downstream (either inside the amplifier's switching scheme or added on the board) then smooths those pulses back into a clean audio waveform the speaker can reproduce. The PAM8406 is "filterless", meaning its switching scheme is clean enough to skip an external filter and drive a speaker directly, but this board adds a small LC filter per channel anyway to cut down EMI further.

The PAM8406 delivers **5W into a 2Ω load** or **3.14W into 4Ω**, both at 5V and 10% THD, and its efficiency depends on the load: around 80% into 2Ω, up to **90%** into 8Ω. Short-circuit protection and a 150°C thermal shutdown (with 30°C of hysteresis) keep the chip safe if something goes wrong, and the MODE pin lets you fall back to Class-AB if Class-D's switching noise ever causes problems, at the cost of efficiency. This board's onboard pull-up on MODE defaults to Class-D.

---

## Control pins

The PAM8406 doesn't use a data bus like I2C or SPI. Three digital pins on the K3 header control it directly: MODE picks Class-D or Class-AB, SHDN shuts the whole chip down when pulled low, and MUTE silences the output when pulled low. All three work with a plain `digitalWrite()`, no library needed. SHDN and MUTE both have internal pull-ups inside the PAM8406, so the amplifier runs normally even with nothing connected to them.
