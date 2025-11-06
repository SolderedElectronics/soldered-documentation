---
slug: /soldered-nula-beginner-kit-micropython/parking-sensor-project
title: Parking Sensor Project
id: parking-sensor-project
hide_title: true
---

<SectionTitle title="Parking Sensor Project" backgroundImage="/img/arduino_bg.jpg" />

<CenteredImage src="/img/under_construction.png" alt="Under construction" caption="Short example demonstration video" width="700px" />

In this example we will use **HC-SR04 ultrasonic distance sensor** combined with a **buzzer** to simulate a car parking sensor system where the buzzer's beeping rate increases as objects get closer and closer.

**At the end of this example you will learn:**
- How to play sound through a buzzer
- How to use `time` library to measure / compare time

---

**Parts required:**
- **Soldered NULA Mini Board**
- **Breadboard**
- **HC-SR04 Ultrasonic distance sensor**
- **Buzzer**
- **1 x Qwiic cable**
- **Some jumper wires**

## Putting the components together

<CenteredImage src="/img/under_construction.png" alt="Under construction" caption="Required components" width="400px" />

- Place the buzzer on the breadboard, connect the positive pin on GPIO 5, and other pin to GND.
- Connecting the Ultrasonic sensor is pretty simple and straightforward, just plug in one end of **Qwiic** cable in the NULA Mini board, and the other end in the sensor itself.
- If you have the **native** version (no Qwiic connector), follow the table below for connections:

<CenteredImage src="/img/under_construction.png" alt="Under construction" caption="Components connected together" width="400px" />

| **Ultrasonic sensor** | **NULA Mini** |
|---|---|
| VCC | VCC (5V) |
| GND | GND |
| ECHO | IO18 (any GPIO) |
| TRIG | IO19 (any GPIO) |

## Code Example

Import needed modules for Ultrasonic sensor along with `Pin` and `PWM` for the buzzer.

```python
from UltrasonicSensor import UltrasonicSensor
from machine import I2C, Pin, PWM
import time
```

Here are defined constants that are used for controlling the sound behaviour. They specify when the sound starts / stops playing based on distance, and how fast / slow are the 'beeps' being played based on distance.

```python
CONTINUOUS_THRESHOLD_CM = 35    # Below this threshold - play continous tone
BEEP_START_DIST_CM = 170        # No sound played if measured distance is beyond this value
MIN_BEEP_PERIOD_MS = 60         # Shortest beep cycle (fastest beeping rate)
MAX_BEEP_PERIOD_MS = 700        # Longest beep cycle (slowest beeping rate)
MAX_BEEP_ON_TIME_MS = 50        # Max play time for each 'beep'
```

Buzzer is connected to pin 5 on microcontroller and it will be driven at a frequency of 2000 Hz (this is the pitch). Duty cycle sets the loudness (higher = louder).

```python
BUZZ_PIN = 5
BUZZ_FREQ_HZ = 2000
BUZZ_DUTY = 30000

buzz_pwm = PWM(Pin(BUZZ_PIN))
buzz_pwm.freq(BUZZ_FREQ_HZ)
buzz_pwm.duty_u16(0)
```

Create an ultrasonic sensor object that communicates via I2C (Qwiic mode).

```python
i2c = I2C(0, scl=Pin(7), sda=Pin(6))
sensor = UltrasonicSensor(i2c)

# If you are using native version of the sensor
# sensor = UltrasonicSensor(trig_pin=19, echo_pin=18)
```

Variables to control timing and state for how often to measure distance and how the buzzer will behave.

```python
MEAS_PERIOD_MS = 80             # Value that sets how often to take distance measurements
last_meas = time.ticks_ms()     # Store timestamp of last distance measurement
last_toggle = time.ticks_ms()   # Track timestamp of last time buzzer changed state
beep_on = False                 # Flag to save buzzer state
period_ms = -1                  # Sound behavior : -1 = silent, 0 = continuous, > 0 = beep period
BEEP_ON_TIME_MS = 0             # Duration of play time (ON time) of each beep
```

Mapping function to convert a value from one range to another. In this case, we are mapping distance value to a beep period.

```python
# Map function used to map distance to beep period
def map_distance_value(value, in_min, in_max, out_min, out_max):
    if value < in_min:
        value = in_min
    elif value > in_max:
        value = in_max
    return int((value - in_min) * (out_max - out_min) / (in_max - in_min) + out_min)
```

Main loop that constantly takes new measures, and plays the buzzer tone accordingly. Based on how close the object is, set one out of 3 sound modes (CONTINUOUS, BEEPING, SILENT). While 'beeping' map the measured distance value to a `period_ms` (beep period) and set how long each beep stays on: `BEEP_ON_TIME_MS`. The closer the object, the faster the beeping sound.

```python
# Main loop
while True:
    # Store current 'clock' time
    now = time.ticks_ms()
    
    # ticks_diff() used for measuring difference between 2 ticks
    # If 80 ms passed -> get reading & play sound
    if time.ticks_diff(now, last_meas) >= MEAS_PERIOD_MS:
        sensor.takeMeasure()
        last_meas = now # Store the time of measurement
        distance = sensor.getDistance() # Get distance from sensor
        # Choose 'sound mode' based on measured distance
        if distance <= CONTINUOUS_THRESHOLD_CM:
            period_ms = 0 # Set to continuous
        elif distance >= BEEP_START_DIST_CM:
            period_ms = -1 # Set to silent
        else:
            # Map distance reading from [35, 200] to a beep period [60, 700], store in period_ms
            period_ms = map_distance_value(distance, CONTINUOUS_THRESHOLD_CM, BEEP_START_DIST_CM, MIN_BEEP_PERIOD_MS, MAX_BEEP_PERIOD_MS)
        # Define duration of the 'ON time' of each beep, make the beep last a quarter of period cycle,
        # always between 10 and 50 milliseconds
        on_time = int(period_ms / 4)
        if on_time < 10:
            on_time = 10
        elif on_time > MAX_BEEP_ON_TIME_MS:
            on_time = MAX_BEEP_ON_TIME_MS
        BEEP_ON_TIME_MS = on_time

    # Based on period_ms, turn the buzzer ON or OFF depending on mode    
    # Continuous mode 
    if period_ms == 0:
        if not beep_on: # If the buzzer isn't ON
            # Play continuous sound and keep it turned ON
            buzz_pwm.duty_u16(BUZZ_DUTY)
            beep_on = True
            
    # Silent mode
    elif period_ms == -1:
        if beep_on: # If the buzzer is ON
            # Turn off buzzer
            buzz_pwm.duty_u16(0)
            beep_on = False
            
    # Beeping mode
    else:
        if not beep_on: # Currently OFF
            # Wait for 'silent' part to finish (period_ms - BEEP_ON_TIME_MS), then turn it ON
            if time.ticks_diff(now, last_toggle) >= (period_ms - BEEP_ON_TIME_MS):
                buzz_pwm.duty_u16(BUZZ_DUTY) # Turn ON buzzer
                beep_on = True # Change state
                last_toggle = now # Track toggle time
        else: # Currently ON
            # Wait until 'ON-time (BEEP_ON_TIME_MS)' has passed, then turn if OFF
            if time.ticks_diff(now, last_toggle) >= BEEP_ON_TIME_MS:
                buzz_pwm.duty_u16(0) # Turn OFF buzzer
                beep_on = False # Change state
                last_toggle = now # Track toggle time
```

## Full Example

<QuickLink 
  title="3.2_Ultrasonic_Sensor_Buzz.py"
  url="https://github.com/SolderedElectronics/PRIMJER" 
/>