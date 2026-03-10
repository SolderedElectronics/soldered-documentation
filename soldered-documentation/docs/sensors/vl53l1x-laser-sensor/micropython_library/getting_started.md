---
slug: /vl53l1x-laser-sensor/micropython/getting-started
title: VL53L1X ToF Laser Distance Sensor - Getting Started (MicroPython)
id: laser-distance-sensor-micropython
sidebar_label: Getting Started
hide_title: False
---

## MicroPython library

To upload VL53L1X MicroPython module onto your board you can use **Thonny IDE** or **mpremote**:

<QuickLink  
  title="VL53L1X Laser Distance Sensor MicroPython Library"  
  description="Laser Distance Sensor MicroPython library by Soldered"  
  url="https://github.com/SolderedElectronics/Soldered-MicroPython-Modules/tree/main/Sensors/LaserDistanceSensor"  
/>

## Installing using mpremote

To use **mpremote** first **[install the mpremote package](https://docs.micropython.org/en/latest/reference/mpremote.html)**, connect the board to your computer and then upload the module to the board using the following command:

```
python -m mpremote mip install github:SolderedElectronics/Soldered-Micropython-modules/Sensors/LaserDistanceSensor
```

## Installing using Thonny IDE

1. Connect your board to computer with USB
2. Open **Thonny**, select the correct interpreter
    - **Tools** > **Options** > **Interpreter**
    - Select MicroPython (Raspberry Pi Pico / ESP32 / ...)
    - Choose correct port and click **OK**
3. Open the `modules/` folder from **[MicroPython Modules](https://github.com/SolderedElectronics/Soldered-MicroPython-Modules/tree/main)**
4. For each module:
    - Open the `.py` file in Thonny
    - Go to **File** > **Save as...**
    - Choose **MicroPython device**
    - Save the file inside the `/lib/` directory on the device (create it if it doesn't exist)
5. Once the module is uploaded on your board, you can import it just like any other module:

```python
from VL53L1X import VL53L1X
``` 

---

<InfoBox>

New to MicroPython? Check out our **MicroPython overview** to get started:
<QuickLink  
  title="MicroPython Overview"  
  description="Getting started with MicroPython guide"  
  url="https://soldered.com/documentation/micropython/overview"  
/>

</InfoBox>

