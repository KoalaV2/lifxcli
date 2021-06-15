#!/usr/bin/env python3
# coding=utf-8
import sys
from time import sleep

from lifxlan import BLUE, CYAN, GREEN, LifxLAN, ORANGE, PINK, PURPLE, RED, YELLOW, COLD_WHITE, WARM_WHITE, GOLD


def main(color):

    print("Discovering lights...")
    lifx = LifxLAN(1)

    devices = lifx.get_lights()
    #if devices == []:
        #print("No lights found")
        #return ""
    print(f"Found light: {devices}")

    original_colors = lifx.get_color_all_lights()

    color_up = str(color.upper())

    if color_up == "OFF":
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
            "YELLOW":YELLOW,
            "GOLD":GOLD,
            "WARM": WARM_WHITE,
            "COLD": COLD_WHITE
            }

    print("Turning on the light...")
    lifx.set_power_all_lights("on")

    if color_up in color_name:
        print(f"Setting color to {color_up}")
        lifx.set_color_all_lights(color_name[color_up])
    else:
        print("Color not found, defaulting to pink")
        lifx.set_color_all_lights(PINK)

if __name__=="__main__":
    try:
        color = sys.argv[1]
    except IndexError:
        color = input("What color do you want to set the light to? \n :")
    main(color)
