position = 1
while position < 100 or position == 0:
    dice = int(input())
    if dice == 0:
        position = 0
        break

    if position + dice <= 100:
        position += dice

    if position == 54:
        position = 19
    elif position == 90:
        position = 48
    elif position == 99:
        position = 77
    elif position == 9:
        position = 34
    elif position == 40:
        position = 64
    elif position == 67:
        position = 86
    print("You are now on square", position)

if position == 100:
    print("You Win!")
elif position == 0:
    print("You Quit!")