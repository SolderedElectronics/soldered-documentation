---
slug: /ssd1306_new/arduino/examples 
title: Examples
id: ssd1306_new-arduino-2 
hide_title: False
---

## Initializing the screen

To use the SSD1306 OLED Display, first include the required library, create the display object, and initialize the display in the `setup()` function.

```cpp
//Include the library
#include "OLED-Display-SOLDERED.h"

//Create an instance of the OLED display
OLED_Display display;

void setup() {
  //Initialize serial communication
  Serial.begin(115200);

  //Initialize the display
  if(display.begin())
  {
    //If the display initialized successfully, print a message and show the logo on the display
    Serial.println("OLED display initialized successfully!");
    display.display();
  }
  else
  {
    Serial.println("OLED failed to initialize, check connection");
  }
}

void loop()
{
  
}

```
<InfoBox>If you did everything correctly, you should be greeted with the **Soldered logo!**</InfoBox>

<WarningBox>Image coming soon.</WarningBox>


<FunctionDocumentation
  functionName="display.begin()"
  description="Initializes the OLED Display, setting up communication over I2C and setting the resolution to 128x64"
  returnDescription="Boolean value, returns true if the display was successfully initialized, false if not"
  parameters={[]}
/>

<FunctionDocumentation
  functionName="display.display()"
  description="Displays the content that was previously defined to be drawn"
  returnDescription="None"
  parameters={[]}
/>

<WarningBox>The display is only updated when the display() function is called!</WarningBox>

---

## Writing text

To write text onto the display, you must define the text size, color, and the starting coordinate from which the text will be drawn onto the display.

```cpp
void loop() {
  delay(1000);
  // Clear the last image shown on screen
  display.clearDisplay();
  // Normal 1:1 pixel scale
  display.setTextSize(1);             
  // Draw white text 
  display.setTextColor(SSD1306_WHITE);
  // Start at top-left corner
  display.setCursor(0, 0);
  // Message we want to display             
  String message = "Hello World!";
  // Inform the display of the text you want to print
  display.print(message);
  // Display the message
  display.display();
}
```

<WarningBox>Image coming soon.</WarningBox>

<FunctionDocumentation
  functionName="display.clearDisplay()"
  description="Clears contents of display buffer (sets all pixels to off)."
  returnDescription="None"
  parameters={[]}
/>
<WarningBox>Because the clearDisplay() function only clears the buffer, it has no immediate effect on the screen. The display() function must still be called.</WarningBox>

<FunctionDocumentation
  functionName="display.setTextColor(uint16_t c, uint16_t bg)"
  description="Set text font color with custom background color"
  returnDescription="None"
  parameters={[
  { type: 'int16_t', name: 'c', description: "What color the text will be" },
  { type: 'int16_t', name: 'bg', description: "Optional, what color the background will be, if not set then it is transparent" },
  ]}
/>

<FunctionDocumentation
  functionName="display.setCursor(int16_t x, int16_t y)"
  description="Sets text cursor location"
  returnDescription="None"
  parameters={[
  { type: 'int16_t', name: 'x', description: "x coordinate of cursor" },
  { type: 'int16_t', name: 'y', description: "y coordinate of cursor" },
  ]}
/>

<FunctionDocumentation
  functionName="display.print(const char* message)"
  description="Stores the given message into buffer"
  returnDescription="None"
  parameters={[
  { type: 'const char*', name: 'message', description: "text that will be shown on display" },
  ]}
/>

---

## Drawing shapes

This page contains some examples of drawing and rendering shapes onto the OLED display.

---

### Rectangles

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

### Circles

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

---

## More examples

Since this display offers so much to explore, we encourage you to review the accompanying documentation and examples:

See how advanced functions such as text scrolling and bitmap rendering work by checking out the example included with the library:

<QuickLink  
  title="OLED Display Drawing Example"  
  description="Drawing examples for the SSD1306 OLED Display"  
  url="https://github.com/SolderedElectronics/Soldered-OLED-Display-Arduino-Library/blob/main/examples/Drawing_Example/Drawing_Example.ino"  
/>  

<InfoBox>You can also open the given example inside the Arduino IDE by going to:  
**File>Examples>Soldered Oled Display Arduino Library>Drawing_Example**</InfoBox>

---

## Documentation

You can find in-depth details about specific functions in the **Adafruit GFX Graphics Library** by following the link below:

<QuickLink  
  title="Adafruit GFX Graphics Library"  
  description="Documentation for the Adafruit GFX Graphics Library"  
  url="https://cdn-learn.adafruit.com/downloads/pdf/adafruit-gfx-graphics-library.pdf"  
/>
