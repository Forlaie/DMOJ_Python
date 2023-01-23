num = int(input())
max = 0
person = ""
for i in range(num):
    name = input()
    bid = int(input())
    if bid > max:
        max = bid
        person = name
print(person)