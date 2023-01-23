measurements = input()
length, radius = measurements.split()
length = int(length)
radius = int(radius)

squareArea = length*length
radiusArea = 3.14*radius*radius

if squareArea > radiusArea:
    print("SQUARE")
else:
    print("CIRCLE")