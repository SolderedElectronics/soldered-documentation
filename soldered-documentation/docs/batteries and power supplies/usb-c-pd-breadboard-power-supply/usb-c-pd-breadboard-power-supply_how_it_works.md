---
slug: /usb-c-pd-breadboard-power-supply/how-it-works 
title: How it works
id: usb-c-pd-breadboard-power-supply-how-it-works 
hide_title: False
---  
The **USB-C PD Breadboard Power Supply** is designed to provide configurable power delivery directly to your breadboard. It relies on the **HUSB238**, a highly integrated USB Power Delivery sink controller, to negotiate standard voltages and currents from any compatible USB-C adapter.
    

---

## How Power Negotiation Works

The **HUSB238** acts as a sink role controller. When you connect a USB-C Power Delivery source, the IC communicates over the Configuration Channel lines to read the capabilities of the power adapter. 

It then requests a specific voltage and current based on the configuration of the hardware switches on the board. The voltage and current are set by altering the resistance values connected to the **VSET** and **ISET** pins of the HUSB238.

If the requested voltage and current match what the adapter can provide, the negotiation is successful, and the power is output to the terminal blocks and header pins.

---

## Handling Mismatches

If you request a power profile that the adapter cannot provide, the HUSB238 incorporates mismatch rules. It will automatically fallback to a lower, safe voltage or request the next available lower voltage that meets the current requirements. 

---

## I2C Advanced Configuration

While the board functions perfectly as a standalone hardware-configured device via the onboard switches, the **SDA** and **SCL** pins are broken out. By connecting a microcontroller, you can interface with the HUSB238 over I2C. 

Using I2C overrides the hardware switch configurations, allowing you to read all available power profiles from the connected adapter, dynamically request voltage changes, and monitor the connection status.

---

## Protection Features

The controller integrates several safety mechanisms to protect your connected breadboard circuits. It includes Over-Voltage Protection and Under-Voltage Protection on the VBUS line. It also features Over-Temperature Protection to prevent overheating. The voltage rating goes up to 30V on VIN and GATE pins, ensuring safety even with 20V delivery.
