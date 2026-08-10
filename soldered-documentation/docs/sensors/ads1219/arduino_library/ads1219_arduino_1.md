---
slug: /ads1219/arduino/getting-started 
title: ADS1219 24-bit ADC - Getting started
sidebar_label: Getting started
id: ads1219-arduino-1 
hide_title: False
---

## Arduino library

To install the Arduino library, use the **Arduino library manager** or download it from the GitHub repository:

<QuickLink  
  title="ADS1219 24-bit ADC Arduino library"  
  description="ADS1219 24-bit ADC Arduino library by Soldered"  
  url="https://github.com/SolderedElectronics/Soldered-ADS1219-Arduino-Library/tree/main"  
/>

<InfoBox>

**First time Arduino user?** For a detailed tutorial on getting started with Arduino, see this section of our docs:

<QuickLink  
  title="Getting started with Arduino"  
  description="A full, comprehensive tutorial on how to fully set up and upload code for the first time on an Arduino board, from scratch!"  
  url="/arduino/quick-start-guide"  
/>

</InfoBox>

---

## Connections

Below is an example connection diagram for **NULA Deepsleep**. These pins will be used in the examples throughout this documentation.

If your board has a Qwiic connector, connect it directly to the ADS1219 board with a Qwiic cable:

| **NULA Deepsleep** | **ADS1219 Board** |
| ------------------- | ------------------ |
| Qwiic                | Qwiic               |

<InfoBox>

If you prefer, you can use I2C pins to manually connect:

| **NULA Deepsleep** | **ADS1219 Board** |
| ------------------- | ------------------ |
| IO8 (Default SDA pin) | SDA                 |
| IO9 (Default SCL pin) | SCL                 |
| VCC                   | VCC                 |
| GND                   | GND                 |

</InfoBox>

---

## Using a custom I2C address

All the examples in this documentation assume the default address (**0x40**). If you've configured the [**address jumpers**](/ads1219/hardware#address-selection) for a different address, pass it into the constructor instead of using the default one:

```cpp
#include <Wire.h>
#include "ADS1219-SOLDERED.h"

// Replace 0x44 with whichever address your jumpers are set to
ADS1219_Soldered adc(0x44);
```

<FunctionDocumentation
  functionName="ADS1219_Soldered()"
  description="Constructs the ADC object for a given I2C address and Wire instance."
  returnDescription="None (constructor)."
  parameters={[
  { type: 'uint8_t', name: 'addr', description: "I2C address to use, matching your A0/A1 jumper configuration. Defaults to 0x40 if not given." },
  { type: 'TwoWire &', name: 'wire', description: "Optional. The Wire instance to use, for boards with multiple I2C buses. Defaults to Wire." },
  ]}
/>

<InfoBox>This is most useful when running **multiple ADS1219 boards on the same I2C bus**, each one needs its own object constructed with its own address.</InfoBox>
