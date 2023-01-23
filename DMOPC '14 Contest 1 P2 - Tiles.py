size = input()
width, length = size.split()
width = int(width)
length = int(length)
tile = int(input())

h = int(width/tile)
v = int(length/tile)
n = h*v
print(n)