#!/usr/bin/env python3

# Created by: Kaitlyn Ip
# Created on: Sep 2022
# This program calculates the area and perimeter of a rectangle

import math


def main():
    # this function calculates the circumference of a circle

    # input
    radius_of_circle = int(input("Enter the radius of the circle(mm): "))
    # process
    circumference_of_circle = radius_of_circle * math.tau

    # output
    print("")
    print("Circumference is {0} mm.".format(circumference_of_circle))

    print("\nDone.")


if __name__ == "__main__":
    main()