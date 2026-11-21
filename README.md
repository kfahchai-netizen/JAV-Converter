# 📏 JAV Converter: Unit Converter with a "Fun Mode"

![Python](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)
![Tkinter](https://img.shields.io/badge/GUI-Tkinter-2b5b84)
![Pygame](https://img.shields.io/badge/audio-Pygame-1f9e40)

> A desktop unit converter with a twist. Besides the standard conversions, **Fun Mode** answers questions like *"How many ants long is a guitar?"* or *"How many Swinburne campuses fit in Malaysia?"*

## ✨ Features

### Standard mode
| Category | Units |
|---|---|
| Length | m · km · cm · mm · µm |
| Area | m² · km² · cm² · mm² · µm² |
| Volume | L · mL · cm³ · m³ · mm³ · km³ |
| Weight | g · kg · mg · t |
| Temperature | °C · °F · K |
| Time | 24-hour ⇄ 12-hour (AM/PM) |

Each conversion shows a random **fun fact** about that category.

### 🎉 Fun mode
Press **Toggle Fun** to switch to a pink theme and convert between everyday objects:

| Category | Example objects |
|---|---|
| Length | Ant · Guitar · Red blood cell · Eiffel Tower · Moon diameter |
| Area | Malaysia · Swinburne campus · Computer screen · Bacterium · Grain of salt |
| Volume | Adult human blood · Pacific Ocean · Earth · Water bottle · Water droplet |
| Weight | Mouse · Elephant · Aeroplane · Ringgit note · Mount Everest |
| Data size | Swinburne logo PNG · All of Wikipedia |
| Age | Human years ⇄ Dog years 🐶 |

### Also included
- **Conversion history:** every result is saved to `conversion_history.txt`. You can view it in its own window or clear it.
- **Sound effects** for button presses and toggling Fun Mode (via Pygame).
- **Built-in help** dialog.

## 🚀 Getting started

```bash
git clone https://github.com/kfahchai-netizen/JAV-Converter.git
cd JAV-Converter
pip install pygame
python Main_module.py
```

> Tkinter comes with most Python installs. 🔊 Turn your volume up: the app uses sound!

## 🏗️ Architecture

The app keeps the conversion maths separate from the interface:

```
Main_module.py              # ▶ Entry point: main window, theme toggle, navigation
├── Gui_module.py           # Standard-unit windows, history window, fun facts
├── Gui_items_module.py     # Fun-mode windows (reuses a generic form builder)
├── Converter_module.py     # Pure functions: length, area, volume, weight, temperature, time
└── Converter_items_module.py  # Pure functions: object-based conversions, dog years
```

All object conversions use one formula: `value × size(from) / size(to)`, with real-world reference sizes stored in dictionaries. Adding a new object is a one-line change.

## 📚 Key concepts

Modular programming · Separating logic from UI · Tkinter event handling · Dictionaries as lookup tables · File I/O · Theming

---

<sub>Made by **Kean Fah Chai** · Swinburne University of Technology Sarawak</sub>
