---
slug: /hc-sr04/arduino/examples 
title: Measuring distance and delay (examples)
id: hc-sr04-arduino-2 
hide_title: False
---

This page contains some simple examples with function documentation on how to take measurements using the HC-SR04 ultrasonic sensor.

---

## Connections for this example

<CenteredImage src="/img/hc-sr04/connection.png" alt="connection" />

---

## Initialization

To use the HC-SR04 sensor, first include the required library, create the sensor object, and initialize the sensor in the `setup()` function:
```cpp
//Include the library
#include <Ultrasonic-distance-sensor-easyC-SOLDERED.h>

//Create an instance of the sensor
Ultrasonic_Sensor hc_ultrasonic;

void setup() {
  //Start serial communication with PC via UART
  Serial.begin(115200); 
  //Initialize the sensor 
  hc_ultrasonic.begin();

}
// ...
```

<FunctionDocumentation
  functionName="hc_ultrasonic.begin()"
  description="Initializes the HC-SR04 sensor, setting up communication over I2C."
  returnDescription="None"
  parameters={[]}
/>

---

## Measuring distance

To measure the distance, first take the measurement using the `takeMeasure()` function. After a short delay (the measurement takes at most 38 ms), you can call the `getDistance()` function to obtain the distance value:

```cpp
void loop() {
  //Send command to sensor to take a measurement
  hc_ultrasonic.takeMeasure();
  
  //Measurement takes at most 38 milliseconds                             
  delay(38);  

  //Get the distance saved in the sensor's register
  int distance = hc_ultrasonic.getDistance();

  Serial.print("Distance from obstacle is: ");
  Serial.print(distance);               
  Serial.println(" cm.");  

  //Small delay between taking measurements
  delay(100);

}
```

<CenteredImage src="/img/hc-sr04/distance.png" alt="Serial monitor temperature readings" caption="Serial monitor distance measurement output" width="100%" />

<FunctionDocumentation
  functionName="hc_ultrasonic.takeMeasure()"
  description="Starts a distance measurement."
  returnDescription="Integer value, returns an error code from the Wire.h library"
  parameters={[]}
/>

<InfoBox>

Error codes that the function returns mean the following:

| **Error code**       | **Meaning**                              |
| -------------------- | -----------------------------------------|
| 0                    | Success                                  |
| 1                    | Data too long to fit in transmit buffer  |
| 2                    | Received NACK on transmit of address     |
| 3                    | Received NACK on transmit of data.       |
| 4                    | Other error.                             |
| 5                    | Timeout                                  |

</InfoBox>

<FunctionDocumentation
  functionName="hc_ultrasonic.getDistance()"
  description="Receives data and converts the binary data into a distance value in centimeters."
  returnDescription="Integer value, returns the distance from obstacle in centimeters"
  parameters={[]}
/>

---

## Measuring wave duration

To measure the duration the ultrasonic wave takes to travel back, first take the measurement using the `takeMeasure()` function. After a short delay (the measurement takes at most 38 ms), you can call the `getDuration()` function to obtain the duration value in microseconds:

```cpp
void loop() {
  //Send command to sensor to take a measurement
  hc_ultrasonic.takeMeasure();

  //Measurement takes at most 38 milliseconds                             
  delay(38);  

  //Get the duration saved in the sensor's register
  int duration = hc_ultrasonic.getDuration();

  Serial.print("Time it took the wave to return: ");
  Serial.print(duration);               
  Serial.println(" uS.");

  //Small delay between taking measurements
  delay(100);

}
```

<CenteredImage src="/img/hc-sr04/duration.png" alt="Serial monitor wave duration readings" caption="Serial monitor wave duration measurement output" width="100%" />

<FunctionDocumentation
  functionName="hc_ultrasonic.getDuration()"
  description="Receives data and converts it into the time required for the echoed sound wave to return to the sensor."
  returnDescription="Integer value, returns the time in microseconds needed for the echoed sound wave to return"
  parameters={[]}
/>

---

## Full example
Try all of the functions mentioned above in this full example, which prints out the distance and wave duration over Serial at 115200 baud:

```cpp
//Include the library
#include <Ultrasonic-distance-sensor-easyC-SOLDERED.h>

//Create an instance of the sensor
Ultrasonic_Sensor hc_ultrasonic;

void setup() {
  //Start serial communication with PC via UART
  Serial.begin(115200); 
  //Initialize the sensor 
  hc_ultrasonic.begin();

}

void loop() {
  //Send command to sensor to take a measurement
  hc_ultrasonic.takeMeasure();

  //Measurement takes at most 38 milliseconds                             
  delay(38);  

  //Get the distance saved in the sensor's register
  int distance = hc_ultrasonic.getDistance();

  Serial.print("Distance from obstacle is: ");
  Serial.print(distance);               
  Serial.println(" cm.");  

  //Get the duration saved in the sensor's register
  int duration = hc_ultrasonic.getDuration();

  Serial.print("Time it took the wave to return: ");
  Serial.print(duration);               
  Serial.println(" uS.");  

  //Small delay between taking measurements
  delay(100);
}
```
<QuickLink 
  title="getDistance_easyC.ino" 
  description="Example file for using HC-SR04 sensor with Qwiic"
  url="https://github.com/SolderedElectronics/Soldered-Ultrasonic-Sensor-easyC-Arduino-Library/blob/main/examples/getDistance_easyC/getDistance_easyC.ino" 
/>

<CenteredImage src="/img/hc-sr04/full_example.png" alt="Serial monitor Distance and duration readings" caption="Serial monitor Distance and duration readings" width="100%" />