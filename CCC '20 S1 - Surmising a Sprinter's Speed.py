observations = int(input())
info = []
for i in range(observations):
    ah = input()
    test = ah.split(" ")
    test[0] = int(test[0])
    test[1] = int(test[1])
    info.append(test)
info.sort()

max = 0
for i in range(observations-1):
    speed = abs(info[i+1][1] - info[i][1]) / (info[i+1][0] - info[i][0])
    if speed > max:
        max = speed
print(max)