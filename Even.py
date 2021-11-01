'''
Trevor Golusinski
Even or Odd
This program determines whether an inputted number is even or odd.
10/5/2020
'''
def main():
    number = float(input("Give me a number: "))
    if number % 2 == 0:
        print(int(number), "is even.")
    elif number % 2 == 1:
        print(int(number), "is odd.")
    else:
        print(number, "is very strange!")


main()
