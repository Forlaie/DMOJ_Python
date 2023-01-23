nikkyf = int(input())
nikkyb = int(input())
byronf = int(input())
byronb = int(input())
num = int(input())
nikkyt = num
byront = num
nikkys = 0
byrons = 0

while nikkyt != 0 and byront != 0:
    if nikkyt >= nikkyf:
        nikkys += nikkyf
        nikkyt -= nikkyf
    else:
        nikkys += nikkyt
        nikkyt = 0
    if byront >= byronf:
        byrons += byronf
        byront -= byronf
    else:
        byrons += byront
        byront = 0
    if nikkyt >= nikkyb:
        nikkys -= nikkyb
        nikkyt -= nikkyb
    else:
        nikkys -= nikkyt
        nikkyt = 0
    if byront >= byronb:
        byrons -= byronb
        byront -= byronb
    else:
        byrons -= byront
        byront = 0

if nikkys > byrons:
    print("Nikky")
elif byrons > nikkys:
    print("Byron")
else:
    print("Tied")