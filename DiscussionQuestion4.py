'''
Discussion Question 4
This program calculates several for loops and returns their values.
Trevor Golusinski
9/7/2020
'''

def main():
    print("Part A:")
    for i in range(1, 11):
        print(i*i)
    print("Part B:")
    for i in [1,3,5,7,9]:
        print(i, ":", i**3)
        print(i)
    print("Part C:")
    x=2
    y = 10
    for j in range(0, y, x):
        print(j, end="")
        print(x + y)
    print("done")
    print("Part D:")
    ans = 0
    for i in range(1, 11):
        ans = ans + i*i
        print(i)
    print (ans)

main()
