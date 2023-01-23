actions = input()
position = [1, 0, 0]
for i in range(len(actions)):
    if actions[i] == "A":
        og = position[0]
        position[0] = position[1]
        position[1] = og
    elif actions[i] == "B":
        og = position[1]
        position[1] = position[2]
        position[2] = og
    else:
        og = position[2]
        position[2] = position[0]
        position[0] = og

if position[0] == 1:
    print(1)
elif position[1] == 1:
    print(2)
else:
    print(3)