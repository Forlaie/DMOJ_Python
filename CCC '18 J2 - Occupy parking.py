spaces = int(input())
today = input()
yesterday = input()
count = 0

for i in range(len(today)):
    if today[i] == "C" and yesterday[i] == "C":
        count += 1

print(count)