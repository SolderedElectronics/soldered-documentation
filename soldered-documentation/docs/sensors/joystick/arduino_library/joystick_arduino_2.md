---
slug: /joystick/arduino/examples 
title: Controlling the module (example)
id: joystick-arduino-2 
hide_title: False
---

This page contains some basic examples with function documentation on how to use Joystick module.

--

## Moving X and Y axis
To read values of the potentiometers, call `analogRead()` function.
```cpp
#define X_PIN 12
#define Y_PIN 13

int x_Value=0;
int y_Value=0;

void setup(){
    Serial.begin(115200);
}
void loop(){
    x_Value=analogRead(X_PIN);
    y_Value=analogRead(Y_PIN);
    Serial.print("x = ");
    Serial.println(x_Value);
    Serial.print("y = ");
    Serial.println(y_Value);
    delay(200);
}
```

<FunctionDocumentation
  functionName="analogRead()"
  description="Get ADC value for specified pin"
  returnDescription="Returns integer value that is the result of analog to digital conversion."
  parameters={[
    { type: 'uint8_t', name: 'pin', description: "Pin used for ADC." },
  ]}
/>

## Serial monitor output
---

## Detecting button press

## Serial monitor output

---

## Full example
Try all of the above mentioned functions in this full example which prints out the  x,y position and button state:

```cpp
```