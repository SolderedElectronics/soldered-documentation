---
slug: /gpio expander pcal6416a breakout/arduino/troubleshooting
title: PCAL6416AHF - Troubleshooting
sidebar_label: Troubleshooting
id: gpio expander pcal6416a breakout-arduino-4
hide_title: False
pagination_next: null
---
This page contains some tips if you are experiencing problems with the PCAL6416A GPIO expander.

<ExpandableSection title="My expander won't initialize!">

#### Check wiring
Ensure that your Qwiic/easyC cable is properly connected and in good condition. Try using the same cable with another easyC-compatible device to verify that it works.

#### Check I2C pins
If you are connecting the board using standard I2C pins, double-check that SDA and SCL are connected to the correct pins on your microcontroller.

#### Scan for I2C devices
Run an [**I2C scanner sketch**](https://github.com/SolderedElectronics/Soldered-Hacky-Codes/tree/main/I2C_Scanner) to check if the PCAL6416A is detected on the I2C bus.

#### Check I2C address
Make sure the address used in code matches the detected address. For example:

```cpp
expander.begin(0x20);
```

</ExpandableSection>

<ExpandableSection title="My input or output pin is not working!">

#### Check pin mode
Make sure the pin is configured correctly before reading or writing:

```cpp
expander.pinModePCAL(PCAL6416A_A0, INPUT_PULLUP);
expander.pinModePCAL(PCAL6416A_A1, OUTPUT);
```

#### Check your wiring
For button examples, connect the pushbutton between the input pin and GND.  
For LED examples, connect the LED with a resistor to the output pin and GND.

#### Check pull-up settings
If using a button, enable `INPUT_PULLUP` so the input has a stable state when the button is not pressed.

</ExpandableSection>

<ExpandableSection title="Other common issues">

#### The button always reads HIGH or LOW
Check that the button is connected to the correct GPIO pin and GND. If using `INPUT_PULLUP`, the pin should read `HIGH` when released and `LOW` when pressed.

#### The LED does not turn on
Check LED polarity, the resistor connection, and whether the selected pin is configured as `OUTPUT`.

#### I2C communication is unstable
Check cable length, loose connections, and whether the I2C pull-up jumpers are configured correctly.

#### The wrong device is responding
If multiple I2C devices are connected, make sure no other device uses the same I2C address.

</ExpandableSection>

<InfoBox>In case you haven't found the answer to your question, please **contact us** via [**this**](https://soldered.com/contact/) link.</InfoBox>

