# HackPad Advanced Firmware (KMK)

This folder contains an advanced default firmware for the RP2040-Zero-based HackPad.

## What You Get

- Correct matrix pin mapping from your PCB
- Rotary encoder support (turn + click)
- 4 layers: Base, Nav, Media, System
- Tap-dance (`ESC` on single tap, `` ` `` on double tap)
- Layer-tap keys (tap sends key, hold changes layer)
- Chord combos:
  - `Copy + Paste` -> `Select All`
  - `Undo + Redo` -> `Save`

## Pin Mapping (from KiCad)

- Columns: `GP14 GP15 GP26`
- Rows: `GP27 GP28 GP29 GP13`
- Encoder A/B/SW: `GP10 GP11 GP12`

## Install Steps

1. Flash CircuitPython to the RP2040 Zero.
2. Download KMK and copy the `kmk` folder to the CIRCUITPY drive.
3. Copy [firmware/kmk/code.py](code.py) to the root of CIRCUITPY as `code.py`.
4. Replug the board.

## Layer Overview

- `Layer 0 (Base)`: editing shortcuts and layer access
- `Layer 1 (Nav)`: arrows, home/end, page movement
- `Layer 2 (Media)`: media transport and volume
- `Layer 3 (System)`: function keys and reset/boot helpers

The bottom row of Layer 0 is layer-tap:

- Left key: tap `Space`, hold Layer 1
- Middle key: tap `Enter`, hold Layer 2
- Right key: tap `Tab`, hold Layer 3

## Notes

- If the matrix scans inverted on first boot, switch
  `DiodeOrientation.ROW2COL` to `DiodeOrientation.COL2ROW` in [firmware/kmk/code.py](code.py).
- `KC.BOOT` and `KC.RESET` are provided on Layer 3 for recovery/reflash flows.
