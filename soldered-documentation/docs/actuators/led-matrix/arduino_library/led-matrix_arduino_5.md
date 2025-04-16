---
slug: /led-matrix/arduino/displaying-animation 
title: Displaying animation (Pacman example)
id: led-matrix-arduino-5
hide_title: False
---

This page contains a simple example with function documentation on how to display simple animation.

---

## Initialization

To use the matrix, first, include the required library, create the sensor object and initialize the sensor in the `setup()` function. You can use the return of `begin()` to check if everything is connected correctly:

```cpp

#include "Led-Matrix-SOLDERED.h"
#include <SPI.h>


#define HARDWARE_TYPE Led_Matrix::PAROLA_HW
#define MAX_DEVICES   3
#define CLK_PIN       18 // or SCK
#define DATA_PIN      23 // or MOSI
#define CS_PIN        4 // or LOAD

Led_Matrix mx = Led_Matrix(HARDWARE_TYPE, CS_PIN, MAX_DEVICES); // SPI hardware interface

// --------------------
// Constant parameters
//
#define ANIMATION_DELAY 75 // Milliseconds
#define MAX_FRAMES      4  // Number of animation frames

// ========== General Variables ===========
//
const uint8_t pacman[MAX_FRAMES][18] = // Pacman pursued by a ghost
    {
        {0xfe, 0x73, 0xfb, 0x7f, 0xf3, 0x7b, 0xfe, 0x00, 0x00, 0x00, 0x3c, 0x7e, 0x7e, 0xff, 0xe7, 0xc3, 0x81, 0x00},
        {0xfe, 0x7b, 0xf3, 0x7f, 0xfb, 0x73, 0xfe, 0x00, 0x00, 0x00, 0x3c, 0x7e, 0xff, 0xff, 0xe7, 0xe7, 0x42, 0x00},
        {0xfe, 0x73, 0xfb, 0x7f, 0xf3, 0x7b, 0xfe, 0x00, 0x00, 0x00, 0x3c, 0x7e, 0xff, 0xff, 0xff, 0xe7, 0x66, 0x24},
        {0xfe, 0x7b, 0xf3, 0x7f, 0xf3, 0x7b, 0xfe, 0x00, 0x00, 0x00, 0x3c, 0x7e, 0xff, 0xff, 0xff, 0xff, 0x7e, 0x3c},
};
const uint8_t DATA_WIDTH = (sizeof(pacman[0]) / sizeof(pacman[0][0]));

uint32_t prevTimeAnim = 0; // Remember the millis() value in animations
int16_t idx;               // Display index (column)
uint8_t frame;             // Current animation frame
uint8_t deltaFrame;        // The animation frame offset for the next frame

// ========== Control routines ===========
//
void resetMatrix(void)
{
    mx.control(Led_Matrix::INTENSITY, MAX_INTENSITY / 2);
    mx.control(Led_Matrix::UPDATE, Led_Matrix::ON);
    mx.clear();
}

void setup()
{
    mx.begin(); // Init matrix
    resetMatrix();
    prevTimeAnim = millis(); // Remember the last animation time

    // Init serial communication if it's needed

}

void loop(void)
{
    static boolean bInit = true; // Initialise the animation

    // Is it time to animate?
    if (millis() - prevTimeAnim < ANIMATION_DELAY)
        return;
    prevTimeAnim = millis(); // Starting point for next time

    mx.control(Led_Matrix::UPDATE, Led_Matrix::OFF);

    // Initialize
    if (bInit)
    {
        mx.clear();
        idx = -DATA_WIDTH;
        frame = 0;
        deltaFrame = 1;
        bInit = false;

        // Lay out the dots
        for (uint8_t i = 0; i < MAX_DEVICES; i++)
        {
            mx.setPoint(3, (i * COL_SIZE) + 3, true);
            mx.setPoint(4, (i * COL_SIZE) + 3, true);
            mx.setPoint(3, (i * COL_SIZE) + 4, true);
            mx.setPoint(4, (i * COL_SIZE) + 4, true);
        }
    }

    // Clear old graphic
    for (uint8_t i = 0; i < DATA_WIDTH; i++)
        mx.setColumn(idx - DATA_WIDTH + i, 0);
    // Move reference column and draw new graphic
    idx++;
    for (uint8_t i = 0; i < DATA_WIDTH; i++)
        mx.setColumn(idx - DATA_WIDTH + i, pacman[frame][i]);

    // Advance the animation frame
    frame += deltaFrame;
    if (frame == 0 || frame == MAX_FRAMES - 1)
        deltaFrame = -deltaFrame;

    // Check if we are completed and set initialise for next time around
    bInit = (idx == mx.getColumnCount() + DATA_WIDTH);

    mx.control(Led_Matrix::UPDATE, Led_Matrix::ON);

    return;
}
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

<FunctionDocumentation
  functionName="mx.control()"
  description="Set the control status of the specified parameter for all devices."
  returnDescription="none"
  parameters={[
  { type: 'ControlRequest_t', name: 'mode', description: "One of the defined control requests." },
  { type: 'uint8_t', name: 'csPin', description: "Digital pin number for data communication" },
  { type: 'int', name: 'values', description: "Parameter value or one of the control status defined." }
  ]}
/>

<FunctionDocumentation
  functionName="mx.clear()"
  description="Clears the buffer and all dislay data on the devices"
  returnDescription="none"
/>

<FunctionDocumentation
  functionName="mx.begin()"
  description="Initialize the object."
  returnDescription="none"
/>

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

<FunctionDocumentation
  functionName="mx.getChar()"
  description="Load a character from the font data into a user buffer."
  returnDescription="Width (in columns) of the character, 0 if parameter error"
  parameters={[
  { type: 'uint16_t', name: 'c', description: "The character to retrieve." },
  { type: 'uint8_t', name: 'size', description: "The size of the user buffer in unit8_t units" },
  { type: 'uint8_t', name: '*buf*', description: "Address of the user buffer supplied" }
  ]}
/>

<FunctionDocumentation
  functionName="mx.transform()"
  description="Apply a transformation to the data in contiguous subset of devices."
  returnDescription="Returns bool value, fales if parameter errors, true otherwise"
  parameters={[
  { type: 'transformType_t', name: 'ttype', description: "The character to retrieve." }
  ]}
/>

<FunctionDocumentation
  functionName="mx.setColumn()"
  description="Set all LEDs in a specific column to a new state."
  returnDescription="Returns bool value, fales if parameter errors, true otherwise"
  parameters={[
  { type: 'uint8_t', name: 'c', description: "Column which is to be set [0..getColumnCount()-1]." },
  { type: 'uint8_value', name:'vale', description:"Each bit set to 1 will light up the corresponding LED." }
  ]}
/>

<FunctionDocumentation
  functionName="mx.getColumnCount()"
  description="Gets the maximum number of columns for devices attached to this class instance."
  returnDescription="Returns uint16_t representing the number of columns."
/>

---

## Full example
Try all of the above mentioned functions and more in this full example which detects presence of magnetic object.

<QuickLink 
  title="Led_Matrix_Pacman.ino" 
  description="Example file for using the library to display a Pacman animation."
  url="https://github.com/SolderedElectronics/Soldered-8x8-MAX7219-LED-Matrix-Arduino-Library/blob/main/examples/Led_Matrix_Pacman/Led_Matrix_Pacman.ino" 
/>