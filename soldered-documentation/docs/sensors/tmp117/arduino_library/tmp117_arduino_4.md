---
slug: /tmp117/arduino/alert-pin
title: TMP117 Temperature Sensor – Alert Pin
sidebar_label: Alert Pin
id: tmp117-arduino-4
---

# Alert pin

This example demonstrates how to use the **TMP117’s ALR (Alert) pin** to trigger an alert when the measured temperature goes outside a specified range. When the temperature crosses the **low (20 °C)** or **high (28 °C)** threshold, the sensor pulls the alert pin low and reports the event through the Serial Monitor.

## Reading temperature with alerts

Open the Serial Monitor at **115200 baud** to view temperature readings and alert messages.

```cpp
#include "Soldered-TMP117.h"

#define ALERT_PIN               26
#define LOW_TEMPERATURE_ALERT   20
#define HIGH_TEMPERATURE_ALERT  28

bool alert_flag = false;
Soldered_TMP117 tmp;

void setup() {
  Wire.begin();
  Serial.begin(115200);

  tmp.init(new_temperature);
  tmp.setConvMode(TMP117_CMODE::CONTINUOUS);
  tmp.setConvTime(TMP117_CONVT::C15mS5);
  tmp.setAveraging(TMP117_AVE::NOAVE);
  
  tmp.setAlertMode(TMP117_PMODE::ALERT);
  tmp.setAlertCallback(temperature_alert, ALERT_PIN);
  tmp.setAlertTemperature(LOW_TEMPERATURE_ALERT, HIGH_TEMPERATURE_ALERT);
}

void loop() {
  tmp.update();

  if (alert_flag) {
    if (tmp.getAlertType() == TMP117_ALERT::HIGHALERT) {
      Serial.print("High temperature alert: ");
      Serial.print(tmp.getTemperature());
      Serial.println(" °C");
    } else if (tmp.getAlertType() == TMP117_ALERT::LOWALERT) {
      Serial.print("Low temperature alert: ");
      Serial.print(tmp.getTemperature());
      Serial.println(" °C");
    }
    alert_flag = false;
  }
  delay(100);
}

void new_temperature() {
  Serial.print("Temperature: ");
  Serial.print(tmp.getTemperature());
  Serial.println(" °C");
}

void temperature_alert() {
  alert_flag = true;
}
```

## Function reference

<FunctionDocumentation
  functionName="tmp.init(void (*newDataCallback) = nullptr)"
  description="Initializes communication with the TMP117 sensor and optionally registers a callback function that is triggered when new temperature data is available."
  returnDescription="bool, true if the sensor was successfully initialized."
/>

<FunctionDocumentation
  functionName="tmp.setConvMode(TMP117_CMODE mode)"
  description="Sets the sensor’s conversion mode. Supported modes include CONTINUOUS (continuous readings), ONESHOT (single reading), and SHUTDOWN (low-power standby)."
  returnDescription="None"
/>

<FunctionDocumentation
  functionName="tmp.setConvTime(TMP117_CONVT convTime)"
  description="Configures the time between temperature conversions. Shorter conversion times provide faster updates at the cost of higher power consumption."
  returnDescription="None"
/>

<FunctionDocumentation
  functionName="tmp.setAveraging(TMP117_AVE avg)"
  description="Sets the number of samples to average per temperature reading. Averaging can help reduce noise at the expense of speed."
  returnDescription="None"
/>

<FunctionDocumentation
  functionName="tmp.setAlertMode(TMP117_PMODE mode)"
  description="Configures the TMP117’s alert mode behavior. In ALERT mode, the ALR pin is triggered when the temperature crosses programmed thresholds; in THERM mode, it operates as a comparator output."
  returnDescription="None"
/>

<FunctionDocumentation
  functionName="tmp.setAlertCallback(void (*callback)(), int alertPin)"
  description="Registers a callback function that is executed when the alert pin changes state. The alert pin number must be specified."
  returnDescription="None"
/>

<FunctionDocumentation
  functionName="tmp.setAlertTemperature(float lowLimit, float highLimit)"
  description="Sets the low and high temperature thresholds for alert generation in degrees Celsius."
  returnDescription="None"
/>

<FunctionDocumentation
  functionName="tmp.getAlertType()"
  description="Returns the type of alert currently active — either HIGHALERT or LOWALERT — depending on which threshold was crossed."
  returnDescription="TMP117_ALERT, Enumeration value indicating alert type."
/>

<FunctionDocumentation
  functionName="tmp.update()"
  description="Updates the sensor data and checks for new readings or alert conditions. Should be called regularly in the main loop."
  returnDescription="None"
/>

<FunctionDocumentation
  functionName="tmp.getTemperature()"
  description="Reads and returns the latest measured temperature value."
  returnDescription="float, Temperature in degrees Celsius."
/>


<CenteredImage 
  src="/img/tmp117/alertconnection.jpg" 
  alt="TMP117 alert pin connection" 
  caption="Dasduino CONNECTPLUS connected to the TMP117 temperature sensor, showing the ALR pin connection for alert functionality." 
  width="800px" 

/>

<br></br>

<CenteredImage 
  src="/img/tmp117/alertoutput.png" 
  alt="TMP117 alert pin example" 
  caption="Serial Monitor showing high and low temperature alerts from the TMP117 sensor." 
  width="800px" 
/>


## Full example

<QuickLink 
  title="alertPin.ino" 
  description="Example that shows how to use the TMP117’s alert pin to detect high and low temperature events."  
  url="https://github.com/SolderedElectronics/Soldered-Temperature-Sensor-TMP117-Arduino-Library/blob/main/examples/alertPin/alertPin.ino"  
/>  