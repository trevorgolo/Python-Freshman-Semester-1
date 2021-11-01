'''
Trevor Golusinski
Lab 4 Exercises
This program is the answer to Lab 4
10/5/2020
'''
def main():
    n = int(input("Number: "))
    if n < 0:
        print("The absolute value of ", n, "is ", -n)
    else:
        print("The absolute value of ", n, "is ", n)

    a = 0
    while a < 10:
        a = a + 1
        if a > 5:
            print(a, ">", 5)
        elif a <= 3:
            print(a, "<=", 3)
        else:
            print("Neither test was true.")

    print(5 == 6)
    x = 5
    y = 8
    print(x == y)


main()
