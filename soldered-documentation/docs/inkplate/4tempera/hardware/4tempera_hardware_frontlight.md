---  
slug: /inkplate/4tempera/hardware/frontlight  
title: Frontlight  
id: 4tempera-hardware-frontlight  
hide_title: true  
---

<SectionTitle title="Frontlight Overview" backgroundImage="img/frontlight.jpg" />

The Inkplate 4 TEMPERA includes a built-in **frontlight system** designed to provide even illumination across the display surface, making the screen readable in dark or low-light environments. Unlike backlit displays, this frontlight preserves the e-paper’s natural, glare-free appearance while enhancing visibility.

---

## Key Features

- Integrated **white LED frontlight layer** bonded with the **ED038TH2** e-paper panel  
- **64 levels of adjustable brightness**, controlled via software  
- Uniform light diffusion across the entire screen  
- Energy-efficient LED design with smooth dimming capability  
- Operates independently of display updates, with no effect on image quality or refresh behavior  

<InfoBox>The frontlight is an integral part of the original ED038TH2 display assembly used in Inkplate 4 TEMPERA. It is tested for brightness control and consistency during production.</InfoBox>

---

## Usage and Design Considerations

- Ideal for use in **low-light or variable-light environments**  
- Can be dynamically adjusted using simple Inkplate library functions (e.g., via PWM)  
- Fully functional on both **USB and battery power**  
- Runs separately from the e-paper controller, so it does **not cause ghosting or screen interference**  

---

## Tips for Effective Use

- Use lower brightness levels when running on battery to extend runtime  
- Consider turning off the frontlight when the display is inactive or during deep sleep  
- For ambient-reactive behavior, pair with a **light sensor** to adjust brightness automatically  
- Plan power budgets accordingly — higher brightness levels increase current draw  

---

## Related Examples

<QuickLink 
  title="Frontlight Brightness Example" 
  description="Basic sketch to control frontlight brightness on Inkplate 4 TEMPERA."
  url="https://github.com/SolderedElectronics/Inkplate-Arduino-library/blob/dev/examples/Inkplate4TEMPERA/Basic/Inkplate4TEMPERA_Simple_Frontlight/Inkplate4TEMPERA_Simple_Frontlight.ino"
/>