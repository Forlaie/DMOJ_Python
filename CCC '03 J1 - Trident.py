tines = int(input())
spacing = int(input())
handle = int(input())

for i in range(tines):
    print("*" + " "*spacing + "*" + " "*spacing + "*")
print("*"*(spacing*2+3))
for i in range(handle):
    print(" "*(spacing+1) + "*")