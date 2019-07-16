
from random import choice

field_game = [1, 2, 3,
              4, 5, 6,
              7, 8, 9]

num = None


print(field_game[0], field_game[1], field_game[2])
print(field_game[3], field_game[4], field_game[5])
print(field_game[6], field_game[7], field_game[8])

num = input()
num = int(num)
if num == 1:
    field_game[0] = "x"

print(field_game[0], field_game[1], field_game[2])
print(field_game[3], field_game[4], field_game[5])
print(field_game[6], field_game[7], field_game[8])




