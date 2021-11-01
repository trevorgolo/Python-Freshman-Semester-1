'''
Trevor Golusinski
Average 1
This program prints the average of a given set of values.
10/5/2020
'''
def main():
    count = 0
    sum = 0.0
    number = 1
    print("Enter 0 to exit the loop.")
    while number != 0:
        number = float(input("Enter a number: "))
        if number != 0:
            count = count + 1
            sum = sum + number
        if number == 0:
            print("The average is: ", sum / count)
    input("Press <ENTER> to exit.")

main()
