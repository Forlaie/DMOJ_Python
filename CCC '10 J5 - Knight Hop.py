def bfs(queue, visited, count, goal):
  if queue[0] == goal:
    return count
  while queue:
    count += 1
    levelsize = len(queue)
    while levelsize != 0:
      neighbour = [queue[0][0]+2, queue[0][1]+1]
      if neighbour == goal:
        return count
      else:
        if neighbour not in visited:
          if not (neighbour[0] > 8 or neighbour[0] < 1 or neighbour[1] > 8 or neighbour[1] < 1):
            queue.append(neighbour)
            visited.append(neighbour)
      neighbour = [queue[0][0]+2, queue[0][1]-1]
      if neighbour == goal:
        return count
      else:
        if neighbour not in visited:
          if not (neighbour[0] > 8 or neighbour[0] < 1 or neighbour[1] > 8 or neighbour[1] < 1):
            queue.append(neighbour)
            visited.append(neighbour)
      neighbour = [queue[0][0]-2, queue[0][1]+1]
      if neighbour == goal:
        return count
      else:
        if neighbour not in visited:
          if not (neighbour[0] > 8 or neighbour[0] < 1 or neighbour[1] > 8 or neighbour[1] < 1):
            queue.append(neighbour)
            visited.append(neighbour)
      neighbour = [queue[0][0]-2, queue[0][1]-1]
      if neighbour == goal:
        return count
      else:
        if neighbour not in visited:
          if not (neighbour[0] > 8 or neighbour[0] < 1 or neighbour[1] > 8 or neighbour[1] < 1):
            queue.append(neighbour)
            visited.append(neighbour)
      neighbour = [queue[0][0]+1, queue[0][1]+2]
      if neighbour == goal:
        return count
      else:
        if neighbour not in visited:
          if not (neighbour[0] > 8 or neighbour[0] < 1 or neighbour[1] > 8 or neighbour[1] < 1):
            queue.append(neighbour)
            visited.append(neighbour)
      neighbour = [queue[0][0]-1, queue[0][1]+2]
      if neighbour == goal:
        return count
      else:
        if neighbour not in visited:
          if not (neighbour[0] > 8 or neighbour[0] < 1 or neighbour[1] > 8 or neighbour[1] < 1):
            queue.append(neighbour)
            visited.append(neighbour)
      neighbour = [queue[0][0]+1, queue[0][1]-2]
      if neighbour == goal:
        return count
      else:
        if neighbour not in visited:
          if not (neighbour[0] > 8 or neighbour[0] < 1 or neighbour[1] > 8 or neighbour[1] < 1):
            queue.append(neighbour)
            visited.append(neighbour)
      neighbour = [queue[0][0]-1, queue[0][1]-2]
      if neighbour == goal:
        return count
      else:
        if neighbour not in visited:
          if not (neighbour[0] > 8 or neighbour[0] < 1 or neighbour[1] > 8 or neighbour[1] < 1):
            queue.append(neighbour)
            visited.append(neighbour)
      queue.pop(0)
      levelsize -= 1

startposition = input()
startx, starty = startposition.split()
endposition = input()
endx, endy = endposition.split()
startx = int(startx)
starty = int(starty)
endx = int(endx)
endy = int(endy)
print(bfs([[startx, starty]], [[startx, starty]], 0, [endx, endy]))