size = int(input())
list = []
for i in range(size):
    num = int(input())
    list.append(num)
list.sort()

for i in range(size):
    print(list[i])