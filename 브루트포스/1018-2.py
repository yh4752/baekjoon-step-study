def check_board(x, y, board):
    count = 0
    for i in range(8):
        for j in range(8):
            # 번갈아가면서 흑 백 만들기
            expected = 'B' if (i+j) % 2 == 0 else 'W'
            if expected != board[x+i][y+j]:
                count +=1
    return min(count, 64-count)

n, m = map(int, input().split())
board = [input().strip() for _ in range(n)]

min_count = 64

for i in range(n-7):
    for j in range(m-7):
        min_count = min(min_count, check_board(i, j, board))

print(min_count)