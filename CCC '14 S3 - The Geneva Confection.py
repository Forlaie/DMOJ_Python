tests = int(input())

def recipe(mountain, totalcars):
    branch = []
    need = 1
    while need != totalcars:
        if need in mountain:
            if need == mountain[-1]:
                mountain.pop()
                need += 1
            else:
                mountainsubarray = mountain[mountain.index(need)+1:]
                mountainsubarray.reverse()
                branch += mountainsubarray
                mountain = mountain[:mountain.index(need)]
                need += 1
        else:
            if need == branch[-1]:
                branch.pop()
                need += 1
            else:
                return "N"
    return "Y"

for i in range(tests):
    mountain = []
    cars = int(input())
    for j in range(cars):
        number = int(input())
        mountain.append(number)
    print(recipe(mountain, cars))