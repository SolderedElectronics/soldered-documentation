---
slug: /inkplate/4tempera/peripherals/bme688
title: Environmental sensor (BME688)
id: 4tempera-periph-bme688
hide_title: true
---

<SectionTitle title="Environmental Sensor" backgroundImage="/img/inkplate_2/hardware.png" />

The **BME688** is a high-performance environmental sensor integrated into the Inkplate 4 TEMPERA. It combines **temperature**, **humidity**, **barometric pressure**, **gas resistance**, and **altitude estimation** capabilities in one compact package. This makes it ideal for indoor air quality monitoring, weather stations, and general environmental sensing.

---

## Features

- Temperature measurement with calibration offset
- Relative humidity reading (%RH)
- Barometric pressure in hectopascals (hPa)
- Gas resistance (used to estimate air quality)
- Approximate altitude (based on pressure)
- Fully supported by the Inkplate library — no need to install external drivers

<InfoBox>The BME688 is powered using `inkplate.wakePeripheral(INKPLATE_BME688)`. Always ensure it's enabled before attempting to read values.</InfoBox>

---

## Initialization

To start using the BME688, call `wakePeripheral()` and then initialize the sensor:

```cpp
inkplate.wakePeripheral(INKPLATE_BME688);
inkplate.bme688.begin();
```

<FunctionDocumentation functionName="inkplate.wakePeripheral()" description="Powers on a peripheral device on the Inkplate board." returnDescription="None" parameters={[{ type: 'uint8_t', name: 'peripheral', description: 'Peripheral constant, e.g. INKPLATE_BME688' }]} />

<FunctionDocumentation functionName="inkplate.bme688.begin()" description="Initializes the BME688 sensor and configures it for reading." returnDescription="Returns true if the sensor is initialized successfully." />

---

## Reading Sensor Data

Once the sensor is initialized, you can read individual values:

```cpp
float temperature = inkplate.bme688.readTemperature() + offset; // °C
float humidity = inkplate.bme688.readHumidity(); // %RH
float pressure = inkplate.bme688.readPressure(); // hPa
float gas = inkplate.bme688.readGasResistance(); // mOhm
float altitude = inkplate.bme688.readAltitude(); // m
```

<FunctionDocumentation functionName="inkplate.bme688.readTemperature()" description="Reads the ambient temperature in degrees Celsius." returnDescription="Returns the temperature as a float." />

<FunctionDocumentation functionName="inkplate.bme688.readHumidity()" description="Reads the relative humidity in %RH." returnDescription="Returns the humidity as a float." />

<FunctionDocumentation functionName="inkplate.bme688.readPressure()" description="Reads barometric pressure in hectopascals (hPa)." returnDescription="Returns the pressure as a float." />

<FunctionDocumentation functionName="inkplate.bme688.readGasResistance()" description="Reads the gas resistance value in milliohms." returnDescription="Returns gas resistance as a float." />

<FunctionDocumentation functionName="inkplate.bme688.readAltitude()" description="Estimates altitude based on the current pressure reading." returnDescription="Returns altitude as a float in meters." />

---

## Displaying Data

Use standard `Inkplate` drawing functions to display sensor readings alongside icons or labels. The `partialUpdate()` method can be used to update the screen without flicker, and full refreshes can be used occasionally to maintain image quality.

```cpp
inkplate.setCursor(100, 200);
inkplate.print("Temperature: ");
inkplate.print(temperature);
inkplate.print(" C");
inkplate.partialUpdate();
```

<CenteredImage src="/img/inkplate_4_tempera/bme.png" alt="Expected output on Inkplate display" caption="Full example display" width="600px" />

---

## Full Example

<QuickLink 
  title="Inkplate4TEMPERA_BME688_Read.ino" 
  description="Full Arduino example showing how to read and display data from the onboard BME688 sensor."
  url="https://github.com/SolderedElectronics/Inkplate-Arduino-library/blob/master/examples/Inkplate4TEMPERA/Advanced/Sensors/Inkplate4TEMPERA_BME688_Read/Inkplate4TEMPERA_BME688_Read.ino" 
/>