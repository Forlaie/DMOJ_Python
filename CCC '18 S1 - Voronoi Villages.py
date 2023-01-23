times = int(input())
villages = []

for i in range(times):
    house = int(input())
    villages.append(house)

villages.sort()

neighbourhood = []
for i in range(1,len(villages)-1):
    size = 0
    size = (villages[i] - villages[i-1])/2 + (villages[i+1]-villages[i])/2
    neighbourhood.append(size)

neighbourhood.sort()
smallest = neighbourhood[0]
smallest = round(smallest,1)

print(smallest)