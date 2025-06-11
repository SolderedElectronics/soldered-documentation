---  
slug: /w5500/arduino/examples  
title: Initialization  
id: w5500-arduino-2  
hide_title: False  
---  
This page provides a simple example of how to initialize and use the W5500 module with Dasduino CONNECTPLUS.

## Initialization

To use the W5500 module with an Arduino, you need to include the appropriate libraries, define the **CS** pin, create an instance of the EthernetClient object, and initialize it within the `setup()` function.

Here's an example of how to initialize the W5500 module:

```cpp
#include <SPI.h>
#include <Ethernet.h>

#define CS_PIN 5 //Define the connected Chip Select pin

// Enter a MAC address for your controller below.
// It can be any free address in your network
byte mac[] = { 0xDE, 0xAD, 0xBE, 0xEF, 0xFE, 0xED };

EthernetClient client;

void setup(){
    Ethernet.init(CS_PIN);
}
//...
```

<FunctionDocumentation
  functionName="Ethernet.init()"
  description="Used to configure the CS (chip select) pin for the Ethernet controller chip."
  returnType="None"
  parameters={[  
    { type: 'int', name: 'sspin', description: 'The pin number to use for CS.' },
  ]}
/>