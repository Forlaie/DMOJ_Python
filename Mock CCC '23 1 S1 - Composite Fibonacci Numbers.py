times = int(input())
for i in range(times):
    num = int(input())

    # check concat
    if num < 10:
        print("NO")
    else:
        # check composite
        composite = False
        for j in range(2, int(num/2+1)):
            if num % j == 0:
                composite = True
                break
        if composite:
            print("YES")
        else:
            print("NO")