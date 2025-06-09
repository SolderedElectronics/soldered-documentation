---
slug: /cn3791/how-it-works 
title: How it works
id: cn3791-how-it-works 
hide_title: False
---  

The **CN3791** ia a **PWM** switch-mode lithium ion battery charger controller that can be powered by photovoltaic cell with maximum power point tracking function with few extarnal components. The CN3791 is specially designed for charging lithium ion batteries with constant current and constant voltage mode. In constant voltage mode, the regulation voltage can be fixed at 4.2V with ± 1% accuracy.

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

## Photovoltaic Systems Maximum Power Point Tracking

### Abstract

Photovoltaic (PV) systems have been used for many decades. Today, with the focus on greener sources
of power, PV has become an important source of power for a wide range of applications. Improvements in
converting light energy into electrical energy as well as the cost reductions have helped create this growth.
Even with higher efficiency and lower cost, the goal remains to maximize the power from the PV system
under various lighting conditions.


### Introduction

The power delivered by a PV (Photovoltaic) system of one or more photovoltaic cells is dependent on the irradiance,
temperature, and the current drawn from the cells. Maximum Power Point Tracking (MPPT) is used to
obtain the maximum power from these systems. Such applications as putting power on the grid, charging
batteries, or powering an electric motor benefit from MPPT. In these applications, the load can demand
more power than the PV system can deliver. In this case, a power conversion system is used to maximize
the power from the PV system.

There are many different approaches to maximising the power from a PV, these range from using simple voltage relationships to more complex multiple sample based analysis.

---

## How CN3791 works

The charge current is set by an external sense resistor (RCS) across the **CSP** and **BAT** pins. The final battery regulation voltage in constant voltage mode is set at **4.2V** typical with 1% accuracy. A charge cycle begins when the voltage at the VCC pin rises above **V**UVLO and the battery voltage by **V**SLPR, and the voltage at **MPPT pin is greater than 1.23V**. At the beginning of the charge cycle, if the battery voltage is less than **66.5%** of regulation voltage (VREG), the charger goes into **trickle charge mode**. The trickle charge current is internally set to **17.5%(Typical)** of the full-scale current. When the battery voltage exceeds 66.5% of regulation voltage, the charger goes into the **full-scale constant current charge mode**. In constant current mode, the charge current is set by the external sense resistor RCS and an internal 120mV reference, the **charge current equals to 120mV/RCS**. When the battery voltage approaches the regulation voltage, the charger goes into constant voltage mode, and the charge current will start to decrease. When the charge current drops to **16% of the full-scale current**, the charge **cycle is terminated**, the **DRV pin is pulled up to VCC**, and an internal comparator turns off the internal pull-down N-channel MOSFET at the CHRG pin, another internal pull-down N-channel MOSFET at the DONE pin is turned on to indicate the termination status. 

To **restart the charge cycle**, just remove and reapply the input voltage. Also, a new charge cycle will begin if the battery voltage drops below the recharge threshold voltage of 95.5% of the regulation voltage. The CN3791 adopts the constant voltage method to track the photovoltaic cell’s maximum power point. The **MPPT pin’s voltage is regulated to 1.205V**to track the maximum power point of the solar panel. When the input voltage is not present, the charger automatically goes into sleep mode, all the internal circuits are shutdown.

An **overvoltage comparator** guards against voltage transient overshoots (>7% of regulation voltage). In this case, P-channel MOSFET are turned off until the overvoltage condition is cleared. This feature is useful for battery load dump or sudden removal of battery. 

<CenteredImage src="/img/cn3791/charging_graph.png" alt="charging graph" caption="The Charging Profile" width="600px" />

CN3791 adopts the **constant voltage method** to track the photovoltaic cell's maximum power point. From I-V
curve of photovoltaic cell, under a given temperature, the photovoltaic cell’s voltages at the maximum power
point are nearly constant regardless of the different irradiances. So the maximum power point can be tracked if
the photovoltaic cell’s output voltage is regulated to a constant voltage. 