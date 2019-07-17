
from random import randint

field_game = [1, 2, 3,
              4, 5, 6,
              7, 8, 9]

num = None
round = 1

# module for choose who is first player

p1 = input("who is player 1: ")
p2 = input("who is player 2: ")

first = randint(1, 2)

if first == 1:
    print(f"\nfirst player is {p1}")
    first = p1
    second = p2
else:
    print(f"\nfirst player is {p2}")
    first = p2
    second = p1

# X O game module

while round < 10:
    while round % 2 != 0:
        if field_game[0:3] == ["o", "o", "o"]:
            print(f"\n{second} WIN!\n")
            round = 20
            break
        elif field_game[3:6] == ["o", "o", "o"]:
            print(f"\n{second} WIN!\n")
            round = 20
            break
        elif field_game[6:9] == ["o", "o", "o"]:
            print(f"\n{second} WIN!\n")
            round = 20
            break
        elif field_game[0] == "o" and field_game[3] == "o" and field_game[6] == "o":
            print(f"\n{second} WIN!\n")
            round = 20
            break
        elif field_game[1] == "o" and field_game[4] == "o" and field_game[7] == "o":
            print(f"\n{second} WIN!\n")
            round = 20
            break
        elif field_game[2] == "o" and field_game[5] == "o" and field_game[8] == "o":
            print(f"\n{second} WIN!\n")
            round = 20
            break
        elif field_game[0] == "o" and field_game[4] == "o" and field_game[8] == "o":
            print(f"\n{second} WIN!\n")
            round = 20
            break
        elif field_game[2] == "o" and field_game[4] == "o" and field_game[6] == "o":
            print(f"\n{second} WIN!\n")
            round = 20
            break
        else:
            print("\n")
            print(field_game[0], field_game[1], field_game[2])
            print(field_game[3], field_game[4], field_game[5])
            print(field_game[6], field_game[7], field_game[8])
            print("\n")
            round += 1
            num = input(f"{first} time (x) ")
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
                print(f"\n{first} WIN!\n")
                round = 20
                break
            elif field_game[3:6] == ["x", "x", "x"]:
                print(f"\n{first} WIN!\n")
                round = 20
                break
            elif field_game[6:9] == ["x", "x", "x"]:
                print(f"\n{first} WIN!\n")
                round = 20
                break
            elif field_game[0] == "x" and field_game[3] == "x" and field_game[6] == "x":
                print(f"\n{first} WIN!\n")
                round = 20
                break
            elif field_game[1] == "x" and field_game[4] == "x" and field_game[7] == "x":
                print(f"\n{first} WIN!\n")
                round = 20
                break
            elif field_game[2] == "x" and field_game[5] == "x" and field_game[8] == "x":
                print(f"\n{first} WIN!\n")
                round = 20
                break
            elif field_game[0] == "x" and field_game[4] == "x" and field_game[8] == "x":
                print(f"\n{first} WIN!\n")
                round = 20
                break
            elif field_game[2] == "x" and field_game[4] == "x" and field_game[6] == "x":
                print(f"\n{first} WIN!\n")
                round = 20
                break
            else:
                print("\n")
                print(field_game[0], field_game[1], field_game[2])
                print(field_game[3], field_game[4], field_game[5])
                print(field_game[6], field_game[7], field_game[8])
                print("\n")
                round += 1
                num = input(f"{second} time (o) ")
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
    if round == 20:
        print("Thanks, for playing!")
    else:
        print("it's tie")

print(field_game[0], field_game[1], field_game[2])
print(field_game[3], field_game[4], field_game[5])
print(field_game[6], field_game[7], field_game[8])





