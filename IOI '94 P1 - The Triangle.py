# def dfs(triangle, r, c, sums, curr):
#     curr += triangle[r][c]
#     if r == len(triangle)-1:
#         sums.append(curr)
#     else:
#         dfs(triangle, r+1, c, sums, curr)
#         if c != len(triangle[r+1])-1:
#             dfs(triangle, r+1, c+1, sums, curr)
#     return sums

num = int(input())
triangle = []
for i in range(num):
    n = input()
    triangle.append(list(map(int, n.split())))
# print(max(dfs(numbers, 0, 0, [], 0)))

prevRow = [triangle[0][0]]
nextRow = [0, 0]

for i in range(1, num):
    for j in range(len(triangle[i])):
        if j == 0:
            nextRow[j] = prevRow[j] + triangle[i][j]
        elif j == len(triangle[i])-1:
            nextRow[j] = prevRow[j-1] + triangle[i][j]
        else:
            nextRow[j] = max(prevRow[j-1], prevRow[j]) + triangle[i][j]
    prevRow = nextRow
    nextRow = [0 for i in range(len(prevRow)+1)]
print(max(prevRow))

# [7, 0, 0, 0, 0]
# [10, 15, 0, 0, 0]

# [10, 15, 0, 0, 0]
# [18, 16, 15, 0, 0]