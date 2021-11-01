'''
Ladder Problem
This program calculates the height of a ladder, given the height of a building and the angle it makes with the building.
Trevor Golusinski
9/7/2020
'''

import math

def main():
    height = float(input("Please enter the height of the building in feet: "))
    angle = float(input("Please enter the angle, in degrees, that the ladder makes with the building: "))
    radians = (math.pi / 180) * angle
    ladder = height / math.cos(radians)
    print("Height of the ladder, in feet:")
    print(round(ladder, 2))

          
main()
