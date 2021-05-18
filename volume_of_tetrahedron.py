#!/usr/bin/env python3

# Created by: Artur Grigoryev
# Created on: May 2021
# Python program to calculate volume of a tetrahedron
# create a function that calculates the volume


import math


def main():
    # Function that calculates the volume of the tetrahedron
    # User input
    edge = int(input("Enter the value (mm): "))
    # Process
    volume = (edge ** 3) / (6 * math.sqrt(2))
    # Output
    print("This is the volume: {} mm³".format(volume))


if __name__ == "__main__":
    main()
