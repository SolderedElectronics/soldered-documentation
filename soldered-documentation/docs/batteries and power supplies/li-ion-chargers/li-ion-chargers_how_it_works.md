---
slug: /li-ion-chargers/how-it-works 
title: Li-ion Charger - How it works
sidebar_label: How it works
id: li-ion-chargers-how-it-works
pagination_next: null
---

The **Li-Ion Charger** and **Li-Ion Charger with Protection** are compact modules designed to safely charge single-cell lithium-ion (3.7V nominal) batteries. They incorporate efficient charge management ICs that follow the standard **CC/CV (Constant Current / Constant Voltage)** algorithm.

<CenteredImage src="/img/chargers/333013.png" alt="Li-Ion Charger" caption="Li-Ion Charger" width="400px" />
<CenteredImage src="/img/chargers/333014.png" alt="Li-Ion Charger with Protection" caption="Li-Ion Charger with Protection" width="400px" />

---

## How Charging Works

### 1. Constant Current (CC) Phase

When the battery is deeply discharged, the charger supplies a **constant current** (up to 500mA depending on the module) to the battery while monitoring its voltage. This rapidly charges the battery from 3.0V to approximately 4.2V.

### 2. Constant Voltage (CV) Phase

Once the battery voltage reaches **4.2V**, the charger switches to **constant voltage** mode. The charging current gradually decreases while maintaining the 4.2V level. Charging ends when the current drops below a preset threshold (usually about 10% of the initial current).

---

## Charging Process Steps

1. **Battery Detection** – The IC detects the battery and checks its voltage level.
2. **Preconditioning** – If the battery voltage is very low, the charger applies a gentle current to revive it.
3. **CC Phase** – The charger delivers full current until approximately 4.2V is reached.
4. **CV Phase** – Voltage is held steady while the current drops gradually.
5. **Charge Complete** – When the current drops low enough, charging stops, as indicated by the status LED.

---

## Charger with Protection

The version with protection includes a **battery protection circuit**, which prevents:

- **Over-discharge** – Stops discharging below approximately 2.5V.
- **Overcharge** – Cuts off charging above approximately 4.25V.
- **Short circuit** – Immediately disconnects the output.
- **Overcurrent** – Limits the maximum current draw.

This makes it suitable for **standalone battery packs** where no additional BMS is used.

<WarningBox>For older Li-ion charger with protection boards, connect the TEMP pin to GND to initiate charging. The onboard CHRG LED will indicate the charging status. </WarningBox>

---

## TP4056 Charging IC

The **TP4056** is a linear charger designed for single-cell lithium-ion batteries. It includes an internal PMOSFET, thermal regulation, and current monitoring.

<CenteredImage src="/img/chargers/tp4056.png" alt="TP4056 IC" caption="TP4056 Linear Li-ion Charger Controller" width="500px"/>

### Key features:
- Constant-current / constant-voltage operation
- 1% charging accuracy
- Built-in protection for overvoltage and undervoltage
- LED charge and full indicators

---

## DW01 + FS8205A Protection Circuit

The **Li-ion Charger with Protection** includes the **DW01A** battery protection IC and **FS8205A** dual MOSFET to guard against overcharge, overdischarge, and short circuits.

<CenteredImage src="/img/chargers/protected-chip.png" alt="DW01 + FS8205A" caption="DW01 and FS8205A on protected charger" width="500px"/>

### Additional Protection Features:
- Overcharge protection at 4.28V
- Overdischarge cutoff at 2.4V
- Short-circuit and overcurrent protection
- Automatically resumes operation when safe

---

## Status LEDs

- **Red LED** – Charging
- **Green LED** – Charge complete

<CenteredImage src="/img/chargers/charging_red.png" alt="charging" caption="Red LED - Charging status" width="500px"/>

---

## Input Power Sources

These modules can be powered from:

- **USB-C port**
- **Header pins (5V in)**

Make sure the input is at least 5V for proper operation. The output is typically **4.2V max** when charging and follows the battery voltage when discharging.