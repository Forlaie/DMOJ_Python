startCoords = input()
endCoords = input()

startX, startY = startCoords.split()
startX = int(startX)
startY = int(startY)

endX, endY = endCoords.split()
endX = int(endX)
endY = int(endY)

batteryGiven = int(input())

batteryUsed = abs(startX-endX) + abs(startY-endY)

if (batteryGiven - batteryUsed) >= 0 and (batteryGiven - batteryUsed) % 2 == 0:
    print("Y")
else:
    print("N")
