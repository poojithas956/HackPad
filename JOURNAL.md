---
title: "HackPad"
author: "poojithas536"
description: "A custom mini keyboard or macro board, where every physical key is fully programmable to launch apps, trigger shortcuts, control media, or run multi-step automated commands with a single press of a button."
created_at: "2026-10-12"
---

# 2026-10-12: BOM.md

**Total time spent: 18 min**


Approximate vendor pricing based on 1 USD = 94 INR.

| Item | Qty | Vendor | Price (USD) | Price (INR) | Notes |
|---|---:|---|---:|---:|---|
| PCB | 5 | Robu | $10 | Rs. 960 | PCB
| [Waveshare RP2040 Zero without header](https://robu.in/product/waveshare-rp2040-zero-without-header/) | 1 | Robu | $4.47 | ₹420 | Main controller |
| [1N4148 diode](https://robu.in/product/1n4148-tap-vishay-1n4148-tap-small-signal-diode-single-100-v-150-ma-1-v-8-ns-2-a/) | 12 | Robu | $0.83 total | ₹78 total | Matrix diodes |
| [EC11 rotary encoder with push switch](https://robu.in/product/hongyan-ec11h-7ce15p1zy15f7-rotary-encoder-with-push-button-switch-vertical-plug-in/) | 1 | Robu | $0.62 | ₹58 | Knob + click |
| [MDA Lavender numpad keycaps](https://stackskb.com/store/numpad-keycaps/?attribute_variant=MDA+Lavender) | 12 | Stackskb | $1.60 | ₹150 | Keycaps |
| [Gateron Baby Kangaroo 2.0 tactile switches](https://stackskb.com/store/gateron-baby-kangaroo-2-0-tactile-switch-pack-of-10/) | 20 | Stackskb | $9.57 | ₹900 | Pack of 20 |
| [Gateron hotswap sockets](https://stackskb.com/store/gateron-hotswap-sockets/) | 13 | Stackskb | $1.38 total | ₹130 total | Socketed switch support |
| 1x4 right-angle pin header | 1 | Self-supplied | $0.00 | ₹0 | UART / expansion |
| Tax and Shipping | | | $5 | Rs400 | incl. Tax + Shipping fee + Conversion rate to INR | 
| Total | — | — | $35 | ₹2,636 | Estimated project total |

## Cart

![image.png](https://cdn.hackclub.com/01a1326f-002d-710a-a59b-e2fc6797866f/image.png)

![image.png](https://cdn.hackclub.com/01a1326f-873b-767a-8116-63e7c7423f7e/image.png)

# 2026-10-12: Firmware

**Total time spent: 35 min**

After finishing the board and case work, I moved to firmware and built a KMK setup for the HackPad using CircuitPython on the RP2040 Zero.

I first mapped the firmware directly to the KiCad netlist so the matrix and encoder behavior matched the hardware exactly. The matrix is configured as a 4x3 scan with ROW1-ROW4 on GP27, GP28, GP29, and GP13, and COL1-COL3 on GP14, GP15, and GP26. For the EC11 rotary encoder, I mapped A/B/SW to GP10, GP11, and GP12.

Then I implemented a layered keymap with advanced behavior:

- Layer 0 (Base): daily editing macros (cut, copy, paste, undo, redo, save, find)
- Layer 1 (Nav): arrows, home/end, page navigation
- Layer 2 (Media): transport and volume controls
- Layer 3 (System): utility keys including boot/reset access

I also added extra firmware features to make the pad feel more useful:

- Tap-dance for Esc/Grave
- Layer-tap keys on the bottom row (tap sends key, hold changes layer)
- Chord combos for common workflow actions:
  - Copy + Paste -> Select All
  - Undo + Redo -> Save
- Layer-aware encoder actions (volume, nav, media, paging depending on active layer)

Finally, I wrote setup documentation so flashing is straightforward and includes troubleshooting notes (like switching diode orientation if scan direction is inverted on first boot).

The firmware script compiles cleanly with Python syntax checks, so this revision is ready for on-device testing.

![image.png](https://cdn.hackclub.com/01a13259-bcc8-7dd3-9142-74c9994143d7/image.png)

*AI was used for debugging the firmware !!

* Also please don't deflate it, I have written these journals honestly and 10 hours for a hackpad is pretty justified ..

Happy Forging !

# 2026-10-12: Designing the CAD for the HackPad

**Total time spent: 4 hr**

For designing the case, I chose Onshape because it’s simple to use and performs better on my system, especially since I’m dealing with a GPU bottleneck.

I started by creating the base, i.e., the bottom case, and then assembled it in Onshape by importing the PCB from KiCad along with all its components to ensure precise alignment and accuracy. Once the bottom case was finalized, I downloaded the plate design from the ai03 Plate Generator and imported the .DXF file into a sketch. I then modified the plate to match the case dimensions, ensuring the plate thickness was exactly 1.4 mm.

After completing the plate, I assembled everything again and made a few aesthetic improvements. Finally, I fine-tuned the dimensions for the cutouts, including spaces for heat inserts, screws, and nuts.


![image.png](https://cdn.hackclub.com/01a13255-1f19-75f3-8fb5-47eb7f2e6e37/image.png)

![image.png](https://cdn.hackclub.com/01a13255-d436-7889-b1b6-397f11a2c5a0/image.png)

![image.png](https://cdn.hackclub.com/01a13256-45f4-7d21-9032-221a3b2f3240/image.png)

![image.png](https://cdn.hackclub.com/01a13256-ad49-7346-8911-ef12c18e6dba/image.png)

![image.png](https://cdn.hackclub.com/01a13257-1280-7164-947c-373d55ebb181/image.png)

### Onshape: [Link](https://cad.onshape.com/documents/0b41c2a43364fbf889c51837/w/9b38bee00f76805735f359c7/e/e1c15f719b395e4b4723bcd3?renderMode=0&uiState=6acd6ca877de21c16f19ffa1)

# 2026-10-12: Routing the Board

**Total time spent: 3 hr 27 min**

Next, I moved on to PCB routing. I started by using the keyboard auto-layout for the 12 MX switches, then set the board outline to 101.7 × 66.7 mm. After that, I placed the MCU and the EC11 rotary encoder, and finally added the UART pins.

![image.png](https://cdn.hackclub.com/01a13215-d2b7-7cac-a332-124bb082eb01/image.png)

Feeling the board being a bit boring and empty, I added some silkscreen logo adding color to the PCB 

Front
![image.png](https://cdn.hackclub.com/01a13217-9975-7acf-9ba4-7d515a900756/image.png)

Back
![image.png](https://cdn.hackclub.com/01a13218-d694-7348-94a3-270a3e2c9dd8/image.png)


# 2026-10-12: Drawing Schematic

**Total time spent: 2 hr 25 min**

Next I started with Schematics, I choose KiCAD as its free and has a huge communtiy resources. 

***
### Layout
 I started with the [keyboard layout](https://www.keyboard-layout-editor.com/) and decided to go with 3x4 matrix grid

![layout](https://cdn.hackclub.com/01a1321b-d81b-7287-8722-7d1b6b1d4b07/image.png)

***
### Downloading the required footprint
 Next I started downloading the required footprint like the RP2040-zero from waveshare, and some logos, like HackClub and Stasis. Converting it into silkscreen. 

***
### Placing the footprint
 I started routing the MCU and the Matrix grid first using labels. Then, routed other components 

![schematic](https://cdn.hackclub.com/01a1321b-6e18-7864-8edc-61699933cae7/image.png)

***


# 2026-10-12: Reasearch

**Total time spent: 30 min**

## Project Specifications
 I decided my 2nd project would be a HackPad pairing it with my 60% Keyboard. 

Specs
- RP2040 Zero - MCU
- 12x MX style Switches (3x4 Matric)
- 1x EC11 Rotary Encoder + Switch
- 1x UART pin
- 100x65 PCB dimension
- x4 M2.5 Mounting holes

***
![Let's go](https://forge.hackclub.com/dino_images/strong_dino_1.png)
***



