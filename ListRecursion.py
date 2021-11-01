'''
Trevor Golusinski
List Recursion Example
This program creates a list and allows items to be added to it. The next function takes the sum of the items in the list.
11/2/2020
'''

print("attach_head():")
# Return a new list that is the result of
# adding element to the head (i.e. front) of input_list
def attach_head(element, list1):
    return [element] + list1
    print(list1)
   
attach_head(1,                                                  # Will return [1, 46, -31, "hello"]
            attach_head(46,                                     # Will return [46, -31, "hello"]
                        attach_head(-31,                        # Will return [-31, "hello"]
                                    attach_head("hello", [])))) # Will return ["hello"]
#together, returns [1, 46, -31, 'hello']

print("list_sum_recursive():")
def list_sum_recursive(input_list):
    # Base case
    if input_list == []:
        return 0
        #End

    # Recursive case
    # Decompose the original problem into simpler instances of the same problem
    # by making use of the fact that the input is a recursive data structure
    # and can be deﬁned in terms of a smaller version of itself
    else:
        head = input_list[0]
        smaller_list = input_list[1:]
        return head + list_sum_recursive(smaller_list)
        #loop

print(list_sum_recursive([1, 2, 3]))
