times = int(input())
numbers = []

for i in range(times):
    thing = int(input())
    numbers.append(thing)

unique = set(numbers)
print(len(unique))