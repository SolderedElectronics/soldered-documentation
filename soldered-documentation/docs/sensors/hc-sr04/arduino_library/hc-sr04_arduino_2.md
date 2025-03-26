---
slug: /hc-sr04/arduino/examples 
title: Measuring distance and delay (examples)
id: hc-sr04-arduino-2 
hide_title: False
---

This page contains some simple examples with function documentation on how to take measurements using the HC-SR04 ultrasonic sensor.

---

## Initialization

To use the HC-SR04 sensor, first, include the required library, create the sensor object and initialize the sensor in the `setup()` function:
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

To measure the distance, first take tke measurement using the `takeMeasure()` function, and after a short delay (Measurement takes at most 38 ms), you can call the `getDistance()` function to get the distance value:

```cpp
void loop() {
  //Send command to sensor to take a measurement
  hc_ultrasonic.takeMeasure();
  
  //Measurement takes at most 38 miliseconds                             
  delay(38);  

  //Get distance saved in sensors register
  int distance=hc_ultrasonic.getDistance();

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
  description="Starts a distance measurement"
  returnDescription="Integer value, returns an error code from the Wire.h library"
  parameters={[]}
/>

<InfoBox>

Error codes that the function returns mean the following:

| **Error code**       | **Meaning**                              |
| -------------------- | -----------------------------------------|
| 0                    | Success                                  |
| 1                    | data too long to fit in transmit buffer  |
| 2                    | received NACK on transmit of address     |
| 3                    | received NACK on transmit of data.       |
| 4                    | other error.                             |
| 5                    | timeout                                  |

</InfoBox>

<FunctionDocumentation
  functionName="hc_ultrasonic.getDistance()"
  description="receives data and converts distance from binary code to value in centimeters."
  returnDescription="Integer value, returns distance from obstacle in centimeters"
  parameters={[]}
/>

---

## Measuring wave duration

To measure the duration the ultrasonic wave took to travel back, first take tke measurement using the `takeMeasure()` function, and after a short delay (Measurement takes at most 38 ms), you can call the `getDuration()` function to get the duration value in microseconds:

```cpp
void loop() {
  //Send command to sensor to take a measurement
  hc_ultrasonic.takeMeasure();

  //Measurement takes at most 38 miliseconds                             
  delay(38);  

  //Get duration saved in sensors register
  int duration=hc_ultrasonic.getDuration();

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
  description="Receives data and converts it to time needed for bounced sound wave to return to sensor"
  returnDescription="Integer value, returns time in microseconds needed for bounced sound wave to return"
  parameters={[]}
/>

---

## Full example
Try all of the above mentioned functions in this full example which prints out the distance and wave duration over Serial at 115200 baud:

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

  //Measurement takes at most 38 miliseconds                             
  delay(38);  

  //Get distance saved in sensors register
  int distance=hc_ultrasonic.getDistance();

  Serial.print("Distance from obstacle is: ");
  Serial.print(distance);               
  Serial.println(" cm.");  


  //Get duration saved in sensors register
  int duration=hc_ultrasonic.getDuration();

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