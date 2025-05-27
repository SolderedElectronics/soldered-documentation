---
slug: /tca9548a/arduino/troubleshooting
title: "TCA9548A I2C multiplexer \u2013 Arduino troubleshooting"
id: tca9548a-arduino-3
hide_title: false
pagination_next: null
---
This page contains some tips in case you are having problems using this product.

<ExpandableSection title="The I2C communication won't initialize!">

#### Check wiring
Ensure that the TCA9548A breakout board is correctly wired to your microcontroller:

*   **SDA/SCL** pins on the microcontroller should connect to the **SDA/SCL** pins on the multiplexer.  
*   Ensure that **GND** is connected between the microcontroller and the breakout board.  
*   Verify that **VCC** is connected to a stable power source (3.3V or 5V).
  
#### Verify Address Configuration
Check that the **A0**, **A1**, and **A2** jumpers are configured correctly to set unique addresses for each multiplexer.

#### Try Running Examples

If you're confident that your wiring and configuration are correct, try running our [Arduino Example Code](tca9548a_arduino_2.md#full-example) to test communication with sensors.

</ExpandableSection>

<ExpandableSection title="I can't access devices on specific channels!">

#### Open/Close Channels

Ensure that you are opening and closing channels correctly in your code:

*   Use I2CMux.openChannel(channel) to enable communication with devices on a specific channel.   
*   Use I2CMux.closeChannel(channel) or I2CMux.closeAll() to isolate devices on other channels.
  
### Check Device Wiring

Verify that devices connected to individual channels are properly wired:

*   **SDAx/SCLx** pins should connect to the corresponding pins on the device.
*   Ensure GND and VCC are connected properly.

</ExpandableSection>




<InfoBox>In case you haven't found the answer to your question, please **contact us** via [**this**](https://soldered.com/contact/) link.</InfoBox>