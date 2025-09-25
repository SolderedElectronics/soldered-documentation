---  
slug: /inkplate/6color/micropython/basics/drawing-shapes
title: Inkplate 6COLOR – Drawing colorful shapes
sidebar_label: Drawing colorful shapes
id: drawing-shapes  
hide_title: false  
---

## Colorful Shapes Example

<InfoBox> See all available colors and their values **[here](/documentation/inkplate/6color/micropython/basics/print-text#simple-colored-text-example)**. </InfoBox>

<CenteredImage src="/img/6color/basic-color.jpg" alt="Expected output on Inkplate display" caption="Geometric Shapes output on display" />

```python
# Let's draw some shapes!
# This example will draw shapes around the upper left corner, and then rotate the screen
# This creates a symmetrical-looking pattern of various shapes
for r in range(4):

    # Sets the screen rotation
    display.setRotation(r)

    # Drawing objects
    inkplate.drawPixel(100, 100, inkplate.BLACK)
    inkplate.drawRect(50, 50, 75, 75, inkplate.GREEN)
    inkplate.fillRect(50, 50, 50, 60, inkplate.GREEN)
    inkplate.drawCircle(200, 200, 30, inkplate.BLUE)
    inkplate.fillCircle(200, 200, 15, inkplate.BLUE)
    inkplate.fillCircle(300, 300, 30, inkplate.RED)
    inkplate.drawFastHLine(20, 100, 50, inkplate.BLACK)
    inkplate.drawFastVLine(100, 20, 50, inkplate.ORANGE)
    inkplate.drawLine(100, 100, 400, 400, inkplate.ORANGE)
    inkplate.drawRoundRect(100, 10, 100, 100, 10, inkplate.BLACK)
    inkplate.fillRoundRect(10, 100, 100, 100, 10, inkplate.ORANGE)
    inkplate.fillRoundRect(35, 125, 50, 50, 10, inkplate.BLACK)
    inkplate.drawTriangle(300, 100, 400, 150, 400, 100, inkplate.BLACK)
    inkplate.fillTriangle(350, 100, 400, 175, 400, 100, inkplate.YELLOW)

# Reset the rotation
display.setRotation(0)

# Show on the display
display.display()
```

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
    { type: 'int', name: 'x0', description: 'X coordinate for first point' },
    { type: 'int', name: 'y0', description: 'Y coordinate for first point' },
    { type: 'int', name: 'x1', description: 'X coordinate for second point' },
    { type: 'int', name: 'y1', description: 'Y coordinate for second point' },
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
  functionName="inkplate.fillTriangle()"
  description="Function to draw a triangle filled with specified color"
  returnDescription="None"
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