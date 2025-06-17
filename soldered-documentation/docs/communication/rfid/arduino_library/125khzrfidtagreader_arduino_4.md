---
slug: /125khzrfidtagreader/arduino/troubleshooting
title: 125Khzrfidtagreader - Troubleshooting
id: 125khzrfidtagreader-arduino-4
hide_title: false
pagination_next: null
---
This page contains some tips in case you experience problems using this product.

<ExpandableSection title="My connection is not established!">

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

<ExpandableSection title="My MCP2518FD CAN communication isn't working!">

### Check SPI connection
Ensure that the SPI interface between your microcontroller and the MCP2518FD is properly connected. Double-check the SCK, SDI, SDO, and nCS pins, and make sure they're wired to the correct pins on your microcontroller. Verify that the SPI settings (mode 0 or 1, max 20 MHz) match the MCP2518FD requirements.

### Confirm power stability
The MCP2518FD and its associated transceiver require a stable power supply. If you're experiencing inconsistent behavior (e.g., communication working only after multiple resets), add a decoupling capacitor (e.g., 470 µF) between VCC and GND close to the module to help filter voltage fluctuations.

### Check CANH and CANL behavior
Monitor CANH and CANL with an oscilloscope or logic analyzer during transmission attempts. Both lines should show differential signaling (typically 2.5 V idle, ~1.5 V–3.5 V during activity). If the voltage stays fixed or mimics SPI traffic, the transceiver may not be operating correctly, or the controller isn't initiating transmission.

### Validate termination
Ensure that the CAN bus is correctly terminated with a 120 Ω resistor at both ends of the bus. Missing or incorrect termination can cause signal reflections, noise, and failed communication.

### Review interrupt handling
The MCP2518FD uses INT, INT0, or INT1 pins to signal events to the microcontroller. Make sure your firmware is checking and clearing interrupts via SPI commands, otherwise new messages may not be processed.

### Verify CAN configuration
Ensure the MCP2518FD is properly initialized in your code. This includes setting up bit timing, mode (CAN FD or Classic), filters, and FIFO buffers. Any misconfiguration could prevent successful communication. Refer to the CiCON and FIFO control registers for proper setup.

</ExpandableSection>
<InfoBox>Still having trouble? Contact our technical support team via this form — we're here to help!</InfoBox>

