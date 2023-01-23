num = int(input())
for i in range(num):
    info = input()
    a, b, p = info.split()
    a = int(a)
    b = int(b)
    p = int(p)
    if a * b != p:
        print("16 BIT S/W ONLY")
    else:
        print("POSSIBLE DOUBLE SIGMA")