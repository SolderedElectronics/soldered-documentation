---
slug: /relay/arduino/regular-example 
title: Switching the relay (regular example)
id: relay-arduino-2 
hide_title: False
---

This page contains a simple example with function documentation on how to control a one- or multi-channel regular relay board.

## Code example for 2 channel

```cpp
// Include our CH_Relay library
#include "Relays-SOLDERED.h"

#define RElAY_PIN1 4
#define RELAY_PIN2 5

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
  description="Creates relay object, number of channels depends on how many parameters are given to the constructor (there can be 1, 2, or 4 arguments)"
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
  description="Initializes the relay library"
  returnDescription="none"
/>

<FunctionDocumentation
  functionName="Relay.relayControl()"
  description="Sets the specified relay to a high or low state"
  returnDescription="none"
  parameters={[
    { type: 'uint16_t', name: 'channel', description: "Channel selection" },
    { type: 'uint16_t', name: 'mode', description: "Sets the relay to HIGH (on) or LOW (off) mode" }
  ]}
/>

<CenteredImage src="/img/relay/relay_working.gif" alt="Channel 2 on relay board working" caption="Channel 2 on relay board working" width="700px" />

---

## Full example

Try all of the above mentioned functions in this full example.

<QuickLink 
  title="RelayControl1CHNative.ino" 
  description="Example file to show how to control 1 channel relay board."
  url="https://github.com/SolderedElectronics/Soldered-Relay-Arduino-Library/blob/dev/examples/Native/RelayControl1CHNative/RelayControl1CHNative.ino" 
/>