---
slug: /tmp117/arduino/troubleshooting 
title: Troubleshooting
id: tmp117-arduino-5
hide_title: true
pagination_next: null
---

# Troubleshooting

This page lists common issues and quick checks when using the **TMP117 High-Accuracy Temperature Sensor**.

<ExpandableSection title="Sensor not detected on I²C bus">

- Make sure wiring is correct:  
  - **3V3 / VCC → 3.3 V** (or 5 V if using onboard regulator)  
  - **GND → GND**  
  - **SDA → SDA (e.g., IO21 on ESP32)**  
  - **SCL → SCL (e.g., IO22 on ESP32)**  
  - **ALERT → optional (any GPIO if used)**  

- Default I²C address is **0x49**.  
  Depending on **ADD0 connection**, addresses can be:  
  - **0x48** – ADD0 → GND  
  - **0x49** – ADD0 → VCC (default)  
  - **0x4A** – ADD0 → SDA  
  - **0x4B** – ADD0 → SCL  

- Run an **I²C scanner sketch** to confirm the device appears on the bus.  
- Verify pull-up resistors (~10 kΩ) are present on **SDA**, **SCL**, and **ALERT** (they are included on the breakout).  

</ExpandableSection>

<ExpandableSection title="Readings show -256 °C or 0 °C">

- This usually means the sensor **did not respond** or the I²C transaction failed.  
- Ensure correct wiring and that the sensor has stable power (1.7–5.5 V).  
- If using multiple sensors, check that **each has a unique address**.  
- Confirm your code calls `tmp.init()` before attempting to read.  

</ExpandableSection>

<ExpandableSection title="Temperature reading seems wrong or unstable">

- Allow the sensor to **thermally stabilize** after power-up (~1 s).  
- Avoid touching the sensor during measurement — body heat can cause drift.  
- Verify averaging mode: use `tmp.setAveraging(TMP117_AVE::AVE8)` for smoother results.  
- Ensure no strong heat sources (voltage regulators, Wi-Fi chips) are close to the sensor.  
- If readings are offset by a fixed amount, use `tmp.setOffsetTemperature(x)` for calibration.  
- Typical conversion time is **15.5 ms** per measurement (one-shot mode).  
- Continuous mode defaults to **1 Hz sampling** with optional averaging.  

</ExpandableSection>

<ExpandableSection title="ALERT pin never triggers">

- The ALERT pin is **open-drain** and needs an external or onboard **pull-up resistor** (~10 kΩ).  
- By default, ALERT is **active low**, but it can be inverted via the **POL bit** in the configuration register.  
- Make sure alert thresholds are configured:  
  ```cpp
  tmp.setHighLimit(28.0);
  tmp.setLowLimit(20.0);
  tmp.enableAlertMode();
  ```
- Confirm the correct alert mode (therm or data ready) is selected.  

</ExpandableSection>

<ExpandableSection title="EEPROM read returns 0 or garbage values">

- EEPROM access requires the sensor to be **idle** (not converting).  
  Use `tmp.setConvMode(TMP117_CMODE::SHUTDOWN)` before reading EEPROM.  
- EEPROM writes require about **7 ms** per write cycle. Avoid power-off or I²C activity during that period.  
- Confirm correct register address if reading manually over I²C.  
- Avoid powering off the board while writing to EEPROM — incomplete writes may corrupt data.  

</ExpandableSection>

<ExpandableSection title="Sensor freezes or Arduino resets">

- Ensure solid I²C connections — intermittent SDA/SCL can cause bus lockups.  
- Avoid long jumper wires (>30 cm) without proper pull-ups.  
- If using 5 V logic (e.g., Arduino Uno), make sure to use a **level shifter** if the sensor runs at 3.3 V.  
- Power the sensor from a **stable 3.3 V regulator**; brownouts can reset communication.  

</ExpandableSection>

<ExpandableSection title="No output in Serial Monitor">

- Check that the **Serial Monitor baud rate is set to 115200**.  
- Make sure `Serial.begin(115200)` is called before printing.  
- Upload the sketch again — sometimes the board needs a full reset after connecting peripherals.  

</ExpandableSection>
