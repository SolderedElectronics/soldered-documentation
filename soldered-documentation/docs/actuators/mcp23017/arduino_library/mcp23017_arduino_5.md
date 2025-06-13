---
slug: /mcp23017/arduino/button-interrupt-example
title: Mcp23017 - Button interrupt example
sidebar_label: Button interrupt example
id: mcp23017-arduino-5
hide_title: false
---

This page contains an example for receiving an interrupt on a specific port of the board and sending it to the main board.

---

## Connections for this example

<CenteredImage src="/img/mcp23017/interrupt_connection.png" width="100%" />

---

## Initialization

First, we must include the library and create an instance of the object. We also have to create the interrupt service routine and the variable that will be modified by that function:

```cpp

#include "MCP23017-SOLDERED.h"

MCP_23017 mcp;

// is interrupted variable
volatile char state = 0;

// interrupt handler, should be as fast as possible
void interruptHandler()
{
    state = 1;
}

```

---

## Setup

In the `setup()` function, we initialize the I2C communication for the board. We also define the port on which we want to enable interrupts and the pin that will receive the interrupt on our main board:

```cpp

void setup()
{
    // Initialize MCP23017
    mcp.begin();

    // Initialize serial communication
    Serial.begin(115200);

    // Set pin 1 to input
    mcp.pinMode(GPB1, INPUT_PULLUP);

    // setup interrupts to be independent
    mcp.interruptMode(MCP23017InterruptMode::Separated); // Note no _ in the name of enum, thats because we are using
                                                         // blemasle's class enums

    // Enable interrupt on bank B (all GPB pins)
    mcp.interrupt(MCP23017Port::B, FALLING);


    // Adding interrupt to our boards inputs.
    pinMode(4, INPUT_PULLUP);

    // Set interrupt pin on our MCU board
    attachInterrupt(digitalPinToInterrupt(4), interruptHandler, FALLING);

    // Clear if mcp already interrupted
    mcp.clearInterrupts();
}

```

<FunctionDocumentation
  functionName="mcp.begin()"
  description="Initializes the I/O extender via I2C"
  returnDescription="None"
  parameters={[]}
/>

<FunctionDocumentation
  functionName="mcp.pinMode(uint8_t pin, uint8_t mode)"
  description="Controls a single pin direction"
  returnDescription="None"
  parameters={[
    { type: 'uint8_t', name: 'pin', description: "pin number" },
  { type: 'uint8_t', name: 'mode', description: "OUTPUT, INPUT or INPUT_PULLUP" },
  ]}
/>

<FunctionDocumentation
  functionName="mcp.interruptMode(MCP23017InterruptMode intMode)"
  description="Controls if the two interrupt pins mirror each other."
  returnDescription="None"
  parameters={[
    { type: 'MCP23017InterruptMode', name: 'intMode', description: "Can have two values: Separated(The ports are independent) and Or(They are mirrored)" },
  ]}
/>

<FunctionDocumentation
  functionName="mcp.interrupt(MCP23017Port port, uint8_t mode);"
  description="Configures interrupt registers using an Arduino-like API."
  returnDescription="None"
  parameters={[
    { type: 'MCP23017Port', name: 'port', description: "Defines on what port we want the interrupt to happen, can be A or B" },
    { type: 'uint8_t', name: 'mode', description: "Defines on what signal change we want the interrupt to trigger, can be CHANGE, FALLING or RISING" },
  ]}
/>

<FunctionDocumentation
  functionName="mcp.clearInterrupts()"
  description="Clears interrupts on both ports."
  returnDescription="None"
  parameters={[]}
/>

## Loop

In the `loop()` function, we are checking if an interrupt has occurred; if it has, we send a message to the serial monitor:

```cpp

void loop()
{
    if (!state)
    {
        // just to be sure that arduino and mcp are in the "same state"
        // regarding interrupts
        mcp.clearInterrupts();
        return;
    }

    if (state)
    {
        // we are in interrupt, so we can do something
        Serial.println("Interrupted!");

        // clear interrupt
        mcp.clearInterrupts();
        state = 0;
    }

    delay(100);
}

```

---

## Full example

See the full example here:

```cpp

#include "MCP23017-SOLDERED.h"

MCP_23017 mcp;

// is interrupted variable
volatile char state = 0;

// interrupt handler, should be as fast as possible
void interruptHandler()
{
    state = 1;
}

void setup()
{
    // Initialize MCP23017
    mcp.begin();

    // Initialize serial communication
    Serial.begin(115200);

    // Set pin 1 to input
    mcp.pinMode(GPB1, INPUT_PULLUP);

    // setup interrupts to be independent
    mcp.interruptMode(MCP23017InterruptMode::Separated); // Note no _ in the name of enum, thats because we are using
                                                         // blemasle's class enums

    // Enable interrupt on bank B (all GPB pins)
    mcp.interrupt(MCP23017Port::B, FALLING);


    // Adding interrupt to our boards inputs.
    pinMode(4, INPUT_PULLUP);

    // Set interrupt pin on our MCU board
    attachInterrupt(digitalPinToInterrupt(4), interruptHandler, FALLING);

    // Clear if mcp already interrupted
    mcp.clearInterrupts();
}

void loop()
{
    if (!state)
    {
        // just to be sure that arduino and mcp are in the "same state"
        // regarding interrupts
        mcp.clearInterrupts();
        return;
    }

    if (state)
    {
        // we are in interrupt, so we can do something
        Serial.println("Interrupted!");

        // clear interrupt
        mcp.clearInterrupts();
        state = 0;
    }

    delay(100);
}

```