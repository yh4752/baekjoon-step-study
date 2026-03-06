def check_board(x, y, answer, board):
    count = 0
    for i in range(x, x+8):
        for j in range(y, y+8):
            if answer[i-x][j-y] != board[i][j]:
                count += 1
    return count

n,m = map(int, input().split())
answer = [
    ['B','W','B','W','B','W','B','W'],
    ['W','B','W','B','W','B','W','B'],
    ['B','W','B','W','B','W','B','W'],
    ['W','B','W','B','W','B','W','B'],
    ['B','W','B','W','B','W','B','W'],
    ['W','B','W','B','W','B','W','B'],
    ['B','W','B','W','B','W','B','W'],
    ['W','B','W','B','W','B','W','B'],
]
answer_2 = [
    ['W','B','W','B','W','B','W','B'],
    ['B','W','B','W','B','W','B','W'],
    ['W','B','W','B','W','B','W','B'],
    ['B','W','B','W','B','W','B','W'],
    ['W','B','W','B','W','B','W','B'],
    ['B','W','B','W','B','W','B','W'],
    ['W','B','W','B','W','B','W','B'],
    ['B','W','B','W','B','W','B','W'],
]


board = []
for i in range(n):
    board.append(list(input()))

min_count = n*m
for i in range(0, n-7):
    for j in range(0, m-7):
        count1 = check_board(i, j, answer, board)
        count2 = check_board(i,j,answer_2, board)
        count = min(count1, count2)
        if count < min_count:
            min_count = count
        

print(min_count)