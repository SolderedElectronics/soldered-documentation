---
slug: /inkplate/6motion/peripherals/apds9960
title: 6Motion - Gesture and proximity sensor
id: 6motion-periph-apds9960
---



The **APDS9960** sensor enables **gesture recognition, proximity sensing, ambient light detection, and color sensing**. It's located on the front of your Inkplate 6 MOTION, at the top edge of the PCB. It's usages can be navigating user menus with gestures or detecting if someone is in front of Inkplate, is the light in the room on or off etc.

<CenteredImage src="/img/inkplate_6_motion/6motion_apds9960.jpg" alt="APDS9960 gesture and proximity sensor on the front of Inkplate 6 MOTION" caption="APDS9960 on the Inkplate 6 MOTION" width="600px" />

<InfoBox>The **APDS9960** implementation in the Inkplate library uses this library from **SparkFun**:<QuickLink title="SparkFun APDS9960 RGB and Gesture Sensor Arduino Library" 
  description="The original library which is included in the Inkplate 6 MOTION library"
  url="https://github.com/sparkfun/SparkFun_APDS-9960_Sensor_Arduino_Library" 
/></InfoBox>

---

## Initialization

<InfoBox>Before using the **APDS9960**, it must be turned on via `peripheralState`, see this page for more info:<QuickLink 
  title="Peripheral basics" description="How to power peripherals on and off on Inkplate 6 MOTION"
  url="/inkplate/6motion/peripherals/introduction#powering-on" 
/></InfoBox>

Initialiazion is simply done with `inkplate.apds9960.init()` which also returns if the sensor initialization was successful or not:
```cpp
// Turn on the gesture sensor peripheral
inkplate.peripheralState(INKPLATE_PERIPHERAL_APDS9960, true);

// Initialize APDS9960, notify user if init has failed
if (!inkplate.apds9960.init())
{
    inkplate.println("APDS-9960 initialization failed");

    // Error? Stop the code!
    inkplate.display();
    while (1)
        ;
}
```
<FunctionDocumentation functionName="inkplate.apds9960.init()" description="Configures I2C communications and initializes registers to defaults." returnDescription="Returns true if initialization was successful, false otherwise." />

---

## Gesture detection

Before reading gestures, make sure to call `enableGestureSensor` as demonstrated in the example below:

```cpp
// Enable gesture sensor without interrupts
inkplate.apds9960.enableGestureSensor(false);

// Now, let's detect gestures in a loop
while(true)
{
    // Check if new gesture is detected periodically
    if (inkplate.apds9960.isGestureAvailable())
    {
        // Get the detected gesture and print the gesture on the screen
        switch (inkplate.apds9960.readGesture())
        {
        case DIR_UP:
            inkplate.println("UP");
            break;
        case DIR_DOWN:
            inkplate.println("DOWN");
            break;
        case DIR_LEFT:
            inkplate.println("LEFT");
            break;
        case DIR_RIGHT:
            inkplate.println("RIGHT");
            break;
        case DIR_NEAR:
            inkplate.println("NEAR");
            break;
        case DIR_FAR:
            inkplate.println("FAR");
            break;
        default:
            // If some unspecified movement is detected print out "?"
            inkplate.println("?");
        }

        // Show on the display with a partial update
        inkplate.partialUpdate(false);
    }
    delay(10); // Slight delay between readings, helps with smoother detection
}
```

<FunctionDocumentation functionName="inkplate.apds9960.enableGestureSensor()" description="Starts the gesture recognition engine on the APDS-9960." returnDescription="Returns true if the engine was enabled correctly, false otherwise." parameters={[ { type: 'bool', name: 'interrupts', description: "True to enable hardware external interrupt on gesture detection." } ]} />

<FunctionDocumentation functionName="inkplate.apds9960.isGestureAvailable()" description="Polls the sensor if a gesture is available for reading." returnDescription="Returns true if a gesture is available, false otherwise." />

<FunctionDocumentation functionName="inkplate.apds9960.readGesture()" description="Processes a gesture event and returns the best guessed gesture." returnDescription="Returns a number corresponding to the detected gesture, or -1 on error." />

Possible gestures to detect are as follows:

| Gesture   | Enum Value  | Description                            |
| --------- | ----------- | -------------------------------------- |
| **None**  | `DIR_NONE`  | No gesture detected                    |
| **Left**  | `DIR_LEFT`  | Motion from **right to left**          |
| **Right** | `DIR_RIGHT` | Motion from **left to right**          |
| **Up**    | `DIR_UP`    | Motion from **bottom to top**          |
| **Down**  | `DIR_DOWN`  | Motion from **top to bottom**          |
| **Near**  | `DIR_NEAR`  | Object moving **closer** to the sensor |
| **Far**   | `DIR_FAR`   | Object moving **away** from the sensor |
| **All**   | `DIR_ALL`   | Detects any movement                   |

---

## Using interrupts

Instead of polling, you can use **interrupts** to trigger gesture recognition. In your sketch, you will need to create a `volatile` flag which will become set when and the APDS9960 interrupt pin changes state:
```cpp
// ISR flag - Automatically set to true in case of Interrupt event from the IO Expander
volatile bool isrFlag = false;
// ISR handler function - Called when IO expander fires INT
void ioExpanderISR()
{
    isrFlag = true;
}
```
<InfoBox>The APDS9960 interrupt pin is **IO_PIN_A0** on the internal IO expander.</InfoBox>
Then, in the body of the sketch, attatch the interrupt and use the flag to detect if there is a new gesture:

```cpp
// Let's enable interrupts
// Set APDS INT pin on IO Expander as input. Override any GPIO pin protection
inkplate.internalIO.pinModeIO(IO_PIN_A0, INPUT, true);
// Set interrupts on IO expander
inkplate.internalIO.setIntPinIO(IO_PIN_A0);
// Enable interrptus on STM32
// NOTE: Must be set to CHANGE!
attachInterrupt(digitalPinToInterrupt(PG13), ioExpanderISR, CHANGE);

// Enable the gesture sensor, as always
inkplate.apds9960.enableGestureSensor(true);

// Check the ISR flag in a loop
while(true)
{
    // If the ISR flag was set...
    if (isrFlag)
    {
        // Check if the INT pin for the APDS9960 is set to low. Otherwise ignore the INT event
        // (must be set to low for INT event from APDS). Override any GPIO pin protection
        if (!inkplate.internalIO.digitalReadIO(IO_PIN_A0, true))
        {

            // Check if new gesture is detected
            if (inkplate.apds9960.isGestureAvailable())
            {
                // Get the detected gesture and print the gesture on the screen
                switch (inkplate.apds9960.readGesture())
                {
                case DIR_UP:
                    inkplate.print("UP");
                    break;
                case DIR_DOWN:
                    inkplate.print("DOWN");
                    break;
                //...
                // Other gestures can be read here, as in the previous example
                default:
                    // If no gesture is detected, but some movement is detected, print out "?"
                    inkplate.print("?");
                }

                // Show on the display!
                inkplate.partialUpdate(true);
            }
        }
        // Clear the flag so that new interrupt event can be detected
        isrFlag = false;
    }
}
```
<WarningBox>The ISR flag needs to be reset after processing the gesture!</WarningBox>

---

## Proximity, color and light

In addition to gesture sensing, the **APDS9960** sensor also supports **ambient light, color sensing (RGB), and proximity detection**. These features can be used to determine the light level in the environment, detect object proximity, or very basic reading of colors.

Before usage, make sure to enable these features with `enableLightSensor` and `enableProximitySensor`:

```cpp
// Enable sensor functionalities
inkplate.apds9960.enableLightSensor(false);     // Enable light sensor with no interrupts
inkplate.apds9960.enableProximitySensor(false); // Enable proximity sensor with no interrupts

// Read light, proximity and color periodically
while (true)
{
    // Variables for sensor data
    uint16_t ambient_light = 0;
    uint16_t red_light = 0, green_light = 0, blue_light = 0;
    uint8_t proximity_data = 0;

    // Clear previous display buffer
    inkplate.clearDisplay();
    inkplate.setCursor(50, 50);
    inkplate.print("APDS9960 Sensor readings:");

    // Read ambient light and color data
    if (inkplate.apds9960.readAmbientLight(ambient_light) &&
        inkplate.apds9960.readRedLight(red_light) &&
        inkplate.apds9960.readGreenLight(green_light) &&
        inkplate.apds9960.readBlueLight(blue_light))
    {
        // Display ambient light and color sensor data
        inkplate.setCursor(50, 150);
        inkplate.printf("Ambient: %d | R: %d G: %d B: %d", 
        ambient_light, 
        red_light, 
        green_light, 
        blue_light);
    }
    else
    {
        inkplate.setCursor(50, 150);
        inkplate.println("Error reading light values");
    }

    // Read proximity data
    if (inkplate.apds9960.readProximity(proximity_data))
    {
        // Display proximity data
        inkplate.setCursor(50, 250);
        inkplate.printf("Proximity: %d", proximity_data);
    }
    else
    {
        inkplate.setCursor(50, 250);
        inkplate.println("Error reading proximity");
    }

    // Update display with partial update
    inkplate.partialUpdate();
    delay(1000); // Update every 1000ms
}
```

<FunctionDocumentation functionName="inkplate.apds9960.enableLightSensor()" description="Starts the light (R/G/B/Ambient) sensor on the APDS-9960." returnDescription="Returns true if the sensor was enabled correctly, false on error." parameters={[ { type: 'bool', name: 'interrupts', description: "True to enable hardware interrupt on high or low light levels." }, ]} />

<FunctionDocumentation functionName="inkplate.apds9960.enableProximitySensor()" description="Starts the proximity sensor on the APDS-9960." returnDescription="Returns true if the sensor was enabled correctly, false on error." parameters={[ { type: 'bool', name: 'interrupts', description: "True to enable hardware external interrupt on proximity detection." }, ]} />

<FunctionDocumentation functionName="inkplate.apds9960.readAmbientLight()" description="Reads the ambient (clear) light level as a 16-bit value." returnDescription="Returns true if operation is successful, false otherwise." parameters={[ { type: 'uint16_t&', name: 'val', description: "Reference variable to store the ambient light level." }, ]} />

<FunctionDocumentation functionName="inkplate.apds9960.readRedLight()" description="Reads the red light level as a 16-bit value." returnDescription="Returns true if operation is successful, false otherwise." parameters={[ { type: 'uint16_t&', name: 'val', description: "Reference variable to store the red light level." }, ]} />

<FunctionDocumentation functionName="inkplate.apds9960.readGreenLight()" description="Reads the green light level as a 16-bit value." returnDescription="Returns true if operation is successful, false otherwise." parameters={[ { type: 'uint16_t&', name: 'val', description: "Reference variable to store the green light level." }, ]} />

<FunctionDocumentation functionName="inkplate.apds9960.readBlueLight()" description="Reads the blue light level as a 16-bit value." returnDescription="Returns true if operation is successful, false otherwise." parameters={[ { type: 'uint16_t&', name: 'val', description: "Reference variable to store the blue light level." }, ]} />

<FunctionDocumentation functionName="inkplate.apds9960.readProximity()" description="Reads the proximity level as an 8-bit value." returnDescription="Returns true if operation is successful, false otherwise." parameters={[ { type: 'uint8_t&', name: 'val', description: "Reference variable to store the proximity value." }, ]} />

---

## Full examples

For full working code examples, which provide a great overwiew, a real-world use scenario and **code comments**, see the links below:

<QuickLink 
  title="Inkplate_6_MOTION_GestureSensor_Gesture.ino" 
  description="Full Arduino example on how to use the basic features of the APDS9960 gesture sensor on Inkplate 6 MOTION"
  url="https://github.com/SolderedElectronics/Inkplate_Motion_Arduino_Library/blob/main/examples/Inkplate6Motion/Advanced/Sensors_Other/Inkplate_6_MOTION_GestureSensor_Gesture/Inkplate_6_MOTION_GestureSensor_Gesture.ino" 
/>

<QuickLink 
  title="Inkplate_6_MOTION_GestureSensor_Interrupts.ino" 
  description="Full example on how to detect gesture readings via interrupt"
  url="https://github.com/SolderedElectronics/Inkplate_Motion_Arduino_Library/blob/main/examples/Inkplate6Motion/Advanced/Sensors_Other/Inkplate_6_MOTION_GestureSensor_Interrupts/Inkplate_6_MOTION_GestureSensor_Interrupts.ino" 
/>

<QuickLink 
  title="Inkplate_6_MOTION_GestureSensor_Other.ino" 
  description="Ambient light and proximity reading on the APDS9960"
  url="https://github.com/SolderedElectronics/Inkplate_Motion_Arduino_Library/blob/main/examples/Inkplate6Motion/Advanced/Sensors_Other/Inkplate_6_MOTION_GestureSensor_Other/Inkplate_6_MOTION_GestureSensor_Other.ino" 
/>