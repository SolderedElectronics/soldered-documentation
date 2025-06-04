---
slug: /inkplate/6flick/hardware/touchscreen
title: Touchscreen
id: 6flick-hardware-touchscreen
hide_title: true
---

<SectionTitle title="Touchscreen Overview" backgroundImage="img/touchscreen.jpg" />

The Inkplate 6FLICK features a built-in **capacitive touchscreen** bonded to the **ED060XC3 e-paper panel**, allowing intuitive, direct interaction with the display surface. This integrated solution makes it ideal for projects involving touch-based menus, drawing interfaces, and simple games — all with the low power consumption and clarity of e-paper.

---

## Key Features

- **Capacitive touch panel** bonded to the 6.0″ ED060XC3 e-paper display  
- **Two-point multitouch detection** for gesture support and dual-finger interaction  
- Responsive input tracking suitable for fast UI updates and drawing  
- Integrated directly into the display module — no external controller or overlay needed  
- Fully compatible with both **1-bit (black and white)** and **3-bit (grayscale)** display modes

---

## Usage and Design Considerations

- Optimized for use with **bare fingers** or **capacitive styluses** (non-resistive)  
- The touch layer covers the **entire screen area**, providing full-surface interactivity  
- Touch input is temporarily **disabled during screen refreshes**, so structure your code to avoid polling during updates  
- Use in applications that involve **navigation, annotation, or interactive content**

<InfoBox>The touchscreen panel is part of the original Kindle display assembly. Although reused, each panel is tested for full touch functionality as part of the Inkplate 6Flick production process.</InfoBox>

---

## Tips for Effective Touch UI Design

- Define **touch zones** clearly using visual markers (e.g., buttons, borders)  
- Provide **immediate feedback** on touch to reinforce responsiveness  
- Avoid placing important interactive elements near screen edges to prevent accidental touches  
- Consider **debouncing** or simple logic guards to handle repeated taps cleanly  
- Limit screen refreshes during rapid input to maintain touch responsiveness