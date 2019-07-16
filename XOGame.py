
from random import choice

field_game = [1, 2, 3,
              4, 5, 6,
              7, 8, 9]

num = None


print(field_game[0], field_game[1], field_game[2])
print(field_game[3], field_game[4], field_game[5])
print(field_game[6], field_game[7], field_game[8])
print("\n")


x = 1
y = 2
round = 1


while round < 10:
    if x == 1 or y == 0:
        if x == 2 or y == 2:
            while round % 2 != 0:
                print(field_game[0], field_game[1], field_game[2])
                print(field_game[3], field_game[4], field_game[5])
                print(field_game[6], field_game[7], field_game[8])
                round += 1
                num = input("player1 ")
                num = int(num)
                if num == 1:
                    field_game[0] = "x"
                if num == 2:
                    field_game[1] = "x"
                if num == 3:
                    field_game[2] = "x"
                if num == 4:
                    field_game[3] = "x"
                if num == 5:
                    field_game[4] = "x"
                if num == 6:
                    field_game[5] = "x"
                if num == 7:
                    field_game[6] = "x"
                if num == 8:
                    field_game[7] = "x"
                if num == 9:
                    field_game[8] = "x"
            while round % 2 == 0:
                if round < 10:
                    print(field_game[0], field_game[1], field_game[2])
                    print(field_game[3], field_game[4], field_game[5])
                    print(field_game[6], field_game[7], field_game[8])
                    round += 1
                    num = input("player2 ")
                    num = int(num)
                    if num == 1:
                        field_game[0] = "o"
                    if num == 2:
                        field_game[1] = "o"
                    if num == 3:
                        field_game[2] = "o"
                    if num == 4:
                        field_game[3] = "o"
                    if num == 5:
                        field_game[4] = "o"
                    if num == 6:
                        field_game[5] = "o"
                    if num == 7:
                        field_game[6] = "o"
                    if num == 8:
                        field_game[7] = "o"
                    if num == 9:
                        field_game[8] = "o"
                else:
                    break
        else:
            print("player2 win")
            break
    else:
        print("player1 win")
        break
else:
    print("it's tie")






