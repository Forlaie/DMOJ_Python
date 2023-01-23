times = int(input())
x = 0
y = 0

for i in range(times):
    direction = input()
    number = int(input())
    if direction == "North":
        y += number
    elif direction == "South":
        y -= number
    elif direction == "East":
        x += number
    else:
        x -= number

print(x, y)