---
slug: /arduino 
title: Arduino tutorial backup page
id: arduino-backup
hide_title: False
pagination_next: null
pagination_prev: null
---


<ExpandableSection title="More info on EasyC/Qwiic">

EasyC was our original name for this connector system, but we are **retiring it in favor of Qwiic**. Functionally, EasyC and Qwiic are the same—both use the **JST-SH 4-pin connector (1.00mm pitch)** and are fully compatible with **SparkFun Qwiic and Adafruit STEMMA QT**.  

Find the mechanical drawing of the female connector [**here**](https://soldered.com/productdata/2018/07/Soldered_A1001-SR04_datasheet.pdf) and the male connector on the cable [**here**](https://soldered.com/productdata/2018/07/Soldered_A1001-H04_datasheet.pdf).

The **4-pin EasyC/Qwiic cable** follows this **standard color coding**:  

| Color  | Function  |
|--------|----------|
| **Black**  | **GND** (Ground) |
| **Red**    | **3.3V** (Power) |
| **Blue**   | **SDA** (I2C Data) |
| **Yellow** | **SCL** (I2C Clock) |

---

EasyC/Qwiic is a **solder-free, plug-and-play connection system** designed for **I2C communication** between microcontroller boards, sensors, and actuators. With EasyC/Qwiic, you can **focus on coding and prototyping** without dealing with messy wiring or soldering. 
- You can **chain multiple devices together** without extra wiring. This allows for **efficient expansion** of projects, such as IoT-enabled weather stations.  
- The **polarized connectors** prevent incorrect connections, so you never mix up **SDA and SCL lines** or accidentally reverse a connection.  
- Since EasyC/Qwiic is based on **I2C**, multiple sensors and modules can be **connected in parallel** to a single microcontroller, simplifying wiring for complex projects.  
- Works with **any board that supports I2C**. If your board **doesn’t have an EasyC/Qwiic connector**, you can use an **adapter** to convert a standard I2C header into EasyC/Qwiic. 

---

<YouTubeEmbed videoId="fkst0veJaEw" width={520} />

</ExpandableSection>    


## Installing Arduino IDE

In case you don't have Arduino IDE yet, install it from the [**official website**](https://www.arduino.cc/en/software).

<InfoBox>

We reccomend installing and using the latest version

</InfoBox>

<CenteredImage src="/img/arduino_ide.png" alt="Arduino IDE" width="450px" caption="Arduino IDE" />

---

## Installing Dasduino board definitions

If you're using a Dasduino board in your project, you will need to **install our board definition package** so you can compile and upload code. 

Copy the following URL:

```
https://github.com/SolderedElectronics/Dasduino-Board-Definitions-for-Arduino-IDE/raw/master/package_Dasduino_Boards_index.json
```

And add it to the lude Library > Add .ZIP Library...`, select the downloaded ZIP file, and let the Arduino IDE handle the installation.

<InfoBox>

If you prefer a manual installation, follow these steps:

1. Extract the downloaded ZIP file.
2. Locate the extracted folder and ensure it contains the `.cpp` and `.h` files, as well as the `library.properties` file.
3. Rename the folder (if necessary) to match the library name exactly.
4. Move the folder to your Arduino libraries directory:
   - **Windows**: `Documents/Arduino/libraries/`
   - **Mac**: `~/Documents/Arduino/libraries/`
   - **Linux**: `~/Arduino/libraries/`
5. Restart the Arduino IDE to detect the new library.
6. 
</InfoBox>

`Additional boards manager URLs` in Arduino preferences:

<CenteredImage src="/img/add_board_def.png" alt="Add Dasduino to Arduino boards Manager" caption="Adding the Dasduino boards link to Arduino IDE" width="600px" />

Now, you can open the Boards Manager, search for `Dasduino` and find your specific board and install it:
<CenteredImage src="/img/install_dasduino_board_defs.png" alt="Install Dasduino boards" caption="Installing Dasduino boards" width="300px" />

---

## Installing the Arduino Library

<!--
In the Arduino Library Manager, search for `SHTC3 Soldered Library` library and click `Install`:
<CenteredImage src="/img/install_lib.png" alt="Install SHTC3 Soldered Library" caption="Installing the Arduino library" width="400px" />

<WarningBox>This is a placeholder image! It needs to be replaced when the library is uploaded to Arduino Library Manager.</WarningBox>
-->
<WarningBox>This library needs to be intsalled manually by downloading it from the [**GitHub repository**](https://github.com/SolderedElectronics/Soldered-SHTC3-Temperature-Humidity-Sensor-Arduino-Library).</WarningBox> 

Go to `Sketch > Inc