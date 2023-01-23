numerator = int(input())
denominator = int(input())
integer = numerator//denominator
numerator %= denominator
if numerator == 0:
    print(integer)
else:
    for i in reversed(range(numerator+1)):
        if numerator%i == 0 and denominator%i == 0:
            numerator //= i
            denominator //= i
            break
    if integer != 0:
        print(f"{integer} {numerator}/{denominator}")
    else:
        print(f"{numerator}/{denominator}")