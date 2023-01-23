angle1 = int(input())
angle2 = int(input())
angle3 = int(input())
if angle1 + angle2 + angle3 != 180:
    print("Error")
else:
    if angle1 == angle2 == angle3:
        print("Equilateral")
    elif angle1 != angle2 != angle3 and angle1 != angle3:
        print("Scalene")
    else:
        print("Isosceles")