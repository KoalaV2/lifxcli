#!/usr/bin/env python3
# coding=utf-8

import sys
from lifxlan import BLUE, CYAN, GREEN, LifxLAN, ORANGE, PINK, PURPLE, RED, YELLOW, COLD_WHITE, WARM_WHITE, GOLD


def main(color):

    print("Discovering lights...")
    lifx = LifxLAN(1)

    devices = lifx.get_lights()
    print(f"Found light: {devices}")

    if color == "OFF":
        lifx.set_power_all_lights("off")
        print("Turned off the light..")
        return()

    # TODO: Be able to set warmth / brightness

    color_name = {
            "RED":RED,
            "BLUE":BLUE,
            "CYAN":CYAN,
            "GREEN":GREEN,
            "ORANGE":ORANGE,
            "PURPLE":PURPLE,
            "PINK":PINK,
            "YELLOW":YELLOW,
            "GOLD":GOLD,
            "WARM": WARM_WHITE,
            "COLD": COLD_WHITE
            }

    print("Turning on the light...")
    lifx.set_power_all_lights("on")

    if color in color_name:
        print(f"Setting color to {color}")
        lifx.set_color_all_lights(color_name[color])
    else:
        print("Color not found.")

if __name__=="__main__":
    try:
        color = sys.argv[1]
    except IndexError:
        color = input("What color do you want to set the light to? \n :")
    main(color.upper())
