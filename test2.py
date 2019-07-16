
x = 1
y = 2
round = 1


while round < 10:
    if x == 1 or y == 0:
        if x == 2 or y == 2:
            while round % 2 == 0:
                round += 1
                print("player1")
            while round % 2 != 0:
                round += 1
                print("player2")
        else:
            print("player2 win")
            break
    else:
        print("player1 win")
        break
else:
    print("it's tie")