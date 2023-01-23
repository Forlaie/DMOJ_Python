limit = input()
limit = limit.split()
limit = list(map(int, limit))
current = [0, 0]

while True:
    move = input()
    if move == "0 0":
        break
    else:
        move = move.split()
        move = list(map(int, move))
        if current[0] + move[0] < 0:
            current[0] = 0
        elif current[0] + move[0] > limit[0]:
            current[0] = limit[0]
        else:
            current[0] += move[0]

        if current[1] + move[1] < 0:
            current[1] = 0
        elif current[1] + move[1] > limit[1]:
            current[1] = limit[1]
        else:
            current[1] += move[1]
    print(f"{current[0]} {current[1]}")