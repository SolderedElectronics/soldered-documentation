---
slug: /joystick/arduino/examples
title: Joystick - Using the module (example)
sidebar_label: Using the module (example)
id: joystick-arduino-2
hide_title: false
---

This page contains some basic examples with function documentation on how to use Joystick module.

---

## Moving X and Y axis
To read values of the potentiometers, call `analogRead()` function.
```cpp
#define X_PIN 13
#define Y_PIN 14

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

### Serial monitor output
<CenteredImage src="/img/joystick/joystick_serial_monitor_example1.jpg" alt="Output from Serial Monitor" caption="Output from Serial Monitor" width="400px" />
---

## Detecting button press
To read value from the button, call `digitalRead()` function.
```cpp
#define SW 15
int swValue=0;
void setup(){
    Serial.begin(115200);
    pinMode(SW,INPUT);
}
void loop(){
    swValue=digitalRead(SW);

    //reverse logic!
    if(swValue==0){
      Serial.println("Button pressed!");
    }
    else{
      Serial.println("Button not pressed!");
    }
    delay(200);
}
```
### Serial monitor output
<CenteredImage src="/img/joystick/joystick_serial_monitor_example2.jpg" alt="Output from Serial Monitor" caption="Output from Serial Monitor" width="400px" />
---

## Full example
Try all of the above mentioned functions in this full example which prints out the  x,y position and button state:

```cpp
#define X_PIN 13
#define Y_PIN 14
#define SW 15

int xValue=0;
int yValue=0;
int swValue=0;

void setup(){
    Serial.begin(115200);
    pinMode(SW,INPUT);
}
void loop(){
    xValue=analogRead(X_PIN);
    yValue=analogRead(Y_PIN);
    swValue=digitalRead(SW);

    //reverse logic!
    if(swValue==0){
      Serial.println("Button pressed!");
    }
    else{
      Serial.println("Button not pressed!");
    }
    Serial.print("x = ");
    Serial.print(xValue);
    Serial.print(" y = ");
    Serial.print(yValue);
    delay(200);
}
```