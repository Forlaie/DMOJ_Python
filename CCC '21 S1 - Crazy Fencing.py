num = int(input())
sides = input()
sides = sides.split()
sides = list(map(int, sides))
width = input()
width = width.split()
width = list(map(int, width))
area = 0
for i in range(len(width)):
    area += width[i] * (sides[i] + sides[i+1]) / 2
print(area)