# This file lets the project run on a PC,
# but does no real action on hardware.
BCM = 0
IN = 0
OUT = 0
PUD_DOWN = 0
RISING = 0
LOW = 0
HIGH = 0
def setmode(pinmode): pass
def cleanup(pin=0): pass
def setup(pin, dir, pull_up_down=0, initial=0): pass
def add_event_detect(pin, edge, callback): pass
def remove_event_detect(pin): pass
def output(pin, dir): pass
def setwarnings(warn): pass
