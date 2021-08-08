from itertools import combinations

n = int(input())
s = [list(map(int,input().split())) for _ in range(n)]
members = [i for i in range(n)]
possible_team = []

for team in list(combinations(members,n//2)):
    possible_team.append(team)

min_stat_gap = 1000
for i in range(len(possible_team)//2):
    # A팀
    team = possible_team[i]
    stat_A = 0
    for j in range(n//2):
        member = team[j]
        for k in team:
            stat_A += s[member][k]
    # A를 제외한 나머지 팀
    team = possible_team[-i-1]
    stat_B = 0
    for j in range(n//2):
        member = team[j]
        for k in team:
            stat_B += s[member][k]
    min_stat_gap = min(min_stat_gap,abs(stat_A-stat_B))

print(min_stat_gap)