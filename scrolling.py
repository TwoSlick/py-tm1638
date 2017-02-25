#!/usr/bin/env python

# TM1638 playground

import TM1638
import time

# These are the pins the display is connected to. Adjust accordingly.
# In addition to these you need to connect to 5V and ground.

DIO = 17
CLK = 21
STB = 22

display = TM1638.TM1638(DIO, CLK, STB)

display.enable(1)

display.scroll_text("Scroll some text with method 1")
display.set_text("Scroll some text with method 2", scrolling=True, print_forward=False)
display.set_text("Start scroll from left", scrolling=True, print_forward=True)
