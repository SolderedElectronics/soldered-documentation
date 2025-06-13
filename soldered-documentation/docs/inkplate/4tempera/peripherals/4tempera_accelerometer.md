---  
slug: /inkplate/4tempera/peripherals/accelerometer  
title: Inkplate 4TEMPERA – Accelerometer and gyroscope
sidebar_label: Accelerometer and gyroscope
id: 4tempera-periph-accelerometer  
hide_title: true
---

<SectionTitle title="Accelerometer and Gyroscope" backgroundImage="/img/inkplate_2/hardware.png" />

The **LSM6DS3** sensor on the Inkplate 4 TEMPERA provides **accelerometer and gyroscope data**, allowing motion detection, tilt sensing, and rotation tracking. It is used both for general movement sensing and to demonstrate 3D projections based on device tilt.

<InfoBox>The **LSM6DS3** implementation in the Inkplate library is built-in and does not require installing an external library.</InfoBox>

---

## Initialization

Before retrieving sensor data, the LSM6DS3 must be powered on and initialized:

```cpp
inkplate.wakePeripheral(INKPLATE_ACCELEROMETER);
if (inkplate.lsm6ds3.begin() != 0) {
    inkplate.println("LSM6DS3 init failed");
    inkplate.display();
    esp_deep_sleep_start();
}
```

<FunctionDocumentation
  functionName="inkplate.wakePeripheral()"
  description="Powers on a peripheral device. Required before using the LSM6DS3."
  returnDescription="None"
  parameters={[{ type: 'uint8_t', name: 'peripheral', description: 'Use INKPLATE_ACCELEROMETER to enable the LSM6DS3 sensor.' }]}
/>

<FunctionDocumentation
  functionName="inkplate.lsm6ds3.begin()"
  description="Initializes the LSM6DS3 accelerometer and gyroscope sensor."
  returnDescription="Returns 0 on success; non-zero on failure."
/>

---

## Reading Data

Once initialized, you can read accelerometer and gyroscope values directly:

### Accelerometer
```cpp
float ax = inkplate.lsm6ds3.readRawAccelX();
float ay = inkplate.lsm6ds3.readRawAccelY();
float az = inkplate.lsm6ds3.readRawAccelZ();
```
<FunctionDocumentation functionName="inkplate.lsm6ds3.readRawAccelX()" description="Reads X-axis raw accelerometer data." returnDescription="Float value representing acceleration." />
<FunctionDocumentation functionName="inkplate.lsm6ds3.readRawAccelY()" description="Reads Y-axis raw accelerometer data." returnDescription="Float value representing acceleration." />
<FunctionDocumentation functionName="inkplate.lsm6ds3.readRawAccelZ()" description="Reads Z-axis raw accelerometer data." returnDescription="Float value representing acceleration." />

### Gyroscope
```cpp
float gx = inkplate.lsm6ds3.readFloatGyroX();
float gy = inkplate.lsm6ds3.readFloatGyroY();
float gz = inkplate.lsm6ds3.readFloatGyroZ();
```
<FunctionDocumentation functionName="inkplate.lsm6ds3.readFloatGyroX()" description="Reads X-axis gyroscope angular velocity." returnDescription="Float value in degrees/second." />
<FunctionDocumentation functionName="inkplate.lsm6ds3.readFloatGyroY()" description="Reads Y-axis gyroscope angular velocity." returnDescription="Float value in degrees/second." />
<FunctionDocumentation functionName="inkplate.lsm6ds3.readFloatGyroZ()" description="Reads Z-axis gyroscope angular velocity." returnDescription="Float value in degrees/second." />

---

## 3D Projection Demo

In the official example, the LSM6DS3's accelerometer values are used to control the tilt of a **3D wireframe cube**, illustrating how orientation data can be used for interactive graphics:

- 3D cube rendered using trigonometry and vector rotation
- Accelerometer values used to rotate the cube in real time
- Gyroscope and acceleration values printed on screen
- Optimized display refresh using `partialUpdate()` and periodic full `display()` calls

<InfoBox>The 3D projection is a visualization technique that smooths motion by using the previous accelerometer value to reduce jitter and increase realism.</InfoBox>

<CenteredImage src="/img/inkplate_4_tempera/accel.png" alt="Expected output on Inkplate display" caption="Full example display" width="800px" />

<InfoBox>This sketch uses real-time accelerometer data to rotate a projected cube on the e-paper display. Each corner of the cube is rotated in 3D space and then projected onto the 2D screen. To avoid flickering, the cube is updated using `partialUpdate()` until 35 frames have passed, at which point a full `display()` refresh is performed.</InfoBox>

The projection function handles 3-axis rotation:
```cpp
void project(float *v, float angleX, float angleY, float angleZ, int *x, int *y)
```
It uses the following sequence:
- Rotate the vertex around the **X**, **Y**, and **Z** axes
- Project to 2D screen space
- Adjust projection scale and center based on display size

This approach enables smooth, interactive rendering—an ideal demo for providing visual feedback based on motion.

---

## Full Example

<QuickLink 
  title="Inkplate4TEMPERA_Accelerometer_Gyroscope_Read.ino" 
  description="Demonstrates accelerometer and gyroscope readings and 3D cube visualization."
  url="https://github.com/SolderedElectronics/Inkplate-Arduino-library/blob/master/examples/Inkplate4TEMPERA/Advanced/Sensors/Inkplate4TEMPERA_Accelerometer_Gyroscope_Read/Inkplate4TEMPERA_Accelerometer_Gyroscope_Read.ino" 
/>