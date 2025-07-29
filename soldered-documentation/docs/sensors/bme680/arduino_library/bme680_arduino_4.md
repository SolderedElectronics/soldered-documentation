---
slug: /bme680/arduino/measuring-temperature-humidity-pressure
title: Bme680 - Measuring temperature, humidity and pressure (examples)
sidebar_label: Measuring temperature, humidity and pressure (examples)
id: bme680-arduino-4
hide_title: false
---
## All measurements

To get the values for all measurements (temperature, humidity, and pressure), use the `readSensorData()` function. The sensor retrieves the reading values, stores them in the addresses of the function arguments, and scales the values into the appropriate form.

```cpp
void loop()
{
  float temperature, humidity, pressure, gas;
  bme680.readSensorData(temperature, humidity, pressure, gas);
  Serial.println(
    "Temperature: "+String(temperature)+"C\n"+
    "Humidity: " + String(humidity) + "%\n" +
    "Pressure: " + String(pressure) + "hPa\n" +
    "Gas: " + String(gas) + "mOhms\n"
  );
  delay(1000); // 1 second delay between measurements
}
```
<CenteredImage src="/img/bme680/bme680_allvalues.png" alt="Serial monitor all readings" caption="Serial monitor" width="100%" />

<FunctionDocumentation
  functionName="bme680.readSensorData(float &temp, float &humidity, float &pressure, float &gas)"
  description="Gets the reading values, stores them in the addresses of the function arguments, and scales the values into the appropriate form."
  returnDescription="None"
  parameters={[
  { type: 'float', name: 'temp', description: "Variable in which the temperature value will be stored" },
  { type: 'float', name: 'humidity', description: "Variable in which the humidity value will be stored" },
  { type: 'float', name: 'pressure', description: "Variable in which the pressure value will be stored" },
  { type: 'float', name: 'gas', description: "Variable in which the gas value will be stored" },
  ]}
/>
---

## Temperature

To get temperature values only, use the `readTemperature()` function. The sensor samples temperature in degrees Celsius.

```cpp
void loop()
{
  float temperature;
  // Store the sensor data into the variable
  temperature = bme680.readTemperature();
  // Print the value onto the screen
  Serial.println("Temperature: "+String(temperature)+"C \n");
  delay(1000); // 1 second delay between measurements
}
```

<WarningBox>

Because the sensor by itself generates heat, a temperature offset may be needed. Make an independent temperature reading and add an offset if needed:

```cpp
void loop()
{
  float temperature;
  float offset = 2.5; // If needed, add an offset
  // Store the sensor data into the variable
  temperature = bme680.readTemperature();
  temperature += offset; // Add the offset to the temperature
  // Print the value onto the screen
  Serial.println("Temperature: "+String(temperature)+"C \n");
  delay(1000); // 1 second delay between measurements
}
```

</WarningBox>

<CenteredImage src="/img/bme680/bme680_temperature.png" alt="Serial monitor temperature readings" caption="Serial monitor" width="100%" />

<FunctionDocumentation
  functionName="bme680.readTemperature()"
  description="Reads the value from the sensor and returns the scaled Celsius value"
  returnDescription="Float value of the temperature reading in degrees Celsius"
  parameters={[]}
/>
---

## Pressure

To get pressure values only, use the `readPressure()` function. The sensor samples the pressure in hPa.

```cpp
void loop()
{
  float pressure;
  // Store the sensor data into the variable
  pressure = bme680.readPressure();
  // Print the value onto the screen
  Serial.println("Pressure: "+String(pressure)+"hPa \n");
  delay(1000); // 1 second delay between measurements
}
```
<CenteredImage src="/img/bme680/bme680_pressure.png" alt="Serial monitor pressure readings" caption="Serial monitor" width="100%" />

<FunctionDocumentation
  functionName="bme680.readPressure()"
  description="Reads the value from the sensor and returns the scaled hPa value"
  returnDescription="Float value of the pressure reading in hPa"
  parameters={[]}
/>
---

## Humidity

To get humidity values only, use the `readHumidity()` function. The sensor samples humidity as a percentage.

```cpp
void loop()
{
  float humidity;
  // Store the sensor data into the variable
  humidity = bme680.readHumidity();
  // Print the value onto the screen
  Serial.println("Humidity: "+String(humidity)+"% \n");
  delay(1000); // 1 second delay between measurements
}
```
<CenteredImage src="/img/bme680/bme680_humidity.png" alt="Serial monitor humidity readings" caption="Serial monitor" width="100%" />

<FunctionDocumentation
  functionName="bme680.readHumidity()"
  description="Reads the value from the sensor and returns the scaled percentage value"
  returnDescription="Float value of the humidity reading in %"
  parameters={[]}
/>