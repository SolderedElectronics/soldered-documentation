---
slug: /li-ion-battery-charger-board/how-it-works
title: How it works
sidebar_label: How it works
id: li-ion-battery-charger-board-how-it-works
hide_title: false
pagination_next: null
---

Both boards charge single-cell 3.7V Li-ion batteries using the standard **CC/CV (Constant Current / Constant Voltage)** algorithm via the TP4056 IC. The protected version adds the DW01A battery protection IC on top of that.

<InfoBox>Image coming soon.</InfoBox>

---

## How charging works

### 1. Constant current (CC) phase

When the battery is deeply discharged, the charger supplies a constant current (up to 500mA) while monitoring the voltage. This charges the battery from 3.0V up to approximately 4.2V.

### 2. Constant voltage (CV) phase

Once the battery reaches **4.2V**, the charger holds that voltage steady while the current tapers off. Charging ends when the current drops below roughly 10% of the initial value.

---

## Charging process steps

1. **Battery detection**: the IC checks the battery voltage level.
2. **Preconditioning**: if the battery is very low, a gentle current revives it.
3. **CC phase**: full current delivered until ~4.2V is reached.
4. **CV phase**: voltage held at 4.2V while current gradually drops.
5. **Charge complete**: charging stops and the status LED changes.

---

## Charger with protection

The protected version adds a battery protection circuit that prevents:

- **Over-discharge**: cuts off below ~2.4V
- **Overcharge**: cuts off above ~4.3V
- **Short circuit**: immediately disconnects the output
- **Overcurrent**: limits maximum current draw

This makes it suitable for standalone battery packs where no additional BMS is present.

---

## TP4056 charging IC

The **TP4056** is a linear charger IC for single-cell Li-ion batteries with an internal PMOSFET, thermal regulation, and current monitoring.

<InfoBox>Image coming soon.</InfoBox>

- Constant-current / constant-voltage operation
- 1% charging voltage accuracy
- Undervoltage lockout and charge termination
- LED charge and full indicators

---

## DW01 + FS8205A protection circuit

The protected version includes the **DW01A** protection IC and **FS8205A** dual MOSFET.

<InfoBox>Image coming soon.</InfoBox>

- Overcharge protection at 4.3V
- Overdischarge cutoff at 2.4V
- Short-circuit and overcurrent protection
- Automatically resumes when safe

---

## Status LEDs

- **Red LED**: charging in progress
- **Blue LED**: charge complete

<InfoBox>Image coming soon.</InfoBox>

---

## Input power sources

These modules can be powered from a USB-C port or directly via the 5V header pins. The input must be at least 5V for proper operation.
