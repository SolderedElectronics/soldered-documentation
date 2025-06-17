---
slug: /w5500/arduino/troubleshooting
title: W5500 - Troubleshooting
id: w5500-arduino-5
hide_title: False
sidebar_label: Troubleshooting
pagination_next: null
---

This page contains some tips in case you experience problems using this product.

<ExpandableSection title="My module won't initialize!">

### Check wiring
Ensure that your SPI communication pins are connected properly. Some MCUs have more than one set of SPI pins, commonly named VSPI pins. Try switching to these pins.

### Check for conflicting devices
If multiple devices on the same network have the exact same MAC address, there will be problems during module initialization. Verify that no other device is using the same address. Try running this function in CMD to see the ARP table of all devices on the network: `arp -a`.

### Try reinitializing
If the module fails to initialize, try resetting your microcontroller or reinitializing the device in your code. For example, call the initialization function for the module again or perform a system reboot to resolve potential initialization issues.

</ExpandableSection>

<InfoBox>In case you haven't found the answer to your question, please **contact us** via [**this**](https://soldered.com/contact/) link.</InfoBox>