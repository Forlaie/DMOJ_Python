numOfPages = int(input())
adjlist = [[0]]
for i in range(numOfPages):
    pageOptions = input()
    pageOptionsList = pageOptions.split()
    pageOptionsList = list(map(int, pageOptionsList))
    if pageOptionsList[0] != 0:
        pageOptionsList.pop(0)
    adjlist.append(pageOptionsList)
visited = [False for i in range(numOfPages+1)]
visited[1] = True

queue = [1]
level = [0 for i in range(numOfPages+1)]
while len(queue) != 0:
    page = queue[0]
    for i in range(len(adjlist[page])):
        if not visited[adjlist[page][i]]:
            visited[adjlist[page][i]] = True
            queue.append(adjlist[page][i])
            level[adjlist[page][i]] = level[page] + 1
    queue.pop(0)

if False not in visited:
    print("Y")
else:
    print("N")
print(level[0])