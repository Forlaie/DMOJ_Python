monthlyMegabyte = int(input())
months = int(input())
remaining = (months+1)*monthlyMegabyte
for i in range(months):
    used = int(input())
    remaining -= used
print(remaining)