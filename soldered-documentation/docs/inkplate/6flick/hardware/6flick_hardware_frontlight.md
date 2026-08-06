---
slug: /inkplate/6flick/hardware/frontlight
title: Inkplate 6FLICK – Frontlight
sidebar_label: Frontlight
id: 6flick-hardware-frontlight
hide_title: true
---

<SectionTitle title="Frontlight Overview" />

The Inkplate 6FLICK features a built-in **frontlight system** designed to evenly illuminate the e-paper screen in low-light conditions. Unlike backlit displays, the frontlight enhances visibility while preserving the display's natural, paper-like appearance, making it ideal for reading or ensuring UI visibility in dim environments.

---

## Key features

- Integrated **white LED frontlight layer** bonded with the **ED060XC3** e-paper panel  
- **64 brightness levels** (0 to 63) adjustable in real time via software  
- Uniform lighting across the entire display area  
- Low power consumption, with efficient LED drive circuitry  
- Can be used continuously without interfering with e-paper refresh operations  

<InfoBox>The frontlight is part of the original Kindle panel assembly reused in Inkplate 6FLICK. It is factory-integrated and fully supported in software.</InfoBox>

---

## Usage and design considerations

- Best suited for **dark environments**, indoor displays, or any use case with variable lighting  
- Brightness is set by an on-board **MCP47A1 DAC over I2C**, not by PWM, so there is no flicker at intermediate levels  
- Two calls control it: `display.frontlight.setState()` enables the circuit and `display.frontlight.setBrightness()` sets the level from 0 to 63  
- Works independently of the e-paper controller, so it will not cause ghosting  
- Compatible with both **USB and battery-powered** operation  

---

## Tips for effective use

- Set lower brightness levels when running on battery to conserve power  
- Automatically turn off the frontlight during **sleep modes** or prolonged inactivity  
- Consider pairing with a **light sensor** for ambient-responsive brightness control  
- Be mindful that maximum brightness will draw additional current, plan power budgets accordingly

---

## Related Examples

<QuickLink 
  title="Frontlight Brightness Example" 
  description="Simple sketch demonstrating how to control frontlight brightness using software."
  url="https://github.com/SolderedElectronics/Inkplate-Arduino-library/blob/master/examples/Inkplate6FLICK/Basic/Inkplate6FLICK_Simple_Frontlight/Inkplate6FLICK_Simple_Frontlight.ino"
/>