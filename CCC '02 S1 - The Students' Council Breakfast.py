pink = int(input())
green = int(input())
red = int(input())
orange = int(input())
total = int(input())
count = 0
min = 100000000

for i in range(total//pink+1):
    for j in range(total//green+1):
        for l in range(total//red+1):
            for k in range(total//orange+1):
                if i*pink + j*green + l*red + k*orange == total:
                    print(f"# of PINK is {i} # of GREEN is {j} # of RED is {l} # of ORANGE is {k}")
                    count += 1
                    if i+j+l+k < min:
                        min = i+j+l+k
print(f"Total combinations is {count}.")
print(f"Minimum number of tickets to print is {min}.")