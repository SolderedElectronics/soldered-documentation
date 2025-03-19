---
slug: /bme680/arduino/measuring-altitude-and-gas
title: Measuring Altitude and Gas Resistance
id: bme680-arduino-2 
hide_title: False
---

## Altitude
### Based on sensor reading
The altitude value can be calculated by using the `readAltitude()` function, The value is calculated by the pressure value and sea level

```cpp
void loop()
{
  float altitude;
  //Store the sensor data into the variable
  altitude=bme680.readAltitude();
  //Print the value onto the screen
  Serial.println("Altitude: "+String(altitude)+"m \n");
  delay(1000); //1 second delay between mesurements
}
```
<CenteredImage src="/img/bme680/bme680_altitude.png" alt="Serial monitor humidity readings" caption="Serial monitor" width="100%" />

<FunctionDocumentation
  functionName="bme680.readAltitude()"
  description="Calculates the altitude by taking the pressure reading"
  returnDescription="Float value of altitude in meters"
  parameters={[]}
/>

---

### Based on given pressure value

```cpp
void loop()
{
  float altitude, pressure;
  //First get a pressure reading
  pressure=bme680.readPressure();
  //Store the calculated result into the variable
  altitude=bme680.calculateAltitude(pressure);
  //Print the value onto the screen
  Serial.println("Altitude: "+String(altitude)+"m \n");
  delay(1000); //1 second delay between mesurements
}
```

<FunctionDocumentation
  functionName="bme680.calculateAltitude(float pressure)"
  description="Calculates the altitude by the given pressure value in the argument"
  returnDescription="Float value in altitude in meters"
  parameters={[
  { type: 'float', name: 'pressure', description: "Pressure value in hPa" },
  ]}
/>

---

## Gas Resistance

The get gas resistance readings, use the `readGasResistance` function, The sensor samples it in mOhms.

```cpp
void loop()
{
  float gas;
  //Store the sensor data into the variable
  gas=bme680.readGasResistance();
  //Print the value onto the screen
  Serial.println("Gas Resistance: "+String(gas)+"mOhm \n");
  delay(1000); //1 second delay between mesurements
}
```

<CenteredImage src="/img/bme680/bme680_gas.png" alt="Serial monitor pressure readings" caption="Serial monitor" width="100%" />

<FunctionDocumentation
  functionName="bme680.readGasResistance()"
  description="Reads the value from the sensor and returns the scaled mOhm value"
  returnDescription="Float value of the gas resistance in mOhms"
  parameters={[]}
/>