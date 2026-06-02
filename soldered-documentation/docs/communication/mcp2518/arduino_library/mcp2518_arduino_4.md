---
slug: /mcp2518/arduino/troubleshooting 
title: CAN Transceiver MCP2518 - Troubleshooting
id: mcp2518-arduino-4 
sidebar_label: Troubleshooting
hide_title: false
pagination_next: null
---

This page covers the most common issues when getting started with the MCP2518 CAN breakout.

<ExpandableSection title="CAN init fail - begin() never returns CAN_OK">

The most common cause is an SPI wiring problem. Check the following:

- Verify that NCS is connected to the correct pin and matches the pin number passed to the `CANBus` constructor.
- Confirm MOSI, MISO, and SCK are connected to the correct hardware SPI pins for your board (D11, D12, D13 on Dasduino CORE).
- Make sure VCC and GND are connected and the board is receiving the correct supply voltage (2.7 V to 5 V).
- The MCP2518FD requires several milliseconds to start up after power-on. The `while (0 != CAN.begin(...))` retry loop in the examples handles this - do not replace it with a single call.

</ExpandableSection>

<ExpandableSection title="No data received - receiver never sees CAN_MSGAVAIL">

If the sender reports success but the receiver sees nothing:

- Check that **CANH is connected to CANH** and **CANL to CANL** on both boards. Swapping the two wires is the most common wiring mistake.
- Both nodes must use the **same bit rate**. A sender at `CAN_125KBPS` and a receiver at `CAN_500KBPS` will not communicate.
- For CAN FD, both the arbitration rate and the data rate must match (e.g., both using `CAN_125K_500K`).
- At least one end of the CAN bus must be terminated with a 120 Ω resistor. Close jumper **JP1** on one (or both) boards to enable the onboard termination resistor.
- If the bus is very short (under 1 m on a bench), you can close JP1 on both boards.

</ExpandableSection>

<ExpandableSection title="CAN FD frames are not received or cause errors">

When switching from CAN 2.0B to CAN FD:

- Use `CAN.begin(CAN_125K_500K)` (or another FD speed constant) on **both** the sender and receiver. A CAN 2.0B node on the same bus will not decode CAN FD frames and may generate error frames.
- Use `CANFD::len2dlc(len)` for the DLC parameter in `sendMsgBuf()` when sending payloads larger than 8 bytes.
- The receive buffer must be at least 64 bytes when using CAN FD: `unsigned char buf[64]`.

</ExpandableSection>

<ExpandableSection title="Interrupt pin (INT/INT0/INT1) does not trigger">

All interrupt outputs on the MCP2518FD are **active low** - they go LOW when an event occurs and return HIGH when cleared. If you are polling the pin, check for `LOW`, not `HIGH`. In code:

```cpp
if (digitalRead(INT_PIN) == LOW) {
  // message or error event pending
}
```

Make sure the pin is configured as `INPUT` (not `INPUT_PULLDOWN`) and that it is connected to a pin that supports external interrupts on your board.

</ExpandableSection>

<ExpandableSection title="Data corruption or frequent CRC errors">

CRC errors usually indicate a signal integrity problem:

- Keep CANH and CANL wires twisted together or use a twisted-pair cable.
- Add the 120 Ω termination resistor at each end of the bus (close JP1 on each end node).
- Reduce the data bit rate if the bus is long or unshielded. CAN FD at 8 Mbps requires very short, well-terminated runs; 500 kbps or 1 Mbps is more forgiving.
- Check that no other node on the bus is using a different baud rate, which will cause continuous error frames and can lock the bus.

</ExpandableSection>

<InfoBox>In case you haven't found the answer to your question, please **contact us** via [**this**](https://soldered.com/contact/) link.</InfoBox>
