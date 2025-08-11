---  
slug: /inkplate/projects/epub-reader 
title: Inkplate Projects - Epub Reader
sidebar_label: Epub Reader
id: epub-reader 
hide_title: false  
pagination_prev: null  
---

## Overview

staviti sliku 

The **Inkplate 6FLICK Epub Reader** transforms your e-paper display into a open source epub reader (e-book reader). By using the provided python script that converts the epub file into a easier-to-manage and usable format on the esp32, the device allows you to read your e-books on the **Inkplate 6FLICK** itself.

The code smartly implements dynamic allocation for most of the files being stored on the SDcard. Wether it is Double linked lists for storing books and pages, or simple heap allocation for a specific page data, the code intends to use as little space as possible, so that there is space for as much books as it's possible.


## Requirements

For this project, you need:
- **Inkplate 6FLICK** (because the UI is touchscreen based)
- **SDcard** (ESP32 on it's own doesn't have enough memory to store large amounts of data, a **single book is several MBs at best!**)
- **Epub e-books** (We recomend [The Guttenberg Project]("https://www.gutenberg.org/") as a legal way to get free e-books)

## Setting up

Create a `/books` folder on your SDcard, it will be used to store all of the books that you convert. The SDcard structure should look something like this: `D:/books`.

<CenteredImage src="/img/epub-reader/books-folder.png" alt="Books folder inside SDcard" width="80%" />


The Arduino sketch doesn't have to be modified in order to work. First, open the **Arduino IDE** and navigate to
`FIle->Examples->InkplateLibrary->Inkplate6FLICK->Projects->Inkplate_Epub_Reader`:

<CenteredImage src="/img/epub-reader/arduino-sketch.png" alt="Arduino sketch path directions" width="80%" />

### Uploading the code
After completing all the previous steps, uploading the project to the Inkplate is as simple as pressing the **Upload** button in the Arduino IDE:

<CenteredImage src="/img/epub-reader/upload.png" alt="Arduino upload button" width="80%" />

### Converting the .epub file

Download the python script "epubToImg.py" that is provided with the project.
After that, download the .epub file and copy its absolute path. (**.epubs without pictures are prefered because they will not be displayed**).

<CenteredImage src="/img/epub-reader/guttenberg-project.png" alt="Book downloaded from project Guttenberg" width="80%" />

Go inside the script folder and run it trough CMD/PowerShell. Command structure looks as follows:

`python .\epubToImg.py [book absolute path] [destination path + **BOOK NAME**] --width 758 --height 930 --text-size "[size]"`

<InfoBox>The --text-size parameter is optional, it is best to use it when displayed text is to small for your liking. Size can be any css supported type of value, for example: --text-size "14px" / "1.5em" ...</InfoBox>

Here is an example on how the script is called:

<CenteredImage src="/img/epub-reader/terminal.png" alt="Script called from Terminal" width="80%" />

<InfoBox>Due to the time complexity of our conversion solution, it is not rare to experience long conversion time, especially with larger books. So don't stress if the script "frezes" for a bit, all good things take time.</InfoBox>

After the conversion is complete, you will get a message on terminal:

staviti sliku

## How to use the device

After completing all the steps from Setting up part, you can put the SDcard in the ondoard SDcard slot on the device. Reset the device so that the SDcard gets registered. If all is correct, you should get to HOME menu for available book (the ones you converted):

staviti sliku glavnog izbornika

By using **PREV** and **NEXT** buttons, you can traverse the books. When you get to your desired book, press the **SELECT** button to "open" it.

staviti video navigiranja kroz menu

You can traverse the book page-by-page using the **PREV** and **NEXT** buttons or you can go to a specific page using the **GOTO** button.

staviti video navigiranja kroz knjigu

To return to the Home menu, press the **HOME** menu.

