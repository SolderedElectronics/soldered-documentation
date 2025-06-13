---
slug: /mq/arduino/measuring-gas
title: MQ Gas Sensors – Measuring gas
sidebar_label: Measuring gas
id: mq-arduino-5 
hide_title: False
---

When you have initialized the sensor (either Qwiic or Native), we can read the sensor measurements in the `loop()` function:

```cpp
void loop()
{
  mq131.update();      // Update data, read voltage level from sensor
  Serial.println("O3: " + String(mq131.readSensor())+"ppb"); // Print the readings to the serial monitor
  delay(500);        // Sampling frequency
}
```

<CenteredImage src="/img/mq/reading.png" alt="Sensor reading on serial monitor" caption="Sensor reading on serial monitor" width="80%" />

<FunctionDocumentation
  functionName="mq131.update()"
  description="Updates the data and reads the sensor's voltage"
  returnDescription="None"
  parameters={[]}
/>

<FunctionDocumentation
  functionName="mq131.readSensor()"
  description="Calculates gas concentration via the regression method and returns it"
  returnDescription="Float value, gas concentration in ppm, ppb or mg/L, depending on the sensor"
  parameters={[]}
/>

## Full example

<QuickLink  
  title="MQ-131-Qwiic.ino"  
  description="Gas measurement example for the Qwiic version of MQ131 sensor"  
  url="https://github.com/SolderedElectronics/Soldered-MQ-Gas-Sensor-Arduino-Library/blob/main/examples/Qwiic/MQ-131-Qwiic/MQ-131-Qwiic.ino"  
/>

<InfoBox>
While this example covered the MQ131, the process is practically identical for every sensor, Qwiic and Native. We encourage you to check out all the examples [**here**](https://github.com/SolderedElectronics/Soldered-MQ-Gas-Sensor-Arduino-Library/tree/main/examples)
</InfoBox>