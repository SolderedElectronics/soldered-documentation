---  
slug: /inkplate/projects/e-reader  
title: Inkplate Projects - e Reader  
sidebar_label: E-Reader  
id: e-reader  
hide_title: false  
pagination_prev: null  
---

## Overview

<CenteredImage src="/img/e-reader/product.png" alt="Completed"  /> 

<ReactPlayer src='../../../videos/e-reader-page-next.mp4' width='100%' height='auto' muted='true' autoPlay='true' loop='true' style={{transform: 'rotate(180deg)'}} />

The **Inkplate 6FLICK e Reader** transforms your e-paper display into an open source e-reader (e-book reader). By using the provided Python script that converts the EPUB file into an easier-to-manage and usable format on the ESP32, the device allows you to read your e-books on the **Inkplate 6FLICK** itself.

The code smartly implements dynamic allocation for most of the files being stored on the Micro SD card. The code intends to use as little space as possible, so that there is space for as many books as possible.

## Requirements

For this project, you need:  
- **Inkplate 6FLICK** (because the UI is touchscreen-based)  
- **Micro SD card** (ESP32 on its own doesn't have enough memory to store large amounts of data, a **single book is several MB at best!**)  
- **e-books** (We recommend **[The Gutenberg Project](https://www.gutenberg.org)** as a legal way to get free e-books)  

## Setting up

<QuickLink  
  title="Inkplate 6FLICK E-Reader example"  
  description="Link to the official github page of the inkplate6FLICK_E_Reader example"  
  url="https://github.com/SolderedElectronics/Inkplate-Arduino-library/tree/master/examples/Inkplate6FLICK/Projects/Inkplate6FLICK_E_Reader"  
/>

Create a `/books` folder on your Micro SD card; it will be used to store all of the books that you convert. The Micro SD card structure should look something like this: `D:/books`.

<CenteredImage src="/img/e-reader/books-folder.png" alt="Books folder inside Micro SDcard"  />

The Arduino sketch doesn't have to be modified in order to work. First, open the **Arduino IDE** and navigate to  
`File->Examples->InkplateLibrary->Inkplate6FLICK->Projects->Inkplate_e_Reader`:

<CenteredImage src="/img/e-reader/arduino-sketch.png" alt="Arduino sketch path directions"  />

### Uploading the code
After completing all the previous steps, uploading the project to the Inkplate is as simple as pressing the **Upload** button in the Arduino IDE:

<CenteredImage src="/img/e-reader/upload.png" alt="Arduino upload button" width="80%" />

### Converting the .epub file

Download the Python script **[epubToImg.py](https://github.com/SolderedElectronics/Inkplate-Arduino-library/tree/master/examples/Inkplate6FLICK/Projects/Inkplate6FLICK_E_Reader/epubToImg)** that is provided with the project.  
After that, download the .epub file and copy its absolute path. (**.epubs without pictures are preferred because they will not be displayed**).

<CenteredImage src="/img/e-reader/guttenberg-project.png" alt="Book downloaded from project Gutenberg"  />

Script is built on **Python 3.13.2**
Go inside the script folder and run `pip install -r requirements.txt` from Terminal/Command Prompt to install all dependencies used by the script. After that, run the script. Command structure looks as follows:

`python .\epubToImg.py [book absolute path] [destination path + **BOOK NAME**] --width 758 --height 930 --text-size "[size]"`

<InfoBox>The --text-size parameter is optional; it is best to use it when displayed text is too small for your liking. Size can be any CSS-supported type of value, for example: --text-size "14px" / "1.5em" ...</InfoBox>

Here is an example of how the script is called:

<CenteredImage src="/img/e-reader/terminal.png" alt="Script called from Terminal"  />

<InfoBox>Due to the time complexity of our conversion solution, it is not rare to experience long conversion times, especially with larger books. So don't stress if the script "freezes" for a bit, all good things take time.</InfoBox>

After the conversion is complete, you will get a message in the terminal:

<CenteredImage src="/img/e-reader/terminal-done.png" alt="Completed"  />

## Reading on Inkplate 6FLICK

After completing all the steps from the *Setting up* part, you can put the Micro SD card in the onboard Micro SD card slot on the device. After inserting the Micro SD card, power on your Inkplate. If all is correct, you should get to the HOME menu for available books (the ones you converted and placed on the Micro SD card):

<CenteredImage src="/img/e-reader/home-menu.png" alt="Completed"  />

By using the **PREV** and **NEXT** buttons, you can traverse the books. When you get to your desired book, press the **SELECT** button to "open" it.

<ReactPlayer src='../../../videos/e-reader-home-next.mp4' width='100%' height='auto' muted='true' autoPlay='true' loop='true' style={{transform: 'rotate(180deg)'}} />

<ReactPlayer src='../../../videos/e-reader-home-prev.mp4' width='100%' height='auto' muted='true' autoPlay='true' loop='true' style={{transform: 'rotate(180deg)'}} />

<ReactPlayer src='../../../videos/e-reader-home-select.mp4' width='100%' height='auto' muted='true' autoPlay='true' loop='true' style={{transform: 'rotate(180deg)'}} />

You can traverse the book page-by-page using the **PREV** and **NEXT** buttons, or you can go to a specific page using the **GOTO** button.

<ReactPlayer src='../../../videos/e-reader-page-next.mp4' width='100%' height='auto' muted='true' autoPlay='true' loop='true' style={{transform: 'rotate(180deg)'}} />

<ReactPlayer src='../../../videos/e-reader-page-prev.mp4' width='100%' height='auto' muted='true' autoPlay='true' loop='true' style={{transform: 'rotate(180deg)'}} />

<ReactPlayer src='../../../videos/e-reader-page-goto.mp4' width='100%' height='auto' muted='true' autoPlay='true' loop='true' style={{transform: 'rotate(180deg)'}} />

To return to the Home menu, press the **HOME** button.
