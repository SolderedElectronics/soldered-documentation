---
slug: /tcrt5000/arduino/example
title: Example usage (Arduino)
id: tcrt5000-arduino-2 
hide_title: False
---

This page contains a simple example with function documentation on how to take measurements using the TCRT5000 sensor.

## Measuring with both digital and analog output
To use this sensor, basic functions are sufficient. The output values can be interpreted in two ways. First, black objects absorb the transmitted IR radiation and reflect it poorly, so the output will be smaller for analog and LOW for digital output if a black object is in front of the sensor. However, if a shinier object is placed in front of the sensor, the output becomes larger for analog and HIGH for digital output. Second, if an object is placed further away from the sensor, the output value becomes smaller.

```cpp
#define digitalPin 14
#define analogPin 15

int dVal = 0;
int aVal = 0;
void setup() {
  // put your setup code here, to run once:
  Serial.begin(115200);
  pinMode(digitalPin, INPUT);
  pinMode(analogPin, INPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  dVal = digitalRead(digitalPin);
  aVal = analogRead(analogPin);
  Serial.print("Analog Reading= ");
  Serial.println(aVal);
  Serial.print("Digital Reading= ");
  Serial.println(dVal);
  delay(500);
}
```

### Serial Monitor output
<CenteredImage src="/img/tcrt5000/obstacle_sensor_output.jpg" alt="Output from Serial Monitor" caption="Output from Serial Monitor" width="400px" />