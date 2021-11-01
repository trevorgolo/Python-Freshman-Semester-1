'''
Trevor Golusinski
Delivering Presents Example
This program uses iteration and recursion to distribute Santa's work among his elves.
11/2/2020
'''

houses = ["Eric's house", "Kenny's house", "Kyle's house", "Stan's house"]

print("Santa's Work:")
#This function represents Santa's job
def deliver_presents_iteratively():
    for house in houses:
        print("Delivering presents to", house)

deliver_presents_iteratively()

print("Elves Work:")      
# Each function call represents an elf doing his work 
def deliver_presents_recursively(houses):
    # Worker elf
    if len(houses) == 1:
        house = houses[0]
        print("Delivering presents to", house)

    # Manager elf
    else:
        mid = len(houses) // 2
        first_half = houses[:mid]
        second_half = houses[mid:]

        # Divides the work among two elves
        deliver_presents_recursively(first_half)
        deliver_presents_recursively(second_half)

deliver_presents_recursively(houses)
