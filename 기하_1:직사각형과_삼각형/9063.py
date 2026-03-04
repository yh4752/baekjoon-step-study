INF = 1e9
n = int(input())

min_x = INF
max_x = -1*INF
min_y = INF
max_y = -1*INF
for _ in range(n):
    x,y = map(int, input().split())
    if x < min_x:
        min_x = x
    if x > max_x:
        max_x = x
    if y < min_y:
        min_y = y
    if y > max_y:
        max_y = y
if n > 2:
    print((max_x - min_x) * (max_y - min_y))
else:
    print(0)