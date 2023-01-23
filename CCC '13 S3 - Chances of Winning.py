favTeam = int(input())
num = int(input())
games = [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]
points = [0]*4

for i in range(num):
    team1, team2, score1, score2 = list(map(int, input().split()))
    games.remove([team1, team2])
    team1 -= 1
    team2 -= 1

    if score1 > score2:
        points[team1] += 3
    elif score1 == score2:
        points[team1] += 1
        points[team2] += 1
    else:
        points[team2] += 3

print(games)
print(points)