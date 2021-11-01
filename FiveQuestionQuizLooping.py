'''
Trevor Golusinski
5-Question Quiz With Looping
This program will ask five questions, using looping instead of scoring.
9/28/2020
'''

def main():
    again = 0
    play = 1
    print("This is a five question quiz.")
    while play == 1:
        correct = 0
        while correct == 0:
            print("What city is Marist located in?")
            print(" a. Manhattan")
            print(" b. New York City")
            print(" c. Poughkeepsie")
            Q1 = input("Enter your response (a, b, or c) here: ")
            Q1 = Q1.lower()
            if Q1 == "c":
                print("Correct!")
                correct = 1
            elif Q1 == "skip":
                correct = 1
                print("Skpped. The correct answer was: C")
            else:
                print("Incorrect. Please try again, or type 'skip' to skip.")

        correct = 0
        while correct == 0:
            print("What is Marist's mascot?")
            print(" a. A red fox")
            print(" b. A blue whale")
            print(" c. An eagle")
            Q2 = input("Enter your response (a, b, or c) here: ")
            Q2 = Q2.lower()
            if Q2 == "a":
                print("Correct!")
                correct = 1
            elif Q2 == "skip":
                correct = 1
                print("Skipped. The correct answer was: A")
            else:
                 print("Incorrect. Please try again, or type 'skip' to skip.")

        correct = 0
        while correct == 0:
            print("What is the name of Marist's mascot?")
            print(" a. Franklin the Turtle")
            print(" b. Betty the Whale")
            print(" c. Frankie the Fox")
            Q3 = input("Enter your response (a, b, or c) here: ")
            Q3 = Q3.lower()
            if Q3 == "c":
                print("Correct!")
                correct = 1
            elif Q3 == "skip":
                correct = 1
                print("Skipped. The correct answer was: C")
            else:
                print("Incorrect. Please try again, or type 'skip' to skip.")

        correct = 0
        while correct == 0:
            print("What is the name of the river that Marist resides next to?")
            print(" a. The Henry Hudson Trail")
            print(" b. The Hudson River")
            print(" c. The Nile River")
            Q4 = input("Enter your response (a, b, or c) here: ")
            Q4 = Q4.lower()
            if Q4 == "b":
                print("Correct!")
                correct = 1
            elif Q4 == "skip":
                correct = 1
                print("Skipped. The correct answer was: B")
            else:
                print("Incorrect. Please try again, or type 'skip' to skip.")

        correct = 0
        while correct == 0:
            print("True or False: Marist has a football team.")
            Q5 = input("Enter your response ('True' or 'False') here: ")
            Q5 = Q5.lower()
            if Q5 == "true":
                print("Correct!")
                correct = 1
            elif Q5 == "skip":
                correct = 1
                print("Skipped. The correct answer was: True")
            else:
                print("Incorrect. Please try again, or type 'skip' to skip.")

        print("Thank you for taking this quiz!")
        again = input("Do you want to play again? Type 'yes' to play again, or 'no' to stop playing: ")
        again = again.lower()
        if again == "yes":
            play = 1
            print("Thank you for choosing to play again!")
        elif again == "no":
            play = 0
            input("Thank you for playing! Press <ENTER> to quit.")
        else:
            play = 0
            input("Thank you for playing! Press <ENTER> to quit.")
    

main()
