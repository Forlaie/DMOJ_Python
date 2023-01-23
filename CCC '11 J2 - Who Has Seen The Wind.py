humidity = int(input())
time = int(input())
hit = False
for i in range(1, time+1):
    altitude = -6*i**4 + humidity*i**3 + 2*i**2 + i
    if altitude <= 0:
        hour = i
        hit = True
        break

if hit:
    print("The balloon first touches ground at hour:")
    print(hour)
else:
    print("The balloon does not touch ground in the given time.")