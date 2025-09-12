---  
slug: /inkplate/6color/micropython/setup/uploading-code
title: Inkplate 6COLOR – Uploading Code
sidebar_label: Uploading Code
id: upload-code
hide_title: false
---

Before running code on your Inkplate, first we need to upload required libraries.

---

On the [Inkplate-MicroPython GitHub](https://github.com/SolderedElectronics/Inkplate-micropython) repo, navigate to *Inkplate6COLOR* folder and find the **inkplate6COLOR.py** file and upload it to your board using **VS Code** or **Thonny IDE**

<CenteredImage src="/img/6color/github_py_file.png" alt="Inkplate 6 color GitHub" caption="inkplate6COLOR.py"/>

After you uploaded main **.py** file, go back to starting directory and from *Dependencies* folder upload all **.py** files onto your board. 

<CenteredImage src="/img/6color/github_dependencies.png" alt="Inkplate 6 color GitHub dependencies" caption="Inkplate 6 COLOR Dependecies"/>

Now that all of the steps for loading the firmware and uploading required libraries are completed we can start writing our own code!

---

## Initializing Inkplate and display

Here is a basic Inkplate object creation and display initialization which we will use in every example in following tutorials.

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