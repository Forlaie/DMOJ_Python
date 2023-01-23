def sumac_sequence(pnum, num, count):
    nnum = pnum - num
    pnum = num
    num = nnum
    if pnum >= num:
        count += 1
    else:
        return count
    return sumac_sequence(pnum, num, count)

def main():
    pnum = int(input())
    num = int(input())
    print(sumac_sequence(pnum, num, 3))
main()