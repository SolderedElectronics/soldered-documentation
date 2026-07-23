---
slug: /pam8406/how-it-works 
title: 5W Stereo Audio Amplifier PAM8406 – How it works
sidebar_label: How it works
id: pam8406-how-it-works 
hide_title: False
---

The PAM8406 is a Class-D stereo audio amplifier made by Diodes Incorporated. Instead of amplifying an analog waveform directly the way a Class-AB amplifier does, it converts the incoming audio signal into a high-frequency switching pattern and uses that to drive the speaker. This board wraps the PAM8406 with input coupling, an output filter, and a control header, so you can feed it line-level stereo audio and get amplified sound out the other side.

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

Each channel's audio input passes through a coupling capacitor into the PAM8406, where it modulates a high-frequency PWM carrier. That PWM signal drives a pair of output transistors per channel in a full-bridge (BTL) configuration, switching the speaker terminals between the supply rails rather than sweeping them through a continuous range like a linear amplifier would. Because the output transistors are mostly either fully on or fully off, very little power is wasted as heat, which is why Class-D amplifiers reach efficiencies that Class-AB designs can't match.

The PAM8406 is rated for **5W output into a 2Ω load at 10% THD with a 5V supply**, or 3W into 4Ω under the same conditions, and reaches **up to 90% efficiency** in Class-D mode. Its output stage is "filterless", meaning the chip's own switching scheme is designed to keep enough energy out of the audio band that a speaker can be driven directly without a bulky LC low-pass filter. This board still adds a small output filter, a 4.7µH inductor and a shunt capacitor per channel, on top of that to cut down further on radiated EMI before the signal reaches the speaker terminals.

The MODE pin lets you fall back to Class-AB operation if the switching noise of Class-D ever causes problems in a particular circuit, at the cost of the efficiency advantage. On this board MODE has an onboard pull-up, so it defaults to Class-D unless you pull it low yourself.

The PAM8406 also includes short-circuit protection with automatic recovery and a thermal shutdown at 150°C (with 30°C of hysteresis before it re-enables), so a shorted speaker wire or an overheating board won't take out the chip.

---

## Control pins

The PAM8406 doesn't use a data bus like I2C or SPI. Instead, three digital pins on the K3 header control its behavior directly: MODE selects Class-D or Class-AB operation, SHND puts the whole chip into a low-power shutdown state when pulled low, and MUTE silences the output without powering anything down when pulled low. Driving these from a microcontroller is as simple as three `digitalWrite()` calls, no library needed. SHND and MUTE have no onboard pull-up, so both need to be actively driven high (tied to VCC or set high from a GPIO pin) before the amplifier will produce any sound.
