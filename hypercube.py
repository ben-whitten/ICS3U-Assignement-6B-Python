#!/usr/bin/env python3

# Created by: Ben Whitten
# Created on: November 2019
# This is a program which finds the area of a hypercube.

import math


# This allows me to do things with the text.
class color:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'


def calculations(side_copy):
    # This does the calculations
    area = (24 * (side_copy**2))
    return area


def main():
    # This is what gets the dimensions of the hypercube
    while True:
        side_as_string = input(color.YELLOW + "Input the side length" +
                               " of the hypercube: " + color.END)

        try:
            side = int(side_as_string)

            if side >= 0:
                area = calculations(side_copy=side)
                print("{0}cm^2".format(area))
                break

            else:
                print('')
                print(color.PURPLE + color.UNDERLINE + 'That is not a valid'
                      ' number...' + color.END)
                print("")
                print("")

        except Exception:
            print('')
            print(color.PURPLE + color.UNDERLINE + 'That is not a valid'
                  ' number...' + color.END)
            print("")
            print("")


if __name__ == "__main__":
    main()
