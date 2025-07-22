---
slug: /sonar/final-build
title: Full system integration
sidebar_label: Final build
id: final-system-build
hide_title: false
---

This page shows the full functionality of the project by integrating all individual components into a working system. This section shows how the hardware and software are implemented together to create a functional radar-like style distance measurement system using a compatible microcontroller, a TFT touchscreen, a servo motor, and a laser distance sensor. 

---

## System Behavior
When the system is powered on, the servo begins its sweeping motion, rotating the laser distance sensor 90 degrees to the right and left (180 degree sweep). By default, the display shows the radar-like graphical interface which visually represents scanned objects in real time.

Two interactive buttons are displayed on the bottom of touchscreen:
- **Start/Stop Button** - allows the user to start or pause the system. When stopped, servo stops rotating and distance readings are no longer updated.
- **Display Button** - toggles between radar-like display and distance meter. When distance meter display is active the servo doesn't rotate, it provides measured distance directly in front of the sensor. 

For radar graph, detected objects are displayed as colored "triangles". Closer objects are represented in `red` (distance < 150cm), more distance objects are shown in `yellow` (between 150 and 200 cm), while objects that surpass 200cm are drawn in `green`.

Distance meter uses the same logic, only the objects that pass max visual range are displayed as one bar.

---
