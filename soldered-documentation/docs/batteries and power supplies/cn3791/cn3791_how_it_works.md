---
slug: /cn3791/how-it-works 
title: How it works
id: cn3791-how-it-works 
pagination_next: null
hide_title: False
---  

The **CN3791** is a **PWM** switch-mode lithium-ion battery charger controller that can be powered by a photovoltaic cell with maximum power point tracking functionality using only a few external components. The CN3791 is specially designed for charging lithium-ion batteries using constant current and constant voltage modes. In constant voltage mode, the regulated voltage is fixed at **4.2V** with ±1% accuracy.

<CenteredImage src="/img/cn3791/cn3791_highlighted.png" alt="CN3791 on board" caption="CN3791 on board" width="500px" />

---

## Datasheet
For an in-depth look at technical specifications, refer to the official CN3791 Datasheet:

<QuickLink  
  title="CN3791 Datasheet"  
  description="Detailed technical documentation for the CN3791"  
  url="https://www.alldatasheet.com/datasheet-pdf/pdf/1132685/CONSONANCE/CN3791.html"  
/>

---

## How to Use This Module

To use this module, follow these steps:

1. **Set the Voltage Jumper**  
   Short the `SOLAR VOLTAGE` jumper that matches the output voltage of your solar panel.

2. **Connect the Solar Panel**  
   Attach your solar panel to the `SOLAR` terminals (`+` and `-`).

3. **Connect the Battery**  
   Connect your battery to the `BATTERY` terminals.

4. **Connect Your Circuit**  
   Connect your circuit to the `BATTERY OUT` terminals.

5. **Expose to Sunlight**  
   Place your solar panel in direct sunlight to begin charging.
