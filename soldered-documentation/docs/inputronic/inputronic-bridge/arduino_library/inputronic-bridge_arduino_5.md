---
slug: /inputronic-bridge/arduino/troubleshooting 
title: Troubleshooting
id: inputronic-bridge-arduino-5 
hide_title: False
pagination_next: null
---
This page contains some tips in case you are having problems using this product.

<ExpandableSection title="The communication won't initialize!">

#### Check your wiring
Ensure that the Inputronic BRIDGE is correctly wired to your microcontroller:
* For **I2C**: Ensure the Qwiic (formerly easyC) cable is properly seated or SDA/SCL pins are correctly connected. 
* For **UART**: Ensure RX is connected to TX, and TX is connected to RX.
* For **SPI**: Verify MOSI, MISO, CLK, and CS pin connections.
* Verify that **GND** and **3V3** are securely connected to a stable power source.

#### Check protocol jumpers (JP3 & JP4)
The active communication protocol is determined by the onboard hardware jumpers. If you are initializing the library in SPI mode but the jumpers are left open (defaulting to I2C), the board will not respond.
* **I2C:** Leave JP3 and JP4 open.
* **UART / SPI:** Solder the respective jumpers as marked on the back of the board.

#### Verify I2C Address
If using I2C, the default address is `0x50`. Ensure your code uses `parser.configureI2c(0x50)` before calling the `begin()` function.

</ExpandableSection>

<ExpandableSection title="The board initializes, but I am not receiving any input data!">

#### Check the FAULT LED
The board features a Female USB-A connector with overcurrent protection. The maximum allowed current draw is **260mA**. If you plug in a high-power device (like a mechanical keyboard with bright RGB lighting), the protection circuit might trip. If the **FAULT LED** turns on, your USB device is drawing too much power. Try turning off the device's RGB lighting or use a simpler device.

#### Non-standard USB HID devices
The Inputronic BRIDGE automatically parses standard Keyboard, Mouse, and MIDI devices. If you plugged in a proprietary device or a specialized controller, standard event parsing might not work. In this case, use the library's raw HID polling functions to receive raw USB descriptors and raw HID reports to parse them manually.

#### Check the INT pin (if using interrupt mode)
If you are using the interrupt-driven mode instead of constant polling, verify that the **INT** pin is physically connected to your microcontroller and that you configured the correct pin in the software.

</ExpandableSection>

<ExpandableSection title="The communication bus is slow or freezing!">

#### Implement a delay or use interrupts
If you are continuously polling events in a tight loop without any delays, you might be spamming the I2C or SPI bus, causing it to lock up. Try adding a small delay (e.g., 10ms) in your main loop. 

For the most efficient setup, connect the **INT** pin to your host microcontroller and configure the library to use interrupt-driven event reading. This way, the host only requests data when the BRIDGE signals that new HID data is parsed and ready.

</ExpandableSection>
