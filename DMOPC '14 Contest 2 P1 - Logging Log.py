days = int(input())

for i in range(days):
    ntrees = int(input())
    mass = 0
    for j in range(ntrees):
        mtree = int(input())
        mass += mtree
    if mass == 0:
        print("Weekend")
    else:
        print("Day", str(i+1) + ":", mass)