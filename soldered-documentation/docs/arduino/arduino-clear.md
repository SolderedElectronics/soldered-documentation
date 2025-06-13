---  
slug: /arduino/clear-cache   
title: Arduino - Clear Arduino Boards and Cache  
id: arduino-clear  
hide_title: False  
pagination_next: null  
---

This page provides a short guide for clearing compiler errors and generally resetting the software to its default state. If you're familiar with the issue, you can just jump to the [Windows](arduino-clear.md#for-windows-users), [macOS](arduino-clear.md#for-macos-users) or [Linux](arduino-clear.md#for-linux-users-ubuntu-fedora-etc) sections of the guide.

### Why Clear Arduino Boards and Cache?

When installing or updating a board (like ESP32, STM32, etc.), the download process can sometimes fail or install incorrectly. This can lead to several issues, such as:

*   **Compiler errors**
*   **Missing tools or definitions**
*   **Unexpected bugs that don’t match your code**
    
<InfoBox>By clearing the **packages folder**, you remove potentially broken or outdated board files, allowing you to reinstall a fresh, clean version.</InfoBox>

The Arduino IDE stores tools (like compilers, uploaders, and scripts) in these folders. If any of these tools are:

*   Not fully downloaded
*   Mismatched with the board version
*   Corrupted

You may encounter strange compile errors unrelated to your code. Clearing these folders forces the IDE to re-download the correct tools and ensures everything functions as expected. This guide explains how to safely delete these files step by step.

---

### For Windows Users

#### Step 1: Show Hidden Folders

1.  Open any folder (e.g., “This PC” or “Documents”).
2.  Click the **View** tab at the top.
3.  Check **Hidden items** to make hidden folders visible.
    
<CenteredImage src="/img/arduino-clear/windows1.png" width="1000px" />

#### Step 2: Go to the Arduino Cache Folder

1.  Press **Windows + R** on your keyboard.
2.  In the box that appears, type:
```cpp
%LOCALAPPDATA%\\Arduino15
```
3.  Click **OK**.
    
<CenteredImage src="/img/arduino-clear/windows2.png" width="400px" />

1.  In this folder, delete the following: 
    *   The **packages** folder.  
    *   The **cache** folder. _(Right-click each folder and select Delete.)_
        
<CenteredImage src="/img/arduino-clear/windows3.png" width="700px" />

<InfoBox>Optional: To completely reset Arduino, you can delete the entire **Arduino15** folder. Note that this will remove all installed boards and some settings.</InfoBox>

---

### For macOS Users

#### Step 1: Open the Library Folder

1.  Open **Finder** and click **Go** in the top menu bar.
2.  Hold down the **Option (⌥)** key – you’ll see “Library” appear in the list.
3.  Click **Library**.
    
#### Step 2: Find and Open the Arduino15 Folder

1.  In the **Library** folder, scroll down and open **Arduino15**.
2.  Inside, delete:
    *   The **packages** folder.  
    *   The **cache** folder. _(Right-click each folder and select Delete.)_
        
<InfoBox>Optional: To completely reset Arduino, you can delete the entire **Arduino15** folder. Note that this will remove all installed boards and some settings.</InfoBox>

#### Step 3: Optionally Clean Preferences

1.  Navigate to **Documents > Arduino**.
2.  If you see a file named preferences.txt, you can delete it to reset personal settings (not usually necessary).

---

### For Linux Users (Ubuntu, Fedora, etc.)

#### Step 1: Show Hidden Files

1.  Open your **Home** folder.
2.  Press **Ctrl + H** to show hidden folders.
3.  Alternatively, use the menu to select “Show Hidden Files.”
    
#### Step 2: Navigate to the Arduino Cache Folder

1.  Open the hidden folder called .arduino15. _(The dot at the beginning means it’s usually invisible.)_
2.  Delete:
    *   The **packages** folder.
    *   The **cache** folder.
        
<InfoBox>Optional: To completely reset Arduino, you can delete the entire **Arduino15** folder. Note that this will remove all installed boards and some settings.</InfoBox>

#### Step 3: Optional Sketchbook Cleanup

1.  Still in your Home folder, open the **Arduino** folder.
2.  If there’s a file called preferences.txt, you can delete it to reset settings.
