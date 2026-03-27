import sys
input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

score = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        score[i][j] += arr[i][j] + arr[j][i]

min_val = float('inf')
teamA = [0]
visitied = [False] * n
visitied[0] = True

def get_team_score(team):
    total = 0
    for i in range(len(team)):
        for j in range(i + 1, len(team)):
            total += score[i][j]
    return total

def dfs(start):
    global min_val

    if len(teamA) == n//2:
        teamB = []
        for i in range(n):
            if not visitied[i]:
                teamB.append(i)
        
        scoreA = get_team_score(teamA)
        scoreB = get_team_score(teamB)

        min_val = min(abs(scoreA - scoreB), min_val)
        return
    
    for i in range(start, n):
        if not visitied[i]:
            visitied[i] = True
            teamA.append(i)
            dfs(i+1)
            teamA.pop()
            visitied[i] = False

dfs(1)
print(min_val)