low = int(input())
high = int(input())
count = 0

# 0, 1, 6, 8, 9

for i in range(low, high+1):
    if "2" in str(i) or "3" in str(i) or "4" in str(i) or "5" in str(i) or "7" in str(i):
        continue
    else:
        test = ""
        for j in range(len(str(i))):
            if str(i)[j] == "0":
                test += "0"
            elif str(i)[j] == "1":
                test += "1"
            elif str(i)[j] == "6":
                test += "9"
            elif str(i)[j] == "8":
                test += "8"
            elif str(i)[j] == "9":
                test += "6"
        if str(i) == test[::-1]:
            count += 1
print(count)