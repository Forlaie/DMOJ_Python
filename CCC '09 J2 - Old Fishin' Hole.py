trout = int(input())
pike = int(input())
pickerel = int(input())
total = int(input())
count = 0

for i in range(total//trout+1):
    for j in range(total//pike+1):
        for l in range(total//pickerel+1):
            if i == 0 and j == 0 and l == 0:
                continue
            else:
                if l*pickerel + j*pike + i*trout <= total:
                    count += 1
                    print(f"{i} Brown Trout, {j} Northern Pike, {l} Yellow Pickerel")
print(f"Number of ways to catch fish: {count}")