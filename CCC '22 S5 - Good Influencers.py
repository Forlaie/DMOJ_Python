numOfStudents = int(input())
adj = [[] for i in range(numOfStudents+1)]

for i in range(numOfStudents-1):
    friends = input()
    f1, f2 = friends.split()
    f1 = int(f1)
    f2 = int(f2)
    adj[f1].append(f2)
    adj[f2].append(f1)

CCC = input()
writing = [False]
for i in range(len(CCC)):
    if CCC[i] == "Y":
        writing.append(True)
    else:
        writing.append(False)

payment = input()
payment = payment.split()
payment = list(map(int, payment))
payment.insert(0, 0)

# Maintain a min Priority Queue (PQ) that sorts edges based on min edge cost
# This will be used to determine the next node to visit and the edge used to get there
# Start the algorithm on any node s
# Mark s as visited and iterate over all edges of s, adding them to the PQ
# While the PQ is not empty and a MST has not been formed, deque the next cheapest edge from the PQ
# If the dequeued edge is outdated (meaning the node it points to has already been visited) the skip it and poll again
# Otherwise, mark the current node as visited and add the selected edge to the MST
# Iterate over the new current node's edges and add al its edges to the PQ
# Do not add edges to the PQ which point to already visited nodes

PQ = []
cost = [1]
visited = [False for i in range(numOfStudents+1)]
visited[1] = True

for i in range(len(adj[1])):
    # cost, start node, destination
    if not visited[adj[1][i]]:
        info = [payment[1], 1, adj[1][i]]
        PQ.append(info)
PQ.sort()

while len(PQ) != 0:
    edge = PQ[0][2]
    cost.append(edge)
    PQ.pop(0)
    visited[edge] = True
    for i in range(len(adj[edge])):
        if not visited[adj[edge][i]]:
            info = [payment[edge], edge, adj[edge][i]]
            PQ.append(info)
    PQ.sort()
print(cost)