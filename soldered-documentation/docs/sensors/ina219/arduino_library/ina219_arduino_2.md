---
slug: /ina219/arduino/examples 
title: INA219 - Taking measurements
sidebar_label: Taking measurements
id: ina219-arduino-2 
hide_title: False
---

This page contains a simple example of taking measurements with the INA219 sensor.

---

## Connections for this example

<CenteredImage src="/img/ina219/connections.jpg" alt="Connections"  />

---

## Initialization

To measure with the INA219 sensor, first include the required library and create the sensor object:

```cpp
//Include the library
#include "INA219-SOLDERED.h"

//Create an instance of the INA219 object
INA219 ina;
```

Next, in the `setup()` function, we have to initialize and configure the sensor:

```cpp
void setup()
{
    Serial.begin(115200);

    Serial.println("Initialize INA219");
    Serial.println("-----------------------------------------------");

    // Default INA219 address is 0x40
    ina.begin();

    // Configure INA219
    ina.configure(INA219_RANGE_32V, INA219_GAIN_320MV, INA219_BUS_RES_12BIT, INA219_SHUNT_RES_12BIT_1S);

    // Calibrate INA219. Rshunt = 0.1 ohm, Max expected current = 2A
    ina.calibrate(0.1, 2);

    Serial.println("-----------------------------------------------");
}
```

<FunctionDocumentation
  functionName="ina.begin(uint8_t address)"
  description="Initializes the INA219 sensor, setting up communication over I2C"
  returnDescription="Boolean value, true for successful I2C communication, false for error"
  parameters={[
  { type: 'uint8_t', name: 'address', description: "Optional, sets the I2C address of the INA219 sensor, if none is given then 0x40 is assigned" },
  ]}
/>

<FunctionDocumentation
  functionName="ina.configure(ina219_range_t range, ina219_gain_t gain, ina219_busRes_t busRes, ina219_shuntRes_t shuntRes, ina219_mode_t mode)"
  description="Initializes the INA219 sensor, setting up communication over I2C"
  returnDescription="Boolean value, true if successful, false for error"
  parameters={[
  { type: 'ina219_range_t', name: 'range', description: "Optional, sets the expected maximum voltage range, if none is given then 32V is assigned" },
  { type: 'ina219_gain_t', name: 'gain', description: "Optional, sets the gain of the sensor, if none is given then 320mV is assigned" },
  { type: 'ina219_busRes_t', name: 'busRes', description: "Optional, sets the bus resolution of the sensor, if none is given then 12-bit is assigned" },
  { type: 'ina219_shuntRes_t', name: 'shuntRes', description: "Optional, sets the shunt resolution of the sensor, if none is given then 12-bit is assigned" },
  { type: 'ina219_mode_t', name: 'mode', description: "Optional, sets the work mode of the sensor, if none is given then INA219_MODE_SHUNT_BUS_CONT is assigned" },
  ]}
/>

<FunctionDocumentation
  functionName="ina.calibrate(float rShuntValue, float iMaxExpected)"
  description="Configures the shunt resistor value in ohms and the max expected current"
  returnDescription="Boolean value, true if successful, false if not"
  parameters={[
  { type: 'float', name: 'rShuntValue', description: "Optional, sets the value of the shunt resistor in ohms, if none is given then 0.1 is assigned" },
  { type: 'float', name: 'iMaxExpected', description: "Optional, sets the value of the max expected current in Amps, if none is given then 2 is assigned" },
  ]}
/>

---

## Taking measurements

In the `loop()` function, we take measurements of the bus voltage, power, shunt voltage, and shunt current:

```cpp
void loop()
{
    Serial.print("Bus voltage:   ");
    Serial.print(ina.readBusVoltage(), 5);  //Read bus voltage
    Serial.println(" V");

    Serial.print("Bus power:     ");
    Serial.print(ina.readBusPower(), 5);  //Read bus power
    Serial.println(" W");


    Serial.print("Shunt voltage: ");
    Serial.print(ina.readShuntVoltage(), 5);  //Read shunt voltage
    Serial.println(" V");

    Serial.print("Shunt current: ");
    Serial.print(ina.readShuntCurrent(), 5);  //Read shunt current
    Serial.println(" A");

    Serial.println("");
    delay(1000);
}
```

<CenteredImage src="/img/ina219/readings.png" alt="Serial monitor sensor readings" caption="Serial monitor" width="100%" />

<FunctionDocumentation
  functionName="ina.readBusVoltage()"
  description="Reads the current voltage on the bus"
  returnDescription="Float value, voltage in Volts"
  parameters={[]}
/>

<FunctionDocumentation
  functionName="ina.readBusPower()"
  description="Reads the current power on the bus"
  returnDescription="Float value, power in Watts"
  parameters={[]}
/>

<FunctionDocumentation
  functionName="ina.readShuntVoltage()"
  description="Reads the current shunt voltage"
  returnDescription="Float value, voltage in Volts"
  parameters={[]}
/>

<FunctionDocumentation
  functionName="ina.readShuntCurrent()"
  description="Reads the shunt current"
  returnDescription="Float value, current in amperes"
  parameters={[]}
/>

---

## Full example

You can find the full sketch below:

<QuickLink  
  title="INA219-Simple.ino"  
  description="An example of taking simple measurements with the INA219 sensor"  
  url="https://github.com/SolderedElectronics/Soldered-INA219-Current-Sensor-Arduino-Library/blob/main/examples/INA219-Simple/INA219-Simple.ino"  
/>