# def maybedp(count):
#     for r in range(row):
#         for c in range(column):
#             if r == 0 and c == 0:
#                 count[r][c] = 1
#                 continue
#             if map[r][c] == "*":
#                 continue
#
#             possible = []
#             if r != 0:
#                 if count[r-1][c] != 0:
#                     count[r][c] = count[r-1][c] + 1
#             if c != 0:
#                 if count[r][c-1] != 0:
#                     if map[r][c-1] == "+" or map[r][c-1] == "-":
#                         possible.append(count[r][c-1])
#             if c != column-1:
#                 if count[r][c+1] != 0:
#                     if map[r][c+1] == "+" or map[r][c+1] == "-":
#                         possible.append(count[r][c+1])
#             if r != 0:
#                 if count[r-1][c] != 0:
#                     if map[r-1][c] == "+" or map[r-1][c] == "|":
#                         possible.append(count[r-1][c])
#             if len(possible) != 0:
#                 count[r][c] = min(possible) + 1
#         for a in range(column-2, -1, -1):
#             if count[r][a] == 0 and count[r][a+1] != 0:
#                 count[r][a] = count[r][a+1]+1
#     return count
#
# def dfs(r, c, count, route):
#     route += 1
#     visited[r][c] = True
#     if r == row-1 and c == column-1:
#         count.append(route)
#     else:
#         if map[r][c] == "+":
#             if r != row-1:
#                 if map[r+1][c] != "*" and not visited[r+1][c]:
#                     dfs(r+1, c, count, route)
#             if c != column-1:
#                 if map[r][c+1] != "*" and not visited[r][c+1]:
#                     dfs(r, c+1, count, route)
#             if c != 0:
#                 if map[r][c-1] != "*" and not visited[r][c-1]:
#                     dfs(r, c-1, count, route)
#             if r != 0:
#                 if map[r-1][c] != "*" and not visited[r-1][c]:
#                     dfs(r-1, c, count, route)
#         elif map[r][c] == "-":
#             if c != column-1:
#                 if map[r][c+1] != "*" and not visited[r][c+1]:
#                     dfs(r, c+1, count, route)
#             if c != 0:
#                 if map[r][c-1] != "*" and not visited[r][c-1]:
#                     dfs(r, c-1, count, route)
#         elif map[r][c] == "|":
#             if r != row-1:
#                 if map[r+1][c] != "*" and not visited[r+1][c]:
#                     dfs(r+1, c, count, route)
#             if r != 0:
#                 if map[r-1][c] != "*" and not visited[r-1][c]:
#                     dfs(r-1, c, count, route)
#     return count

def bfs(currChildren, nextChildren):
    level = 1
    while len(currChildren) != 0:
        r = currChildren[i][0]
        c = currChildren[i][1]
        if map[r][c] == "+":
            if r != row-1:
                if map[r+1][c] != "*" and not visited[r+1][c]:
                    nextChildren.append([r+1, c])
                    visited[r+1][c] = True
            if r != 0:
                if map[r-1][c] != "*" and not visited[r-1][c]:
                    nextChildren.append([r-1, c])
                    visited[r-1][c] = True
            if c != column-1:
                if map[r][c+1] != "*" and not visited[r][c+1]:
                    nextChildren.append([r, c+1])
                    visited[r][c+1] = True
            if c != 0:
                if map[r][c-1] != "*" and not visited[r][c-1]:
                    nextChildren.append([r, c-1])
                    visited[r][c-1] = True
        elif map[r][c] == "-":
            if c != column-1:
                if map[r][c+1] != "*" and not visited[r][c+1]:
                    nextChildren.append([r, c+1])
                    visited[r][c+1] = True
            if c != 0:
                if map[r][c-1] != "*" and not visited[r][c-1]:
                    nextChildren.append([r, c-1])
                    visited[r][c-1] = True
        elif map[r][c] == "|":
            if r != row-1:
                if map[r+1][c] != "*" and not visited[r+1][c]:
                    nextChildren.append([r+1, c])
                    visited[r+1][c] = True
            if r != 0:
                if map[r-1][c] != "*" and not visited[r-1][c]:
                    nextChildren.append([r-1, c])
                    visited[r-1][c] = True
        currChildren = nextChildren
        nextChildren = []
        level += 1
    return level

cases = int(input())

for i in range(cases):
    row = int(input())
    column = int(input())
    visited = [[False]*column for t in range(row)]
    map = []
    for j in range(row):
        street = input()
        map.append(street)

    currChildren = [[0, 0]]
    nextChildren = []
    level = 1
    possible = False
    while len(currChildren) != 0:
        for i in range(len(currChildren)):
            r = currChildren[i][0]
            c = currChildren[i][1]
            if r == row-1 and c == column-1:
                print(level)
                possible = True
                break
            if map[r][c] == "+":
                if r != row - 1:
                    if map[r + 1][c] != "*" and not visited[r + 1][c]:
                        nextChildren.append([r + 1, c])
                        visited[r + 1][c] = True
                if r != 0:
                    if map[r - 1][c] != "*" and not visited[r - 1][c]:
                        nextChildren.append([r - 1, c])
                        visited[r - 1][c] = True
                if c != column - 1:
                    if map[r][c + 1] != "*" and not visited[r][c + 1]:
                        nextChildren.append([r, c + 1])
                        visited[r][c + 1] = True
                if c != 0:
                    if map[r][c - 1] != "*" and not visited[r][c - 1]:
                        nextChildren.append([r, c - 1])
                        visited[r][c - 1] = True
            elif map[r][c] == "-":
                if c != column - 1:
                    if map[r][c + 1] != "*" and not visited[r][c + 1]:
                        nextChildren.append([r, c + 1])
                        visited[r][c + 1] = True
                if c != 0:
                    if map[r][c - 1] != "*" and not visited[r][c - 1]:
                        nextChildren.append([r, c - 1])
                        visited[r][c - 1] = True
            elif map[r][c] == "|":
                if r != row - 1:
                    if map[r + 1][c] != "*" and not visited[r + 1][c]:
                        nextChildren.append([r + 1, c])
                        visited[r + 1][c] = True
                if r != 0:
                    if map[r - 1][c] != "*" and not visited[r - 1][c]:
                        nextChildren.append([r - 1, c])
                        visited[r - 1][c] = True
        currChildren = nextChildren
        nextChildren = []
        level += 1
    if not possible:
        print(-1)


    # result = maybedp(count)
    # if result[-1][-1] == 0:
    #     print(-1)
    # else:
    #     print(result[-1][-1])
    # result = dfs(0, 0, [], 0)
    # if len(result) == 0:
    #     print(-1)
    # else:
    #     print(result[-1])
