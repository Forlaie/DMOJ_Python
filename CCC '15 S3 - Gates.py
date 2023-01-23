gates = int(input())
planes = int(input())
prevPlane  = 0
prevResult = 0
availableGates = [i+1 for i in range(gates)]
count = 0

def binarySearch(list, planeGate, higha, lowa):
    low = lowa
    high = higha
    potential = -1
    while high >= low:
        mid = int((low + high) / 2)
        if planeGate == list[mid]:
            return mid
        elif planeGate < list[mid]:
            high = mid - 1
        else:
            low = mid + 1
            potential = mid
    return potential

for i in range(planes):
    planeGate = int(input())
    if planeGate < prevPlane:
        result = binarySearch(availableGates, planeGate, max(0, prevResult-1), 0)
    else:
        if availableGates[min(prevResult, len(availableGates)-1)] <= planeGate:
            result = binarySearch(availableGates, planeGate, len(availableGates)-1, min(prevResult, len(availableGates)-1))
        else:
            result = prevResult-1
    if result == -1:
        break
    else:
        availableGates.pop(result)
        count += 1
    prevPlane = planeGate
    prevResult = result
print(count)