departure = input()
hour, minute = departure.split(":")
hour = int(hour)
minute = int(minute)

commuteDistance = 2*60

while commuteDistance != 0:
    if 7 <= hour < 10 or 15 <= hour < 19:
        minute += 10
        commuteDistance -= 5
    else:
        minute += 10
        commuteDistance -= 10

    if minute == 60:
        hour += 1
        minute = 0
    if hour == 24:
        hour = 0

if hour < 10:
    hour = "0" + str(hour)
if minute == 0:
    minute = "00"
print(str(hour) + ":" + str(minute))