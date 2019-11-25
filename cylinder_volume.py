#!/usr/bin/env python3

# Created by: Manuel Garcia Yuste
# Created on : November 2019
# This program calculate the volume of a cylinder


import math


def volume_calculator(radius, height):
    # This'll determine the mark

    # process
    volume = math.pi * radius * radius * height
    return round(volume, 2)


def main():
    # Welcome
    input("Press Enter to start.")

    while True:
        try:
            # input
            radius = float(input("What is the radius: "))
            height = float(input("What is the height: "))
            # runs volume_calculator()
            volume = volume_calculator(height=height, radius=radius)
            # output
            print("The volume is " + str(volume) + " units cubed.")
            break
        except ValueError:
            print("Invalid input.")


if __name__ == "__main__":
    main()
