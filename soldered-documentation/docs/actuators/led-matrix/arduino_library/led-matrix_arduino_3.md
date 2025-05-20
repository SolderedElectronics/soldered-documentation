---
slug: /relay/arduino/basic-functionality
title: Relay - Basic functionality
id: led-matrix-arduino-3
hide_title: false
---

This page contains some basic examples with function documentation on how to use LED matrix board.

---

## Controlling a specific LED
To control a specific LED on matrix, call `setPoint()` function.
```cpp
    mx.setPoint(0,0,true);
```
<FunctionDocumentation
  functionName="mx.setPoint()"
  description="Set the status of a single LED, addressed as a pixel."
  returnDescription="Returns bool value, false if parameter errors, true otherwise."
  parameters={[
  { type: 'uint16_t', name: 'r', description: "Row coordinate for the point [0..ROW_SIZE-1]." },
  { type: 'uint16_t', name: 'c', description: "Column coordinate for the point [0..getColumnCount()-1]" },
  { type: 'bool', name: 'state', description: "Sets the state of pixel." }
  ]}
/>

---

## Controlling a specific row or column
To control an entire row or column, call `setRow()` function for rows or `setColumn()` function for columns. Using `setPoint()` function in for-loop also works!
```cpp
mx.setRow(3,0xff);
mx.setColumn(5,0xff);
```
<FunctionDocumentation
  functionName="mx.setColumn()"
  description="Set all LEDs in a specific column to a new state."
  returnDescription="Returns bool value, false if parameter errors, true otherwise"
  parameters={[
  { type: 'uint8_t', name: 'c', description: "Column which is to be set [0..getColumnCount()-1]." },
  { type: 'uint8_value', name:'value', description:"Each bit set to 0xff will light up the corresponding LED." }
  ]}
/>

<FunctionDocumentation
  functionName="mx.setRow()"
  description="Set all LEDs in a specific row to a new state."
  returnDescription="Returns bool value, false if parameter errors, true otherwise"
  parameters={[
  { type: 'uint8_t', name: 'c', description: "Row which is to be set [0..getRowCount()-1]." },
  { type: 'uint8_value', name:'value', description:"Each bit set to 0xff will light up the corresponding LED." }
  ]}
/>

---

## Controlling the intensity of LEDs
To control the status of the specified parameter, for example in this code brightness, call `control()` function.

```cpp
for(int8_t i=0;i<MAX_INTENSITY;i++){
    delay(500);
    mx.control(Led_Matrix::INTENSITY, i);
}
```
<FunctionDocumentation
  functionName="mx.control()"
  description="Set the control status of the specified parameter for all devices."
  returnDescription="none"
  parameters={[
  { type: 'controlRequest_t', name: 'mode', description: "One of the defined control requests." },
  { type: 'int', name:'value', description:" Parameter value for one of the control status defined." }
  ]}
/>

---

## Full example
Try all of the above mentioned functions in this full example:
```cpp
#include "Led-Matrix-SOLDERED.h"
#include <SPI.h>

#define HARDWARE_TYPE Led_Matrix::PAROLA_HW
#define MAX_DEVICES   1
#define CLK_PIN       18 // or SCK
#define DATA_PIN      23 // or MOSI
#define CS_PIN        4 // or LOAD
Led_Matrix mx = Led_Matrix(HARDWARE_TYPE, CS_PIN, MAX_DEVICES); // SPI hardware interface


void setup() {
  mx.begin();
  
}

void loop() {
  mx.setPoint(0,0,true);
  mx.setRow(3,0xff);
  mx.setColumn(5,0xff);
  for(int8_t i=0;i<MAX_INTENSITY;i++){
    delay(500);
    mx.control(Led_Matrix::INTENSITY, i);
  }
}

```