---  
slug: /inkplate/6color/micropython/basics/drawing_objects
title: Inkplate 6COLOR – Draw colorful objects
sidebar_label: Draw colorful objects
id: drawing-objects  
hide_title: false  
---

## Drawing Geometric Shapes

<CenteredImage src="/img/6color/basic-color.jpg" alt="Expected output on Inkplate display" caption="Geometric Shapes output on display" />

```python
# Let's draw some shapes!
# This example will draw shapes around the upper left corner, and then rotate the screen
# This creates a symmetrical-looking pattern of various shapes
for r in range(4):

    # Sets the screen rotation
    display.setRotation(r)

    # All drawing functions
    # Available colors are:
    # Black, white, green, blue, red, yellow, orange
    display.drawPixel(100, 100, display.BLACK)
    display.drawRect(50, 50, 75, 75, display.GREEN)
    display.drawCircle(200, 200, 30, display.BLUE)
    display.fillCircle(300, 300, 30, display.RED)
    display.drawFastHLine(20, 100, 50, display.BLACK)
    display.drawFastVLine(100, 20, 50, display.ORANGE)
    display.drawLine(100, 100, 400, 400, display.ORANGE)
    display.drawRoundRect(100, 10, 100, 100, 10, display.BLACK)
    display.fillRoundRect(10, 100, 100, 100, 10, display.YELLOW)
    display.drawTriangle(300, 100, 400, 150, 400, 100, display.BLACK)

# Reset the rotation
display.setRotation(0)

# Show on the display
display.display()
```

## Drawing Functions Definitions

<FunctionDocumentation
  functionName="inkplate.setRotation()"
  description="Sets the rotation of the screen, adjusting the (x, y) coordinate origin point"
  returnDescription="None"
  parameters={[ 
    { type: 'int', name: 'x', description: 'Value from 0 to 3 (1 rotates by 90 degrees, 2 by 180 degrees, 3 by 270 degrees, 0 is default rotation)' }
  ]}
/>
<FunctionDocumentation
  functionName="inkplate.drawPixel()"
  description="Sets pixel data on given (x, y) position"
  returnDescription="None"
  parameters={[ 
    { type: 'int', name: 'x', description: 'X coordinate' },
    { type: 'int', name: 'y', description: 'Y coordinate' },
    { type: 'int', name: 'c', description: 'Pixel color' }
  ]}
/>
<FunctionDocumentation
  functionName="inkplate.drawRect()"
  description="Function to draw a rectangle"
  returnDescription="None"
  parameters={[ 
    { type: 'int', name: 'x', description: 'X coordinate' },
    { type: 'int', name: 'y', description: 'Y coordinate' },
    { type: 'int', name: 'width', description: 'Rectangle width' },
    { type: 'int', name: 'height', description: 'Rectangle height' },
    { type: 'int', name: 'c', description: 'Rectangle color' }
  ]}
/>
<FunctionDocumentation
  functionName="inkplate.drawCircle()"
  description="Function to draw a circle"
  returnDescription="None"
  parameters={[ 
    { type: 'int', name: 'x', description: 'X coordinate' },
    { type: 'int', name: 'y', description: 'Y coordinate' },
    { type: 'int', name: 'r', description: 'Circle radius' },
    { type: 'int', name: 'c', description: 'Circle color' }
  ]}
/>
<FunctionDocumentation
  functionName="inkplate.fillCircle()"
  description="Function to draw a filled circle with specified color"
  returnDescription="None"
  parameters={[ 
    { type: 'int', name: 'x', description: 'X coordinate' },
    { type: 'int', name: 'y', description: 'Y coordinate' },
    { type: 'int', name: 'r', description: 'Circle radius' },
    { type: 'int', name: 'c', description: 'Circle fill color' }
  ]}
/>
<FunctionDocumentation
  functionName="inkplate.drawFastHLine()"
  description="Function to draw a horizontal line"
  returnDescription="None"
  parameters={[ 
    { type: 'int', name: 'x', description: 'X start coordinate' },
    { type: 'int', name: 'y', description: 'Y start coordinate' },
    { type: 'int', name: 'width', description: 'Line width to set how many pixels to draw' },
    { type: 'int', name: 'c', description: 'Line color' }
  ]}
/>
<FunctionDocumentation
  functionName="inkplate.drawFastVLine()"
  description="Function to draw a vertical line"
  returnDescription="None"
  parameters={[ 
    { type: 'int', name: 'x', description: 'X coordinate' },
    { type: 'int', name: 'y', description: 'Y coordinate' },
    { type: 'int', name: 'width', description: 'Line width to set how many pixels to draw' },
    { type: 'int', name: 'c', description: 'Line color' }
  ]}
/>
<FunctionDocumentation
  functionName="inkplate.drawLine()"
  description="Function to draw a line from start to end"
  returnDescription="None"
  parameters={[ 
    { type: 'int', name: 'x0', description: 'X coordinate' },
    { type: 'int', name: 'y0', description: 'Y coordinate' },
    { type: 'int', name: 'x1', description: 'X coordinate' },
    { type: 'int', name: 'y1', description: 'Y coordinate' },
    { type: 'int', name: 'width', description: 'Line width' },
    { type: 'int', name: 'c', description: 'Line color' }
  ]}
/>
<FunctionDocumentation
  functionName="inkplate.drawRoundRect()"
  description="Function to draw a rectangle with rounded edges"
  returnDescription="None"
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
  functionName="inkplate.fillRoundRect()"
  description="Function to draw a rounded rectangled filled with specified color"
  returnDescription="None"
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
  functionName="inkplate.drawTriangle()"
  description="Function to draw a triangle"
  returnDescription="None"
  parameters={[ 
    { type: 'int', name: 'x0', description: 'X0 coordinate for first point' },
    { type: 'int', name: 'y0', description: 'Y0 coordinate for first point' },
    { type: 'int', name: 'x1', description: 'X1 coordinate for second point' },
    { type: 'int', name: 'y1', description: 'Y1 coordinate for second point' },
    { type: 'int', name: 'x2', description: 'X2 coordinate for third point' },
    { type: 'int', name: 'y2', description: 'Y coordinate for third point' },
    { type: 'int', name: 'c', description: 'Triangle color' }
  ]}
/>
