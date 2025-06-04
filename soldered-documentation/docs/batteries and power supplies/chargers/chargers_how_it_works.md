---
slug: /chargers/how-it-works
title: How it works
id: chargers-how-it-works
hide_title: False
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

---

## Status LEDs

- **Red LED** – Charging
- **Green LED** – Charge complete

---

## Input Power Sources

These modules can be powered from:

- **USB-C port**
- **Header pins (5V in)**

Make sure the input is at least 5V for proper operation. The output is typically **4.2V max** when charging and follows the battery voltage when discharging.