#Trevor Golusinski
#5-Question Quiz
#This program will ask five questions and return the score.
#9/21/2020
def main():
    score = 0
    print("This is a five question quiz.")
    print("What city is Marist located in?")
    print(" a. Manhattan")
    print(" b. New York City")
    print(" c. Poughkeepsie")
    Q1 = input("Enter your response (a, b, or c) here: ")
    Q1 = Q1.lower()
    if Q1 == "c":
        print("Correct.")
        score = score + 1
    else:
        print("Incorrect.")
        
    print("What is Marist's mascot?")
    print(" a. A red fox")
    print(" b. A blue whale")
    print(" c. An eagle")
    Q2 = input("Enter your response (a, b, or c) here: ")
    Q2 = Q2.lower()
    if Q2 == "a":
        print("Correct.")
        score = score + 1
    else:
        print("Incorrect.")

    print("What is the name of Marist's mascot?")
    print(" a. Franklin the Turtle")
    print(" b. Betty the Whale")
    print(" c. Frankie the Fox")
    Q3 = input("Enter your response (a, b, or c) here: ")
    Q3 = Q3.lower()
    if Q3 == "c":
        print("Correct.")
        score = score + 1
    else:
        print("Incorrect.")

    print("What is the name of the river that Marist resides next to?")
    print(" a. The Henry Hudson Trail")
    print(" b. The Hudson River")
    print(" c. The Nile River")
    Q4 = input("Enter your response (a, b, or c) here: ")
    Q4 = Q4.lower()
    if Q4 == "b":
        print("Correct.")
        score = score + 1
    else:
        print("Incorrect.")

    print("True or False: Marist has a football team.")
    Q5 = input("Enter your response ('True' or 'False') here: ")
    Q5 = Q5.lower()
    if Q5 == "true":
        print("Correct.")
        score = score + 1
    else:
        print("Incorrect.")
        
    if score == 5:
        print("You finished with a score of ", score, ". Awesome! You rock!")
    elif 3<= score <= 4:
        print("You finished with a score of ", score, ". Not bad. Try again soon!")
    elif score <= 2:
        print("You finished with a score of ", score, ". Better luck next time.")
    input("Thank you for taking this quiz! Press <ENTER> to quit.")
    

main()
