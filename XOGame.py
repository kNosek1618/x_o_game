
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
    while round % 2 != 0:
        if field_game[0:3] == ["o", "o", "o"]:
            print("player2 win")
            round = 20
            break
        elif field_game[3:6] == ["o", "o", "o"]:
            print("player2 win")
            round = 20
            break
        elif field_game[6:9] == ["o", "o", "o"]:
            print("player2 win")
            round = 20
            break
        elif field_game[0] == "o" and field_game[3] == "o" and field_game[6] == "o":
            print("player2 win")
            round = 20
            break
        elif field_game[1] == "o" and field_game[4] == "o" and field_game[7] == "o":
            print("player2 win")
            round = 20
            break
        elif field_game[2] == "o" and field_game[5] == "o" and field_game[8] == "o":
            print("player2 win")
            round = 20
            break
        elif field_game[0] == "o" and field_game[4] == "o" and field_game[8] == "o":
            print("player2 win")
            round = 20
            break
        elif field_game[2] == "o" and field_game[4] == "o" and field_game[6] == "o":
            print("player2 win")
            round = 20
            break
        else:
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
            if field_game[0:3] == ["x", "x", "x"]:
                print("player1 win")
                round = 20
                break
            elif field_game[3:6] == ["x", "x", "x"]:
                print("player1 win")
                round = 20
                break
            elif field_game[6:9] == ["x", "x", "x"]:
                print("player1 win")
                round = 20
                break
            elif field_game[0] == "x" and field_game[3] == "x" and field_game[6] == "x":
                print("player1 win")
                round = 20
                break
            elif field_game[1] == "x" and field_game[4] == "x" and field_game[7] == "x":
                print("player1 win")
                round = 20
                break
            elif field_game[2] == "x" and field_game[5] == "x" and field_game[8] == "x":
                print("player1 win")
                round = 20
                break
            elif field_game[0] == "x" and field_game[4] == "x" and field_game[8] == "x":
                print("player1 win")
                round = 20
                break
            elif field_game[2] == "x" and field_game[4] == "x" and field_game[6] == "x":
                print("player1 win")
                round = 20
                break
            else:
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
    print("it's tie")






