number = 1
while number != 0:
    factors = []
    l = 0
    w = 0
    perimeter = 0
    number = int(input())
    if number == 0:
        break
    for i in range(1, number+1):
        if number%i == 0:
            factors.append(i)
        if i*i == number:
            factors.append(i)
    l = factors[(len(factors)//2)]
    w = factors[len(factors)//2-1]
    perimeter = 2*l + 2*w
    print("Minimum perimeter is", perimeter, "with dimensions", w, "x", l)