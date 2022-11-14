# https://www.w3schools.com/python/
# https://docs.python.org/3/
# https://stackabuse.com/guide-to-pythons-keyboard-module/

import keyboard

print("hello world")
print()
keyboard.wait("esc")  # wait for escape key to be pressed

name = "mark"  # string
print("Hello, my name is", name)
print()
keyboard.wait("esc")

age = 12  # integer
print("Hello, my name is", name, "and I am", age)
print()
keyboard.wait("esc")

print(f"Hello, my name is {name} and I am {age}.")
print()
keyboard.wait("esc")

averageGrade = 91.34  # float
print(f"Mt average greade is {averageGrade}.")
print()
keyboard.wait("esc")


colors = ["red", "green", "blue", "yellow"]  # list
print(colors)
print()
keyboard.wait("esc")

for clr in colors:
    print(clr)
print()
keyboard.wait("esc")

mixed = [12, "john", 45, "joe"]
for d in mixed:
    print(d)
print()
keyboard.wait("esc")

print(mixed[2])
print()
keyboard.wait("esc")

mixed.append(50)
for d in mixed:
    print(d)
print()
keyboard.wait("esc")

mixed[0] = 21
print(mixed)
print()
keyboard.wait("esc")


clrs = ("red", "green", "blue", 34, "yellow")  # tuple
for clr in clrs:
    print(clr)
print()
print(clrs[2])
print()
keyboard.wait("esc")

"""
List has mutable nature i.e., list can be changed 
or modified after its creation according to needs 
whereas tuple has immutable nature i.e., tuple 
can't be changed or modified after its creation.
"""

# clrs[0] = 99
# print(clrs)
# print()


for n in range(5):
    print(n)
print()
keyboard.wait("esc")


def add(a, b, c):
    sum = a + b + c
    return sum


mySum = add(4, 6, 5)
print(mySum)
print()
keyboard.wait("esc")


x = 6
y = 6
if x == y:
    print("x equals y")
if x > y:
    print("x is greater than y")
if x < y:
    print("x is less than y")
