---
slug: /sonar/final-build
title: Full system build
sidebar_label: Final build
id: final-system-build
hide_title: false
---

This page shows the full functionality of the project by integrating all individual components into a working system to create a functional radar-like style distance measurement system using a compatible microcontroller, a TFT touchscreen, a servo motor, and a laser distance sensor. 

---

## System Behavior
When the system is powered on, the servo begins its sweeping motion, rotating the laser distance sensor 90 degrees to the right and left (180 degree sweep). By default, the display shows the radar-like graphical interface which visually represents scanned objects in real time.

Two interactive buttons are displayed on the bottom of touchscreen:
- **START/STOP Button** - allows the user to start or pause the system. When stopped, servo stops rotating and distance readings are no longer updated.
- **Display Button** - toggles between radar-like display and distance meter. When distance meter display is active the servo doesn't rotate, it provides measured distance directly in front of the sensor. 

For easire visual understanding, detected objects are displayed as colored *triangles*. Objects that are closer appear in `red`, more distant objects are shown in `yellow`. This same color logic is used in both radar graph and distance meter display, with only minor differences in how they are shown.


<CenteredImage src="/img/under_construction.png" alt="Working system example" caption="Full demo of working system" width="600px"/>

---

## Code structure
The code is organized into separate files for better readability and maintenance. Here is a short breakdown of key components:
- `main_sketch.ino`
  - Program setup and loop logic
  - Touch input handling
  - Switching between radar and distance meter display
  - Controlling the system START/STOP state
  - Calling sensor readings and updates display based on mode

- `GUI.h / GUI.cpp`
  - Initializes display and touchscreen
  - Handles screen clearing, redrawing elements and dynamic updates
  - Provides functions for radar mode and distance meter
  - Renders touch buttons
  - Animates sweeping line
  
- `Sensors.h / Sensors.cpp`
  - Initializes servo and laser sensor
  - Sets servo angles for scanning
  - Getting distance values from laser sensor
  

### Main program loop

```cpp
void loop() {
    ts.service(); 
    if (ts.getPressure()) { // Wait for screen touch
        updateProgramStatus();
    }

    if (isSystemRunning) {
        unsigned long now = millis();
        if (now - lastMove >= 50) { // Adjust speed (ms)
            lastMove = now;
            Serial.println(currentDistance);
            
            if (usingRadarGraph) { // true = radar-like graph | false = distance meter
                sensors.setServoAngle(angle); // Rotate servo
                currentDistance = sensors.getDistance();
                // Erase the sweep line
                gui.updateSweepLine(prev_angle, ILI9341_BLACK);
                // Erase the object from the angle 
                gui.eraseDetectedObject(angle); 
                // Update the graph
                gui.redrawRadar();
                // Draw current sweep line
                gui.updateSweepLine(angle, ILI9341_GREEN);
                // Draw current detected object
                gui.drawDetectedObject(angle, currentDistance);
                // Update angle display
                gui.updateAngleDisplay(angle);

                prev_angle = angle; // Storing previous angle for sweep line deletion
                angle += dir;
                if (angle >= 180 || angle <= 0) dir = -dir; // Change direction
            }
            else {
                currentDistance = sensors.getDistance();
                gui.drawDistanceMeter(currentDistance);
            }
        }
    }
}
```

### View full code on GitHub
<QuickLink 
  title="Sonar Project" description=""
  url=""
/>
