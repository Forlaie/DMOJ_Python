info = input()
houses, roads, s, d = info.split()
houses = int(houses)
roads = int(roads)
s = int(s)
d = int(d)
adj = [[] for i in range(houses)]

for i in range(roads):
    road = input()
    x, y = road.split()
    x = int(x)
    y = int(y)
    adj[x-1].append(y)
    adj[y-1].append(x)

distance = [float('inf')]*houses
distance[s-1] = 0

queue = []
queue.append(s)

while len(queue) != 0:
    current = queue[0]
    queue.pop(0)
    for i in range(len(adj[current-1])):
        if distance[current-1]+1 < distance[adj[current-1][i]-1]:
            distance[adj[current-1][i]-1] = distance[current-1]+1
            queue.append(adj[current - 1][i])

if distance[d-1] != float('inf'):
    print("GO SHAHIR!")
else:
    print("NO SHAHIR!")