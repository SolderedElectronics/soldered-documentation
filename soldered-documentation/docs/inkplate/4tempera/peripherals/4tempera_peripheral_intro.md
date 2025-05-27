---
slug: /inkplate/4tempera/peripherals/introduction
title: Peripheral basics
id: 4tempera-periph-intro
hide_title: true
---

<SectionTitle title="Peripheral Basics" backgroundImage="/img/inkplate_2/hardware.png" />

Inkplate 4 TEMPERA includes several onboard peripherals designed to extend its functionality and adapt it to a wide range of projects. These include sensors, a touchscreen, a frontlight system, and more. To conserve power and ensure proper initialization, each peripheral must be individually powered on before use.

All peripherals are managed through the Inkplate library using the `wakePeripheral()` and `sleepPeripheral()` functions.

---

## Powering on

Peripherals are asleep by default. You must explicitly wake them before use with `inkplate.wakePeripheral()` — failing to do so will lead to initialization or communication failures.

To enable a peripheral:

```cpp
inkplate.wakePeripheral(INKPLATE_APDS9960); // Wake the gesture sensor
```

<FunctionDocumentation functionName="inkplate.wakePeripheral()" description="Powers on a peripheral device on the Inkplate 4 TEMPERA." returnDescription="None" parameters={[ { type: 'uint8_t', name: 'peripheral', description: "Peripheral constant (e.g., INKPLATE_TOUCH, INKPLATE_BME688, INKPLATE_APDS9960)." } ]} />

---

## Powering off

To save power, especially during battery operation or deep sleep, you can power off peripherals when they’re not in use:

```
inkplate.sleepPeripheral(INKPLATE_APDS9960); // Put the gesture sensor to sleep
```

<FunctionDocumentation functionName="inkplate.sleepPeripheral()" description="Puts the selected peripheral into low-power sleep mode." returnDescription="None" parameters={[ { type: 'uint8_t', name: 'peripheral', description: "Peripheral constant (same values as used with wakePeripheral)." } ]} />