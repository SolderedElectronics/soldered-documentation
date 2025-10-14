---
slug: /vl53l1x-laser-sensor/how-it-works 
title: VL53L1X - How it works
id: sensor-how-it-works 
sidebar_label: How it works
hide_title: False
---  

## Datasheet

For an in-depth look at technical specifications visit the official **VL53L1X Documentation** 

<QuickLink  
  title="VL53L1X Datasheet"  
  description="View full VL53L1X Laser Sensor specfications"  
  url="https://www.st.com/resource/en/datasheet/vl53l1x.pdf"  
/>  


## How the sensor works
The VL53L1X is an advanced and compact **Time-of-Flight (ToF)** distance sensor, meaning it measures how long the light has taken to bounce back to sensor unlike IR sensors that measure amount of light reflected back to them. It uses a very narrow light source, which makes it very precise at determining the distance of the surface in front of it.

<CenteredImage src="/img/vl53l1x_laser_sensor/vl53l1x-principle.png" alt="VL53L1X Laser Sensor image"/>

### Measurement process

**1. Laser Pulse emmission**
- The sensor emits a quick pulse of **invisible infrared light** using a tiny laser (VCSEL - vertical-cavity surface-emitting laser) at 940nm.

**2. Bounce Back**
- The emitted light pulse travles through the air, **hits an object**, and reflects back to the onboard sensor.

**3. Single Photon Detection**
- The reflected light is captured by a very sensitive array of detectors called **SPADS (Single Photon Avalanche Diodes)**, capable of detecting single photons of light.

**4. Time measurement**
- The sensor's built-in microcontroller precisely calculates how long it took for the light to go out and reflect back. Since the **speed of light is constant**, this time can be used to calculate the exact distance to the object.
  

### Additional features
- **Programmable region of interest (ROI)**
  - ROI size and position are programmable.
  - Choose custom FoV from 4x4 SPADs (min.) up to 16x16 SPADs (full FoV)
- **Shutdown Pin**
  - **SHTD** pin allows to put the sensor into hardware standby mode
- **GPIO Interrupt**
  - Digital output that acts as an interrupt line from the sensor to your microcontroller
  - It can signal new distance measurement, a threshold condition has been met

## Qwiic I²C communication

This product uses I²C communication. The breakout board operates with a default I²C address of **0x29** but can be changed with onboard jumpers. To change the breakout board's address, check out the [**Address selection**](/vl53l1x%20laser%20sensor/hardware/#jumper-details).