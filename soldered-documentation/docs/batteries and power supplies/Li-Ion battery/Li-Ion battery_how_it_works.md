---
slug: /li-ion-battery-new/how-it-works
title: How it works
sidebar_label: How it works
id: li-ion-battery-new-how-it-works
hide_title: false
pagination_next: null
---

The Li-ion batteries in this documentation are made by [**Fullest Energy Co., Ltd**](http://www.fullyenergy.com/index.php) for use in portable electronics.

<CenteredImage src="/img/li-ion-battery/333275.jpg" alt="Li-ion battery 40mAh 3.7V" caption="Li-ion battery 40mAh 3.7V" width="400px" />

---

## How Li-Ion batteries work

Li-ion batteries store and release energy through electrochemical reactions. During discharge, lithium ions travel from the anode to the cathode through the electrolyte, while electrons flow through the external circuit to power the device. Charging reverses this: an external voltage drives the ions back to the anode. A separator inside the cell keeps the electrodes apart while letting ions pass through.

<CenteredImage src="/img/li-ion-battery/scheme.jpg" alt="Schematic of a lithium ion battery" caption="Schematic of a lithium ion battery" width="400px" />

---

## Components

| Component | Role |
|-----------|------|
| Cathode | Positive electrode; stores lithium ions and sets the voltage |
| Anode | Negative electrode; stores ions during charging, typically graphite |
| Electrolyte | Lets ions move between electrodes while blocking electron flow |
| Separator | Keeps electrodes from touching while allowing ion flow |

---

## Discharge and recharge

During discharge, lithium ions (Li⁺) travel from the anode to the cathode through the electrolyte. At the cathode, they recombine with electrons arriving via the external circuit.

During recharge, the external source reverses the flow. Ions migrate back to the anode, where they recombine with electrons in a process called intercalation.

---

## Storage

Store at 0°C to +35°C for long-term storage. Short-term storage (up to 3 months) is acceptable at -10°C to +40°C, 45-85% RH. If storing for more than 3 months, recharge the battery periodically to maintain capacity.

---

## Onboard protection

Each battery includes a protection circuit that monitors voltage, current, and temperature:

- **Overcharging**: cuts off charge before the cell exceeds maximum voltage
- **Over-discharging**: stops discharge before the cell drops below minimum voltage, which causes permanent capacity loss
- **Short circuits**: interrupts current on a detected fault
