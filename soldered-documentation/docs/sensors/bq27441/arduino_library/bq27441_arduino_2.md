---
slug: /bq27441/arduino/examples 
title: BQ27441 – Measuring battery information (example)
sidebar_label: Measuring battery information (example)
id: bq27441-arduino-2 
hide_title: False
---

This page contains an example with function documentation on how to get battery readings (state of charge, voltage and current).

---

## Connections for this example

<CenteredImage src="/img/bq27441/connections.png" alt="Connections"  />

---

## Initialization
To use the BQ27441 sensor, first, include the required library, create the sensor object and initialize the sensor in the `setup()` function. You can use the return of `begin()` to check if everything is connected correctly:

```cpp 
//Include the library
#include <BQ27441-G1-SOLDERED.h>

BQ27441 battery;

const unsigned int BATTERY_CAPACITY = 1200; //Put the value of your battery

void setup(){
    Serial.begin(115200);
    //Initialize sensor
    if (!battery.begin()) // begin() will return true if communication is successful
    {
        // If communication fails, print an error message and loop forever.
        Serial.println("Error: Unable to communicate with BQ27441.");
        Serial.println("  Check wiring and try again.");
        while (1)
            delay(1);
    }

}
//...
```
<FunctionDocumentation
  functionName="battery.begin()"
  description="Initializes the BQ27441 sensor, setting up communication over I2C and verifying its presence."
  returnDescription="Returns true if initialization is successful, false otherwise."
  parameters={[]}
/>

---

## Taking measurements
Before taking measurements, call `soc()˝` for state of charge, `voltage()` for battery voltage, `current()` for average current, `capacity()` to read battery capacity, `power()` for average power draw and `soh()` for state of health.

```cpp
#include <BQ27441-G1-SOLDERED.h>

BQ27441 battery;

// Set BATTERY_CAPACITY to the design capacity of your battery in mAh.
const unsigned int BATTERY_CAPACITY = 1200;

void setup()
{
    // Begin serial communication
    Serial.begin(115200);

    // Use battery.begin() to initialize the BQ27441-G1A and confirm that it's
    // connected and communicating.
    if (!battery.begin()) // begin() will return true if communication is successful
    {
        // If communication fails, print an error message and loop forever.
        Serial.println("Error: Unable to communicate with BQ27441.");
        Serial.println("  Check wiring and try again.");
        while (1)
            delay(1);
    }
    Serial.println("Connected to BQ27441!");

    // Uset battery.setCapacity(BATTERY_CAPACITY) to set the design capacity
    // of your battery.
    battery.setCapacity(BATTERY_CAPACITY);
}

void loop()
{
    // Read battery stats from the BQ27441-G1A
    unsigned int soc = battery.soc();                   // Read state-of-charge (%)
    unsigned int volts = battery.voltage();             // Read battery voltage (mV)
    int current = battery.current(AVG);                 // Read average current (mA)
    unsigned int fullCapacity = battery.capacity(FULL); // Read full capacity (mAh)
    unsigned int capacity = battery.capacity(REMAIN);   // Read remaining capacity (mAh)
    int power = battery.power();                        // Read average power draw (mW)
    int health = battery.soh();                         // Read state-of-health (%)

    // Now print out those values:
    String toPrint = String(soc) + "% | ";
    toPrint += String(volts) + " mV | ";
    toPrint += String(current) + " mA | ";
    toPrint += String(capacity) + " / ";
    toPrint += String(fullCapacity) + " mAh | ";
    toPrint += String(power) + " mW | ";
    toPrint += String(health) + "%";

    Serial.println(toPrint);

    // Wait a bit
    delay(2000);
}
```

<CenteredImage src="/img/bq27441/serial_monitor.jpg" alt="Serial Monitor output" caption="Serial monitor output" />


<FunctionDocumentation
  functionName="battery.soc()"
  description="Reads and returns specified state of charge measurement."
  returnDescription="Returns integer representation of charge measurement in %."
/>

<FunctionDocumentation
  functionName="battery.voltage()"
  description="Reads and returns the battery voltage."
  returnDescription="Returns integer representation of voltage measurement in %."
/>

<FunctionDocumentation
  functionName="battery.current()"
  description="Reads and returns the specified current measurement."
  returnDescription="Returns integer representation of voltage measurement in %."
  parameters={[
    { type: 'current_measure', name: 'type', description: "Optional, default is AVG. Command specifying the type of measurement to be performed." },
  ]}
/>

<FunctionDocumentation
  functionName="battery.capacity()"
  description="Reads and returns the specified current measurement."
  returnDescription="Returns integer representation of voltage measurement in %."
  parameters={[
    { type: 'capacity_measure', name: 'type', description: "Optional, default is FULL. Reads and returns the specified capacity measurement." },
  ]}
/>

<FunctionDocumentation
  functionName="battery.power()"
  description="Reads and returns measured average power."
  returnDescription="Returns integer representation of power measurement in mAh."
/>

<FunctionDocumentation
  functionName="battery.soh()"
  description="Reads and returns specified state of health measurement."
  returnDescription="Returns specified state of health measurement in %, or status bits."
  parameters={[
    { type: 'soh_measure', name: 'type', description: "Optional, default is PERCENT. Reads and returns the specified state of health measurement." },
  ]}
/>

---

## Full example

Try all of the above mentioned functions in this full example which prints out the measured temperature and humidity over Serial at 115200 baud:

<QuickLink 
  title="BasicBatteryReading.ino" 
  description="This example is to show how BQ27441-G1 can be used for basic battery readings."
  url="https://github.com/SolderedElectronics/Soldered-BQ27441-Battery-Fuel-Gauge-Arduino-Library/blob/main/examples/BasicBatteryReading/BasicBatteryReading.ino" 
/>