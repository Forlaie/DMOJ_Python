flooringAvailable = int(input())
rows = int(input())
columns = int(input())

floorplan = []
visited = [[False for i in range(columns)] for j in range(rows)]

for i in range(rows):
    column = input()
    column = list(column)
    floorplan.append(column)

def dfs(count, i, j):
    visited[i][j] = True
    count.append(1)

    if i > 0:
        if floorplan[i-1][j] == "." and not visited[i-1][j]:
            dfs(count, i-1, j)
    if i < rows-1:
        if floorplan[i+1][j] == "." and not visited[i+1][j]:
            dfs(count, i+1, j)
    if j > 0:
        if floorplan[i][j-1] == "." and not visited[i][j-1]:
            dfs(count, i, j-1)
    if j < columns-1:
        if floorplan[i][j+1] == "." and not visited[i][j+1]:
            dfs(count, i, j+1)
    return len(count)

cc = []
for i in range(rows):
    for j in range(columns):
        if not visited[i][j] and floorplan[i][j] == ".":
            count = []
            cc.append(dfs(count, i, j))

cc.sort(reverse=True)

rooms = 0

for i in range(len(cc)):
    if flooringAvailable - cc[i] >= 0:
        rooms += 1
        flooringAvailable -= cc[i]
    else:
        break

if rooms == 1:
    print(f"1 room, {flooringAvailable} square metre(s) left over")
else:
    print(f"{rooms} rooms, {flooringAvailable} square metre(s) left over")