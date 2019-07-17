
from random import randint

p1 = input("who is player 1: ")
p2 = input("who is player 2: ")

first = randint(1, 2)

if first == 1:
    print(f"first player is {p1}")
    first = p1
    print(first)

else:
    print(f"first player is {p2}")
