<!--
SEO TITLE (max 60 chars): E-Ink vs LCD vs OLED: Which Display Should You Use?
META DESCRIPTION (152 chars): E-Ink, LCD, and OLED each suit different projects. Compare power consumption, refresh rate, and sunlight readability to pick the right display.
PRIMARY KEYWORD: e-ink vs LCD vs OLED
SECONDARY KEYWORDS: e-paper display, battery-powered display, display power consumption, OLED vs LCD
-->

# Choosing Your Display: E-Ink, LCD, or OLED — Strengths, Weaknesses, and When to Use Each

E-Ink, LCD, and OLED work differently enough that the wrong pick can mean redesigning parts of your project later. The choice depends on how often the content changes, where the display will be used, and how long it needs to run on battery.

---

## E-Ink

[E Ink](https://en.wikipedia.org/wiki/E_Ink) displays use microcapsules filled with charged black and white particles. Voltage moves them to form an image, then the screen holds it without drawing any power. No backlight, no emission. It reads like a printed page and works fine in direct sunlight.

Power draw is near zero: less than 1 mW during a refresh, exactly 0 mW on a static image. On a 1000 mAh battery, that's over 10,000 hours on static content. The weak point is refresh speed. A full update takes 250 ms to 2 seconds, and partial refreshes can leave ghosting. For video, animations, or a constantly updating UI, E-Ink is the wrong choice.

---

## LCD

An LCD panel passes backlight through liquid crystals. The backlight runs constantly regardless of what's on screen, so power draw doesn't change with content. A small TFT draws 100-400 mW, a 7" touchscreen typically 500 mW to 1 W. LCD handles video, fast UIs, and static content equally well. Standard panels run 0 to +50°C, high-temperature models down to -20°C, and IPS panels give you wide viewing angles.

The trade-off is efficiency on static content. The backlight runs at full draw no matter what's displayed, so for battery builds where the screen mostly shows the same thing, LCD uses significantly more power than E-Ink.

---

## OLED

Each pixel in an OLED display is its own light source. When a pixel is black, it's off, which is why OLED contrast is higher than LCD. Response time is around 10 µs and viewing angles are wide. A dark UI can use up to 40% less power than an equivalent LCD, making OLED a good fit for wearables with dark themes.

Efficiency depends on what's on screen though. A bright white background can draw more than a comparable TFT, and direct sunlight is a weak point since emitted light can't compete with ambient brightness.


---

## Side-by-side

| | E-Ink | LCD | OLED |
|---|---|---|---|
| Power (active) | <1 mW | 100 mW – 1 W | 50–300 mW |
| Power (static image) | 0 mW | 100 mW – 1 W | near 0 mW |
| Battery life (1000 mAh, static text) | 10,000+ hours | 10–20 hours | 15–30 hours |
| Sunlight readability | Excellent | Good (reflective mode) | Poor |
| Refresh rate | 250 ms – 2 s | Fast | Very fast (~10 µs) |
| Color | Black & white (standard) | Full color | Full color |
| Contrast | Medium | Medium | High |
| Temperature range | Varies by panel | -20 to +70°C (industrial) | Varies |

---

## Which one fits your project

For battery-powered projects, go with E-Ink. A 1000 mAh battery runs an OLED for 15-30 hours and E-Ink for over 10,000 hours.

For dashboards and control panels, LCD makes more sense. It handles color, fast updates, and gives you a predictable power budget.

For wearables, OLED is the right call, especially with a dark theme. Off pixels draw no power and the contrast suits small screens well.

E-Ink uses about 7-8 mJ/cm² per full refresh. Fewer than 4 updates per day and E-Ink is the most efficient option. More than 600 and LCD becomes the better pick.

---

## Example projects

**Smart home dashboard.** An E-Ink display showing daily weather, energy usage, or a to-do list is one of the most popular maker builds. It updates a few times a day and runs for months on a small battery. Inkplate boards are built exactly for this.

**Wearable fitness tracker.** OLED is the standard choice here. The screen is small, the background is usually dark, and off pixels cost nothing. Response time is fast enough for smooth animations and step counters.

**Industrial control panel.** LCD handles this well. It works across a wide temperature range, updates instantly, and shows color clearly. You get a predictable power draw and wide viewing angles with an IPS panel.

**Outdoor sensor display.** E-Ink reads clearly in direct sunlight without a backlight, which also keeps power consumption low. A weather station or soil monitor that updates every few hours is a natural fit.

---

## Build with E-Ink at Soldered

The [Inkplate](https://soldered.com/categories/inkplate/) line uses recycled e-paper panels from real e-readers, combined with an ESP32. You connect USB, open an example, and it runs. No additional hardware needed to get started.

If you need OLED or TFT LCD for a project that requires color or fast updates, [display modules are in the Soldered shop](https://soldered.com/categories/displays/) too.

---

## Conclusion

For battery life, E-Ink. For an all-rounder, LCD. For contrast and response time, OLED. Pick the one that fits what your project does.

---

## Display technology FAQs

### What is the difference between E-Ink, LCD, and OLED?
E-Ink reflects ambient light and holds an image without drawing power. LCD uses a constant backlight filtered through liquid crystals. OLED has self-emitting pixels with no backlight.

### Which display uses the least power?
E-Ink draws near zero when displaying a static image and under 1 mW during a refresh. For low-update applications, E-Ink is significantly more efficient than the other two. For content that updates frequently, LCD becomes more practical.

### Can you use E-Ink for video or animations?
No. E-Ink refresh times range from 250 ms to 2 seconds, which makes it unsuitable for video or fast UI updates. Partial refreshes can speed things up slightly but introduce ghosting.

### Is OLED better than LCD?
It depends on the use case. OLED offers better contrast, faster response, and lower power consumption with dark UIs. LCD is more predictable in power draw and handles a wider range of content without trade-offs.

### Which display is best for outdoor use?
E-Ink reads well in direct sunlight because it reflects ambient light like paper. Reflective LCD also works well outdoors. OLED handles bright conditions the worst of the three.

### Which display should I use for a smart home dashboard?
LCD or OLED if the dashboard updates frequently. E-Ink if it mostly shows static information like daily weather, energy usage, or to-do lists. Inkplate boards are a popular choice for home dashboards that don't need real-time updates.

### What is the best display for a battery-powered sensor?
E-Ink, if the reading only updates occasionally. It holds the displayed value without drawing any power between refreshes. If you need frequent updates, a small OLED in dark mode is a reasonable alternative.
