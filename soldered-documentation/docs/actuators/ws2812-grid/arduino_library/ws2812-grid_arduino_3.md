---
slug: /ws2812-grid/arduino/troubleshooting 
title: Troubleshooting
id: ws2812-grid-arduino-3 
hide_title: False
pagination_next: null
---
Here are the most common issues users run into with the WS2812 Grid and how to fix them.
 
<ExpandableSection title="The grid doesn't light up at all">
Start with the power and data wiring. Check the following:
 
- **VCC and GND** are connected firmly. A loose GND is the most common cause of a completely dark grid.
- **DIN** is connected to the correct Arduino pin - the one passed to the `WS2812Grid` constructor in your sketch.
- `grid.begin()` is called in `setup()`. Without it the driver is never initialized and no data reaches the LEDs.
- `grid.show()` is called after `setPixel()` or `fill()`. Pixel data is buffered in RAM until `show()` pushes it to the hardware - forgetting this call means the display stays dark even though the buffer was updated.
- Verify that `grid.setBrightness()` is not set to 0.
</ExpandableSection>
<ExpandableSection title="Only the first few LEDs light up, or the colors look wrong">
This is almost always a signal integrity problem on the DIN line.
 
- **Wire length:** Keep the DIN wire short (under 30 cm). Long wires act as antennas and corrupt the one-wire protocol WS2812B uses.
- **Logic level mismatch:** WS2812B expects a high signal of at least 0.7 × VDD. If the LEDs are powered at 5V but your microcontroller outputs 3.3V, the signal may be marginal. The board already includes a **100 Ω resistor (R1)** on the DIN line, but for longer cable runs or persistent glitches, add a 74HCT125 or similar level shifter between the MCU and DIN.
- **Missing decoupling:** The board has a 100 nF capacitor across each LED's VDD/GND pin (64 total), so per-LED decoupling is already handled. Add a bulk electrolytic capacitor (470-1000 µF) across the VCC/GND supply rail at your power entry point to absorb inrush current.
- **Data resistor:** A 100 Ω series resistor is already present on the board's DIN pad (R1). Do **not** add another external resistor in series - stacking resistors will attenuate the signal too much.
</ExpandableSection>
<ExpandableSection title="The pixel positions look shifted or mirrored">
The WS2812 Grid uses a **serpentine (boustrophedon) layout** inside each 8×8 panel: even rows run left-to-right, odd rows run right-to-left. The library's `xyToIndex()` handles this automatically as long as you use `setPixel(x, y, ...)` with the correct coordinate system (x = 0 is the left column, y = 0 is the top row).
 
If pixels appear in the wrong place:
- Make sure you are not calling `setPixelColor()` directly with a raw linear index calculated by hand. Always use `setPixel(x, y, ...)` or call `xyToIndex()` to get the correct index first.
- If you have a multi-panel (e.g. 16×8 or 8×16) setup, remember that panels are chained **column-first**: all panels in the leftmost panel-column come first in the data chain, then the next column of panels, and so on.
</ExpandableSection>
<ExpandableSection title="The grid flickers or resets randomly">
Flickering under load almost always means the power supply cannot keep up with the current demand.
 
- The board requires **5V** - there is no onboard regulator. Make sure your supply is actually 5V and not 3.3V.
- A full 8×8 grid at full white (`fill(255, 255, 255)`) draws roughly **3.8 A at 5V**. Most USB ports supply only 0.5-2 A. Use a dedicated 5V supply rated for at least 2 A, or keep brightness low (40-80 out of 255 is plenty for most projects).
- The board already has a 100 nF decoupling capacitor on each of the 64 LEDs' VDD pins. To absorb larger inrush spikes, add a **470-1000 µF electrolytic capacitor** across the VCC and GND supply rail at the power entry point (not on the board itself).
- Connect the grid's VCC and GND **directly to your power supply** - do not route the grid's power through the Arduino board. Share only GND between the Arduino and the power supply.
</ExpandableSection>
<ExpandableSection title="The animation runs very slowly or freezes the rest of my code">
`grid.show()` blocks for roughly 30 µs per LED while clocking out the data (about 2 ms for a full 8×8 grid). This is normally not noticeable, but a tight loop that calls `show()` hundreds of times per second can starve other tasks.
 
- Call `show()` only once per animation frame - update all pixels first, then call `show()` once.
- If you need non-blocking behavior, consider restructuring your animation loop with `millis()`-based timing rather than `delay()`.
- Very long `delay()` calls inside animation functions (like `rainbowGrid()`) will block the entire `loop()` for the duration of the animation. Break large animations into small state-machine steps if you need to handle other work concurrently.
</ExpandableSection>
<InfoBox>In case you haven't found the answer to your question, please **contact us** via [**this**](https://soldered.com/contact/) link.</InfoBox>
 