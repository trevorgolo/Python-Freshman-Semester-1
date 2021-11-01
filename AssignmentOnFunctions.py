'''
Trevor Golusinski
Functions Assignment
This program uses functions to ask a 5-question quiz.
10/5/2020
'''
def askQuestion(questionText, questionAnswer):
    userAnswer = input(questionText)
    if userAnswer.lower() == questionAnswer:
        return True
    else:
        return False

def printFinalScore(score):
    if score == 5:
        print("You finished with a score of ", score, ". Awesome! You rock!")
    elif 3<= score <= 4:
        print("You finished with a score of ", score, ". Not bad. Try again soon!")
    elif score <= 2:
        print("You finished with a score of ", score, ". Better luck next time.")

def main():
    userScore = 0
    print("Welcome to my five question quiz!")
    questionList = ["What city is Marist located in? ",
                    "What is Marist's mascot? ",
                    "What is the name of Marist's mascot? ",
                    "What is the name of the river that Marist resides next to? ",
                    "True or False: Marist has a football team? "]
    answerList = ["poughkeepsie",
                  "a red fox",
                  "frankie the fox",
                  "the hudson river",
                  "true"]
    for i in range (5):
        if askQuestion(questionList[i], answerList[i]) == True:
            print("Correct!")
            userScore = userScore + 1
        else:
            print("Incorrect.")
    printFinalScore(userScore)
    input("Thank you for taking this quiz! Press <ENTER> to quit.")
    
main()
