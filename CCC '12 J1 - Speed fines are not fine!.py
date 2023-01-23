speedlimit = int(input())
carspeed = int(input())
if carspeed <= speedlimit:
    print("Congratulations, you are within the speed limit!")
else:
    if 1 <= carspeed - speedlimit <= 20:
        print("You are speeding and your fine is $100.")
    elif 21 <= carspeed - speedlimit <= 30:
        print("You are speeding and your fine is $270.")
    else:
        print("You are speeding and your fine is $500.")