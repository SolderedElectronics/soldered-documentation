---
slug: /inkplate/6flick/hardware/frontlight
title: Inkplate 6FLICK – Frontlight
id: 6flick-hardware-frontlight
hide_title: true
---

<SectionTitle title="Frontlight Overview" backgroundImage="img/frontlight.jpg" />

The Inkplate 6FLICK features a built-in **frontlight system** designed to evenly illuminate the e-paper screen in low-light conditions. Unlike backlit displays, the frontlight enhances visibility while preserving the display's natural, paper-like appearance, making it ideal for reading or ensuring UI visibility in dim environments.

---

## Key Features

- Integrated **white LED frontlight layer** bonded with the **ED060XC3** e-paper panel  
- **64 levels of brightness** adjustable in real time via software  
- Uniform lighting across the entire display area  
- Low power consumption, with efficient LED drive circuitry  
- Can be used continuously without interfering with e-paper refresh operations  

<InfoBox>The frontlight is part of the original Kindle panel assembly reused in Inkplate 6Flick. It is factory-integrated and fully supported in software.</InfoBox>

---

## Usage and Design Considerations

- Best suited for **dark environments**, indoor displays, or any use case with variable lighting  
- Controlled using simple library functions — typically via PWM for brightness  
- Works independently of the e-paper controller, meaning it **won’t cause ghosting or flicker**  
- Compatible with both **USB and battery-powered** operation  

---

## Tips for Effective Use

- Set lower brightness levels when running on battery to conserve power  
- Automatically turn off the frontlight during **sleep modes** or prolonged inactivity  
- Consider pairing with a **light sensor** for ambient-responsive brightness control  
- Be mindful that maximum brightness will draw additional current — plan power budgets accordingly

---

## Related Examples

<QuickLink 
  title="Frontlight Brightness Example" 
  description="Simple sketch demonstrating how to control frontlight brightness using software."
  url="https://github.com/SolderedElectronics/Inkplate-Arduino-library/blob/dev/examples/Inkplate6FLICK/Basic/Inkplate6FLICK_Simple_Frontlight/Inkplate6FLICK_Simple_Frontlight.ino"
/>