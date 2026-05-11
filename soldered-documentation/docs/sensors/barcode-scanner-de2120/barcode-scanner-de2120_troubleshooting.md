---
slug: /barcode-scanner-de2120/troubleshooting
title: DE2120 Barcode Scanner Troubleshooting
sidebar_label: Troubleshooting
id: barcode-scanner-de2120-troubleshooting
hide_title: true
pagination_next: null
---

# Troubleshooting

This page lists common issues and quick checks when using the **DE2120 2D Barcode Scanner**.

## Arduino

<ExpandableSection title="Scanner not detected — begin() returns false">

- **Did you scan the POR232 barcode?**  
  The scanner ships in USB mode. You must scan the **POR232** configuration barcode from the DYScan settings manual to switch it to TTL/RS232 mode before it will communicate over UART.

- **Check TX/RX are not swapped:**  
  The scanner's **TX** must connect to the microcontroller's **RX**, and the scanner's **RX** to the microcontroller's **TX**. This is a very common wiring mistake.

- **Check power:**  
  The DE2120 requires a stable **3.3 V** supply. Supplying 5 V directly may damage the module.

- **Allow startup time:**  
  Add a `delay(500)` before calling `scanner.begin()` to give the scanner time to boot.

- **Check wiring continuity:**  
  Verify all connections with a multimeter if possible.

</ExpandableSection>

<ExpandableSection title="Scanner initializes but no barcodes are printed">

- **Verify Serial Monitor baud rate is 115200.**

- **Check scan distance:**  
  The DE2120 reads barcodes between **25 mm and 400 mm**. Holding the scanner too close or too far from the barcode will result in no decode.

- **Ensure readBarcode() is called in loop():**  
  The function must be polled frequently. Avoid blocking calls (`delay()`) that prevent it from running.

- **Check lighting:**  
  The scanner works best in normal indoor light. Direct bright light or complete darkness may affect performance. Enable the white illumination LEDs with `scanner.lightOn()` if needed.

- **Check barcode print quality:**  
  Minimum print contrast signal (PCS) is 25%. Low-quality or low-contrast barcodes may not decode reliably.

- **Check that the correct symbology is enabled:**  
  If you disabled 1D or 2D symbologies, re-enable them with `scanner.enableAll1D()` or `scanner.enableAll2D()`.

</ExpandableSection>

<ExpandableSection title="Garbled or partial barcode output">

- **Increase BUFFER_LEN:**  
  If the barcode data is longer than your buffer, the string will be truncated. Increase `BUFFER_LEN` (default 40) to accommodate longer barcodes.

- **SoftwareSerial baud rate mismatch:**  
  SoftwareSerial may drop characters at higher baud rates on some microcontrollers. Try switching to a HardwareSerial port if available, as shown in the `HardwareScan` example.

- **Confirm baud rate after negotiation:**  
  The library negotiates the scanner down to 9600 bps. If another sketch changed the baud rate manually, call `scanner.factoryDefault()` to reset to a known state.

</ExpandableSection>

<ExpandableSection title="Scanner beeps on scan but nothing prints in Serial Monitor">

- The beep confirms the scanner decoded a barcode, but the data is not reaching your microcontroller. This usually means the **UART wiring is incorrect** — specifically that the scanner TX is not connected to the MCU RX.

- If you previously used the scanner in **USB mode**, its output may still be routed to the USB interface. Scan the **POR232** barcode to switch back to TTL mode.

- If all else fails, call `scanner.factoryDefault()` to reset all settings to factory defaults, then reconnect.

</ExpandableSection>

<ExpandableSection title="Scanner was working but stopped responding">

- **Check power supply stability:**  
  The DE2120 draws up to 190 mA during active scanning. An insufficient power supply can cause brownouts and communication failures.

- **Avoid `scanner.changeBaudRate()` unless necessary:**  
  If the baud rate was changed and the library can no longer auto-detect it, perform a factory reset by calling `scanner.factoryDefault()`.

- **Restart the scanner:**  
  Power-cycle the breakout board and re-run `scanner.begin()`.

</ExpandableSection>

<ExpandableSection title="No output in Serial Monitor at all">

- Make sure `Serial.begin(115200)` is called in `setup()`.
- Verify the **Serial Monitor baud rate is set to 115200** in the Arduino IDE.
- Upload the sketch again and press the reset button on the board.

</ExpandableSection>

## MicroPython

<ExpandableSection title="Scanner not detected — begin() returns False">

- **Did you scan the POR232 barcode?**  
  The scanner ships in USB mode. You must scan the **POR232** configuration barcode from the DYScan settings manual to switch it to TTL/RS232 mode before it will communicate over UART.

- **Check TX/RX are not swapped:**  
  The scanner's **TX** must connect to the MCU's **RX** (and vice versa). The `tx` and `rx` arguments in `DE2120(tx=5, rx=4)` refer to the **MCU's pins**, so `tx=5` means GPIO5 is the MCU transmit pin → connect to scanner **RX**.

- **Check power:**  
  The DE2120 requires a stable **3.3 V** supply and can draw up to 190 mA. Make sure your power source can supply enough current.

- **Add a startup delay:**  
  The scanner needs time to boot. Make sure there is at least a short delay (or a `time.sleep_ms(500)`) before calling `scanner.begin()`.

- **Check UART peripheral ID:**  
  Different MicroPython boards have different numbers of UART peripherals. The default `uart_id=1` may not be available on your board. Try `uart_id=0` or `uart_id=2`.

</ExpandableSection>

<ExpandableSection title="Scanner initializes but readBarcode() always returns None">

- **Verify the TX/RX wiring:**  
  If `begin()` succeeds but no barcodes arrive, the scanner-to-MCU direction (scanner TX → MCU RX) may be disconnected or swapped.

- **Check scan distance:**  
  The DE2120 reads barcodes between **25 mm and 400 mm** from the scanner face. Position the target within this range.

- **Call readBarcode() frequently in your loop:**  
  The function accumulates bytes as they arrive. If you sleep too long between calls (`time.sleep_ms` > 100 ms), you may miss the carriage return that terminates the barcode string. Keep the polling interval short (20–50 ms).

- **Check that the correct symbologies are enabled:**  
  If you previously disabled 1D or 2D symbologies, re-enable them:
  ```python
  scanner.enableAll1D()
  scanner.enableAll2D()
  ```

</ExpandableSection>

<ExpandableSection title="Garbled or truncated barcode output">

- **The internal buffer is 256 bytes** — long barcodes (e.g., PDF417 with large payloads) will be truncated if they exceed this. This is a library constant (`_MAX_BARCODE_LEN`) that can be increased if needed.

- **Check for UART noise:**  
  Long wires or breadboard connections at UART speeds can introduce errors. Keep wiring short and direct.

- **Verify the baud rate:**  
  The library auto-negotiates to 9600 bps on `begin()`. If another sketch changed the baud rate, call `scanner.factoryDefault()` to reset to a known state, then reconnect.

</ExpandableSection>

<ExpandableSection title="Scanner beeps on scan but readBarcode() returns None">

- The beep confirms the scanner successfully decoded a barcode internally, but data is not reaching your MCU. This almost always means the **scanner TX → MCU RX** connection is missing or broken.

- If the scanner was previously in USB mode, its data output may still be routed to the USB interface. Re-scan the **POR232** barcode and call `scanner.begin()` again.

</ExpandableSection>

<ExpandableSection title="ImportError: no module named 'de2120'">

- The `de2120.py` file must be uploaded to the root of your MicroPython board's filesystem before importing it. Use Thonny or `mpremote` to copy the file to the board.

- Verify the file is present by running in the REPL:
  ```python
  import os
  print(os.listdir())
  ```

</ExpandableSection>

<ExpandableSection title="No output in the REPL at all">

- Make sure you are connected to the correct serial port and that your terminal is set to **115200 baud**.
- Press **Ctrl+D** to soft-reset the board and re-run your script.
- Upload the script again if changes were not saved to the board.

</ExpandableSection>
