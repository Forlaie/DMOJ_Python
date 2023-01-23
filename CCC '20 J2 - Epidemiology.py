goal = int(input())
infect = int(input())
rate = int(input())
increase = infect
day = 0

while infect <= goal:
    increase *= rate
    infect += increase
    day += 1
print(day)