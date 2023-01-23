adjList = [[],[6],[6],[4,5,6,15],[3,5,6],[3,4,6],[1,2,3,4,5,7],[6,8],[7,9],[8,10,12],[9,11],[10,12],[9,11,13],[12,14,15],[13],[3,13],[17,18],[16,18],[16,17],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]

action = ""
while action != "q":
    action = input()

    if action == "i":
        x = int(input())
        y = int(input())
        if y not in adjList[x]:
            adjList[x].append(y)
            adjList[y].append(x)

    elif action == "d":
        x = int(input())
        y = int(input())
        adjList[x].remove(y)
        adjList[y].remove(x)

    elif action == "n":
        x = int(input())
        print(len(adjList[x]))

    elif action == "f":
        x = int(input())
        myList = []
        for i in range(len(adjList[x])):
            myList += adjList[adjList[x][i]]
        mylist = list(dict.fromkeys(myList))
        for i in range(len(adjList[x])):
            if adjList[x][i] in mylist:
                mylist.remove(adjList[x][i])
        mylist.remove(x)
        print(len(mylist))

    elif action == "s":
        level = [[]] * 51
        x = int(input())
        y = int(input())
        visited = [False for i in range(51)]
        queue = [x]
        while len(queue) != 0:
            currentLocation = queue[0]
            if y == currentLocation:
                break
            currentLocationAdjList = adjList[currentLocation]
            visited[currentLocation] = True
            for i in range(len(currentLocationAdjList)):
                if (not visited[currentLocationAdjList[i]]) and (currentLocationAdjList[i] not in queue):
                    level[currentLocationAdjList[i]] = level[currentLocation] + [currentLocation]
                    queue.append(currentLocationAdjList[i])
            queue.pop(0)
        if len(level[y]) == 0:
            print("Not connected")
        else:
            print(len(level[y]))