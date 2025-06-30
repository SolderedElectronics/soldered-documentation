---
slug: /capacitive-soil-sensor/how-to-use
title: Capacitive Soil Sensor - How to Use
sidebar_label: How to use
id: capacitive-soil-sensor-how-to-use
hide_title: false
pagination_next: null
---

This page provides basic usage instructions for the **Capacitive Soil Sensor**, including how to connect it to your microcontroller (e.g., Dasduino Connect Plus), and how to write a simple sketch to start reading soil moisture levels.

---

## How to Connect

The sensor has three pins:

| Pin  | Function        | Description                                                  |
|------|-----------------|--------------------------------------------------------------|
| VCC  | Power            | Connect to 3.3V or 5V on your board.                        |
| GND  | Ground           | Connect to the ground of your board.                        |
| AOUT | Analog Output    | Connect to an analog-capable GPIO pin on your board.        |

<InfoBox>
Always use a pin capable of analog input (ADC). On ESP32-based boards like Dasduino Connect Plus, we recommend using GPIO 32 or 33.
</InfoBox>

---

## Recommended Pins for ESP32

Use **ADC1** channels to avoid Wi-Fi interference. Below are the safe pins for analog input:

| GPIO | ADC Channel | Notes                  |
|------|-------------|------------------------|
| 32   | ADC1_CH4    | Recommended         |
| 33   | ADC1_CH5    | Recommended         |
| 34   | ADC1_CH6    | Input only (safe)      |
| 35   | ADC1_CH7    | Input only (safe)      |
| 36   | ADC1_CH0    | Input only (safe)      |
| 39   | ADC1_CH3    | Input only (safe)      |

<WarningBox>
Avoid using ADC2 pins when Wi-Fi is active, as it causes conflicts and unreliable readings.
</WarningBox>

---

## Example Code

Here’s a simple sketch to read analog soil data using a safe ADC1 pin:

```cpp
const int sensorPin = 33; // Use a safe ADC1 pin like GPIO 32 or 33

void setup() {
  Serial.begin(115200);
}

void loop() {
  int sensorValue = analogRead(sensorPin);
  Serial.print("Soil Moisture Reading: ");
  Serial.println(sensorValue);
  delay(1000);
}
```

<FunctionDocumentation
  functionName="analogRead(pin)"
  description="Reads the analog voltage on the specified pin and returns a value from 0 to 4095 on ESP32 boards."
  returnDescription="Returns an integer analog value between 0 (dry) and 4095 (wet)."
  parameters={[
    { type: 'int', name: 'pin', description: "The GPIO number connected to the sensor’s analog output." }
  ]}
/>

---

## Calibration Tip

You may wish to record the minimum and maximum values observed for your specific soil and water conditions, and map them into a percentage:

```cpp
int value = analogRead(sensorPin);
int percentage = map(value, 1200, 3200, 0, 100); // Adjust based on your readings
percentage = constrain(percentage, 0, 100);
Serial.print("Soil Moisture: ");
Serial.print(percentage);
Serial.println("%");
```

---

## Next Steps

- Try logging the data to an SD card or over Wi-Fi.
- Create alerts or automatic watering based on moisture thresholds.
- Integrate the sensor into a full smart gardening project!
