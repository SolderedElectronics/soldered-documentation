---
slug: /relay/arduino/Initialization 
title: Initialization
id: led-matrix-arduino-2
hide_title: False
---

This page contains the first steps when starting with programing the LED matrix breakout board.

---

## Initialization

To use the LED matrix board, first, include the required library, create the LED matrix object and define CLK_PIN, DATA_PIN, CS_PIN and MAX_DEVICES (it represents the number of daisychained boards, in this example, it will be 1),

```cpp
#include "Led-Matrix-SOLDERED.h"
#include <SPI.h>


#define HARDWARE_TYPE Led_Matrix::PAROLA_HW
#define MAX_DEVICES   3
#define CLK_PIN       18 // or SCK
#define DATA_PIN      23 // or MOSI
#define CS_PIN        4 // or LOAD

Led_Matrix mx = Led_Matrix(HARDWARE_TYPE, CS_PIN, MAX_DEVICES);

void setup() {
  // put your setup code here, to run once:
  mx.begin();
}

//...
```

<FunctionDocumentation
  functionName="Led_Matrix mx = Led_Matrix()"
  description="Creates matrix object"
  returnDescription="none"
  parameters={[
  { type: 'moduleType_t', name: 'mod', description: "Sets the mode in which module will be working" },
  { type: 'uint8_t', name: 'csPin', description: "Digital pin number for data communication" },
  { type: 'uint8_t', name: 'numDevices', description: "Sets the number of daisy chained modules" }
  ]}
/>