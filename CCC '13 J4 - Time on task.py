time = int(input())
repeat = int(input())
things = []
sum = 0
max = 0

for i in range(repeat):
    chore = int(input())
    things.append(chore)

things.sort()

for i in range(len(things)):
    if sum > time:
        break
    else:
        sum += things[i]
        max += 1

print(max-1)