---
slug: /inputronic_bridge/arduino/polling-events 
title: Inputronic BRIDGE - Reading keyboard, mouse, and MIDI events
sidebar_label: Reading HID events
id: inputronic_bridge-arduino-2 
hide_title: False
---

This page walks through the `pollingEvents` example: initializing the `InputronicParser` library and reading keyboard, mouse, and MIDI events by polling.

---

## Connections for this example

<ErrorBox>The connection diagram for this example hasn't been generated yet! We're working on it!</ErrorBox>

Connect the BRIDGE to your microcontroller via Qwiic or the I²C header pins as shown in the Getting Started guide, then plug a USB keyboard, mouse, or MIDI device into its USB-A port.

---

## Initialization

Every sketch starts the same way: bring up the bus you're using, then call `begin()` with the matching protocol. For I²C, that means calling `Wire.begin()` with your SDA/SCL pins first.

```cpp
#include "Inputronic-BRIDGE.h"

InputronicParser parser;

void setup()
{
    Serial.begin(115200);

    Wire.begin(21, 22);
    parser.configureI2c(0x50); // I2C address (default 0x50, optional)
    if (!parser.begin(InputronicParser::PROTOCOL_I2C, Wire))
    {
        Serial.println("Could not connect to BRIDGE over I2C!");
        while (true);
    }

    Serial.println("BRIDGE connected.");
}
```

<FunctionDocumentation
  functionName="parser.configureI2c()"
  description="Sets the I2C address the library will use to talk to the BRIDGE. Only needed if the BRIDGE has been changed from its default address. Call it before begin()."
  returnDescription="None"
  parameters={[
    { type: 'uint8_t', name: 'addr', description: 'I2C address to use, defaults to 0x50' },
  ]}
/>

<FunctionDocumentation
  functionName="parser.begin()"
  description="Initializes I2C mode and pings the BRIDGE to confirm it responds. This is the I2C overload of begin(); SPI and UART have their own overloads shown further down this page."
  returnDescription="True if the BRIDGE answered the ping, false if it didn't respond within the timeout"
  parameters={[
    { type: 'CommProtocol', name: 'p', description: 'Must be PROTOCOL_I2C for this overload' },
    { type: 'TwoWire&', name: 'wire', description: 'The Wire port to use, already started with wire.begin()' },
    { type: 'bool', name: 'enableInterruptParam', description: 'Set true to enable interrupt-driven polling, defaults to false' },
    { type: 'int8_t', name: 'interruptPinParam', description: 'MCU pin wired to the BRIDGE INT output, defaults to -1 (unused)' },
    { type: 'bool', name: 'activeHigh', description: 'True fires the interrupt on a RISING edge, false on FALLING, defaults to true' },
  ]}
/>

---

## Reading keyboard, mouse, and MIDI events

Call `pollEvents()` as often as you like, in the simplest case every pass through `loop()`. It always returns immediately with the most recent data, so checking the `valid` flag on each event tells you whether there's anything new to act on.

```cpp
void loop()
{
    auto events = parser.pollEvents();

    if (events.keyboard.valid)
    {
        for (uint8_t i = 0; i < events.keyboard.keyCount; i++)
        {
            Serial.print(events.keyboard.keys[i]);
        }
        Serial.println();
    }

    if (events.mouse.valid)
        Serial.printf("Mouse X:%d Y:%d L:%d R:%d Scroll:%d\n",
                      events.mouse.x, events.mouse.y, events.mouse.btnLeft,
                      events.mouse.btnRight, events.mouse.scroll);

    if (events.midi.valid)
        Serial.printf("MIDI %02X %02X %02X\n",
                      events.midi.b1, events.midi.b2, events.midi.b3);
}
```

<FunctionDocumentation
  functionName="parser.pollEvents()"
  description="Reads and decodes whatever the BRIDGE has sent since the last call, returning it as a bundle of keyboard, mouse, MIDI, descriptor, and raw HID events. Each event has its own valid flag, so only act on the ones that are set."
  returnDescription="An EventBundle struct containing the latest KeyboardEvent, MouseEvent, MIDIEvent, DescriptorEvent, and HidRawEvent"
  parameters={[]}
/>

<InfoBox>
A `KeyboardEvent` holds up to 8 simultaneously pressed keys in its `keys[]` array with `keyCount` telling you how many are populated. A `MouseEvent` carries signed `x`/`y` deltas, a `scroll` value, and five button flags: `btnLeft`, `btnRight`, `btnMiddle`, `btnBackward`, and `btnForward`.
</InfoBox>

---

## Using UART or SPI instead

If you've bridged JP3 or JP4 to switch the BRIDGE's output protocol, initialize the library with the matching overload instead.

```cpp
// UART: call serial.begin() with your baud rate and RX/TX pins first
Serial1.begin(115200, SERIAL_8N1, 14, 15);
parser.begin(InputronicParser::PROTOCOL_UART, Serial1);

// SPI: call spi.begin() first, then pass the CS pin
SPI.begin();
parser.begin(InputronicParser::PROTOCOL_SPI, SPI, 5);
```

<FunctionDocumentation
  functionName="parser.begin()"
  description="UART overload of begin(). Pings the BRIDGE over the given serial port to confirm it responds."
  returnDescription="True if the BRIDGE answered the ping within 500 ms, false if there was no USB device attached yet or the BRIDGE isn't connected"
  parameters={[
    { type: 'CommProtocol', name: 'p', description: 'Must be PROTOCOL_UART for this overload' },
    { type: 'HardwareSerial&', name: 'serial', description: 'The serial port to use, already started with serial.begin()' },
    { type: 'bool', name: 'enableInterruptParam', description: 'Set true to enable interrupt-driven polling, defaults to false' },
    { type: 'int8_t', name: 'interruptPinParam', description: 'MCU pin wired to the BRIDGE INT output, defaults to -1 (unused)' },
    { type: 'bool', name: 'activeHigh', description: 'True fires the interrupt on a RISING edge, false on FALLING, defaults to true' },
  ]}
/>

<FunctionDocumentation
  functionName="parser.begin()"
  description="SPI overload of begin(). Pings the BRIDGE over the given SPI port and chip-select pin to confirm it responds."
  returnDescription="True if the BRIDGE answered the ping, false if it didn't respond within the timeout"
  parameters={[
    { type: 'CommProtocol', name: 'p', description: 'Must be PROTOCOL_SPI for this overload' },
    { type: 'SPIClass&', name: 'spi', description: 'The SPI port to use, already started with spi.begin()' },
    { type: 'uint8_t', name: 'spiCs', description: 'Chip-select pin driven by the library' },
    { type: 'uint32_t', name: 'spiHz', description: 'SPI clock frequency in Hz, defaults to 1000000' },
    { type: 'bool', name: 'enableInterruptParam', description: 'Set true to enable interrupt-driven polling, defaults to false' },
    { type: 'int8_t', name: 'interruptPinParam', description: 'MCU pin wired to the BRIDGE INT output, defaults to -1 (unused)' },
    { type: 'bool', name: 'activeHigh', description: 'True fires the interrupt on a RISING edge, false on FALLING, defaults to true' },
  ]}
/>

---

## Full example

<QuickLink
    title="pollingEvents"
    description="Polls the BRIDGE for keyboard, mouse, and MIDI events and prints them over Serial."
    url="https://github.com/SolderedElectronics/Soldered-Inputronic-BRIDGE-Library/tree/main/examples/pollingEvents"
/>
