times = int(input())
nonmetals = ["Cl", "Br", "Xe", "Kr", "Si", "As", "Rn", "Ne", "He", "H", "C", "N", "O", "F", "P", "S", "I"]

for i in range(times):
    good = True
    check = True
    count = 1
    compound = input()
    test = compound.split()
    for l in range(len(test)):
        if not check:
            good = False
            break
        for j in range(len(nonmetals)):
            if nonmetals[j] != test[l]:
                check = False
            else:
                check = True
                break
    if good and check:
        print("Molecular!")
    elif not check or not good:
        print("Not molecular!")