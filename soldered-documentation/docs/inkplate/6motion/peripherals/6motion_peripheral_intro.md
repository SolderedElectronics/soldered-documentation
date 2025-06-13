---
slug: /inkplate/6motion/peripherals/introduction
title: 6Motion - Peripheral basics
sidebar_label: Peripheral basics
id: 6motion-periph-intro
---


Inkplate 6 MOTION has some useful peripherals, including **sensors**, **LEDs** and **user inputs**. They are all integrated in the Inkplate MOTION library. This page contains a quick overview of functions which are in common with all peripherals.

---

## Powering on

<WarningBox>To use any peripheral, it **needs to be powered on**. This is important, as trying to communicate with a peripheral which wasn't powered on before results faliure to initialize.</WarningBox>

To power on any peripheral, use `peripheralState`:

```cpp
inkplate.peripheralState(INKPLATE_PERIPHERAL_APDS9960, true);
```

<FunctionDocumentation
  functionName="inkplate.peripheralState()"
  description="Enables or disables Inkplate 6 Motion peripherals to save power during sleep."
  returnDescription="none"
  parameters={[
    { type: 'uint8_t', name: '_peripheral', description: "Selected peripheral (e.g., INKPLATE_PERIPHERAL_SDRAM, INKPLATE_PERIPHERAL_ROTARY_ENCODER). See below for the full list." },
    { type: 'bool', name: '_en', description: "Set the state of the selected peripheral; true enables it (power on), false disables it (power off)." },
  ]}
/>

| Peripheral Name                      | Description                                      | Bit Mask Value |
|---------------------------------------|--------------------------------------------------|---------------|
| ``INKPLATE_PERIPHERAL_SDRAM``         | External SDRAM used for framebuffer storage.    | `1ULL << 0`   |
| ``INKPLATE_PERIPHERAL_ROTARY_ENCODER``| Rotary encoder for user input.                  | `1ULL << 1`   |
| ``INKPLATE_PERIPHERAL_WS_LED``        | WS2812 LED for status indication.               | `1ULL << 2`   |
| ``INKPLATE_PERIPHERAL_SHTC3``         | SHTC3 temperature and humidity sensor.          | `1ULL << 3`   |
| ``INKPLATE_PERIPHERAL_APDS9960``      | APDS9960 gesture and proximity sensor.         | `1ULL << 4`   |
| ``INKPLATE_PERIPHERAL_LSM6DSO32``     | LSM6DSO32 accelerometer and gyroscope.         | `1ULL << 5`   |
| ``INKPLATE_PERIPHERAL_MICROSD``       | microSD card slot for external storage.        | `1ULL << 6`   |
| ``INKPLATE_PERIPHERAL_WIFI``          | Wi-Fi module for wireless connectivity.        | `1ULL << 7`   |
| ``INKPLATE_PERIPHERAL_ALL_PERI``      | Includes all peripherals except SDRAM & Wi-Fi. | Combination of above bit masks |
| ``INKPLATE_PERIPHERAL_ALL``           | Enables all peripherals including SDRAM & Wi-Fi. | Combination of all bit masks |

---

## Powering off

In a similar way, if you want to save power, you can use `peripheralState` to turn all (or individual) peripherals off:

```
inkplate.peripheralState(INKPLATE_PERIPHERAL_ALL, false);
```