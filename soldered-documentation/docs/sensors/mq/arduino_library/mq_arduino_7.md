---
slug: /mq/arduino/debug-print
title: Debugging help example
id: mq-arduino-7
hide_title: False
---
You might want to check the raw voltage, method constants, the Rs/Ro ratio, and more. This can be achieved by using the `serialDebug()` function of the library.
When you have initialized the sensor (either Qwiic or Native), you can read the sensor measurements in the `loop()` function:

```cpp
void loop()
{
  mq131.update();      // Update data; read voltage level from sensor
  mq131.readSensor();
  /*
  Prints all values from and about the sensor, used for calibration and debugging purposes. The format is:
  |ADC_In | Equation_V_ADC | Voltage_ADC | Equation_RS  | Resistance_RS | EQ_Ratio | Ratio (RS/R0) | Equation_PPM | PPM |
  */
  mq131.serialDebug(); 
  delay(500);        // Sampling frequency
}
```

<CenteredImage src="/img/mq/debug.png" alt="Debug print on serial monitor" caption="Debug print on serial monitor" width="80%" />

<FunctionDocumentation
  functionName="mq131.serialDebug()"
  description="Prints all values from and about the sensor, used for calibration and debugging purposes"
  returnDescription="None"
  parameters={[]}
/>

## Full example

See the full example below:

<QuickLink  
  title="Debug-Print-Qwiic.ino"  
  description="Debug print function example for Qwiic MQ sensors"  
  url="https://github.com/SolderedElectronics/Soldered-MQ-Gas-Sensor-Arduino-Library/blob/main/examples/Qwiic/Debug-Print-Qwiic/Debug-Print-Qwiic.ino"  
/>

Also check out the Native version of the example:

<QuickLink  
  title="Debug-Print.ino"  
  description="Debug print function example for Native MQ sensors"  
  url="https://github.com/SolderedElectronics/Soldered-MQ-Gas-Sensor-Arduino-Library/blob/main/examples/native/Custom-Config/Custom-Config.ino"  
/>

<InfoBox>
While this example covers the MQ131, the process is practically identical for every sensor. We encourage you to check out all the examples [**here**](https://github.com/SolderedElectronics/Soldered-MQ-Gas-Sensor-Arduino-Library/tree/main/examples)
</InfoBox>