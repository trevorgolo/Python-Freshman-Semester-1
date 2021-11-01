#Trevor Golusinski
#Payroll Algorithm
#This program will calculate the total wages for the week given the hours worked and pay rate.
#9/21/2020
def main():
    print("Welcome! This program will calculate the total wages for the week given the hours worked and pay rate.")
    hours = eval(input("Please enter the number of hours you worked: "))
    rate = eval(input("Please enter the hourly pay rate: "))
    if hours <= 40:
        total_pay = hours * rate
    elif hours > 40:
        total_pay = rate * 40
        overtime_hours = hours - 40
        overtime_pay = hours * (rate * 1.5)
        total_pay = total_pay + overtime_pay
    print("Your total pay for the week is: $",round(total_pay,2))
    input("Thank you for using this program! Press <ENTER> to exit.")

main()
