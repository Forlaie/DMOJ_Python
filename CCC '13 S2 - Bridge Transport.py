maxweight = int(input())
times = int(input())
weight = []
count = 0
bridge = 0

for i in range(times):
    car = int(input())
    weight.append(car)

for i in range(len(weight)):
    if i < 4:
        bridge += weight[i]
    else:
        bridge += weight[i]
        bridge -= weight[i-4]
    if bridge <= maxweight:
        count += 1
    else:
        break
print(count)