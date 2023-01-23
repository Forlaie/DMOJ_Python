burger = [461, 431, 420, 0]
side = [100, 57, 70, 0]
drink = [130, 160, 118, 0]
dessert = [167, 266, 75, 0]

bchoice = int(input())
bchoice = burger[bchoice-1]
schoice = int(input())
schoice = side[schoice-1]
dchoice = int(input())
dchoice = drink[dchoice-1]
dechoice = int(input())
dechoice = dessert[dechoice-1]

calories = bchoice + schoice + dchoice + dechoice
print("Your total Calorie count is " + str(calories) + ".")