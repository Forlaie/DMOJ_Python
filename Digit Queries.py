q = int(input())
for i in range(q):
    index = int(input())
    digits = 0
    startPos = 1
    d = 1
    while True:
        digits += d * 9 * pow(10, d - 1)
        if digits >= index:
            digits = d
            break
        startPos += d * 9 * pow(10, d - 1)
        d += 1
    startNum = pow(10, digits - 1)

    low = pow(10, digits-1)
    high = pow(10, digits)-1
    while high >= low:
        mid = (low + high) // 2
        midPos = (mid - startNum) * digits + startPos
        if 0 <= index - midPos < digits:
            print(str(mid)[index-midPos])
            break
        elif midPos > index:
            high = mid - 1
        elif midPos < index:
            low = mid + 1