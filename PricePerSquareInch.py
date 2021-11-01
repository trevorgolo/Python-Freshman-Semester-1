'''
Discussion Question 4
This program calculates the price per square inch of a pizza, given the diameter of the pizza and the price of the entire pizza.
Trevor Golusinski
9/7/2020
'''

import math


def main():
    diameter = float(input("Please enter the diameter of the pizza in inches: "))
    price = float(input("Please enter the price of the pizza: "))
    radius = diameter / 2
    area = math.pi * radius ** 2
    ppsi = price / area
    print("Price per square inch:")
    print(round(ppsi, 2))


main()
