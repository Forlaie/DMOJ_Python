height = int(input())
stars = -1
space = height*2

for i in range(height):
    if i >= (height+1)/2:
        stars -= 2
    else:
        stars += 2

    space = (height * 2) - (stars * 2)

    first = "*"*stars
    blank = " "*space
    last = "*"*stars

    print(first + blank + last)