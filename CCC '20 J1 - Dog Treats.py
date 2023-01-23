small = int(input())
medium = int(input())
large = int(input())

happy = small + 2*medium + 3*large

if happy < 10:
    print("sad")
else:
    print("happy")