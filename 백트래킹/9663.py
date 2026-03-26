n = int(input())

count = 0
col_visited = [False] * (n+1)
dig1 = [False] * (2*n)
dig2 = [False] * (2*n)
def nQueen(row):
    if row == n:
        global count
        count += 1
        return
    
    for c in range(0, n):
        if not col_visited[c] and not dig1[row-c+n] and not dig2[row+c]:
            col_visited[c] = True
            dig1[row-c]= True
            dig2[row+c] = True
            nQueen(row+1)
            col_visited[c] = False
            dig1[row-c]= False
            dig2[row+c] = False

nQueen(0)
print(count)