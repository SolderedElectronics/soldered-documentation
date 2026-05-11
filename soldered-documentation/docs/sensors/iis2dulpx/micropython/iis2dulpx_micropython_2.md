---
slug: /iis2dulpx/micropython/examples
title: IIS2DULPX – Measuring acceleration (MicroPython)
sidebar_label: Measuring acceleration
id: iis2dulpx-micropython-2
hide_title: False
---

This page contains examples with function documentation on how to use the **IIS2DULPX Accelerometer breakout** with MicroPython.

---

## Initialization

Copy `iis2dulpx.py` to your board's filesystem, then import it and create the sensor object. Call `begin()` to verify the sensor is connected and configure it:

```python
from iis2dulpx import IIS2DULPX, IIS2DULPX_OK

# Uses default I2C pins (SCL=22, SDA=21) and address 0x18
sensor = IIS2DULPX()

if sensor.begin() != IIS2DULPX_OK:
    raise Exception("Failed to initialize IIS2DULPX sensor")

if sensor.Enable_X() != IIS2DULPX_OK:
    raise Exception("Failed to enable accelerometer")

print("IIS2DULPX initialized successfully.")
```

If you are wiring manually or using different I2C pins, pass the `I2C` object explicitly:

```python
from machine import I2C, Pin
from iis2dulpx import IIS2DULPX, IIS2DULPX_OK

i2c = I2C(0, scl=Pin(22), sda=Pin(21))
sensor = IIS2DULPX(i2c)
```

<FunctionDocumentation
  functionName="sensor.begin()"
  description="Reads the WHO_AM_I register to verify the sensor, then configures BDU, disables I3C, sets FIFO to bypass mode, and powers the accelerometer down. Must be called before any other method."
  returnDescription="Returns `IIS2DULPX_OK` (0) on success, `IIS2DULPX_ERROR` (-1) if the sensor is not found or cannot be configured."
  parameters={[]}
/>

<FunctionDocumentation
  functionName="sensor.Enable_X()"
  description="Powers on the accelerometer and begins acquiring data at the configured ODR and full scale."
  returnDescription="Returns `IIS2DULPX_OK` (0) on success, `IIS2DULPX_ERROR` (-1) on failure."
  parameters={[]}
/>

---

## Reading acceleration data

Once the accelerometer is enabled, call `Get_X_Axes()` to get the current acceleration for all three axes in **mg** (milli-g):

```python
import time

while True:
    x, y, z = sensor.Get_X_Axes()
    print("Accel-X [mg]:{},Accel-Y[mg]:{},Accel-Z[mg]:{}".format(x, y, z))
    time.sleep_ms(50)
```

<FunctionDocumentation
  functionName="sensor.Get_X_Axes()"
  description="Reads the raw 16-bit acceleration output registers and converts the values to mg using the currently configured full-scale sensitivity."
  returnDescription="Returns a tuple `(x, y, z)` where each value is an integer in mg (milli-g)."
  parameters={[]}
/>

---

## Configuring full scale and ODR

You can change the measurement range and output data rate to suit your application:

```python
from iis2dulpx import IIS2DULPX, IIS2DULPX_OK, IIS2DULPX_HIGH_PERFORMANCE

# Set full scale to ±8g
sensor.Set_X_FullScale(8)

# Set ODR to 200 Hz in High Performance mode
sensor.Set_X_OutputDataRate_With_Mode(200.0, IIS2DULPX_HIGH_PERFORMANCE)
```

<FunctionDocumentation
  functionName="sensor.Set_X_FullScale(full_scale)"
  description="Configures the accelerometer full-scale range. Automatically selects the nearest supported range."
  returnDescription="Returns `IIS2DULPX_OK` (0) on success, `IIS2DULPX_ERROR` (-1) on failure."
  parameters={[
    { name: "full_scale", type: "int", description: "Desired range in g. Accepted values: 2, 4, 8, 16." }
  ]}
/>

<FunctionDocumentation
  functionName="sensor.Set_X_OutputDataRate_With_Mode(odr, power_mode)"
  description="Sets the output data rate and power mode simultaneously. The ODR is rounded up to the nearest supported rate for the selected mode."
  returnDescription="Returns `IIS2DULPX_OK` (0) on success, `IIS2DULPX_ERROR` (-1) on failure."
  parameters={[
    { name: "odr", type: "float", description: "Desired output data rate in Hz (e.g. 1.6, 6.0, 12.5, 25.0, 50.0, 100.0, 200.0, 400.0, 800.0)." },
    { name: "power_mode", type: "int", description: "Power mode constant: IIS2DULPX_ULTRA_LOW_POWER, IIS2DULPX_LOW_POWER, or IIS2DULPX_HIGH_PERFORMANCE." }
  ]}
/>

---

## Full example — Serial Plotter

This example continuously reads X/Y/Z acceleration and prints values in a format compatible with serial plotters:

```python
# FILE: iis2dulpx-serialPlotter.py
# AUTHOR: Josip Simun Kuci @ Soldered
# BRIEF: Poll IIS2DULPX acceleration values for serial plotting
# WORKS WITH: IIS2DULPX Accelerometer breakout: www.solde.red/333363

from machine import I2C, Pin
from iis2dulpx import IIS2DULPX, IIS2DULPX_OK
import time

# If you are not using the Qwiic connector, manually enter your I2C pins
# i2c = I2C(0, scl=Pin(22), sda=Pin(21))
# sensor = IIS2DULPX(i2c)

sensor = IIS2DULPX()

if sensor.begin() != IIS2DULPX_OK:
    raise Exception("Failed to initialize IIS2DULPX sensor")

if sensor.Enable_X() != IIS2DULPX_OK:
    raise Exception("Failed to enable accelerometer")

print("IIS2DULPX sensor initialized and accelerometer enabled.")

while True:
    x, y, z = sensor.Get_X_Axes()
    print("Accel-X [mg]:{},Accel-Y[mg]:{},Accel-Z[mg]:{}".format(x, y, z))
    time.sleep_ms(50)
```

<QuickLink
  title="iis2dulpx-serialPlotter.py"
  description="Continuously polls X/Y/Z acceleration and outputs it for serial plotting."
  url="https://github.com/SolderedElectronics/Soldered-MicroPython-Modules/tree/main/Sensors/IIS2DULPX/IIS2DULPX/examples/iis2dulpx-serialPlotter.py"
/>

---

## Interrupt-based wake-up detection

The IIS2DULPX can generate an interrupt on **INT1** or **INT2** when motion above a threshold is detected. In MicroPython, use `Pin.irq()` to attach a callback:

```python
# FILE: iis2dulpx-interruptWakeup.py
# AUTHOR: Josip Simun Kuci @ Soldered
# BRIEF: Use IIS2DULPX wake-up interrupt to detect movement
# WORKS WITH: IIS2DULPX Accelerometer breakout: www.solde.red/333363

from machine import Pin, I2C
from iis2dulpx import IIS2DULPX, IIS2DULPX_OK, IIS2DULPX_INT1_PIN
import time

# Hardware setup:
# - Connect breakout INT1 pin to INT1_PIN below
# - Optional: connect a buzzer or LED to ALERT_PIN
INT1_PIN = 5
ALERT_PIN = 23

mems_event = False


def int1_callback(pin):
    global mems_event
    mems_event = True


# If you are not using the Qwiic connector, manually enter your I2C pins
# i2c = I2C(0, scl=Pin(22), sda=Pin(21))
# sensor = IIS2DULPX(i2c)

sensor = IIS2DULPX()
alert = Pin(ALERT_PIN, Pin.OUT)
int1 = Pin(INT1_PIN, Pin.IN)
int1.irq(trigger=Pin.IRQ_RISING, handler=int1_callback)

if sensor.begin() != IIS2DULPX_OK:
    raise Exception("Failed to initialize IIS2DULPX sensor")

if sensor.Enable_X() != IIS2DULPX_OK:
    raise Exception("Failed to enable accelerometer")

if sensor.Enable_Wake_Up_Detection(IIS2DULPX_INT1_PIN) != IIS2DULPX_OK:
    raise Exception("Failed to enable wake-up detection")

print("Wake-up detection enabled")

while True:
    if mems_event:
        mems_event = False
        status = sensor.Get_X_Event_Status()
        if status["WakeUpStatus"]:
            print("Wake up Detected!")
            alert.on()
            time.sleep_ms(200)
            alert.off()

    time.sleep_ms(10)
```

<FunctionDocumentation
  functionName="sensor.Enable_Wake_Up_Detection(int_pin)"
  description="Enables wake-up detection. Configures the sensor to generate an interrupt on the specified pin when acceleration exceeds the default wake-up threshold. Also sets ODR to 200 Hz and full scale to ±2g."
  returnDescription="Returns `IIS2DULPX_OK` (0) on success, `IIS2DULPX_ERROR` (-1) on failure."
  parameters={[
    { name: "int_pin", type: "int", description: "Interrupt pin to route the event to: `IIS2DULPX_INT1_PIN` or `IIS2DULPX_INT2_PIN`." }
  ]}
/>

<FunctionDocumentation
  functionName="sensor.Get_X_Event_Status()"
  description="Reads the interrupt source registers and returns a dictionary of event flags."
  returnDescription='Returns a dict with keys `"WakeUpStatus"`, `"FreeFallStatus"`, `"TapStatus"`, `"DoubleTapStatus"`, `"D6DOrientationStatus"`, `"StepStatus"`, `"TiltStatus"`, `"SleepStatus"`. Each value is `1` if the event is active, `0` otherwise.'
  parameters={[]}
/>

<FunctionDocumentation
  functionName="sensor.Set_Wake_Up_Threshold(threshold_mg)"
  description="Sets the wake-up detection threshold in mg. Automatically selects the appropriate resolution based on the current full-scale setting."
  returnDescription="Returns `IIS2DULPX_OK` (0) on success, `IIS2DULPX_ERROR` (-1) on failure."
  parameters={[
    { name: "threshold_mg", type: "float", description: "Wake-up threshold in mg." }
  ]}
/>

<QuickLink
  title="iis2dulpx-interruptWakeup.py"
  description="Uses INT1 to detect motion and toggle an output pin on wake-up."
  url="https://github.com/SolderedElectronics/Soldered-MicroPython-Modules/tree/main/Sensors/IIS2DULPX/IIS2DULPX/examples/iis2dulpx-interruptWakeup.py"
/>
