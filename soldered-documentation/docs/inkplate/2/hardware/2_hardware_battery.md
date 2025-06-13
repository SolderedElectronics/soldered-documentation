---
slug: /inkplate/2/hardware/battery
title: Inkplate 2 – Battery
sidebar_label: Battery
id: 2-hardware-battery
hide_title: true
---

<SectionTitle title="Battery" backgroundImage="/img/inkplate_2/hardware.png" />

<WarningBox>This page contains important information about using a battery with Inkplate 2. For safety reasons, **please read this page carefully!**</WarningBox>

Inkplate 2 includes soldering pads for connecting a **3.7V Li-ion battery** directly to the board. The onboard charging IC, **MCP73831**, automatically charges the battery when Inkplate 2 is connected via **USB-C** and switches to battery power when unplugged. This design enables **long battery-powered operation**, especially in **low-power applications**.

<CenteredImage src="/img/inkplate_2/battery_connector.png" alt="Inkplate 2 battery JST connector" caption="Battery connector" width="500px"/>  

<CenteredImage src="/img/inkplate_2/chrg_led.png" alt="Inkplate 2 Onboard charging indicator LED" caption="Onboard charging indicator LED" width="500px"/>  

---

## Battery Connection

Unlike larger Inkplate boards, the Inkplate 2 does **not** include a JST connector for battery attachment. Instead, it provides clearly marked **soldering pads** on the PCB for manual connection of your Li-ion battery wires:

<InfoBox>Be sure to match the battery polarity correctly when soldering wires! The **positive terminal** (+) is clearly marked on the PCB. Reversed polarity can damage the board.</InfoBox>

---

## Supported Battery Types

Inkplate 2 is compatible with **3.7V Li-ion batteries**, ideally with **built-in protection circuits**. These can be sourced from your preferred electronics supplier or from the [**Soldered online store**](https://soldered.com/categories/power-sources-batteries/batteries/lithium-batteries/).

Some recommended battery specs:
- **Voltage:** 3.7V
- **Capacity:** 300 mAh–1000 mAh for typical use
- **Protection Circuit:** Required
- **Connector:** No connector required (battery must be soldered)

<InfoBox>Due to international shipping restrictions, batteries may not be available for delivery outside the EU. For North American customers, consider [**Adafruit’s Li-ion options**](https://www.adafruit.com/category/574).</InfoBox>

---

## Charging Circuit: MCP73831

The **MCP73831** is a compact and highly integrated **Li-ion/Li-Polymer charge management controller**. It is preconfigured on Inkplate 2 to safely and efficiently manage charging behavior.

Key features:
- **USB-powered charging** (via USB-C)
- **Automatic charge termination**
- **Overvoltage and overcurrent protection**
- **Trickle charging when full**
- Compatible with single-cell 3.7V Li-ion batteries

<FunctionDocumentation
  functionName="MCP73831"
  description="Single-cell Li-ion battery charge controller used on Inkplate 2"
  returnDescription="Hardware only – automatic operation without user configuration"
/>

<InfoBox>For advanced users: refer to the [**MCP73831 datasheet**](https://ww1.microchip.com/downloads/en/DeviceDoc/MCP73831-Family-Data-Sheet-DS20001984H.pdf) for full technical details.</InfoBox>

---

## Battery Safety Guidelines

- Always check **battery polarity** before soldering.
- Use **batteries with protection circuits** to avoid over-discharge.
- **Do not charge damaged batteries**.
- Avoid short circuits on the battery pads during assembly.