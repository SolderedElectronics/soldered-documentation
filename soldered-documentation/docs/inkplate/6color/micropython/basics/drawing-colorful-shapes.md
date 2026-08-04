---  
slug: /inkplate/6color/micropython/basics/drawing-shapes
title: Inkplate 6COLOR – Drawing colorful shapes
sidebar_label: Drawing colorful shapes
id: drawing-shapes  
hide_title: false  
---

## Colorful shapes example

<InfoBox> See all available colors and their values **[here](/inkplate/6color/micropython/basics/print-text#simple-colored-text-example)**. </InfoBox>

<CenteredImage src="/img/6color/basic-color.jpg" alt="Expected output on Inkplate display" caption="Geometric Shapes output on display" />

```python
# Include all the required libraries
from inkplate6_color import Inkplate

# Create Inkplate object
inkplate = Inkplate()


# Initialize the display, needs to be called only once
inkplate.begin()

# Let's draw some shapes!
# This example will draw shapes around the upper left corner, and then rotate the screen
# This creates a symmetrical-looking pattern of various shapes
for r in range(4):
    # Sets the screen rotation
    inkplate.set_rotation(r)

    # All drawing functions
    # Available colors are:
    # Black, white, green, blue, red, yellow, orange
    inkplate.draw_pixel(100, 100, inkplate.BLACK)
    inkplate.draw_rect(50, 50, 75, 75, inkplate.GREEN)
    inkplate.draw_circle(200, 200, 30, inkplate.BLUE)
    inkplate.fill_circle(300, 300, 30, inkplate.RED)
    inkplate.draw_fast_hline(20, 100, 50, inkplate.BLACK)
    inkplate.draw_fast_vline(100, 20, 50, inkplate.ORANGE)
    inkplate.draw_line(100, 100, 400, 400, inkplate.ORANGE)
    inkplate.draw_round_rect(100, 10, 100, 100, 10, inkplate.BLACK)
    inkplate.fill_round_rect(10, 100, 100, 100, 10, inkplate.YELLOW)
    inkplate.draw_triangle(300, 100, 400, 150, 400, 100, inkplate.BLACK)

# Reset the rotation
inkplate.set_rotation(0)

# Show on the display
inkplate.display()
```

<FunctionDocumentation
  functionName="inkplate.set_rotation()"
  description="Sets the rotation of the screen, adjusting the (x, y) coordinate origin point"
  returnType="none"
  parameters={[ 
    { type: 'int', name: 'x', description: 'Value from 0 to 3 (1 rotates by 90 degrees, 2 by 180 degrees, 3 by 270 degrees, 0 is default rotation)' }
  ]}
/>
<FunctionDocumentation
  functionName="inkplate.draw_pixel()"
  description="Sets pixel data on given (x, y) position"
  returnType="none"
  parameters={[ 
    { type: 'int', name: 'x', description: 'X coordinate' },
    { type: 'int', name: 'y', description: 'Y coordinate' },
    { type: 'int', name: 'c', description: 'Pixel color' }
  ]}
/>
<FunctionDocumentation
  functionName="inkplate.draw_rect()"
  description="Function to draw a rectangle"
  returnType="none"
  parameters={[ 
    { type: 'int', name: 'x', description: 'X coordinate' },
    { type: 'int', name: 'y', description: 'Y coordinate' },
    { type: 'int', name: 'width', description: 'Rectangle width' },
    { type: 'int', name: 'height', description: 'Rectangle height' },
    { type: 'int', name: 'c', description: 'Rectangle color' }
  ]}
/>
<FunctionDocumentation
  functionName="inkplate.draw_circle()"
  description="Function to draw a circle"
  returnType="none"
  parameters={[ 
    { type: 'int', name: 'x', description: 'X coordinate' },
    { type: 'int', name: 'y', description: 'Y coordinate' },
    { type: 'int', name: 'r', description: 'Circle radius' },
    { type: 'int', name: 'c', description: 'Circle color' }
  ]}
/>
<FunctionDocumentation
  functionName="inkplate.fill_circle()"
  description="Function to draw a filled circle with specified color"
  returnType="none"
  parameters={[ 
    { type: 'int', name: 'x', description: 'X coordinate' },
    { type: 'int', name: 'y', description: 'Y coordinate' },
    { type: 'int', name: 'r', description: 'Circle radius' },
    { type: 'int', name: 'c', description: 'Circle fill color' }
  ]}
/>
<FunctionDocumentation
  functionName="inkplate.draw_fast_hline()"
  description="Function to draw a horizontal line"
  returnType="none"
  parameters={[ 
    { type: 'int', name: 'x', description: 'X start coordinate' },
    { type: 'int', name: 'y', description: 'Y start coordinate' },
    { type: 'int', name: 'width', description: 'Line width to set how many pixels to draw' },
    { type: 'int', name: 'c', description: 'Line color' }
  ]}
/>
<FunctionDocumentation
  functionName="inkplate.draw_fast_vline()"
  description="Function to draw a vertical line"
  returnType="none"
  parameters={[ 
    { type: 'int', name: 'x', description: 'X start coordinate' },
    { type: 'int', name: 'y', description: 'Y start coordinate' },
    { type: 'int', name: 'height', description: 'Line height to set how many pixels to draw' },
    { type: 'int', name: 'c', description: 'Line color' }
  ]}
/>
<FunctionDocumentation
  functionName="inkplate.draw_line()"
  description="Function to draw a line from start to end"
  returnType="none"
  parameters={[ 
    { type: 'int', name: 'x0', description: 'X coordinate for first point' },
    { type: 'int', name: 'y0', description: 'Y coordinate for first point' },
    { type: 'int', name: 'x1', description: 'X coordinate for second point' },
    { type: 'int', name: 'y1', description: 'Y coordinate for second point' },
    { type: 'int', name: 'c', description: 'Line color' }
  ]}
/>
<FunctionDocumentation
  functionName="inkplate.draw_round_rect()"
  description="Function to draw a rectangle with rounded edges"
  returnType="none"
  parameters={[ 
    { type: 'int', name: 'x', description: 'X coordinate' },
    { type: 'int', name: 'y', description: 'Y coordinate' },
    { type: 'int', name: 'width', description: 'Rectangle width' },
    { type: 'int', name: 'height', description: 'Rectangle height' },
    { type: 'int', name: 'radius', description: 'Border radius' },
    { type: 'int', name: 'c', description: 'Rectangle color' }
  ]}
/>
<FunctionDocumentation
  functionName="inkplate.fill_round_rect()"
  description="Function to draw a rounded rectangled filled with specified color"
  returnType="none"
  parameters={[ 
    { type: 'int', name: 'x', description: 'X coordinate' },
    { type: 'int', name: 'y', description: 'Y coordinate' },
    { type: 'int', name: 'width', description: 'Rectangle width' },
    { type: 'int', name: 'height', description: 'Rectangle height' },
    { type: 'int', name: 'radius', description: 'Border radius' },
    { type: 'int', name: 'c', description: 'Rectangle color' }
  ]}
/>
<FunctionDocumentation
  functionName="inkplate.draw_triangle()"
  description="Function to draw a triangle"
  returnType="none"
  parameters={[ 
    { type: 'int', name: 'x0', description: 'X coordinate for first point' },
    { type: 'int', name: 'y0', description: 'Y coordinate for first point' },
    { type: 'int', name: 'x1', description: 'X coordinate for second point' },
    { type: 'int', name: 'y1', description: 'Y coordinate for second point' },
    { type: 'int', name: 'x2', description: 'X coordinate for third point' },
    { type: 'int', name: 'y2', description: 'Y coordinate for third point' },
    { type: 'int', name: 'c', description: 'Triangle color' }
  ]}
/>
<FunctionDocumentation
  functionName="inkplate.fill_triangle()"
  description="Function to draw a triangle filled with specified color"
  returnType="none"
  parameters={[ 
    { type: 'int', name: 'x0', description: 'X coordinate for first point' },
    { type: 'int', name: 'y0', description: 'Y coordinate for first point' },
    { type: 'int', name: 'x1', description: 'X coordinate for second point' },
    { type: 'int', name: 'y1', description: 'Y coordinate for second point' },
    { type: 'int', name: 'x2', description: 'X coordinate for third point' },
    { type: 'int', name: 'y2', description: 'Y coordinate for third point' },
    { type: 'int', name: 'c', description: 'Triangle fill color' }
  ]}
/>