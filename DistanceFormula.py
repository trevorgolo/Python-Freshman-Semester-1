'''
Distance Formula
This program calculates the length of a hypotenuse, given two sets of ordered pairs.
Trevor Golusinski
9/7/2020
'''

import math

def main():
    x1, y1 = eval(input("Please enter the first x and y pair, separating each value by a comma: "))
    x2, y2 = eval(input("Please enter the second x and y pair, separating each value by a comma: "))
    leg1 = x2 - x1
    leg2 = y2 - y1
    leg3 = (leg1 ** 2) + (leg2 ** 2)
    hypotenuse = math.sqrt(leg3)
    print("The length of the hypotenuse is:")
    print(round(hypotenuse))
    print(round(hypotenuse, 1))
    print(math.ceil(hypotenuse))
    

main()
