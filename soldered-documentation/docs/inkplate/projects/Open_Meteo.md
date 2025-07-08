---  
slug: /inkplate/projects/open-meteo-weather-station
title: Inkplate Projects - Open-Meteo Weather Station 
sidebar_label: Open-Meteo Weather Station   
id: open-meteo 
hide_title: false  
pagination_prev: null  
---

## Overview

<CenteredImage src="/img/openai-text-prompt/showcase.jpg" alt="Google Calendar Showcase"  width="100%"/>

The OpenMeteo Weather Station project turns your Inkplate e-paper display into a fully connected, ultra-low-power personal weather dashboard. It fetches real-time data from the Open-Meteo API, including temperature, conditions, and forecasts, and presents it in a clean, readable format—ideal for desktops, walls, or any spot where ambient weather awareness adds value.

Designed for simplicity and efficiency, this project pulls local weather information based on your provided coordinates and timezone, then renders it with partial grayscale for visual clarity. Users can customize the display with their name and city, and optionally switch between metric and imperial units. A dedicated graphical user interface (GUI) component handles drawing, ensuring the screen is both informative and aesthetically pleasing.

Thanks to the Inkplate’s e-paper technology and built-in deep sleep mode, the display remains visible without consuming power, updating only every 30 minutes before going back to sleep. This makes it perfect for long-term, battery-powered use cases—indoors or out.

Whether you're looking for a minimalist smart weather screen or an example of networked IoT design, this project highlights the Inkplate’s ability to connect, retrieve, and present real-world data with elegant efficiency.

## Requirements

For this project, you have to:
- **Have a stable Wi-Fi connection**

Every Inkplate device can run the Open-Meteo Weather Station project. For this example, we will use the **Inkplate 5V2**.

## Setting up

The Arduino sketch must be modified for this project to run. First, open the **Arduino IDE** and navigate to  
`File->Examples->InkplateLibrary->Your Inkplate Device->Projects->Inkplate_OpenMeteo_Weather_Station`:

<CenteredImage src="/img/open-meteo/arduino_direction.png" alt="Arduino sketch path directions"  width="100%" />

### Wi-Fi

Next, in the main .ino file of the project, enter the SSID and password for your Wi-Fi connection. This can be done in the following two lines:

```cpp
const char *ssid = "YOUR_SSID";
const char *password = "YOUR_PASSWORD";
```

### User and location information

To get weather data for your specific location, you must enter your city as well as its coordinates in the main .ino sketch file of the project:
