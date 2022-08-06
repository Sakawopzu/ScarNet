#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from time import sleep
import pyfiglet

i = 1

with open("pyfigletfonts.txt", "r") as file:
    fonts = file.read().splitlines()

for fonty in fonts:
    print(i)
    print("Testing font " + fonty)
    f = pyfiglet.Figlet(font=fonty, width=80)
    print(f.renderText('FooBar'))
    i += 1