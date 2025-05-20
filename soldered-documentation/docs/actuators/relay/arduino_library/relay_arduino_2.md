---
slug: /relay/arduino/regular-example
title: Relay - Switching the relay (regular example)
id: relay-arduino-2
hide_title: false
---

This page contains a simple example with function documentation on how to control the 1 or multi channel regular relay board.

## Code example for 1 channel

```cpp
// Include our CH_Relay library
#include "Relays-SOLDERED.h"

#define RELAY_PIN 5

CH_Relay Relay(RELAY_PIN); 

void setup()
{
    Relay.begin(); 
}

void loop()
{
    Relay.relayControl(CHANNEL1, HIGH);
    delay(1500);

    Relay.relayControl(CHANNEL1, LOW);
    delay(1500);
}
```

<FunctionDocumentation
  functionName="CH_Relay Relay()"
  description="Creates relay object, number of channels depends on how many parameters are given to the constructor (there can be 1,2,4 arguments)"
  returnDescription="NaN"
  parameters={[
    { type: 'uint16_t', name: 'pin1', description: "digital pin number for controlling relay on channel 1" },
    { type: 'uint16_t', name: 'pin2', description: "digital pin number for controlling relay on channel 2" },
    { type: 'uint16_t', name: 'pin3', description: "digital pin number for controlling relay on channel 3" },
    { type: 'uint16_t', name: 'pin4', description: "digital pin number for controlling relay on channel 4" }
  ]}
/>

<FunctionDocumentation
  functionName="Relay.begin()"
  description="Initializes relay library"
  returnDescription="none"
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
  title="RelayControl1CHNative.ino" 
  description="Example file to show how to control 1 channel relay board."
  url="https://github.com/SolderedElectronics/Soldered-Relay-Arduino-Library/blob/dev/examples/Native/RelayControl1CHNative/RelayControl1CHNative.ino" 
/>