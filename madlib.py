'''
Mad Libs!
This program will tell a story using words inputted by the user.
Trevor Golusinski
8/31/2020
'''
import keyboard


print("This program will tell a story using words that you enter!")


def madlibs():
    place = input("Please enter a place: ")
    thing = input("Please enter an object: ")
    verb = input("Please enter a present-tense verb: ")
    adjective = input("Please enter an adjective: ")
    print("If you ever find yourself walking through " + place + ", be sure to visit and use the " + thing +
          "! There is so much to do there, such as " + verb + " and more! You will have such a(n) " +
          adjective + " time!")
    print("Thank you for playing! Would you like to play again?")
    response = input("Type yes to play again, or press the enter key to exit the program: ")
    if response == "yes":
        print("Thank you for choosing to play again!")
        madlibs()
    elif keyboard.is_pressed("Enter"):
        print("Thank you for playing!")
        exit()
    else:
        print("Let's play again!")


madlibs()
