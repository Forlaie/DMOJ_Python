num = int(input())
coords = []
for i in range(num):
    temp = input()
    coords.append(temp.split(","))
coords = [list(map(int,i)) for i in coords]

minx = coords[0][0]
miny = coords[0][1]
maxx = coords[0][0]
maxy = coords[0][1]

for x in range(len(coords)):
    if coords[x][0] < minx:
        minx = coords[x][0]
    if coords[x][0] > maxx:
        maxx = coords[x][0]
    if coords[x][1] < miny:
        miny = coords[x][1]
    if coords[x][1] > maxy:
        maxy = coords[x][1]

minx -= 1
miny -= 1
maxx += 1
maxy += 1

print(f"{minx},{miny}")
print(f"{maxx},{maxy}")