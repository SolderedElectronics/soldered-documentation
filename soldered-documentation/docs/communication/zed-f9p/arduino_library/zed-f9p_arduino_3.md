---
slug: /zed-f9p/arduino/examples_high_precision
title: ZED-F9P - High Precision and Accuracy
sidebar_label: High Precision and Accuracy
id: zed-f9p-arduino-3 
hide_title: False
pagination_next: null
---

One of the biggest selling points of the ZED-F9P module is the fact that it is a high precision module with multi-band GNSS receiver, which delivers a centimeter accuracy. This page contains some basic examples on how to use that high precision and accuracy functionality.

## Reading High Accuraccy Position Data

To read the high-precision position data from the ZED-F9P module, the receiver uses the **UBX-HPPOSLLH** message. This message contains the position solution with additional high-precision components, allowing the module to achieve centimeter-level accuracy.

The **HPPOSLLH** position values are split into two separate parts:
- A **standard integer component** stored in units of `degrees * 10^-7`
- A **high-precision component** stored in units of `degrees * 10^-9`

Both values must be combined to reconstruct the **final high-precision latitude** and **longitude values**.

<InfoBox>
The same principle applies to altitude values, where the module provides:
- A standard milimeter value
- An additional high-precision fractional component
</InfoBox>

<InfoBox>
To access this data, the library provides dedicated functions for both the standard and high-precision parts of the position solution.
</InfoBox>

Below is an example of reading the **raw high-precision** position values from ZED-F9P:

```cpp
// Read latitude
int32_t latitude = myGNSS.getHighResLatitude();
int8_t latitudeHp = myGNSS.getHighResLatitudeHp();

// Read longitude
int32_t longitude = myGNSS.getHighResLongitude();
int8_t longitudeHp = myGNSS.getHighResLongitudeHp();

// Read altitude above ellipsoid
int32_t ellipsoid = myGNSS.getElipsoid();
int8_t ellipsoidHp = myGNSS.getElipsoidHp();

// Read altitude above mean sea level
int32_t msl = myGNSS.getMeanSeaLevel();
int8_t mslHp = myGNSS.getMeanSeaLevelHp();

// Read horizontal accuracy estimate
uint32_t accuracy = myGNSS.getHorizontalAccuracy();
```

<FunctionDocumentation functionName="getHighResLatitude()" description="Returns the standard latitude component from the HPPOSLLH message." returnDescription="Returns a long, representing latitude in degrees × 10^-7." parameters={[]} />

<FunctionDocumentation functionName="getHighResLatitudeHp()" description="Returns the high-precision latitude component from the HPPOSLLH message." returnDescription="Returns a int, representing latitude fractional component in degrees × 10^-9." parameters={[]} />

<FunctionDocumentation functionName="getHighResLongitude()" description="Returns the standard longitude component from the HPPOSLLH message." returnDescription="Returns a long, representing longitude in degrees × 10^-7." parameters={[]} />

<FunctionDocumentation functionName="getHighResLongitudeHp()" description="Returns the high-precision longitude component from the HPPOSLLH message." returnDescription="Returns a int, representing longitude fractional component in degrees × 10^-9." parameters={[]} />

<FunctionDocumentation functionName="getElipsoid()" description="Returns the altitude above the ellipsoid." returnDescription="Returns a long, representing altitude in millimeters." parameters={[]} />

<FunctionDocumentation functionName="getElipsoidHp()" description="Returns the high-precision altitude component above the ellipsoid." returnDescription="Returns a int, representing altitude fractional component in 0.1 mm units." parameters={[]} />

<FunctionDocumentation functionName="getMeanSeaLevel()" description="Returns the altitude above mean sea level." returnDescription="Returns a long, representing altitude in millimeters." parameters={[]} />

<FunctionDocumentation functionName="getMeanSeaLevelHp()" description="Returns the high-precision altitude component above mean sea level." returnDescription="Returns a int, representing altitude fractional component in 0.1 mm units." parameters={[]} />

<FunctionDocumentation functionName="getHorizontalAccuracy()" description="Returns the estimated horizontal accuracy of the GNSS position." returnDescription="Returns a long, representing accuracy in 0.1 mm units." parameters={[]} />
