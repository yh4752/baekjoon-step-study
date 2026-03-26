n, m = map(int, input().split())

path = []

def dfs():
    if len(path) == m:
        print(" ".join(map(str, path)))
        return
    
    for i in range(1, n+1):
        if i not in path:
            path.append(i)
            dfs()
            path.pop()