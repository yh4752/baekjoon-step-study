import sys
input = sys.stdin.readline

n = int(input())
arr = []
for i in range(n):
    row = list(map(int, input().split()))
    arr.append(row)

min_val = 10000
teamA = []

def get_value(teamA):
    teamB = []
    for i in range(n):
        if i not in teamA:
            teamB.append(i)

    scoreA = 0
    scoreB = 0
    for i in range(n // 2):
        for j in range(i+1, n // 2):
            scoreA += arr[teamA[i]][teamA[j]] + arr[teamA[j]][teamA[i]]
            scoreB += arr[teamB[i]][teamB[j]] + arr[teamB[j]][teamB[i]]
    
    return abs(scoreA - scoreB)
    
def backtracing(start):
    global min_val
    if len(teamA) == n // 2:
        val = get_value(teamA)
        min_val = val if val < min_val else min_val
        return
    
    for i in range(start, n):
        teamA.append(i)
        backtracing(i + 1)
        teamA.pop()

backtracing(0)
print(min_val)