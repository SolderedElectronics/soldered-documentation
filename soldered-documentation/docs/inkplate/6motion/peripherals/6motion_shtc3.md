---
slug: /inkplate/6motion/peripherals/shtc3
title: "Inkplate \u2013 6Motion Peripherals SHTC3"
id: 6motion-periph-shtc3
---
The **SHTC3** sensor provides accurate **temperature and humidity measurements**. It's integrated into Inkplate 6 MOTION and can be used for environmental monitoring applications. 

<CenteredImage src="/img/inkplate_6_motion/6motion_shtc3.jpg" alt="SHTC3 temperature and humidity sensor" caption="SHTC3 on the Inkplate 6 MOTION" width="600px" />

The sensor allows you to retrieve temperature readings in **Celsius or Fahrenheit**, as well as **humidity percentages**. The readings must be updated manually before retrieving values.

<InfoBox>The **SHTC3** implementation in the Inkplate library uses this library from **SparkFun**:<QuickLink 
  title="SparkFun SHTC3 Humidity and Temperature Sensor Library" 
  description="The original library which is included in the Inkplate 6 MOTION library"
  url="https://github.com/sparkfun/SparkFun_SHTC3_Arduino_Library"/></InfoBox>

---

## Initialization

Before reading temperature and humidity, the **SHTC3** sensor must be powered on and initialized.

<InfoBox>The **SHTC3** sensor must be powered on via `peripheralState`. See this page for more details: <QuickLink 
  title="Peripheral basics" 
  description="How to power peripherals on and off on Inkplate 6 MOTION"
  url="/inkplate/6motion/peripherals/introduction#powering-on" 
/></InfoBox>

```cpp
// Turn on the SHTC3 peripheral
inkplate.peripheralState(INKPLATE_PERIPHERAL_SHTC3, true);

// Initialize the sensor
inkplate.shtc3.begin();
```
<FunctionDocumentation functionName="inkplate.shtc3.begin()" description="Initializes the SHTC3 sensor and prepares it for measurement." returnDescription="Returns true if initialization was successful, false otherwise." />
---

## Measuring temperature and humidity



The sensor needs to be polled with the `update()` function and then the temperature and humidity values can be read:    

```cpp
// Update sensor values before reading
if (inkplate.shtc3.update() == SHTC3_Status_Nominal)
{
    // If the sensor update went OK...
    
    // Read and print temperature in Celsius
    float temperature = inkplate.shtc3.toDegC();
    inkplate.printf("Temperature: %.2f C", temperature);

    // Read and print humidity percentage
    float humidity = inkplate.shtc3.toPercent();
    inkplate.printf("Humidity: %.2f%%", humidity);
}
```

<FunctionDocumentation functionName="inkplate.shtc3.update()" description="Forces a sensor reading update. This must be called before retrieving temperature or humidity values." returnDescription="Returns an `SHTC3_Status_TypeDef` indicating success or failure. See below for a table of these values." />

| Status Code            | Enum Value              | Description                                                                                  |
| ---------------------- | ----------------------- | -------------------------------------------------------------------------------------------- |
| **Nominal**            | `SHTC3_Status_Nominal`  | The reading was successful, and data is valid.                                               |
| **General Error**      | `SHTC3_Status_Error`    | A generic error occurred during the update.                                                  |
| **CRC Check Failed**   | `SHTC3_Status_CRC_Fail` | The computed checksum did not match the provided value, indicating possible data corruption. |
| **Device ID Mismatch** | `SHTC3_Status_ID_Fail`  | The sensor's ID did not match the expected format for an SHTC3 device.                       |

<FunctionDocumentation functionName="inkplate.shtc3.toDegC()" description="Retrieves the latest measured temperature in degrees Celsius." returnDescription="Returns the temperature as a float in °C." />

<FunctionDocumentation functionName="inkplate.shtc3.toDegF()" description="Retrieves the latest measured temperature in degrees Fahrenheit." returnDescription="Returns the temperature as a float in °F." />

<FunctionDocumentation functionName="inkplate.shtc3.toPercent()" description="Retrieves the latest measured humidity percentage." returnDescription="Returns the humidity as a float in %." />

---

## Full example

<QuickLink 
  title="Inkplate_6_MOTION_TempSensor.ino" 
  description="Full example of reading temperature and humidity from SHTC3 and printing them out on Inkplate 6 MOTION"
  url="https://github.com/SolderedElectronics/Inkplate_Motion_Arduino_Library/blob/main/examples/Inkplate6Motion/Advanced/Sensors_Other/Inkplate_6_MOTION_TempSensor/Inkplate_6_MOTION_TempSensor.ino" 
/>