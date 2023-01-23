def makeQueue(cells, value, visited, queue):
    for i in range(len(cells)):
        for j in range(len(cells[i])):
            if cells[i][j] == value:
                if not visited[i][j]:
                    if cells[i][j] not in queue:
                        visited[i][j] = True
                        queue.append([i, j])

rows = int(input())
columns = int(input())
cells = []
for i in range(rows):
    cells.append(list(map(int, input().split())))

queue = [[rows-1, columns-1]]
visited = [[False]*columns for i in range(rows)]
nums = []
escapable = False

while len(queue) != 0:
    if queue[0][0] == 0 and queue[0][1] == 0:
        escapable = True
        break
    value = (queue[0][0]+1) * (queue[0][1]+1)
    if value in nums:
        queue.pop(0)
        continue
    if value not in nums:
        nums.append(value)
    makeQueue(cells, value, visited, queue)
    queue.pop(0)
    # x = queue[0][0]
    # y = queue[0][1]
    # visited[x][y] = True
    # value = cells[x][y]
    # if value in nums:
    #     queue.pop(0)
    #     continue
    # else:
    #     nums.append(value)


    # for i in range(1, value//2+1):
    #     if value % i == 0:
    #         tempx = i-1
    #         tempy = (value//i)-1
    #         if tempx < rows and tempy < columns:
    #             if not visited[tempx][tempy]:
    #                 if tempx == rows - 1 and tempy == columns - 1:
    #                     escapable = True
    #                     break
    #                 queue.append([tempx, tempy])
    #         if tempy < rows and tempx < columns:
    #             if not visited[tempy][tempx]:
    #                 if tempy == rows - 1 and tempx == columns - 1:
    #                     escapable = True
    #                     break
    #                 queue.append([tempy, tempx])
    # queue.pop(0)

if escapable:
    print("yes")
else:
    print("no")