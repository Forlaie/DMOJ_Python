x = int(input())
m = int(input())
answer = False

for i in range(1, m):
    if x*i%m == 1:
        print(i)
        answer = True
        break

if not answer:
    print("No such integer exists.")