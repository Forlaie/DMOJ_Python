# DP

num = int(input())
pairs = ""
listOfPoints = [[] for i in range(num-1)]
dp = [0 for i in range(num)]
dp[0] = 1

while pairs != "0 0":
    pairs = input()
    if pairs != "0 0":
        start, end = pairs.split()
        start = int(start)-1
        end = int(end)
        listOfPoints[start].append(end)

for i in range(len(listOfPoints)):
    for j in range(len(listOfPoints[i])):
        dp[listOfPoints[i][j]-1] += dp[i]

print(dp[-1])



# Graph Theory

# numOfMarkedPoints = int(input())
# pairs = ""
# count = []
#
# def search(index):
#     if index+1 == numOfMarkedPoints:
#         count.append(1)
#     else:
#         for i in range(len(listOfPoints[index])):
#             search(listOfPoints[index][i]-1)
#     return len(count)
#
# print(search(0))