times = int(input())
power = []
strongest = True

for i in range(times):
    level = int(input())
    power.append(level)

for i in range(1, times):
    if power[0] <= power[i]:
        strongest = False
        break

if strongest:
    print("YES")
else:
    print("NO")