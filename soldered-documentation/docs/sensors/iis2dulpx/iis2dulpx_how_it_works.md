---
slug: /iis2dulpx/how-it-works 
title: How it works
id: iis2dulpx-how-it-works 
hide_title: False
---

The **IIS2DULPX** is a MEMS accelerometer IC by [**STMicroelectronics**](https://www.st.com/en/mems-and-sensors/iis2dulpx.html). It integrates a 3-axis digital accelerometer and a QVAR (charge variation) sensing channel in a single ultra-low-power package, making it well-suited for wearables, IoT nodes, and industrial applications.

<CenteredImage src="/img/iis2dulpx/onboard.png" alt="IIS2DULPX chip on the board" caption="IIS2DULPX chip on the board" width="600px" />

---

## Datasheet

For an in-depth look at technical specifications, refer to the official IIS2DULPX datasheet:

<QuickLink
  title="IIS2DULPX Datasheet"
  description="Detailed technical documentation for the IIS2DULPX ultra-low-power accelerometer"
  url="https://cdn.shopify.com/s/files/1/0990/5029/1549/files/iis2dulpx.pdf?v=1777288704"
/>

---

## How the accelerometer works

The **accelerometer** measures linear acceleration using a tiny **proof mass suspended by springs** inside the MEMS structure. When the device experiences acceleration, the proof mass displaces relative to its frame due to inertia, compressing or stretching the springs. This displacement is detected by **capacitive sensing elements**, which convert the **mechanical movement into electrical signals**. The signal is then digitized and made available over I2C.

The IIS2DULPX supports four selectable full-scale ranges — **±2g, ±4g, ±8g, and ±16g** — with corresponding sensitivities from **0.061 mg/LSB to 0.488 mg/LSB**. Three power modes are available to trade off noise performance against current draw:

| Power Mode        | Available ODR             |
| ----------------- | ------------------------- |
| Ultra Low Power   | 1.6 Hz, 3 Hz, 25 Hz       |
| Low Power         | 6 Hz – 800 Hz             |
| High Performance  | 6 Hz – 800 Hz             |

---

## How QVAR sensing works

**QVAR (Quasi-Vectorial Acceleration and charge vaRiation)** is an additional sensing channel embedded in the IIS2DULPX. It measures changes in electric charge on the sensor's dedicated analog input pin. This enables applications such as:

- **Capacitive touch** detection (e.g., detecting a finger press)
- **Liquid level** sensing
- **Electric field** variation detection

The QVAR gain is configurable with multipliers of 0.5×, 1×, 2×, or 4× relative to the base gain of 74.4 LSB/mV.

---

## On-chip motion detection features

The IIS2DULPX includes a powerful set of embedded event-detection algorithms that run independently on the sensor, offloading the host microcontroller:

| Feature              | Description                                                  |
| -------------------- | ------------------------------------------------------------ |
| **Wake-up**          | Triggers an interrupt when acceleration exceeds a threshold  |
| **Free-fall**        | Detects when the sensor is in free-fall                      |
| **Tap / Double Tap** | Recognizes single or double-tap gestures                     |
| **6D / 4D Orientation** | Detects the board's orientation in 6 or 4 directions     |
| **Step counter**     | Counts steps using the embedded pedometer                    |
| **Tilt detection**   | Detects when the device is tilted beyond a threshold         |
| **Sleep detection**  | Detects when the device has been stationary for a set time   |

These events can be routed to either of the two interrupt pins (**INT1** or **INT2**).

---

## I2C communication

The Soldered IIS2DULPX breakout communicates with a microcontroller over **I2C**. The I2C address is **0x18** (SDO/SA0 pulled low on the board).

The library initializes I2C communication automatically through the `Wire` library. Upon initialization, the sensor:

1. Disables I3C interface and configures BDU (block data update)
2. Sets FIFO to bypass mode
3. Defaults to High Performance power mode at 100 Hz ODR with ±2g full scale

---

## Measurement process

1. **Initialization**
   - Call `sensor.begin()` to configure the sensor, disable I3C, set BDU, and prepare the FIFO.
   - Call `sensor.Enable_X()` to power on the accelerometer.

2. **Taking a measurement**
   - Call `sensor.Get_X_Axes(&accel)` to retrieve acceleration in **mg** (milli-g) for all three axes.
   - Alternatively, call `sensor.Get_X_AxesRaw(&raw)` for the 16-bit raw ADC values.

3. **Event detection**
   - Configure an interrupt (e.g., `Enable_Wake_Up_Detection(IIS2DULPX_INT1_PIN)`) and attach an ISR to the INT pin.
   - Poll `sensor.Get_X_Event_Status(&status)` inside the ISR handler to identify which event triggered.

4. **Power management**
   - Use `Set_X_OutputDataRate_With_Mode(odr, power_mode)` to balance performance vs. power consumption.
   - Call `sensor.Disable_X()` to put the accelerometer into power-down when not in use.
