import math

num = int(input())
foundPrime = False
prime = num-1
if prime == 0:
    prime = 1
divisorMax = math.floor(math.sqrt(prime))

while not foundPrime:
    prime += 1
    divisorMax = math.ceil(math.sqrt(prime))
    for i in range(1, divisorMax+1):
        if prime % i == 0 and i != 1 and i != prime:
            foundPrime = False
            break
        else:
            foundPrime = True

print(prime)