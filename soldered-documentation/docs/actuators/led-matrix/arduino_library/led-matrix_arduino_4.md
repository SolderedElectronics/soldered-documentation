---
slug: /led-matrix/arduino/examples
title: "LED Matrix \u2013 Arduino examples"
id: led-matrix-arduino-4
hide_title: false
---
This page contains a simple example with function documantation on how to display simple text with scrolling animation.

---

## Initialization

To use the matrix, first, include the required library, create the sensor object and initialize the sensor in the `setup()` function. You can use the return of `begin()` to check if everything is connected correctly:
```cpp
#include "Led-Matrix-SOLDERED.h"
#include <SPI.h>

// We always wait a bit between updates of the display
#define DELAYTIME 300 // in milliseconds

// Define the number of devices we have in the chain and the hardware interface
#define HARDWARE_TYPE Led_Matrix::PAROLA_HW
#define MAX_DEVICES   1
#define CLK_PIN       18 // or SCK
#define DATA_PIN      23 // or MOSI
#define CS_PIN        4 // or LOAD

// SPI hardware interface
Led_Matrix mx = Led_Matrix(HARDWARE_TYPE, CS_PIN, MAX_DEVICES);

#define CHAR_SPACING 1 // Pixels between characters

// Global message buffers shared by Serial and Scrolling functions
#define BUF_SIZE 75
char message[BUF_SIZE] = "Hello!";
bool newMessageAvailable = true;

// Read a message from serial
void readSerial(void)
{
    static uint8_t putIndex = 0;

    while (Serial.available())
    {
        message[putIndex] = (char)Serial.read();
        if ((message[putIndex] == '\n') || (putIndex >= BUF_SIZE - 3)) // End of message character or full buffer
        {
            // Put in a message separator and end the string
            message[putIndex] = '\0';
            // Restart the index for next filling spree and flag we have a message waiting
            putIndex = 0;
            newMessageAvailable = true;
        }
        else
            // Just save the next char in next location
            message[putIndex++];
    }
}

void scrollText(const char *p)
{
    uint8_t charWidth;
    uint8_t cBuf[8]; // This should be ok for all built-in fonts

    mx.clear();

    // Go through the string until the end
    while (*p != '\0')
    {
        charWidth = mx.getChar(*p++, sizeof(cBuf) / sizeof(cBuf[0]), cBuf);

        for (uint8_t i = 0; i <= charWidth; i++) // Allow space between characters
        { 
            mx.transform(Led_Matrix::TSL);
            if (i < charWidth)
                mx.setColumn(0, cBuf[i]);
            delay(DELAYTIME);
        }
    }
}


void setup()
{
    // Init matrix
    mx.begin();

    // Init serial communication
    Serial.begin(115200);
}

void loop()
{
    // Read a message from serial
    readSerial();

    // If there is a new message
    if (newMessageAvailable)
    {
        // Print it on the matrices and Serial Monitor
        scrollText(message);
        newMessageAvailable = false;
    }
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
  { type: 'uint8_value', name:'value', description:"Each bit set to 1 will light up the corresponding LED." }
  ]}
/>

---

## Full example

Try all of the above mentioned functions and more in this full example which detects presence of magnetic object.

<QuickLink 
  title="Led_Matrix_Test.ino" 
  description="Example file for using most of the functions in the library."
  url="https://github.com/SolderedElectronics/Soldered-8x8-MAX7219-LED-Matrix-Arduino-Library/blob/dev/examples/Led_Matrix_Test/Led_Matrix_Test.ino" 
/>