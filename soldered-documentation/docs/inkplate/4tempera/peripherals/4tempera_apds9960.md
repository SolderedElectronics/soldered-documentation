---  
slug: /inkplate/4tempera/peripherals/apds9960  
title: Inkplate 4TEMPERA – Gesture and proximity sensor
id: 4tempera-periph-apds9960  
hide_title: true
---

<SectionTitle title="Gesture and Proximity Sensor" backgroundImage="/img/inkplate_2/hardware.png" />

The **APDS9960** sensor on the Inkplate 4 TEMPERA enables **gesture recognition, proximity sensing, ambient light measurement, and basic RGB color detection**. It’s perfect for swipe-based user interface interaction, detecting nearby motion, or adapting the display based on room lighting.

---

## Initialization and Configuration

Before using the sensor, power it on and initialize it:

```cpp
inkplate.wakePeripheral(INKPLATE_APDS9960);

if (!inkplate.apds9960.init()) {
    inkplate.setCursor(50, 50);
    inkplate.print("Can't init APDS!");
    inkplate.display();
    esp_deep_sleep_start();
}
```

<FunctionDocumentation functionName="inkplate.apds9960.init()" description="Initializes the APDS9960 sensor with default configuration." returnDescription="Returns true if successful, false if initialization fails." />

Then, enable the features you need:

```cpp
inkplate.apds9960.enableProximitySensor(false);
inkplate.apds9960.setProximityGain(1);
inkplate.apds9960.enableGestureSensor();
inkplate.apds9960.setGestureGain(0);
inkplate.apds9960.enableLightSensor(false);
```

<FunctionDocumentation functionName="inkplate.apds9960.enableProximitySensor()" description="Enables the proximity sensing feature." returnDescription="Returns true on success." parameters={[{ type: 'bool', name: 'interrupts', description: 'Set true to use interrupts, false for polling.' }]} />
<FunctionDocumentation functionName="inkplate.apds9960.setProximityGain()" description="Sets the gain for proximity detection." returnDescription="None" parameters={[{ type: 'uint8_t', name: 'gain', description: 'Gain value (0–3)' }]} />
<FunctionDocumentation functionName="inkplate.apds9960.enableGestureSensor()" description="Enables gesture sensing." returnDescription="Returns true if successful." />
<FunctionDocumentation functionName="inkplate.apds9960.setGestureGain()" description="Sets the sensitivity of gesture detection." returnDescription="None" parameters={[{ type: 'uint8_t', name: 'gain', description: 'Gain value (0–3)' }]} />
<FunctionDocumentation functionName="inkplate.apds9960.enableLightSensor()" description="Enables the ambient and RGB light sensing." returnDescription="Returns true on success." parameters={[{ type: 'bool', name: 'interrupts', description: 'Set true to enable interrupt mode.' }]} />

---

## Gesture Detection

```cpp
if (inkplate.apds9960.isGestureAvailable()) {
    int gesture = inkplate.apds9960.readGesture();
    switch (gesture) {
        case DIR_UP:    inkplate.print("Up"); break;
        case DIR_DOWN:  inkplate.print("Down"); break;
        case DIR_LEFT:  inkplate.print("Left"); break;
        case DIR_RIGHT: inkplate.print("Right"); break;
        default: break;
    }
    inkplate.partialUpdate();
}
```

<FunctionDocumentation functionName="inkplate.apds9960.isGestureAvailable()" description="Checks if a gesture has been detected and is ready to read." returnDescription="Returns true if gesture data is available." />
<FunctionDocumentation functionName="inkplate.apds9960.readGesture()" description="Reads and returns the last detected gesture." returnDescription="Returns a DIR_* constant representing the gesture, or -1 on failure." />

---

## Proximity Reading

```cpp
uint8_t proximity;
inkplate.apds9960.readProximity(proximity);
inkplate.print(proximity);
```

<FunctionDocumentation functionName="inkplate.apds9960.readProximity()" description="Reads the proximity value from the sensor." returnDescription="Returns true if successful." parameters={[{ type: 'uint8_t&', name: 'val', description: 'Variable to store the proximity value (0–255).' }]} />

---

## Color Reading (RGB)

```cpp
uint16_t red, green, blue;
inkplate.apds9960.readRedLight(red);
inkplate.apds9960.readGreenLight(green);
inkplate.apds9960.readBlueLight(blue);
inkplate.printf("Red: %d Green: %d Blue: %d", red, green, blue);
```

<FunctionDocumentation functionName="inkplate.apds9960.readRedLight()" description="Reads red light intensity." returnDescription="Returns true if successful." parameters={[{ type: 'uint16_t&', name: 'val', description: 'Red light value.' }]} />
<FunctionDocumentation functionName="inkplate.apds9960.readGreenLight()" description="Reads green light intensity." returnDescription="Returns true if successful." parameters={[{ type: 'uint16_t&', name: 'val', description: 'Green light value.' }]} />
<FunctionDocumentation functionName="inkplate.apds9960.readBlueLight()" description="Reads blue light intensity." returnDescription="Returns true if successful." parameters={[{ type: 'uint16_t&', name: 'val', description: 'Blue light value.' }]} />

---

## Ambient Light

```cpp
uint16_t ambient;
inkplate.apds9960.readAmbientLight(ambient);
inkplate.print(ambient);
```

<FunctionDocumentation functionName="inkplate.apds9960.readAmbientLight()" description="Reads overall ambient light level." returnDescription="Returns true if successful." parameters={[{ type: 'uint16_t&', name: 'val', description: 'Ambient light value.' }]} />

---

## Gesture Types

| Gesture   | Enum Value  | Description                            |
| --------- | ----------- | -------------------------------------- |
| **None**  | `DIR_NONE`  | No gesture detected                    |
| **Left**  | `DIR_LEFT`  | Right to left                          |
| **Right** | `DIR_RIGHT` | Left to right                          |
| **Up**    | `DIR_UP`    | Bottom to top                          |
| **Down**  | `DIR_DOWN`  | Top to bottom                          |
| **Near**  | `DIR_NEAR`  | Object approaching                     |
| **Far**   | `DIR_FAR`   | Object moving away                     |

---

## Example Sketch

The following full example demonstrates how to use all APDS9960 sensor features, including:
- Gesture recognition
- Proximity
- RGB light levels
- Ambient light

<QuickLink 
  title="Inkplate4TEMPERA_APDS9960.ino" 
  description="Full Arduino example on how to use the APDS9960 sensor."
  url="https://github.com/SolderedElectronics/Inkplate-Arduino-library/tree/master/examples/Inkplate4TEMPERA/Advanced/Sensors/Inkplate4TEMPERA_APDS9960" 
/>