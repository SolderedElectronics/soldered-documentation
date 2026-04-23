---  
slug: /inkplate/6color/micropython/microsd/read-write
title: Inkplate 6COLOR – Reading and Writing
sidebar_label: Reading/Writing files
id: read-write-files
hide_title: false
---

Working with files on an SD card in MicroPython is just like using regular Python on your PC. You can open, read, write and append using the same commands, just include `/sd/` in your file path. Once inserted, SD card behaves like a normal folder.

## Basic Write/Read example

```python
from inkplate6COLOR import Inkplate
from os import listdir

# Create Inkplate object
inkplate = Inkplate()

# Initialize the display, needs to be called only once
inkplate.begin()

# Initialize the SD card.
inkplate.initSDCard(fastBoot=True)

# Writing to a .txt file
with open("/sd/text.txt", "w") as f:
    f.write("Hello! This is the file writing example for Inkplate 6COLOR.\n")
    f.write("==================================================\n")
    for i in range(1, 11):
        f.write(f"Line {i} :: {i} + {i} = {i + i}\n")

# Reading .txt file
with open("/sd/text.txt", "r") as f:
    for line in f:
        inkplate.print(line)
        
# Display content from .txt file
inkplate.display()

# Put SD card to sleep
inkplate.SDCardSleep()
```

<WarningBox> Always `close()` files (or use `with`) to avoid file corruption. </WarningBox>

<CenteredImage src="/img/6color/read-write.jpg" alt="Example code" caption="Example display from .txt file" />