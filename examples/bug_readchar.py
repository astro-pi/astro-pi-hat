#!/usr/bin/python3
import time
from sense_hat import SenseHat
import readchar
import sys

"""
    A bug on a colored background, responding to keypresses.

    Modify the starting state in the `state` dict.
    The background changes colors based on the bug's xy coords.

    This version handles input with the readchar 3rd party module.
    
    You nay need to install libncurses5-dev:
    
    sudo apt-get update
    sudo apt-get install libncurses5-dev
    sudo pip3 install readchar
"""

state = { "bug_x" : 4,
          "bug_y" : 4,
          "bug_rgb" : (250,250,250) }

print("Press **Enter** or click the joystick to quit")

sense = SenseHat()

def setscreen():
    """Takes x and y vales and alters screen state"""
    global state
    x = state["bug_x"]
    y = state["bug_y"]
    if sense.low_light:
        zero = 8
    else:
        zero = 48
    brightness = 255 -zero 
    g = int(((x * 32)/255) * brightness + zero)
    b = int(((y * 32)/255) * brightness + zero)
    r = abs(g - b)
    sense.clear((r,g,b))
    print(r,g,b)
    
def draw_bug(key):
    global state
    key_code = key
    if key_code == readchar.key.ENTER:
        sys.exit()
    elif key_code == readchar.key.UP:
        state["bug_x"] = state["bug_x"]
        state["bug_y"] = 7 if state["bug_y"] == 0 else state["bug_y"] - 1
        setscreen()
        sense.set_pixel(state["bug_x"], state["bug_y"], state["bug_rgb"])
    elif key_code == readchar.key.DOWN:
        state["bug_x"] = state["bug_x"]
        state["bug_y"] = 0 if state["bug_y"] == 7 else state["bug_y"] + 1
        setscreen()
        sense.set_pixel(state["bug_x"], state["bug_y"], state["bug_rgb"])
    elif key_code == readchar.key.RIGHT:
        state["bug_x"] = 0 if state["bug_x"] == 7 else state["bug_x"] + 1
        state["bug_y"] = state["bug_y"]
        setscreen()
        sense.set_pixel(state["bug_x"], state["bug_y"], state["bug_rgb"])
    elif key_code == readchar.key.LEFT:
        state["bug_x"] = 7 if state["bug_x"] == 0 else state["bug_x"] - 1
        state["bug_y"] = state["bug_y"] 
        setscreen()
        sense.set_pixel(state["bug_x"], state["bug_y"], state["bug_rgb"])

# Initial state
setscreen()
sense.set_pixel(state["bug_x"], state["bug_y"], state["bug_rgb"])

try:
    while True:
        key = readchar.readkey()
        print(key)
        draw_bug(key)
except KeyboardInterrupt:
    sys.exit()

