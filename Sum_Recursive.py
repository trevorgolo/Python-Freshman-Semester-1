'''
Trevor Golusinski
Sum Recusive example
This program adds the numbers inluding and in between the starting number and the ending number.
11/2/2020
'''
print("Individual threading:")
def sum_recursive(current_number, accumulated_sum):
    # Base case
    # Return the final state
    if current_number == 11:
        return accumulated_sum

    # Recursive case
    # Thread the state through the recursive call
    else:
        return sum_recursive(current_number + 1, accumulated_sum + current_number)
        #loop

print(sum_recursive(1, 0))



# Global mutable state
current_number = 1
accumulated_sum = 0

print("Global:")
def sum_recursive():
   
    global current_number
    global accumulated_sum
    # Base case
    if current_number == 11:
        return accumulated_sum
    # Recursive case
    else:
        accumulated_sum = accumulated_sum + current_number
        current_number = current_number + 1
        return sum_recursive()
        #loop

print(sum_recursive())
