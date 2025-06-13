---
slug: /125khzrfidtagreader/arduino/troubleshooting
title: 125Khzrfidtagreader - Troubleshooting
sidebar_label: Troubleshooting
id: 125khzrfidtagreader-arduino-4
hide_title: false
pagination_next: null
---
This page contains some tips in case you experience problems using this product.

<ExpandableSection title="My sensor won't initialize!">

### Check wiring
Ensure that your Qwiic cable is properly connected to the **125 kHz RFID reader**. Verify that the cable is in good condition by testing it with another **I2C-compatible device**. If the cable does not work, replace it with a new one to rule out potential damage or defects.

### Check I2C pins
If you are connecting the RFID reader using standard I2C pins on your microcontroller, confirm that you are using the **correct pins**. Different microcontrollers may label their I2C pins differently, so consult your microcontroller's documentation for proper pin assignments.

### Check for conflicting devices
If multiple I2C devices are connected to the same bus, ensure there are no address conflicts. The 125 kHz RFID reader has a specific I2C address (refer to its documentation for details), so verify that no other device is using the same address.

### Try reinitializing
If the RFID reader fails to initialize, try resetting your microcontroller or reinitializing the device in your code. For example, call the initialization function for the RFID reader again, or perform a system reboot to resolve potential initialization issues.

### Try swapping TX and RX pin allocations
If the RFID reader is connected via UART, ensure that the TX and RX pins are correctly assigned. Sometimes, communication issues arise due to incorrect pin allocations. Swap the TX and RX connections (e.g., connect the reader's TX pin to the microcontroller's RX pin and vice versa) and test the setup again.

</ExpandableSection>

<InfoBox>In case you haven't found the answer to your question, please **contact us** via [**this**](https://soldered.com/contact/) link.</InfoBox>