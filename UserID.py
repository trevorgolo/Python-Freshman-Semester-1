'''
User ID Assignment
This program creates a user's ID, given their first and last name
Trevor Golusinski
9/20/2020
Modified on 9/28/2020
'''

def main():
    first_name = input("Please enter your first name: ")
    last_name = input("Please enter your last name: ")
    first = first_name[0:1]
    last = last_name[0:7]
    userid = first + last
    userid = userid.lower()
    print(userid)
    input("The program has ended. Please press <ENTER> to quit.")

main()
