---
slug: /bmv080/arduino/duty-cycle
title: BMV080 Particulate Matter Sensor - Duty Cycle
id: bmv080-arduino-3
sidebar_label: Duty Cycle
hide_title: true
---

<SectionTitle title="BMV080 - Duty Cycle" backgroundImage="/img/faq.webp" />

This example demonstrates how to operate the BMV080 sensor using **duty cycling**. Instead of running continuously, the sensor is powered and triggered periodically to take a measurement, then returned to a low-power state.

Duty cycling is useful for **battery-powered devices**, as it significantly reduces power consumption while still providing regular air quality updates.

## Setup

```cpp
  // Set the sensor Duty Cycling Period (seconds)
  uint16_t duty_cycling_period = 20;

  if(bmv080.setDutyCyclingPeriod(duty_cycling_period) == true)
  {
    Serial.println("BMV080 set to 20 second duty cycle period.");
  }
  else
  {
    Serial.println("Error setting BMV080 duty cycle period.");
  }

  // Set the sensor mode to Duty Cycle mode
  if(bmv080.setMode(BMV080_MODE_DUTY_CYCLE) == true)
  {
    Serial.println("BMV080 set to Duty Cycle mode");
  }
  else
  {
    Serial.println("Error setting BMV080 mode");
  }
```

<FunctionDocumentation
  functionName="bmv080.setDutyCyclingPeriod()"
  description="Method sets how frequently the sensor takes measurements when operating in duty cycle mode"
  returnDescription="True if period was successfully set, false otherwise"
  returnType="bool"
  parameters={[
    { type: 'uint16_t', name: 'duty_cycling_period', description: 'Time between measurements in seconds' }
  ]}
/>

<FunctionDocumentation
  functionName="bmv080.setMode()"
  description="Sets the operational mode of the BMV080 sensor"
  returnDescription="True if mode was set successfully, false otherwise"
  returnType="bool"
  parameters={[
    { type: 'uint8_t', name: 'mode', description: 'The desired operational mode' }
  ]}
/>

<InfoBox>
**Two supported modes:**
- **BMV080_MODE_CONTINUOUS:** Sensor takes measurements continuously
- **BMV080_MODE_DUTY_CYCLE:** Sensor takes measurements at specified intervals
</InfoBox>

<WarningBox> **NOTE:** While using duty cycling mode hardware interrupt cannot be used as a trigger for sensor readings! </WarningBox> 

## Full code example on GitHub

<QuickLink  
  title="BMV080-DutyCycle"  
  description="Duty cycle example on GitHub repository"  
  url="https://github.com/SolderedElectronics/Soldered-BMV080-Arduino-Library/blob/main/examples/DutyCycle/DutyCycle.ino"  
/>  
