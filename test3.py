
field_game = ["x", "x", "x",
              4, 5, 6,
              7, 8, 9]


rows1 = ''
for e in str(field_game):
    rows1 += e
    print(rows1)

if field_game[0:3] == ["x", "x", "x"]:
    print("brawo")