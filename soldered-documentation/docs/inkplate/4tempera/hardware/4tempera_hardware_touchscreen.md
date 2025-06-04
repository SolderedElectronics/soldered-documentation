---
slug: /inkplate/4tempera/hardware/touchscreen
title: Touchscreen
id: 4tempera-hardware-touchscreen
hide_title: true
---

<SectionTitle title="Touchscreen Overview" backgroundImage="img/touchscreen.jpg" />

The Inkplate 4 TEMPERA features a built-in **capacitive touchscreen** bonded to its **ED038TH2 e-paper panel**, providing smooth, direct interaction with the display surface. This integration makes it ideal for compact user interfaces, drawing apps, control panels, or other interactive applications — all while maintaining the low power consumption of e-paper.

---

## Key Features

- **Capacitive touch layer** integrated with the 3.8″ ED038TH2 e-paper display  
- **Two-point multitouch support** for gesture recognition or dual-finger use  
- Responsive touch tracking with fast screen updates  
- No additional external touch hardware is required — the controller is built in  
- Works in both **1-bit (black-and-white)** and **3-bit (grayscale)** display modes

---

## Usage and Design Considerations

- Optimized for use with **bare fingers** or **capacitive-compatible styluses**  
- The touch surface spans the **entire display area**, enabling full-screen interactivity  
- Touch input is temporarily **disabled during screen refreshes**, so avoid polling at those times  
- Ideal for **compact interactive interfaces** in embedded or portable projects

<InfoBox>Each display is sourced from previously deployed devices and thoroughly tested for touchscreen functionality during Inkplate 4 TEMPERA production and quality control.</InfoBox>

---

## Tips for Effective Touch UI Design

- Define **touch regions** visually using borders, labels, or icons  
- Provide immediate on-screen feedback for user actions  
- Avoid placing critical touch zones near the bezel to reduce accidental inputs  
- Add **debounce logic** or tap thresholds to avoid duplicate interactions  
- Try to minimize unnecessary screen updates while interacting to ensure consistent responsiveness