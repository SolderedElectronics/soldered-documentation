---
slug: /accelerometer-gyroscope/how-it-works
title: How it works
id: accelerometer-gyroscope-how-it-works
hide_title: False
---

The **Accelerometer & Gyroscope LSM6DS 6-DOF** is an integrated circuit by [**STMicroelectronics**](https://www.st.com/en/mems-and-sensors/lsm6ds3tr-c.html). It's all in one package that combines a 3D digital accelerometer and a 3D digital gyroscope, allowing linear acceleration and rotational motion to be tracked in three dimensions.

<CenteredImage src="/img/accelerometer-gyroscope/LSM6DS36_onboard.png" alt="LSM6DS chip on the board" caption="LSM6DS chip on the board" width="400px" />
---

## Datasheet

For an in-depth look at technical specifications, refer to each of the official LSM6DS 6-DOF Datasheets:

<QuickLink  
  title="LSM6DS3 6-DOF Datasheet"  
  description="Detailed technical documentation for the LSM6DS3 6-DOF Accelerometer & Gyroscope"  
  url="https://soldered.com/productdata/2023/08/Soldered_LSM6DS3_datasheet.pdf"  
/>  

<QuickLink  
  title="LSM6DSO32 6-DOF Datasheet"  
  description="Detailed technical documentation for the LSM6DSO32 6-DOF Accelerometer & Gyroscope"  
  url="https://soldered.com/productdata/2023/08/Soldered_lsm6dso32_datasheet.pdf"  
/>

<QuickLink  
  title="LSM6DSO 6-DOF Datasheet"  
  description="Detailed technical documentation for the LSM6DSO 6-DOF Accelerometer & Gyroscope"  
  url="https://soldered.com/productdata/2023/08/Soldered_lsm6dso_datasheet.pdf"  
/>

---

## How the accelerometer works

The **accelerometer** on this board works by reading the movement of its mass, where movement caused by an external force is then transformed into readable input that is transferred into data. It all works by containing a **tiny proof mass (body of mass) attached to a spring** within its casing. When acceleration occurs, the proof mass moves relative to the casing due to inertia, causing the spring to compress or stretch. This movement is **detected by capacitive or piezoresistive sensors**, which convert the **mechanical displacement into electrical signals**. These signals are then processed and amplified by onboard electronics to provide precise measurements of acceleration, supporting full-scale ranges from **±2 g to ±16 g**.

<CenteredImage src="/img/accelerometer-gyroscope/accelerometer.png" alt="lsm6ds accelerometer" caption="Visual representation of the accelerometer" width="400px" />

---

## How the gyroscope works

The **gyroscope** on this board works similarly to the accelerometer, with the difference that it operates by containing tiny vibrating structures that move due to the **Coriolis force** when **rotation occurs**. This movement is detected by **capacitive or piezoresistive sensors**, which convert the **mechanical displacement** into **electrical signals**. These signals are then processed and amplified by onboard electronics to provide precise measurements of angular rate, supporting full-scale ranges from **±125 dps to ±2000 dps**. The gyroscope's operation is based on **MEMS technology**, ensuring high precision and low power consumption, making it suitable for applications such as drone stabilization and robotics. Its design allows for efficient data management and low power modes, ensuring optimal performance without significant energy consumption.

<CenteredImage src="/img/accelerometer-gyroscope/gyroscope.png" alt="lsm6ds gyroscope" caption="Visual representation of the gyroscope" width="400px" />

---

## I2C communication

The LSM6DS3TR-C uses the I2C protocol to communicate with a microcontroller. It operates with a default I2C address of **0x6B**, but this can be changed to **0x6A** by grounding the **SDO/SA0** pin, which was further explained before in the [**Address jumper**](accelerometer-gyroscope_hardware_details.md#address-jumper) section.

The sensor also supports fast mode (400 kHz) for rapid data transmission, where upon request the sensor responds with multiple **16-bit** values—one for the **accelerometer**, one for the **gyroscope**, and one for **temperature**—along with an optional **CRC checksum** for data integrity. These values provide **precise motion tracking and environmental data**.

---

## Measurement process

1. **Power-up and initialization**  
   - LSM6DS3 enters a low-power mode when powered on.  
   - On initialization, send a command to initialize the sensor. This typically involves setting the desired measurement ranges for the accelerometer and gyroscope, as well as configuring any additional features, such as FIFO buffering or interrupt settings.

2. **Taking a measurement**  
   - Send a command to start the measurement process.  
   - The sensor captures data for linear acceleration and angular rate. The measurement process is typically continuous once started, with data being stored in the FIFO buffer if configured.

3. **Data retrieval**  
   - Use I2C or SPI to read the latest data from the sensor. This involves sending a read command to the sensor's address and retrieving the stored data.  
   - The sensor outputs raw data for acceleration and angular velocity, which may need to be converted into meaningful units (e.g., g for acceleration, dps for angular rate) using the sensitivity values provided in the datasheet.

4. **Additional Steps**  
   - If the FIFO buffer is used, manage its contents by reading data regularly to prevent overflow, or use interrupts to signal when new data is available.  
   - Process the retrieved data to extract meaningful information such as orientation, motion patterns, or other desired metrics.