times = int(input())
list = []

for i in range(times):
    number = int(input())
    list.append(number)

list.sort()

for i in range(len(list)):
    print(list[0])
    list.pop(0)