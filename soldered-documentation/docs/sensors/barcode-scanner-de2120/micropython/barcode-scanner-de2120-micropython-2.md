---
slug: /barcode-scanner-de2120/micropython/examples
title: DE2120 Barcode Scanner – Scanning Examples (MicroPython)
sidebar_label: Scanning examples
id: barcode-scanner-de2120-micropython-2
hide_title: false
---

## Basic scan

This example initializes the DE2120 scanner and reads barcodes in **manual trigger mode** — the scanner outputs data each time the physical button on the breakout board is pressed, or when a scan is triggered via software.

```python
from machine import UART
from de2120 import DE2120
import time

# Adjust tx and rx to match the pins you have wired on your board
scanner = DE2120(tx=5, rx=4)

if not scanner.begin():
    print("DE2120 not detected. Check wiring.")
    raise SystemExit

print("DE2120 ready. Press the button on the scanner to read a barcode.")

while True:
    barcode = scanner.readBarcode()
    if barcode:
        print("Scanned:", barcode)
    time.sleep_ms(20)
```

## Function reference

<FunctionDocumentation
    functionName="DE2120(tx, rx, uart_id=1)"
    description="Creates a DE2120 scanner object using the specified TX and RX pin numbers. A UART peripheral is created internally at 9600 baud. You can also pass a pre-built UART object via the uart parameter instead."
    returnDescription="DE2120 object"
    parameters={[
        { type: 'int', name: 'tx', description: 'GPIO pin number for UART TX (MCU → scanner).' },
        { type: 'int', name: 'rx', description: 'GPIO pin number for UART RX (scanner → MCU).' },
        { type: 'int', name: 'uart_id', description: 'UART peripheral ID (default: 1).' },
    ]}
/>

<FunctionDocumentation
    functionName="scanner.begin()"
    description="Verifies communication with the scanner. Automatically detects and negotiates the baud rate down to 9600 bps if needed. Clears any pending data from the receive buffer before returning."
    returnDescription="bool — True if the scanner responded correctly, False if not detected."
/>

<FunctionDocumentation
    functionName="scanner.readBarcode()"
    description="Polls the UART receive buffer for barcode data. Call this repeatedly in a loop. When a complete CR-terminated barcode string arrives, it is returned as a string. Returns None if no complete barcode is available yet."
    returnDescription="str — The decoded barcode string, or None if no scan is ready."
/>

## Full example

<QuickLink
    title="de2120-readBarcode.py"
    description="Basic barcode reading example using manual trigger mode"
    url="https://github.com/SolderedElectronics/Soldered-MicroPython-Modules/blob/main/DE2120/DE2120/Examples/de2120-readBarcode.py"
/>

---

## Continuous read mode

In continuous mode the scanner reads automatically without needing any trigger command. This is useful for checkout-style applications where items are passed in front of the scanner.

```python
from machine import UART
from de2120 import DE2120
import time

scanner = DE2120(tx=5, rx=4)

if not scanner.begin():
    print("DE2120 not detected. Check wiring.")
    raise SystemExit

# Enable continuous read with a 0.5 s repeat interval for duplicate barcodes
scanner.enableContinuousRead(repeat_interval=2)

print("DE2120 in continuous read mode. Point at a barcode.")

while True:
    barcode = scanner.readBarcode()
    if barcode:
        print("Scanned:", barcode)
    time.sleep_ms(50)
```

## Function reference

<FunctionDocumentation
    functionName="scanner.enableContinuousRead(repeat_interval=2)"
    description="Switches the scanner to continuous scanning mode. The repeat_interval controls how duplicate barcodes are handled."
    returnDescription="bool — True on success."
    parameters={[
        { type: 'int', name: 'repeat_interval', description: '0 = output once per barcode, 1 = continuous with no delay, 2 = 0.5 s delay between duplicates (default), 3 = 1 s delay.' },
    ]}
/>

<FunctionDocumentation
    functionName="scanner.disableContinuousRead()"
    description="Returns the scanner to manual (trigger) mode."
    returnDescription="bool — True on success."
/>

<FunctionDocumentation
    functionName="scanner.enableMotionSense(sensitivity=50)"
    description="Enables motion-triggered scanning. The scanner activates automatically when movement is detected in front of it."
    returnDescription="bool — True on success."
    parameters={[
        { type: 'int', name: 'sensitivity', description: 'Motion sensitivity: 15 = highest sensitivity, 20 = high, 30, 50 (default), 100 = lowest.' },
    ]}
/>

<FunctionDocumentation
    functionName="scanner.disableMotionSense()"
    description="Disables motion sensing and returns to manual mode."
    returnDescription="bool — True on success."
/>

## Full example

<QuickLink
    title="de2120-continuousRead.py"
    description="Continuous barcode scanning mode example"
    url="https://github.com/SolderedElectronics/Soldered-MicroPython-Modules/blob/main/DE2120/DE2120/Examples/de2120-continuousRead.py"
/>

---

## Configuring the scanner

This example shows how to send configuration commands to the scanner at runtime. It toggles **Code ID** — a prefix character the scanner prepends to every scan to identify the barcode type (e.g. `A` for Code 128, `Q` for QR Code).

```python
import sys
import uselect
from de2120 import DE2120
import time

scanner = DE2120(tx=5, rx=4)

if not scanner.begin():
    print("Scanner did not respond. Check wiring.")
    raise SystemExit

print("Scanner online!")

poll = uselect.poll()
poll.register(sys.stdin, uselect.POLLIN)

def stdin_available():
    return bool(poll.poll(0))

def flush_stdin():
    while stdin_available():
        sys.stdin.read(1)

while True:
    flush_stdin()
    print()
    print("Transmit Code ID with barcode? (y/n)")

    while not stdin_available():
        barcode = scanner.readBarcode()
        if barcode:
            print("Code found:", barcode)
        time.sleep_ms(200)

    cmd = sys.stdin.read(1)
    if cmd == 'y':
        print("Code ID enabled")
        scanner.sendCommand("CIDENA", "1")
    elif cmd == 'n':
        print("Code ID disabled")
        scanner.sendCommand("CIDENA", "0")
    else:
        print("Command not recognized")
```

## Function reference

<FunctionDocumentation
    functionName='scanner.sendCommand(cmd, arg="", max_wait_ms=3000)'
    description="Sends an arbitrary configuration command to the scanner. The library wraps it in the required protocol format (^_^COMMAND<ARG>.) automatically. Waits up to max_wait_ms milliseconds for an ACK or NACK response."
    returnDescription="bool — True if the scanner acknowledged (ACK), False on NACK or timeout."
    parameters={[
        { type: 'str', name: 'cmd', description: 'Command string (e.g. "CIDENA").' },
        { type: 'str', name: 'arg', description: 'Optional argument string (e.g. "1" to enable).' },
        { type: 'int', name: 'max_wait_ms', description: 'Maximum wait time in milliseconds (default: 3000).' },
    ]}
/>

<FunctionDocumentation
    functionName="scanner.lightOn()"
    description="Turns on the white illumination LEDs."
    returnDescription="bool — True on success."
/>

<FunctionDocumentation
    functionName="scanner.lightOff()"
    description="Turns off the white illumination LEDs."
    returnDescription="bool — True on success."
/>

<FunctionDocumentation
    functionName="scanner.reticleOn()"
    description="Turns on the red aiming reticle LED."
    returnDescription="bool — True on success."
/>

<FunctionDocumentation
    functionName="scanner.reticleOff()"
    description="Turns off the red aiming reticle LED."
    returnDescription="bool — True on success."
/>

<FunctionDocumentation
    functionName="scanner.enableAll1D()"
    description="Enables all supported 1D barcode symbologies."
    returnDescription="bool — True on success."
/>

<FunctionDocumentation
    functionName="scanner.disableAll1D()"
    description="Disables all 1D barcode symbologies."
    returnDescription="bool — True on success."
/>

<FunctionDocumentation
    functionName="scanner.enableAll2D()"
    description="Enables all supported 2D barcode symbologies."
    returnDescription="bool — True on success."
/>

<FunctionDocumentation
    functionName="scanner.disableAll2D()"
    description="Disables all 2D barcode symbologies."
    returnDescription="bool — True on success."
/>

<FunctionDocumentation
    functionName="scanner.changeReadingArea(percent)"
    description="Sets the percentage of the camera frame used for barcode detection. Narrowing the area can speed up decoding in controlled environments."
    returnDescription="bool — True on success."
    parameters={[
        { type: 'int', name: 'percent', description: 'Frame percentage: 100 (full, default), 80, 60, 40, or 20 (center region only).' },
    ]}
/>

<FunctionDocumentation
    functionName="scanner.factoryDefault()"
    description="Resets all scanner settings to factory defaults. Note: the scanner temporarily disconnects from serial while restarting."
    returnDescription="bool — True on success."
/>

## Full example

<QuickLink
    title="de2120-sendCommand.py"
    description="Example showing how to send configuration commands to the DE2120 scanner at runtime"
    url="https://github.com/SolderedElectronics/Soldered-MicroPython-Modules/blob/main/DE2120/DE2120/Examples/de2120-sendCommand.py"
/>

<InfoBox>

For a full interactive menu covering all scanner settings (flashlight, reticle, reading area, scanning mode, and symbologies), see the **de2120-serialSettings.py** example:

<QuickLink
    title="de2120-serialSettings.py"
    description="Full interactive configuration menu for the DE2120 scanner"
    url="https://github.com/SolderedElectronics/Soldered-MicroPython-Modules/blob/main/DE2120/DE2120/Examples/de2120-serialSettings.py"
/>

</InfoBox>
