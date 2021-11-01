'''
Trevor Golusinski
Factorial Example
This program creates and executes the factorial (n!) mathematical formula.
11/2/2020
'''

def factorial_recursive(n):
    # Base case: 1! = 1
    if n == 1:
        return 1
        #End of factorial equation

    
    # Recursive case: n! = n * (n-1)!
    else:
        return n * factorial_recursive(n-1)
        #loop

print(factorial_recursive(5))
