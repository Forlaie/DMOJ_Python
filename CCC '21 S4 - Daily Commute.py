s, w, d = list(map(int, input().split()))
walkways = [[] for i in range(s+1)]
for i in range(w):
    a, b = list(map(int, input().split()))
    walkways[b].append(a)
train = [0]
train += list(map(int, input().split()))

walkingTime = [float('inf') for i in range(len(train))]
walkingTime[-1] = 0
combinedTime = [float('inf') for i in range(len(train))]
queue = [s]
visited = [False for i in range(len(train))]
visited[-1] = True
while len(queue) != 0:
    station = queue[0]
    queue.pop(0)
    for j in range(len(walkways[station])):
        if not visited[walkways[station][j]] and walkways[station][j] not in queue:
            queue.append(walkways[station][j])
            visited[walkways[station][j]] = True
            walkingTime[walkways[station][j]] = walkingTime[station] + 1

for i in range(1, len(train)):
    if (walkingTime[train[i]] + i-1) < minTime:
        minTime = walkingTime[train[i]] + i-1
    combinedTime[train[i]] = walkingTime[train[i]] + i-1

for i in range(d):
    x, y = list(map(int, input().split()))
    temp = train[x]
    train[x] = train[y]
    train[y] = temp

    combinedTime[train[x]] = walkingTime[train[x]] + x-1
    combinedTime[train[y]] = walkingTime[train[y]] + y-1

    print(min(combinedTime))