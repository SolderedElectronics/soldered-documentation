---
slug: /relay/arduino/Qwiic-example
title: Relay - Switching the relay (Qwiic example)
sidebar_label: Switching the relay (Qwiic example)
id: relay-arduino-3
hide_title: false
pagination_next: null
---

This page contains a simple example with function documentation on how to control the 1 channel relay board using Qwiic conncetion.

## Code example for 1 channel 
```cpp
// Include our CH_Relay library
#include "Relays-SOLDERED.h"

#define RELAY_ADDRESS 0x32

CH_Relay Relay;

void setup()
{
    Relay.begin(RELAY_ADDRESS); // Set address on relay hardware switch using provided addresses and here (0x30 - 0x37)
                                // If there are more sensors/breakout boards are connected with same address,
                                // it is needed to change address in order to have normal I2C communication.
                                // Every end device should have unique address on same bus
}

void loop()
{
    // Turn on relay
    Relay.relayControl(CHANNEL1, HIGH);
    delay(1500);

    // Turn off relay
    Relay.relayControl(CHANNEL1, LOW);
    delay(1500);
}
```

<FunctionDocumentation
  functionName="CH_Relay Relay()"
   description="Creates relay object, number of channels depends on how many parameters are given to the constructor (there can be 1,2,4 arguments)"
  returnDescription="none"
/>

<FunctionDocumentation
  functionName="Relay.begin()"
  description="Initializes relay object for I2C communication"
  returnDescription="none"
  parameters={[
    { type: 'uint16_t', name: 'relay_adderss', description: "Board address for I2C communicaion" }
  ]}
/>

<FunctionDocumentation
  functionName="Relay.relayControl()"
  description="Sets specified relay in high or low state"
  returnDescription="none"
  parameters={[
    { type: 'uint16_t', name: 'channel', description: "Channel selection" },
    { type: 'uint16_t', name: 'mode', description: "Set relay in HIGH (on) or LOW (off) mode" }
  ]}
/>

---

## Full example

Try all of the above mentioned functions in this full example.

<QuickLink 
  title="RelayControl1CHEasyC.ino" 
  description="Example file to show how to control 1 channel relay board using Qwiic comunication."
  url="https://github.com/SolderedElectronics/Soldered-Relay-Arduino-Library/blob/dev/examples/EasyC/RelayControl1CHEasyC/RelayControl1CHEasyC.ino" 
/>