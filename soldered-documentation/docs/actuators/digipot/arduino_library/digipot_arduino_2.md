---
slug: /digipot/arduino/examples
title: "Digital potentiometer \u2013 Arduino examples"
id: digipot-arduino-2
hide_title: false
---
This page contains a simple example with function documentation on how to control digital potentiometer.

---

## Initialization
To use the digital potentiometer, first include the required library, create the digipot object and initialize it in the `setup()` function. You can use the return of `begin()` to check if everything is connected correctly.

```cpp
#include "MCP4018-SOLDERED.h" //Include Soldered library for MCP4018 Digipot.

MCP4018-SOLDERED digipot; // Create object for Digipot library.

void setup() {
  digipot.begin(); // Initialize Digipot library.
}
//...
```

<FunctionDocumentation
  functionName="MCP4018-SOLDERED digipot"
  description="Creates digipot object"
  returnDescription="none"
/>

<FunctionDocumentation
  functionName="digipot.begin()"
  description="Initializes the digipot, setting up communication over I2C and verifying its presence."
  returnDescription="Returns true if initialization is successful, false otherwise."
/>

---

## Controlling wiper value
To set wiper value, call `setWhiperPercent()` function. It is possible to increment the value with `increment()` function. To get its current value, call `getWiperValue()` function.

```cpp
#include "MCP4018-SOLDERED.h" //Include Soldered library for MCP4018 Digipot.

MCP4018_SOLDERED digipot; // Create object for Digipot library.

void setup() {
  digipot.begin(); // Initialize Digipot library.
  Serial.begin(115200);
}

void loop() {
  // put your main code here, to run repeatedly:
  digipot.setWiperPercent(0);
  printDigipotData(digipot.getWiperValue());
  delay(2000);

  for(int i=0;i<128;i++){
    digipot.increment();
    printDigipotData(digipot.getWiperValue());
    delay(500);
  }
  digipot.setWiperPercent(0);
  printDigipotData(digipot.getWiperValue());
  delay(2000);

  digipot.setWiperPercent(100);
  printDigipotData(digipot.getWiperValue());
  delay(2000);

}

void printDigipotData(int _v)
{
    Serial.print("Digipot wiper: ");
    Serial.print(_v, DEC);
    Serial.println('%');
}
```

<FunctionDocumentation
  functionName="digipot.setWiperPercent()"
  description="Sets the wiper value"
  returnDescription="none"
/>

<FunctionDocumentation
  functionName="digipot.increment()"
  description="Increments the current value"
  returnDescription="none"
/>

<FunctionDocumentation
  functionName="digipot.getWiperValue()"
  description="Returns the current wiper value"
  returnDescription="Returns byte value that represents current wiper value"
/>

### Serial monitor output 
<CenteredImage src="/img/digipot/digipot_serial_monitor_output1.jpg" alt="Output from Serial Monitor" caption="Output from Serial Monitor" width="400px" />

---

## Full example

Try all of the above mentioned functions in full examples below:

<QuickLink 
  title="digipot_serial.ino" 
  description="Example file to show how to increment and decrement digipot value from Arduino Serial Monitor."
  url="https://github.com/SolderedElectronics/Soldered-Digipot-MCP4018-Arduino-Library/blob/main/examples/digipot_serial/digipot_serial.ino" 
/>
<QuickLink 
  title="get_digipot.ino" 
  description="Example file to show how to set the desired value to digipot and read thta value from it"
  url="https://github.com/SolderedElectronics/Soldered-Digipot-MCP4018-Arduino-Library/blob/main/examples/get_digipot/get_digipot.ino" 
/>
<QuickLink 
  title="set_digipot.ino" 
  description="Example file to show how to set the desired value to digipot and read thta value from it"
  url="https://github.com/SolderedElectronics/Soldered-Digipot-MCP4018-Arduino-Library/blob/main/examples/set_digipot/set_digipot.ino" 
/>