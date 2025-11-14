---
slug: /nula-max-rp2350/hdmi-output
title: NULA Max RP2350 - HDMI Output
sidebar_label: HDMI Output
id: max-rp2350_hdmi_output
pagination_prev: null
hide_title: True
---

# HDMI Output

The **Soldered NULA Max RP2350** board features built-in **HDMI output capability**, enabling it to display images, graphics, and animations directly on any HDMI-compatible display. This is achieved through the **PicoDVI library**, which uses the RP2350’s PIO (Programmable I/O) system to **bit-bang a DVI/HDMI signal entirely in software**—no dedicated video hardware required. The implementation supports **framebuffer-based rendering**, allowing smooth animation and static image output in various color modes. Despite being a software-driven approach, PicoDVI efficiently leverages the RP2350’s dual-core performance and fast I/O to deliver surprisingly fluid HDMI visuals, making the NULA Max ideal for compact embedded projects, UI displays, and creative graphics demos.

<CenteredImage src="/img/nula-max-rp2350/hdmi_showcase.jpg" alt="Showcase of the HDMI capabilities of the RP2350 board" caption="Showcase of a screensaver on the NULA Max board"/>

We have made a fork of the original PicoDVI library, which makes it and the examples plug-and-play with our NULA Max RP2350 board. The library can be found below:

<QuickLink
  title="PicoDVI - Soldered Electronics fork"
  description="A fork of the original PicoDVI library specifically tailored to work with the Soldered NULA Max RP2350 board"
  url="https://github.com/SolderedElectronics/PicoDVI"
/>

Download the library as a .zip file and then, in the Arduino IDE, go to **Sketch->Include Library->Add .ZIP Library**.

The library implements the **Adafruit GFX** library, which greatly simplifies the drawing process.

## Supported resolutions and framerates

The PicoDVI library supports a range of resolutions and framerates for your specific needs; they are defined in the following table:

            | Resolution | Framerate |
            |------------|-----------|
            | 320x240    | 60fps     |
            | 400x240    | 30fps     |
            | 400x240    | 60fps     |
            | 640x480    | 30fps     |
            | 640x480    | 60fps     |
            | 800x480    | 30fps     |
            | 800x480    | 60fps     |
            | 640x240    | 60fps     |
            | 800x240    | 30fps     |
            | 800x240    | 60fps     |

It is also possible to output color in 1-bit, 8-bit, and 16-bit modes.

<WarningBox>While all of these resolutions are supported, the biggest bottleneck here is the RAM size of the RP2350. Some resolutions may only be available in 1-bit mode. When running an example from our library, the onboard WSLED will blink red if there is insufficient RAM to run it.</WarningBox>

## Simple example

In the following example, we will draw a line, a circle, and a triangle on the screen in 800x480 resolution at 30fps.

```cpp
// Simple 1-bit Adafruit_GFX-compatible framebuffer for PicoDVI.

#include <PicoDVI.h>
#include <Adafruit_NeoPixel.h>

// Here's how a 640x480 1-bit (black, white) framebuffer is declared.
// Second argument ('false' here) means NO double-buffering; all drawing
// operations are shown as they occur. Third argument is a hardware
// configuration — examples are written for Soldered NULA RP2350
DVIGFX1 display(DVI_RES_800x480p30, false, soldered_nula_rp2350_dvi_cfg);

// Configure WSLED parameters
Adafruit_NeoPixel pixels(1, 26); // WSLED object

void setup() { // Runs once on startup
  // Initialize the onboard NeoPixel RGB, used for debugging
  pixels.begin();

  // Try to initialize the framebuffer for the video output
  if (!display.begin()) { 
    // Blink LED red infinitely - something's wrong
    while (true)
    {
        pixels.setPixelColor(0, pixels.Color(0x20, 0, 0)); // Set the color to red
        pixels.show();
        delay(400);
        pixels.clear();
        pixels.show();
        delay(400);
    }
  }
  // Draw a circle with the center at (400,240), a radius of 200px, and the color white (1)
  display.drawCircle(400, 240, 200, 1);

  // Draw a triangle with vertices at (200,240), (400,40), (600,240) and the color white (1)
  display.drawTriangle(200, 240, 400, 40, 600, 240, 1);

  // Draw a line from (200,440) to (600,440) with the color white (1)
  display.drawLine(200, 440, 600, 440, 1);
}

void loop() {

}
```

<FunctionDocumentation
  functionName="display.begin()"
  description="Initializes the framebuffer for writing to the display"
  returnDescription="Boolean value, true if the buffer initialization was successful, false if not"
  parameters={[]}
/>

<FunctionDocumentation
  functionName="display.drawCircle()"
  description="Draws a circle outline on the display."
  returnDescription="none"
  parameters={[
    { type: 'int', name: 'x', description: 'The x-coordinate of the circle center.' },
    { type: 'int', name: 'y', description: 'The y-coordinate of the circle center.' },
    { type: 'int', name: 'radius', description: 'The radius of the circle.' },
    { type: 'uint8_t', name: 'color', description: 'The color of the circle outline.' },
  ]}
/>

<FunctionDocumentation
  functionName="display.drawTriangle()"
  description="Draws a triangle outline on the display."
  returnDescription="none"
  parameters={[
    { type: 'int', name: 'x0', description: 'The x-coordinate of the first vertex.' },
    { type: 'int', name: 'y0', description: 'The y-coordinate of the first vertex.' },
    { type: 'int', name: 'x1', description: 'The x-coordinate of the second vertex.' },
    { type: 'int', name: 'y1', description: 'The y-coordinate of the second vertex.' },
    { type: 'int', name: 'x2', description: 'The x-coordinate of the third vertex.' },
    { type: 'int', name: 'y2', description: 'The y-coordinate of the third vertex.' },
    { type: 'uint8_t', name: 'color', description: 'The color of the triangle outline.' },
  ]}
/>

<FunctionDocumentation
  functionName="display.drawLine()"
  description="Draws a straight line between two points on the display."
  returnDescription="none"
  parameters={[
    { type: 'int', name: 'x0', description: 'The x-coordinate of the starting point.' },
    { type: 'int', name: 'y0', description: 'The y-coordinate of the starting point.' },
    { type: 'int', name: 'x1', description: 'The x-coordinate of the ending point.' },
    { type: 'int', name: 'y1', description: 'The y-coordinate of the ending point.' },
    { type: 'uint8_t', name: 'color', description: 'The color of the line.' },
  ]}
/>

<CenteredImage src="/img/nula-max-rp2350/draw_example.jpg" alt="HDMI output" caption="Output on an HDMI monitor"/>

## Text Example

The following example shows how to draw text on the screen.

```cpp
// 1-bit (black, white) text mode for PicoDVI.

#include <PicoDVI.h>
#include <Adafruit_NeoPixel.h>
// Here's how an 80x30 character display is declared. The first argument,
// resolution, is the full display pixel count; character cells are 8x8 pixels,
// yielding the 80x30 result. The 640x240 resolution uses "tall" pixels, which is
// very reminiscent of the classic IBM VGA mode. The second argument is a hardware
// configuration — examples are written for Soldered NULA RP2350.
DVItext1 display(DVI_RES_640x240p60, soldered_nula_rp2350_dvi_cfg);

// Configure WSLED parameters
Adafruit_NeoPixel pixels(1, 26); // WSLED object

void setup() { // Runs once on startup
  // Initialize the onboard NeoPixel RGB, used for debugging
  pixels.begin();

  // Try to initialize the display framebuffer
  if (!display.begin()) { 
    // Blink LED red infinitely - something's wrong
    while (true)
    {
        pixels.setPixelColor(0, pixels.Color(0x20, 0, 0)); // Set the color to red
        pixels.show();
        delay(400);
        pixels.clear();
        pixels.show();
        delay(400);
    }
  }

  // Write to the first line and then move to the next line
  display.println("Hello World!");
  // Continue writing on the next line
  display.print("This is a simple example of drawing some text to the display :D");
}

void loop() {
}
```

<FunctionDocumentation
  functionName="display.print(const char* _c)"
  description="Prints text at the previously set cursor position. This is the standard Arduino print function used in many native Arduino objects and libraries."
  returnDescription="size_t, number of bytes printed."
  parameters={[ 
    { type: 'const char *', name: '_c', description: 'The C-style string to print on the display.' }
  ]}
/>

<FunctionDocumentation
  functionName="display.print(const char* _c)"
  description="Prints text at the previously set cursor position. This is the standard Arduino print function used in many native Arduino objects and libraries."
  returnDescription="size_t, number of bytes printed."
  parameters={[ 
    { type: 'const char *', name: '_c', description: 'The C-style string to print on the display.' }
  ]}
/>

<CenteredImage src="/img/nula-max-rp2350/text_example.jpg" alt="HDMI output" caption="Output on an HDMI monitor"/>

## Animation example

The following is an animation showing the speed at which the display can refresh.

<CenteredImage src="/img/nula-max-rp2350/animation.webp" alt="HDMI output" caption="Output on an HDMI monitor"/>

<InfoBox>If you are experiencing horizontal red lines, in the Arduino IDE, go to Tools->Optimise->Optimise Even More (-O3)</InfoBox>

Code is available at the link below:
<QuickLink
  title="Double buffer example"
  description="An example showing multi-colored balls jumping on the screen"
  url="https://github.com/SolderedElectronics/PicoDVI/blob/master/examples/8bit_double_buffer/8bit_double_buffer.ino"
/>