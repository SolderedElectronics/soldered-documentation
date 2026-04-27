---
slug: /barcode-scanner-de2120/arduino/troubleshooting
title: DE2120 Barcode Scanner Troubleshooting
sidebar_label: Troubleshooting
id: barcode-scanner-de2120-arduino-3
hide_title: true
pagination_next: null
---

# Troubleshooting

This page lists common issues and quick checks when using the **DE2120 2D Barcode Scanner**.

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
