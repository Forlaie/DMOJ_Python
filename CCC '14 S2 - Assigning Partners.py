people = int(input())
first = input()
fp = first.split()
second = input()
sp = second.split()
correct = True

for i in range(people):
    index = sp.index(fp[i])
    if sp[i] != fp[index] or sp[i] == fp[i]:
        correct = False
        break

if correct:
    print("good")
else:
    print("bad")