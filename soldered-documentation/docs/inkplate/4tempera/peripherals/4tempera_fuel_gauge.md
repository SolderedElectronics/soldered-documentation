---
slug: /inkplate/4tempera/peripherals/fuel-gauge
title: Inkplate 4TEMPERA – Fuel Gauge (BQ27441)
sidebar_label: Fuel Gauge (BQ27441)
id: 4tempera-periph-fuel-gauge
hide_title: true
---

<SectionTitle title="Fuel Gauge" backgroundImage="/img/inkplate_2/hardware.png" />

The **BQ2441 Fuel Gauge** is a special type of accessory for lithium batteries that very precisely measures the state of battery.  This includes: **voltage[mV], state of charge[%]** and **remaining capacity in the battery[mAh]**. It comes as an integrated sensor on Inkplate 4 TEMPERA and uses a **0x55** address for **I2C communication**.

---

## Initialization

To start using the BQ2441, call `wakePeripheral()` and then initialize the sensor:

```cpp
inkplate.wakePeripheral(INKPLATE_FUEL_GAUGE);
inkplate.battery.begin();
```

<FunctionDocumentation functionName="inkplate.wakePeripheral()" description="Powers on a peripheral device on the Inkplate board." returnDescription="None" parameters={[{ type: 'uint8_t', name: 'peripheral', description: 'Peripheral constant, e.g. INKPLATE_FUEL_GAUGE' }]} />

<FunctionDocumentation functionName="inkplate.battery.begin()" description="Initializes the BQ2441 sensor and configures it for reading." returnDescription="Returns true if the sensor is initialized successfully." />

---

## Reading Sensor Data

Once the sensor is initialized, you can read individual values:

```cpp
int soc = display.battery.soc();                   // Read state-of-charge (%)
int volts = display.battery.voltage();             // Read battery voltage (mV)
int current = display.battery.current(AVG);        // Read average current (mA)
int fullCapacity = display.battery.capacity(FULL); // Read full capacity (mAh)
int capacity = display.battery.capacity(REMAIN);   // Read remaining capacity (mAh)
int power = display.battery.power();               // Read average power draw (mW)
int health = display.battery.soh();                // Read state-of-health (%)

```

<FunctionDocumentation
  functionName="inkplate.battery.soc()"
  description="Reads and returns specified state of charge measurement."
  returnDescription="Returns integer representation of charge measurement in %."
/>

<FunctionDocumentation
  functionName="inkplate.battery.voltage()"
  description="Reads and returns the battery voltage."
  returnDescription="Returns integer representation of voltage measurement in %."
/>

<FunctionDocumentation
  functionName="inkplate.battery.current()"
  description="Reads and returns the specified current measurement."
  returnDescription="Returns integer representation of voltage measurement in %."
  parameters={[
    { type: 'current_measure', name: 'type', description: "Optional, default is AVG. Command specifying the type of measurement to be performed." },
  ]}
/>

<FunctionDocumentation
  functionName="inkplate.battery.capacity()"
  description="Reads and returns the specified current measurement."
  returnDescription="Returns integer representation of voltage measurement in %."
  parameters={[
    { type: 'capacity_measure', name: 'type', description: "Optional, default is FULL. Reads and returns the specified capacity measurement." },
  ]}
/>

<FunctionDocumentation
  functionName="inkplate.battery.power()"
  description="Reads and returns measured average power."
  returnDescription="Returns integer representation of power measurement in mAh."
/>

<FunctionDocumentation
  functionName="inkplate.battery.soh()"
  description="Reads and returns specified state of health measurement."
  returnDescription="Returns specified state of health measurement in %, or status bits."
  parameters={[
    { type: 'soh_measure', name: 'type', description: "Optional, default is PERCENT. Reads and returns the specified state of health measurement." },
  ]}
/>

---

## Displaying Data

Use standard `Inkplate` drawing functions to display sensor reading alongside icons and labels. The `partialUpdate()` method can be used to update the screen without flicke, and full refreshes can be used occasionally to maintain image quality.

```cpp
int dataFromFuelGauge[] = {soc, volts, current, fullCapacity, capacity, power, health};
for (int i = 0; i < 7; i++)
    {
        // Set the cursor position so it's printed line-by-line
        display.setCursor(30, 30 + 45 * i);
        // Print what the data is and then the number
        display.print(infoNames[i]);
        display.print(dataFromFuelGauge[i]);
    }
// Update the screen
if (numRefreshes > NUM_PARTIAL_UPDATES_BEFORE_FULL_REFRESH)
{                      // Check if you need to do full refresh or you can do partial update
    display.display(); // Do a full refresh
    numRefreshes = 0;  // Reset the counter
}
else
{
    display.partialUpdate(false, true); // Do partial update
    numRefreshes++;                     // Keep track on how many times screen has been partially updated
}
```

<CenteredImage src="/img/inkplate_4_tempera/bq27441.png" alt="Expected output on Inkplate display" caption="Full example display" width="600px" />

---

## Full Example

<QuickLink 
  title="Inkplate4TEMPERA_Fuel_Gauge.ino" 
  description="Full Arduino example showing how to read and display data from the onboard BQ27441 sensor."
  url="https://github.com/SolderedElectronics/Inkplate-Arduino-library/tree/master/examples/Inkplate4TEMPERA/Advanced/Sensors/Inkplate4TEMPERA_Fuel_Gauge" 
/>