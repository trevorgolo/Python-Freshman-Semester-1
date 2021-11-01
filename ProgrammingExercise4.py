'''
Programming Exercise 4 Chapter 5
This program executes the programming exercise 4 in Chapter 5.
Trevor Golusinski
9/17/2020
'''

def main():
    user_input = str(input("Please enter a non-abbreviated term (eg. random access memory): "))
    list1 = user_input.split()
    msg = ""
    holder = ""
    x = 0
    for words in list1:
        msg = msg + words[0:1]
    msg = (msg.upper())
    print("The acronym is: " + msg)


main()
