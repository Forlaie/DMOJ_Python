numOfRows = int(input())
numOfColumns = int(input())
rowsCount = [0 for i in range(numOfRows)]
columnsCount = [0 for i in range(numOfColumns)]
choices = int(input())
count = 0

for i in range(choices):
    action = input()
    place, location = action.split(" ")
    location = int(location)-1
    if place == "R":
        rowsCount[location] += 1
    else:
        columnsCount[location] += 1

for i in range(numOfRows):
    for j in range(numOfColumns):
        if (rowsCount[i] + columnsCount[j]) % 2 != 0:
            count += 1
print(count)