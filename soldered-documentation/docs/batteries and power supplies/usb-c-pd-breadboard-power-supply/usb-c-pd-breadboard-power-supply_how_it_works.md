---
slug: /usb-c-pd-breadboard-power-supply/how-it-works 
title: How it works
id: usb-c-pd-breadboard-power-supply-how-it-works 
hide_title: False
---  
The **USB-C PD Breadboard Power Supply** uses the **HUSB238** USB Power Delivery sink controller to negotiate output voltage and current from any USB-C PD adapter.

---

## How power negotiation works

The HUSB238 is the sink controller in the USB-PD negotiation. On connection, it reads the adapter's available power profiles over the CC (Configuration Channel) lines. It then requests a voltage and current level based on the hardware switch positions, which set resistance values on the VSET and ISET pins. If the adapter supports the requested profile, the negotiated voltage appears on the output headers and terminal block.

---

## Handling mismatches

If the adapter cannot supply the requested profile, the HUSB238 falls back to the next available lower voltage that still meets the current requirement.

---

## I2C advanced configuration

The SDA and SCL pins are broken out for direct I2C access to the HUSB238. Connecting a microcontroller lets you read available adapter profiles, request specific voltages, and monitor connection status. When I2C is used, it overrides the hardware switch configuration.

---

## Protection features

The HUSB238 has over-voltage, under-voltage, and over-temperature protection on the VBUS line. The VIN and GATE pins are rated to 30V, giving clearance when running at 20V PD profiles.
