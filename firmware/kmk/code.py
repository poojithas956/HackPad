import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.modules.combos import Chord, Combos
from kmk.modules.encoder import EncoderHandler
from kmk.modules.holdtap import HoldTap
from kmk.modules.layers import Layers
from kmk.modules.tapdance import TapDance
from kmk.scanners import DiodeOrientation


keyboard = KMKKeyboard()

# Matrix from PCB netlist:
# COL1=GP14, COL2=GP15, COL3=GP26
# ROW1=GP27, ROW2=GP28, ROW3=GP29, ROW4=GP13
keyboard.col_pins = (board.GP14, board.GP15, board.GP26)
keyboard.row_pins = (board.GP27, board.GP28, board.GP29, board.GP13)
keyboard.diode_orientation = DiodeOrientation.ROW2COL

layers = Layers()
holdtap = HoldTap()
tapdance = TapDance()
combos = Combos()
encoder_handler = EncoderHandler()

keyboard.modules = [layers, holdtap, tapdance, combos, encoder_handler]


# Common aliases used in keymap and combos.
UNDO = KC.LCTL(KC.Z)
REDO = KC.LCTL(KC.Y)
CUT = KC.LCTL(KC.X)
COPY = KC.LCTL(KC.C)
PASTE = KC.LCTL(KC.V)
SAVE = KC.LCTL(KC.S)
FIND = KC.LCTL(KC.F)
SELECT_ALL = KC.LCTL(KC.A)

TD_ESC_GRV = KC.TD(KC.ESC, KC.GRV)

# Tap for space, hold for NAV layer.
LT_NAV = KC.LT(1, KC.SPC)
# Tap for enter, hold for MEDIA layer.
LT_MEDIA = KC.LT(2, KC.ENT)
# Tap for tab, hold for SYSTEM layer.
LT_SYS = KC.LT(3, KC.TAB)


# Chords on BASE layer:
# COPY + PASTE -> SELECT_ALL
# UNDO + REDO -> SAVE
combos.combos = [
	Chord((COPY, PASTE), SELECT_ALL),
	Chord((UNDO, REDO), SAVE),
]


# Encoder pins from PCB netlist:
# RES_A=GP10, RES_B=GP11, RES_S1=GP12
encoder_handler.pins = ((board.GP10, board.GP11, board.GP12, False),)

# Per-layer encoder map: (ccw, cw, press)
encoder_handler.map = [
	((KC.VOLD, KC.VOLU, KC.MUTE),),
	((KC.LEFT, KC.RIGHT, KC.ENT),),
	((KC.MPRV, KC.MNXT, KC.MPLY),),
	((KC.PGDN, KC.PGUP, KC.DEL),),
]


keyboard.keymap = [
	# Layer 0: BASE (editing macros)
	[
		TD_ESC_GRV,
		CUT,
		COPY,
		PASTE,
		UNDO,
		REDO,
		SAVE,
		FIND,
		KC.INS,
		LT_NAV,
		LT_MEDIA,
		LT_SYS,
	],
	# Layer 1: NAV
	[
		KC.HOME,
		KC.UP,
		KC.END,
		KC.LEFT,
		KC.DOWN,
		KC.RIGHT,
		KC.PGUP,
		KC.PGDN,
		KC.DEL,
		KC.TRNS,
		KC.TRNS,
		KC.TRNS,
	],
	# Layer 2: MEDIA
	[
		KC.MPRV,
		KC.MPLY,
		KC.MNXT,
		KC.VOLD,
		KC.MUTE,
		KC.VOLU,
		KC.F11,
		KC.F12,
		KC.PSCR,
		KC.TRNS,
		KC.TRNS,
		KC.TRNS,
	],
	# Layer 3: SYSTEM / utilities
	[
		KC.F1,
		KC.F2,
		KC.F3,
		KC.F4,
		KC.F5,
		KC.F6,
		KC.F7,
		KC.F8,
		KC.CAPS,
		KC.BOOT,
		KC.RESET,
		KC.NO,
	],
]


if __name__ == "__main__":
	keyboard.go()
