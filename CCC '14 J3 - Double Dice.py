numberofrounds = int(input())
antoniatotal = 100
davidtotal = 100
for i in range(numberofrounds):
    dice = input()
    antonia, david = dice.split()
    antonia = int(antonia)
    david = int(david)
    if antonia > david:
        davidtotal -= antonia
    if david > antonia:
        antoniatotal -= david
print(antoniatotal)
print(davidtotal)