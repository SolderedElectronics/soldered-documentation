---
slug: /ssd1306/arduino/drawing-shapes
title: Ssd1306 - Drawing shapes
id: ssd1306-arduino-5
hide_title: false
---

This page contains some examples of drawing and rendering shapes onto the OLED display.

---

## Rectangles

Rectangles can be drawn onto the screen using the `drawRect()` function by specifying the upper left x and y coordinates, as well as the height and width of the rectangle. In this example, we draw progressively smaller rectangles until we reach the center:

```cpp

void loop() {
  delay(1000);
  // Clear the last image shown on screen
  display.clearDisplay();
  //Initialize the upper left coordinates of the rectangle
  int16_t x=0,y=0;
  //Stop the loop only when either the x or y coordinate is over the middle of the screen
  while(x<display.width()/2 && y<display.height()/2)
  {

    //Make the width and height smaller as we get to the center
    int16_t rect_width=display.width()-(x*2);
    int16_t rect_height=display.height()-(y*2);

    //Draw the rectangle
    display.drawRect(x,y,rect_width,rect_height,SSD1306_WHITE);
    //Display each rectangle as we put it into the buffer
    display.display();
    delay(500);

    //Create a gap of 1 pixel between each rectangle
    x+=2;
    y+=2;
  }
}

```

<FunctionDocumentation
  functionName="display.drawRect(uint16_t x0, uint16_t y0, uint16_t w, uint16_t h, uint16_t color)"
  description="Puts a rectangle into the buffer, ready to be drawn"
  returnDescription="None"
  parameters={[ 
  { type: 'uint16_t', name: 'x0', description: "Upper left x coordinate of the rectangle" },
  { type: 'uint16_t', name: 'y0', description: "Upper y coordinate of the rectangle" },
  { type: 'uint16_t', name: 'w', description: "Width of the rectangle" },
  { type: 'uint16_t', name: 'h', description: "Height of the rectangle" },
  { type: 'uint16_t', name: 'color', description: "Color of the rectangle" },
  ]}
/>

---

## Circles

Circles can be drawn onto the screen using the `drawCircle()` function by specifying the x and y coordinates of the circle's center, its radius, and its color. In this example, we draw 10-pixel-wide circles until they reach the end of the screen:

```cpp
void loop() {
  delay(1000);
  // Clear the last image shown on screen
  display.clearDisplay();
  int16_t x,y;
  //Iterate the y coordinates every time we fill a row with circles
  for(y=4;y<display.height();y+=8)
  {
    for(x=4;x<display.width();x+=8)
    {
      //Draw a circle at current x and y with a radius of 4 pixels
      display.drawCircle(x, y, 4, SSD1306_WHITE);
      //Display the circle
      display.display();
      delay(300);
    }
  }
}

```

<FunctionDocumentation
  functionName="display.drawCircle(uint16_t x0, uint16_t y0, uint16_t r, uint16_t color)"
  description="Puts a circle into the buffer, ready to be drawn"
  returnDescription="None"
  parameters={[ 
  { type: 'uint16_t', name: 'x0', description: "x coordinate of centre of circle" },
  { type: 'uint16_t', name: 'y0', description: "y coordinate of centre of circle" },
  { type: 'uint16_t', name: 'r', description: "Radius of circle" },
  { type: 'uint16_t', name: 'color', description: "Color of the circle" },
  ]}
/>