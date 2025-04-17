---
slug: /inkplate/6motion/peripherals/accelerometer
title: Accelerometer and gyroscope
id: 6motion-periph-accelerometer
---

The **LSM6DSO32** sensor on Inkplate 6 MOTION provides **accelerometer and gyroscope data**, allowing motion detection, tilt sensing, and rotation tracking.

<InfoBox>The **LSM6DSO32** implementation in the Inkplate library uses this library from **Adafruit**:<QuickLink title="Adafruit LSM6DS" 
  description="The Adafruit LSM6DS 6-DoF Accelerometer and Gyroscope Sensor Library for Arduino, included in the Inkplate 6 MOTION library"
  url="https://github.com/adafruit/Adafruit_LSM6DS" 
/></InfoBox>

---

## Configuration

Before retrieving accelerometer and gyroscope data, the **LSM6DSO32** sensor must be initialized.

<InfoBox>The **LSM6DSO32** sensor must be powered on via `peripheralState`. See this page for more details: <QuickLink 
  title="Peripheral basics" 
  description="How to power peripherals on and off on Inkplate 6 MOTION"
  url="/Inkplate-6MOTION/peripherals/introduction#powering-on" 
/></InfoBox>

```cpp
// Turn on the LSM6DSO32 peripheral
inkplate.peripheralState(INKPLATE_PERIPHERAL_LSM6DSO32, true);
delay(1000); // Allow time for sensor stabilization

// Initialize the sensor
if (!inkplate.lsm6dso32.begin_I2C())
{
    inkplate.println("LSM6DSO32 initialization failed");
    inkplate.display();
    while (true); // Stop execution if initialization fails
}
```
<FunctionDocumentation
  functionName="inkplate.lsm6dso32.begin_I2C()"
  description="Initializes the LSM6DSO32 sensor over I2C. This is the only relevant 'begin' function for Inkplate 6 MOTION as the sensor is connected on the PCB via I2C and no other way. In real usage, this function is called without any parameters as all the defaults are set correctly for Inkplate 6  MOTION."
  returnDescription="Returns true if initialization was successful, otherwise false."
  parameters={[
    { type: 'uint8_t', name: 'i2c_address', description: "Optional. The I2C address to use." },
    { type: 'TwoWire*', name: 'wire', description: "Optional. The Wire object for I2C communication." },
    { type: 'int32_t', name: 'sensor_id', description: "Optional. User-defined ID to differentiate different sensors." },
  ]}
/>

---

### Accelerometer configuration

The accelerometer is configured with the `range` parameter:

<FunctionDocumentation
  functionName="inkplate.lsm6dso32.setAccelRange()"
  description="Sets the accelerometer measurement range."
  returnDescription="none"
  parameters={[
    { type: 'lsm6dso32_accel_range_t', name: 'new_range', description: "The desired accelerometer range. More information is in the table below:" },
  ]}
/>

| Range | Enum Value |
|-------|----------------------------|
| **±4G**  | `LSM6DSO32_ACCEL_RANGE_4_G`  |
| **±8G**  | `LSM6DSO32_ACCEL_RANGE_8_G`  |
| **±16G** | `LSM6DSO32_ACCEL_RANGE_16_G` |
| **±32G** | `LSM6DSO32_ACCEL_RANGE_32_G` |

<InfoBox>The current accelerometer range can be retrieved with: `inkplate.lsm6dso32.getAccelRange()`</InfoBox>

---

### Gyroscope configuration

The gyroscope's `range` can also be configured:

<FunctionDocumentation
  functionName="inkplate.lsm6dso32.setGyroRange()"
  description="Sets the gyroscope measurement range."
  returnDescription="none"
  parameters={[
    { type: 'lsm6ds_gyro_range_t', name: 'new_range', description: "The desired gyroscope range. More info in the table below." },
  ]}
/>

| Range | Enum Value |
|--------|--------------------------------|
| **125°/s**  | `LSM6DS_GYRO_RANGE_125_DPS`  |
| **250°/s**  | `LSM6DS_GYRO_RANGE_250_DPS`  |
| **500°/s**  | `LSM6DS_GYRO_RANGE_500_DPS`  |
| **1000°/s** | `LSM6DS_GYRO_RANGE_1000_DPS` |
| **2000°/s** | `LSM6DS_GYRO_RANGE_2000_DPS` |
| **4000°/s** | `ISM330DHCX_GYRO_RANGE_4000_DPS` |

<InfoBox>The current gyroscope range can be retrieved with: `inkplate.lsm6dso32.getGyroRange()`</InfoBox>

---

### Data rate configuration

As a general setting, you can set the `data rate` of the LSM6DSO32. This refers to how often the data in the sensor is refreshed and updated for reading:

<FunctionDocumentation
  functionName="inkplate.lsm6dso32.setAccelDataRate()"
  description="Sets the accelerometer data update rate."
  returnDescription="none"
  parameters={[
    { type: 'lsm6ds_data_rate_t', name: 'data_rate', description: "The desired accelerometer data rate. More info in the table below." },
  ]}
/>

| Data Rate | Enum Value |
|-----------|----------------------|
| **Shutdown (0 Hz)** | `LSM6DS_RATE_SHUTDOWN` |
| **12.5 Hz** | `LSM6DS_RATE_12_5_HZ` |
| **26 Hz** | `LSM6DS_RATE_26_HZ` |
| **52 Hz** | `LSM6DS_RATE_52_HZ` |
| **104 Hz** | `LSM6DS_RATE_104_HZ` |
| **208 Hz** | `LSM6DS_RATE_208_HZ` |
| **416 Hz** | `LSM6DS_RATE_416_HZ` |
| **833 Hz** | `LSM6DS_RATE_833_HZ` |
| **1.66 kHz** | `LSM6DS_RATE_1_66K_HZ` |
| **3.33 kHz** | `LSM6DS_RATE_3_33K_HZ` |
| **6.66 kHz** | `LSM6DS_RATE_6_66K_HZ` |


<InfoBox>The current accelerometer data rate can be retrieved with: `inkplate.lsm6dso32.getAccelDataRate()`</InfoBox>

---

## Getting sensor data

<FunctionDocumentation
  functionName="inkplate.lsm6dso32.getEvent()"
  description="Retrieves the latest sensor readings, including acceleration, gyroscope, and temperature data."
  returnDescription="Returns true if the data was successfully read."
  parameters={[
    { type: 'sensors_event_t&', name: 'accel', description: "Structure to store acceleration event data." },
    { type: 'sensors_event_t&', name: 'gyro', description: "Structure to store gyroscope event data." },
    { type: 'sensors_event_t&', name: 'temp', description: "Structure to store temperature event data." },
  ]}
/>

The `sensors_event_t` structure is part of the **Adafruit Unified Sensor library** and is used to store sensor readings in a standardized format. It allows multiple types of sensors (such as accelerometers, gyroscopes, temperature sensors, etc.) to report their data consistently.

For the **LSM6DSO32 sensor**, `sensors_event_t` is used to store **acceleration data (m/s²), gyroscope data (°/s), and temperature data (°C)**. The structure includes timestamped values, making it easy to process and compare sensor readings over time.

When calling `getEvent()`, three `sensors_event_t` structures are filled:
- **Acceleration values** are stored in `accel.acceleration.x/y/z`
- **Gyroscope values** are stored in `gyro.gyro.x/y/z`
- **Temperature readings** (if applicable) are stored in `temp.temperature`
```cpp
// Make measurement
inkplate.lsm6dso32.getEvent();

// Read values from the accelerometer
float accelX = accel.acceleration.x;
float accelY = accel.acceleration.y;
float accelZ = accel.acceleration.z;

// Read values from the gyroscope
float gyroX = gyro.gyro.x;
float gyroY = gyro.gyro.y;
float gyroZ = gyro.gyro.z;
```

```cpp
// Turn on the LSM6DSO32 peripheral
inkplate.peripheralState(INKPLATE_PERIPHERAL_LSM6DSO32, true);
delay(1000); // Allow time for sensor stabilization

// Initialize the sensor
if (!inkplate.lsm6dso32.begin_I2C())
{
    inkplate.println("LSM6DSO32 initialization failed");
    inkplate.display();
    while (true); // Stop execution if initialization fails
}

// Read sensor data
sensors_event_t accel, gyro, temp;
inkplate.lsm6dso32.getEvent(&accel, &gyro, &temp);

// Print accelerometer readings
inkplate.printf("Accel X: %.2f m/s²\n", accel.acceleration.x);
inkplate.printf("Accel Y: %.2f m/s²\n", accel.acceleration.y);
inkplate.printf("Accel Z: %.2f m/s²\n", accel.acceleration.z);

// Print gyroscope readings
inkplate.printf("Gyro X: %.2f °/s\n", gyro.gyro.x);
inkplate.printf("Gyro Y: %.2f °/s\n", gyro.gyro.y);
inkplate.printf("Gyro Z: %.2f °/s\n", gyro.gyro.z);
```

---

## Full example

For the best all-in-one overview of this peripheral, have a look at this Arduino example which projects a 3D cube from the accelerometer data and also prints the gyroscope data:

<QuickLink title="Inkplate_6_MOTION_Accelerometer_Cube.ino" 
  description="Full LSM6DSO32 example in the Inkplate library"
  url="https://github.com/SolderedElectronics/Inkplate_Motion_Arduino_Library/blob/main/examples/Inkplate6Motion/Advanced/Sensors_Other/Inkplate_6_MOTION_Accelerometer_Cube/Inkplate_6_MOTION_Accelerometer_Cube.ino" 
/>