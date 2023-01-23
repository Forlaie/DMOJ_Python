tides = int(input())
measurements = input()
order = ""

measurements = measurements.split()
measurements = [int(i) for i in measurements]
measurements.sort()

if tides%2 == 0:
    lowest = int(tides/2)-1
    highest = int(tides/2)
    while lowest >= 0:
        order += str(measurements[lowest])
        order += " "
        order += str(measurements[highest])
        order += " "
        lowest -= 1
        highest += 1
else:
    lowest = int(tides/2)
    highest = int(tides/2)+1
    while lowest >= 0:
        order += str(measurements[lowest])
        order += " "
        if highest <= tides-1:
            order += str(measurements[highest])
        order += " "
        lowest -= 1
        highest += 1

print(order)