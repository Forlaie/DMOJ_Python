times = int(input())

for i in range(times):
    message = input()
    n, l = message.split()
    n = int(n)
    print(l*n)