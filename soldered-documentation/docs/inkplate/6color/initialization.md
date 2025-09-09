---  
slug: /inkplate/6color/micropython/initialization
title: Inkplate 6COLOR – Micropython
sidebar_label: Initialization
id: init
hide_title: true  
---

<SectionTitle title="Initialization" backgroundImage="img/arduino_bg.jpg" />

If you are new to MicroPython, check out our official [MicroPython Guide](https://soldered.com/documentation/micropython/overview) for a full setup and overview on how it works.

---

Using MicroPython on your Inkplate board is very simple and straightforward, just follow the [Setup Tutorial](https://github.com/SolderedElectronics/Inkplate-micropython) on GitHub which runs you through configuration steps for flashing the MicroPython firmware on your Inkplate board.

## Uploading files to Inkplate board

Once you completed the steps for flashing firmware, on the Inkplate-MicroPython GitHub repo, navigate to *Inkplate6COLOR* folder and find the **inkplate6COLOR.py** file and upload it to your board using **VS Code** or **Thonny IDE**. 

<CenteredImage src="/img/6color/github_py_file.png" alt="Inkplate 6 color GitHub" caption="inkplate6COLOR.py"/>

After you uploaded main **.py** file, go back to starting directory and from *Dependencies* folder upload all **.py** files on to your board. 

<CenteredImage src="/img/6color/github_dependencies.png" alt="Inkplate 6 color GitHub dependencies" caption="Inkplate 6 COLOR Dependecies"/>

## Initializing Inkplate and display

Now we can start writing programs in Python to control our Inkplate. Here is a basic Inkplate object creation and display initialization which we will use in every example in following tutorials.

```python
# Include inkplate library
from inkplate6COLOR import Inkplate

# Create Inkplate object
inkplate = Inkplate()

# Initialize the display, needs to be called only once
inkplate.begin()
```

<FunctionDocumentation
  functionName="inkplate.Inkplate()"
  description="Creates an Inkplate object from the Inkplate class."
  returnType="none"
/>
<FunctionDocumentation
  functionName="inkplate.begin()"
  description="In short, this function initializes the Inkplate object. It starts I2C, allocates the required memory for the frame buffer, and initializes the onboard peripherals."
  returnType="none"
/>

Now, let's explore some basic examples!