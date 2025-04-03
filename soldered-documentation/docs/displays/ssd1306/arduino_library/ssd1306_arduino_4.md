---  
slug: /ssd1306/arduino/writing-text  
title: Writing text  
id: ssd1306-arduino-4   
hide_title: False  
---

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

<CenteredImage src="/img/ssd1306/text.png" alt="Hello world displayed"/>

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