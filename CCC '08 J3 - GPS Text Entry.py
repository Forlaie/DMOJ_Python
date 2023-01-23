row1 = ['A', 'B', 'C', 'D', 'E', 'F']
row2 = ['G', 'H', 'I', 'J', 'K', 'L']
row3 = ['M', 'N', 'O', 'P', 'Q', 'R']
row4 = ['S', 'T', 'U', 'V', 'W', 'X']
row5 = ['Y', 'Z', ' ', '-', '.', 'enter']
count = 0
previoush = 1
previousv = 1
horizontal = 1
vertical = 1
word = input()

for i in range(len(word)):
    if word[i] in row1:
        horizontal = row1.index(word[i])+1
        vertical = 1
    elif word[i] in row2:
        horizontal = row2.index(word[i])+1
        vertical = 2
    elif word[i] in row3:
        horizontal = row3.index(word[i])+1
        vertical = 3
    elif word[i] in row4:
        horizontal = row4.index(word[i])+1
        vertical = 4
    elif word[i] in row5:
        horizontal = row5.index(word[i])+1
        vertical = 5

    if horizontal > previoush:
        count += horizontal - previoush
    else:
        count += previoush - horizontal

    if vertical > previousv:
        count += vertical - previousv
    else:
        count += previousv - vertical

    previoush = horizontal
    previousv = vertical

if 6 > previoush:
    count += 6 - previoush
else:
    count += previoush - 6

if 5 > previousv:
    count += 5 - previousv
else:
    count += previousv - 5

print(count)