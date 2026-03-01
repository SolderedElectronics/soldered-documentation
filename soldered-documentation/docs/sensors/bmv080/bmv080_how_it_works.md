---
slug: /bmv080/how-it-works 
title: BMV080 Particulate Matter Sensor - How it works
sidebar_label: How it works
id: bmv080-how-it-works 
hide_title: False
---  

# BMV080 - How it works

The **BMV080** is an ultra-compact particulate matter sensor that measures the concentration of airborne particles such as dust, smoke, and pollution. It uses a **laser-based optical sensing technique** to detect and count particles moving through a small measurement region above the sensor.

Unlike many traditional PM sensors, the BMV080 operates without a fan or air channel, instead relying on **natural ambient airflow**. This allows it to be integrated into very small devices such as portable air quality monitors, wearables, and IoT sensors.

<CenteredImage src="/img/under_construction.png" alt="BMV080 sensor on board" caption="BMV080 sensor on the board" width="500px" />

---

## Datasheet

For an in-depth look at technical specifications, refer to the official BMP180 Datasheet:  

<QuickLink  
  title="BMV080 Datasheet"  
  description="Detailed technical documentation for the BMV080 sensor"  
  url="https://www.bosch-sensortec.com/media/boschsensortec/downloads/datasheets/bst-bmv080-ds000.pdf"  
/>  

## Measurement principle

The BMV080 uses a laser scattering technique to detect particles in the air.

1. A laser inside the sensor emits a focused beam of light.
2. The beam is focused into a sensitive measurement region approximately 5 mm above the sensor lens.
3. Airborne particles passing through this region scatter the laser light.
4. A photodetector inside the sensor measures the scattered light.
5. The sensor analyzes the detected signal to determine particle presence, size, and velocity.

The amount and characteristics of scattered light allow the sensor to estimate particle concentration and size distribution.

## Particle detection

When a particle passes through the laser beam:

- The particle **interacts with the laser light**
- Light is **scattered in multiple directions**
- Some of the scattered light returns to sensor's **photodetector**

The sensor detects this scattered light and **generates a signal**. Multiple particle detections over time allow the sensor to estimate **particle density in the surrounding air.**

Additionally, the scattered light experiences a **Doppler shift** due to particle movement. This helps the sensor estimate the velocity of particles moving through the sensing region.

<CenteredImage
  src="/img/bmv080/bosch-bmv-working-principle.png"
  alt="How it works"
  caption="Sensor operating principle"
  attribution_name="Bosch Sensortec"
  attribution_link="https://www.bosch-sensortec.com/media/boschsensortec/downloads/datasheets/bst-bmv080-ds000.pdf"
/>

## Data processing 

The raw optical measurements are processed internally using algorithms developed by Bosch. These algorithms analyze the detected particle events and convert them into mass concentration values. The sensor outputs its measurements for **PM1, PM2.5 and PM10.**

In addition, several measurement algorithms are available depending on the application:
- **High precision -** highest accuracy measurements
- **Balanced -** compromise between accuracy and responsiveness
- **Fast response -** quicker updates with lower integration time

The sensor typically provides a new measurement approximately **once per second**, depending on configuration.

## Communication protocol

The BMV080 communicates with a host microcontroller using a digital serial interface. The sensor supports two communication protocols:
- **I²C (default)**
- **SPI (must be selected through jumper)**

The address pins (AB0 and AB1) allow multiple sensors to be connected to the same I²C bus by selecting different device addresses.