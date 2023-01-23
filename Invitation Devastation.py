invitation = input()
people = int(input())

for i in range(people):
    name = input()
    message = invitation.replace(">", name)
    print(message)