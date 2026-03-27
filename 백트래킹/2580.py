import sys
input = sys.stdin.readline

board = []
blank = []

row_used = [[False] * 10 for _ in range(9)]
col_used = [[False] * 10 for _ in range(9)]
box_used = [[False] * 10 for _ in range(9)]

for i in range(9):
    row = list(map(int, input().split()))
    board.append(row)
    for j in range(9):
        num = row[j]
        if num == 0:
            blank.append((i, j))
        else:
            row_used[i][num] = True
            col_used[j][num] = True
            box_used[(i // 3) * 3 + (j // 3)][num] = True

def dfs(idx):
    if idx == len(blank):
        for row in board:
            print(*row)
        return True

    x, y = blank[idx]
    b = (x // 3) * 3 + (y // 3)

    for num in range(1, 10):
        if not row_used[x][num] and not col_used[y][num] and not box_used[b][num]:
            board[x][y] = num
            row_used[x][num] = True
            col_used[y][num] = True
            box_used[b][num] = True

            if dfs(idx + 1):
                return True

            board[x][y] = 0
            row_used[x][num] = False
            col_used[y][num] = False
            box_used[b][num] = False

    return False

dfs(0)