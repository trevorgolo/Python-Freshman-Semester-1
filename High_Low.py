'''
Trevor Golusinski
Higher or Lower
This program is an easier, non-random version of higher or lower.
10/5/2020
'''
def main():
    number = 7
    guess = -1
    print("Guess the number!")
    while guess != number:
        guess = int(input("Is it... "))
        if guess == number:
            print("Great job! You guessed it right!")
        elif guess < number:
            print("Bigger than that!")
        elif guess > number:
            print("Not that big!")
    

main()
