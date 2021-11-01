'''
Strings and Lists Chapter 5 Lab
This program calculates answers discussion questions 1-3 in Chapter 5
Trevor Golusinski
9/17/2020
'''

print("Question 1:")
s1 = "spam"
s2 = "ni!"
print("The knights who say, " + s2)
print(3 * s1 + 2 * s2)
print(s1[1])
print(s1[1:3])
print(s1[2] + s2[:2])
print(s1 + s2[-1])
print(s1.upper())
print(s2.upper().ljust(4) * 3)

print("Question 2:")
print(s2[0:2].upper())
print(s2 + s1 + s2)
print((s1.capitalize() + " " + s2.capitalize() + " ") * 2 + s1.capitalize() + " " + s2.capitalize())
print(s1)
list1 = [s1[:2], s1[-1]]
print(list1)
print(s1[0:2] + s1[3])

print("Question 3:")
for ch in "aardvark":
    print(ch)
for w in "Now is the winter of our discontent...".split():
    print(w)
for w in "Mississippi".split("i"):
    print(w, end = " ")
msg = ""
for s in "secret".split("e"):
    msg = msg + s
print(msg)
msg = ""
for ch in "secret":
    msg = msg + chr(ord(ch) + 1)
print(msg)
