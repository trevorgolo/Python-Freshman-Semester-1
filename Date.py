'''
Date Assignment
This program displays the written date, given the numerical values of the date.
Trevor Golusinski
9/20/2020
Modified on 9/28/2020
'''

def main():
    date_input = input("Please enter the date (in the format mm/dd/yyyy): ")
    dateArray = date_input.split("/")
    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    monthint = int(dateArray[0])
    monthint = monthint - 1
    month = months[monthint]
    day = dateArray[1]
    year = dateArray[2]
    print("The date selected is: " + month + " " + day + ", " + year)
    input("The program has ended. Please press <ENTER> to quit.")

main()
