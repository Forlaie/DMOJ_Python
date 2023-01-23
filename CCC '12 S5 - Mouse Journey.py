brother = input()
row, column = brother.split(" ")
rows = int(row)
columns = int(column)
numOfCats = int(input())
cats = []
location = [[0 for i in range(columns)] for j in range(rows)]
location[0][0] = 1

for i in range(numOfCats):
    cat = input()
    cat = cat.split()
    cat = [int(x) for x in cat]
    cats.append(cat)

for i in range(len(cats)):
    location[cats[i][0]-1][cats[i][1]-1] = -1

for r in range(rows):
    for c in range(columns):
        if location[r][c] != -1:
            if c < columns-1 and location[r][c+1] != -1:
                location[r][c+1] += location[r][c]
            if r < rows-1 and location[r+1][c] != -1:
                location[r+1][c] += location[r][c]
print(location[rows-1][columns-1])