import math

times = int(input())

def isPrime(num):
    if num == 2:
        return True
    for j in range(2, math.ceil(math.sqrt(num)) + 1):
        if num % j == 0:
            return False
    return True

for i in range(times):
    primeNum = int(input())

    primeNum *= 2

    for i in range(2, primeNum):
        a = i
        b = primeNum - i
        aIsPrime = isPrime(a)
        bIsPrime = isPrime(b)

        if aIsPrime and bIsPrime:
            print(f"{a} {b}")
            break
