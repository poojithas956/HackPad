# HackPad

A 12-key macropad I built as my second hardware project for Stasis, designed to pair with my 60% keyboard for editing, shortcuts, media control, etc...

Hi there, this is my fully custom keypad from scratch, and I tried to keep it clean, practical, and actually buildable.
 

## Quick Project Summary

- Project: 3x4 macropad + rotary encoder
- MCU: RP2040 Zero
- Switches: 12x MX-style
- Extra input: 1x EC11 rotary encoder with push switch
- Matrix: 3 rows x 4 columns
- PCB size target: about 100mm x 65mm
- Case workflow: KiCad PCB export -> Onshape assembly -> custom bottom case + plate

## Why I Made This

I wanted a dedicated macropad next to my keyboard for common shortcuts (copy/paste, app switching, media, timeline scrubbing, etc.) and I wanted to learn the full flow:

1. keyboard layout planning
2. schematic capture
3. PCB routing
4. case CAD around real board geometry

## Features

- 12 programmable keys (MX style)
- Rotary encoder with click for volume/scroll/tool size/etc.
- RP2040-based and easy to firmware-program
- Through-hole diodes for matrix
- UART header exposed
- Custom silkscreen logos for personality

## Progress pictures

![Firmware progress](https://cdn.hackclub.com/01a13259-bcc8-7dd3-9142-74c9994143d7/image.png)

![CAD case design](https://cdn.hackclub.com/01a13255-1f19-75f3-8fb5-47eb7f2e6e37/image.png)

![CAD assembly](https://cdn.hackclub.com/01a13255-d436-7889-b1b6-397f11a2c5a0/image.png)

![Case front view](https://cdn.hackclub.com/01a13256-45f4-7d21-9032-221a3b2f3240/image.png)

![Case side view](https://cdn.hackclub.com/01a13256-ad49-7346-8911-ef12c18e6dba/image.png)

![PCB routing progress](https://cdn.hackclub.com/01a13257-1280-7164-947c-373d55ebb181/image.png)

![Board routing](https://cdn.hackclub.com/01a13215-d2b7-7cac-a332-124bb082eb01/image.png)

![Front silkscreen](https://cdn.hackclub.com/01a13217-9975-7acf-9ba4-7d515a900756/image.png)

![Back silkscreen](https://cdn.hackclub.com/01a13218-d694-7348-94a3-270a3e2c9dd8/image.png)

![Keyboard layout](https://cdn.hackclub.com/01a1321b-d81b-7287-8722-7d1b6b1d4b07/image.png)

![Schematic capture](https://cdn.hackclub.com/01a1321b-6e18-7864-8edc-61699933cae7/image.png)

![Project kickoff](https://forge.hackclub.com/dino_images/strong_dino_1.png)

## Onshape: [Link](https://cad.onshape.com/documents/0b41c2a43364fbf889c51837/w/9b38bee00f76805735f359c7/e/e1c15f719b395e4b4723bcd3?renderMode=0&uiState=6acd6ca877de21c16f19ffa1)

## Bill of Materials (BOM)

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

For the KiCad design BOM, see [production/bom.csv](production/bom.csv). The full project buying list is also available in [bom.csv](bom.csv).

## Design Files Included

- Schematic: [PCB/HackPad.kicad_sch](PCB/HackPad.kicad_sch)
- PCB: [PCB/HackPad.kicad_pcb](PCB/HackPad.kicad_pcb)
- KiCad project: [PCB/HackPad.kicad_pro](PCB/HackPad.kicad_pro)
- Layout JSON: [PCB/keyboard-layout.json](PCB/keyboard-layout.json)
- Plate DXF: [PCB/plate.dxf](PCB/plate.dxf)
- CAD model: [CAD/HackPad.step](CAD/HackPad.step)
- Production files:
	- [production/bom.csv](production/bom.csv)
	- [production/positions.csv](production/positions.csv)
	- [production/designators.csv](production/designators.csv)
	- [production/netlist.ipc](production/netlist.ipc)

## Firmware

KMK firmware for this board is included in:

- [firmware/kmk/code.py](firmware/kmk/code.py)
- [firmware/kmk/README.md](firmware/kmk/README.md)

It is preconfigured for the exact matrix and encoder pins used in this PCB.


## What I Learned

- Importing the actual PCB into CAD early saves a lot of pain later.
- Matrix labeling in schematic makes routing way less confusing.
- Tiny mechanical details (insert depth, nut traps, plate thickness) matter a lot more than expected.
- Silkscreen art is optional, but morale is not.
