---
slug: /mppt-li-ion-cn3791/how-it-works
title: How it works
id: mppt-li-ion-cn3791-how-it-works
hide_title: false
pagination_next: null
---

The **CN3791** is a PWM buck switch-mode Li-Ion battery charger IC with built-in MPPT for solar panels. It charges in three stages:

- **Trickle charge:** deeply discharged cells receive 17.5% of the programmed current until the cell voltage exceeds 66.5% of the regulation voltage
- **Constant current:** full programmed charge current delivered until the battery approaches 4.2V
- **Constant voltage:** holds 4.2V (±1%) and tapers current until it drops to 16% of the programmed value, at which point charging terminates

If the battery voltage later drops below 95.5% of the regulation voltage, charging restarts automatically. When the input voltage drops below the battery voltage (e.g. at night), the IC enters sleep mode to prevent discharge.

<InfoBox>Image coming soon.</InfoBox>

---

## Datasheet

The official CN3791 datasheet:

<QuickLink  
  title="CN3791 Datasheet"  
  description="Detailed technical documentation for the CN3791"  
  url="https://www.alldatasheet.com/datasheet-pdf/pdf/1132685/CONSONANCE/CN3791.html"  
/>

---

## How to use this module

1. **Set the voltage jumper:** short the `SOLAR VOLTAGE` pin that matches the output voltage of your solar panel.
2. **Connect the solar panel:** attach your solar panel to the `SOLAR` terminals (`+` and `-`).
3. **Connect the battery:** connect your battery to the `BATTERY` terminals.
4. **Connect your circuit:** connect your circuit to the `BATTERY OUT` terminals.
5. **Expose to sunlight:** place your solar panel in direct sunlight to begin charging.
