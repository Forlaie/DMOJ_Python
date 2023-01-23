instructions = input()
direction = ""
while instructions != "99999":
    if (int(instructions[0]) + int(instructions[1])) != 0 and (int(instructions[0]) + int(instructions[1])) % 2 == 0:
        direction = "right"
    elif (int(instructions[0]) + int(instructions[1])) % 2 != 0:
        direction = "left"
    print(direction, instructions[2:])
    instructions = input()