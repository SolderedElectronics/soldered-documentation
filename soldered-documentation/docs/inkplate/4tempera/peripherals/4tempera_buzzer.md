---
slug: /inkplate/4tempera/peripherals/buzzer
title: Buzzer
id: 4tempera-periph-buzzer
hide_title: true
---

<SectionTitle title="Buzzer" backgroundImage="/img/inkplate_2/hardware.png" />

The Inkplate 4 TEMPERA features a small **built-in buzzer** that can be used for sound effects, notifications, or simple melodies. It supports tone generation and frequency control through software.

---

## Initialization

Before using the buzzer, it must be initialized with `initBuzzer()`:

```cpp
inkplate.initBuzzer();
```

<FunctionDocumentation
  functionName="inkplate.initBuzzer()"
  description="Initializes the onboard buzzer hardware. Must be called before any beep functions."
  returnDescription="None"
/>

---

## Playing Beeps

### Basic beep

The most straightforward way to produce a sound is by using `beep(durationMs)`:

```cpp
inkplate.beep(80); // 80ms short beep
```

<FunctionDocumentation
  functionName="inkplate.beep()"
  description="Plays a short beep of a specified duration."
  returnDescription="None"
  parameters={[{ type: 'int', name: 'durationMs', description: "How long the beep should last, in milliseconds." }]}
/>

---

### Beep with frequency

You can also specify the frequency of the beep to create different tones:

```cpp
inkplate.beep(300, 750);   // 300ms beep at 750Hz
inkplate.beep(300, 2400);  // 300ms beep at 2400Hz
```

<FunctionDocumentation
  functionName="inkplate.beep()"
  description="Plays a beep with a specified duration and frequency."
  returnDescription="None"
  parameters={[
    { type: 'int', name: 'durationMs', description: "Duration of the beep in milliseconds." },
    { type: 'int', name: 'frequencyHz', description: "Approximate frequency of the beep in Hz (between 572 Hz and 2933 Hz)." }
  ]}
/>

---

### Manual on/off control

You can also control the buzzer manually:

```cpp
inkplate.beepOn();   // Turn buzzer on
delay(200);
inkplate.beepOff();  // Turn buzzer off
```

<FunctionDocumentation functionName="inkplate.beepOn()" description="Turns the buzzer on indefinitely." returnDescription="None" />
<FunctionDocumentation functionName="inkplate.beepOff()" description="Turns the buzzer off." returnDescription="None" />

---

## Full Example

In the official Inkplate example, a small melody is played using notes from a **Cmaj7 chord** — C (523 Hz), E (659 Hz), G (783 Hz), and B (987 Hz). It also demonstrates multiple playback methods and variable timing.

The loop alternates between playing single notes and repeated tones to simulate musical phrasing:

```cpp
int chord[4] = {523, 659, 783, 987};
int currentNoteIndex = 0;
int repeatCounter = 0;

void loop() {
    if (repeatCounter < 2) {
        inkplate.beep(100, chord[currentNoteIndex]);
        delay(600);
    } else {
        inkplate.beep(100, chord[currentNoteIndex]);
        delay(250);
        inkplate.beep(50, chord[currentNoteIndex]);
        delay(300);
    }

    currentNoteIndex++;
    if (currentNoteIndex >= 4) {
        currentNoteIndex = 0;
        repeatCounter++;
        if (repeatCounter >= 4) {
            repeatCounter = 0;
            delay(3000);
        }
    }
}
```

<QuickLink
  title="Inkplate4TEMPERA_Buzzer.ino"
  description="Complete example using basic and advanced buzzer control, including tones and melody."
  url="https://github.com/SolderedElectronics/Inkplate-Arduino-library/blob/master/examples/Inkplate4TEMPERA/Advanced/Sensors/Inkplate4TEMPERA_Buzzer/Inkplate4TEMPERA_Buzzer.ino"
/>