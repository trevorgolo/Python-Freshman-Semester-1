'''
Chapter 8 While Loops Lab
This program is the code for the Chapter 8 While Loops lab
Trevor Golusinski
9/28/2020
'''

def main():
    #Page 1:
    number = float(input("Please enter a number: "))
    another_number = float(input("Please enter another number: "))
    #Pages 1 & 2:
    while number < 5:
        print("Thank you")
        if number%2 == 0:
            print("The number " + str(number) + "is even.")
        else:
            print("The number " + str(number) + "is odd.")
        number = number + 1
        break
        continue
        #Page 3:
        for number in range(3):
            print("Thank you")
            print("-------------------------------------")
            print("I am outer loop iteration " + str(number))
            for another_number in range(5):
                print("*************************************")
                print("I am inner loop iteration " + str(another_number))
        #Page 4:
        n = 5
        #first five rows:
        for i in range(n):
            for j in range(i):
                print("* ", end="")
            print('')
        #Remaining rows:
        for i in range(n,0,-1):
            for j in range(i):
                print("* ", end="")
            print('')

            
main()
