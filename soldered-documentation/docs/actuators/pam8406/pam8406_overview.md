---
slug: /pam8406/overview
title: 5W Stereo Audio Amplifier PAM8406 - Overview
sidebar_label: Overview
id: pam8406-overview 
hide_title: False
pagination_prev: null
---

## 5W Stereo Audio Amplifier PAM8406

This board is a stereo Class-D audio amplifier built around the **PAM8406**, delivering up to **5W per channel** into a 2Ω speaker load. Audio comes in through an onboard **3.5mm stereo jack** or an alternate wired input header, and each channel is filtered and broken out to its own screw terminal for connecting a speaker directly. A separate control header exposes the amplifier's **mode**, **shutdown**, and **mute** pins, so a microcontroller can enable, disable, or mute playback in software. The board runs directly from **2.5V to 5.5V** with no onboard regulator, so whatever voltage you feed it is what the amplifier sees.

---

## Which products is this documentation for?

<WarningBox>
This product is **coming soon** and is not yet available in our store. Check back soon!
</WarningBox>

---

## Key features
- **PAM8406 Class-D stereo amplifier**, switchable to Class-AB via the MODE pin
- **5W output into 2Ω at 5V** (10% THD), 3.14W into 4Ω at 5V
- **Up to 90% efficiency** in Class-D mode (varies by speaker load: ~80% into 2Ω, up to 90% into 8Ω)
- **Filterless Class-D architecture**, with an onboard LC output filter on each channel for extra EMI suppression
- **2.5V to 5.5V operating range**, powered directly with no onboard regulator
- **3.5mm stereo aux input jack**, plus a wired input header for the same left/right/ground signals
- **Screw terminal outputs** for both speaker channels
- **MODE / SHDN / MUTE control header** for microcontroller-driven mode switching, shutdown, and muting
- **Built-in short-circuit and thermal protection**, with automatic recovery

{/*
TODO - outstanding items for this module:
- Product photo needed (Overview)
- JP1/JP2 jumper photos needed (Hardware details)
- IC-on-board photo needed (Hardware details, How it works)
- Product page QuickLink still pending, replace WarningBox once the real product page/SKU goes live
*/}
